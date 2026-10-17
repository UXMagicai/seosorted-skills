import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

WORK = Path(sys.argv[1])
LIMIT = int(sys.argv[2]) if len(sys.argv) > 2 else 20
MOBILE_RUNS = int(os.environ.get("MOBILE_RUNS", "3"))
CRAWL = WORK / "crawl.json"
TOOL = WORK / "lhtool"
OUT = WORK / "lighthouse"
OUT.mkdir(exist_ok=True)

CHROME_CANDIDATES = [
    os.environ.get("CHROME_PATH", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]
chrome = next((c for c in CHROME_CANDIDATES if c and Path(c).exists()), None)
if not chrome:
    sys.exit("No Chrome/Chromium found; set CHROME_PATH")

lh = TOOL / "node_modules/.bin/lighthouse"
if not lh.exists():
    TOOL.mkdir(exist_ok=True)
    subprocess.run(["npm", "i", "--silent", "--no-audit", "--no-fund", "lighthouse@12.2.1"], cwd=TOOL, check=True)

crawl = json.load(open(CRAWL))
urls = list(dict.fromkeys(p["url"] for p in crawl["pages"] if p.get("status") == 200 and not p.get("non_html")))[:LIMIT]


def run(url, device, n=0):
    name = "".join(ch if ch.isalnum() else "_" for ch in url)[-90:]
    dest = OUT / f"{name}-{device}-{n}.json"
    flags = ["--preset=desktop"] if device == "desktop" else ["--form-factor=mobile"]
    with tempfile.TemporaryDirectory() as prof:
        subprocess.run(
            [str(lh), url, "--quiet", f"--chrome-flags=--headless=new --user-data-dir={prof}", *flags, "--output=json", f"--output-path={dest}"],
            env={**os.environ, "CHROME_PATH": chrome},
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=240,
        )
    if not dest.exists():
        return {"error": "Lighthouse run failed"}
    j = json.load(open(dest))
    if j.get("runtimeError") or not (j.get("categories", {}).get("performance") or {}).get("score"):
        return {"error": (j.get("runtimeError") or {}).get("code", "page did not load")}
    a = j.get("audits", {})
    pick = lambda k: a.get(k, {}).get("displayValue", "")
    return {
        "scores": {k: round((v.get("score") or 0) * 100) for k, v in j.get("categories", {}).items()},
        "lcp": pick("largest-contentful-paint"),
        "fcp": pick("first-contentful-paint"),
        "tbt": pick("total-blocking-time"),
        "cls": pick("cumulative-layout-shift"),
        "si": pick("speed-index"),
        "tti": pick("interactive"),
        "field": {},
        "failing": [
            {"id": k, "title": v.get("title"), "display": v.get("displayValue", ""), "score": v.get("score"), "savings_ms": (v.get("details") or {}).get("overallSavingsMs")}
            for k, v in a.items()
            if v.get("score") is not None and v.get("score") < 0.9 and v.get("scoreDisplayMode") in ("binary", "numeric", "metricSavings")
        ],
    }


def median_run(url, device, runs):
    results = [r for r in (run(url, device, i) for i in range(runs)) if r.get("scores")]
    if not results:
        return {"error": "Lighthouse run failed"}
    results.sort(key=lambda r: r["scores"].get("performance", 0))
    best = dict(results[(len(results) - 1) // 2] if len(results) % 2 else results[len(results) // 2 - 1])
    if len(results) % 2 == 0:
        best["scores"] = dict(best["scores"], performance=round(sum(r["scores"]["performance"] for r in results[len(results) // 2 - 1 : len(results) // 2 + 1]) / 2))
    best["runs"] = [r["scores"].get("performance") for r in results]
    return best


psi = {}
for u in urls:
    for device, runs in (("mobile", MOBILE_RUNS), ("desktop", 1)):
        psi.setdefault(u, {})[device] = median_run(u, device, runs)
        s = psi[u][device].get("scores", {})
        print(f"{device:7} perf {s.get('performance', '—'):>3} runs {psi[u][device].get('runs')}  {u}", flush=True)

crawl["psi"] = psi
json.dump(crawl, open(CRAWL, "w"), indent=1)
