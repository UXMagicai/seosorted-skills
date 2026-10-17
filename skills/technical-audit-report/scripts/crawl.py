import json
import re
import sys
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup

_arg = sys.argv[1] if "://" in sys.argv[1] else "https://" + sys.argv[1]
OUT = sys.argv[2]
APEX = urlparse(_arg).netloc.lower().removeprefix("www.")
WWW = "www." + APEX
HOSTS = {APEX, WWW}
START = [f"https://{APEX}/", f"https://{WWW}/"]
UA = "Mozilla/5.0 (compatible; SEOsortedAudit/1.0; +https://seosorted.ai)"
MAX_PAGES = int(sys.argv[3]) if len(sys.argv) > 3 else 300
S = requests.Session()
S.headers["User-Agent"] = UA

SEC_HEADERS = [
    "strict-transport-security",
    "content-security-policy",
    "x-content-type-options",
    "x-frame-options",
    "referrer-policy",
    "permissions-policy",
]


def norm(u):
    u, _ = urldefrag(u)
    p = urlparse(u)
    host = p.netloc.lower()
    if host in HOSTS:
        host = PRIMARY
    path = p.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return f"https://{host}{path}" + (f"?{p.query}" if p.query else "")


def fetch(url, method="GET", allow_redirects=True, ua=None):
    t = time.time()
    try:
        r = S.request(
            method,
            url,
            allow_redirects=allow_redirects,
            timeout=25,
            headers={"User-Agent": ua} if ua else None,
        )
        return r, int((time.time() - t) * 1000), None
    except Exception as e:
        return None, int((time.time() - t) * 1000), str(e)


def chain(url):
    hops = []
    cur = url
    for _ in range(10):
        r, ms, err = fetch(cur, allow_redirects=False)
        if err:
            hops.append({"url": cur, "status": None, "error": err})
            break
        hops.append({"url": cur, "status": r.status_code, "location": r.headers.get("location")})
        if r.status_code in (301, 302, 303, 307, 308) and r.headers.get("location"):
            cur = urljoin(cur, r.headers["location"])
            continue
        break
    return hops


def analyze(url, r, ms):
    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text(" ", strip=True)
    title = soup.title.get_text(strip=True) if soup.title else ""
    md = soup.find("meta", attrs={"name": re.compile("^description$", re.I)})
    robots = soup.find("meta", attrs={"name": re.compile("^robots$", re.I)})
    canon = soup.find("link", rel=lambda v: v and "canonical" in v)
    html = soup.find("html")
    og = {m.get("property"): m.get("content") for m in soup.find_all("meta", property=re.compile("^og:"))}
    tw = {m.get("name"): m.get("content") for m in soup.find_all("meta", attrs={"name": re.compile("^twitter:")})}
    ld = []
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(s.string or "")
            items = data if isinstance(data, list) else data.get("@graph", [data]) if isinstance(data, dict) else []
            for it in items:
                if isinstance(it, dict):
                    t = it.get("@type")
                    ld.extend(t if isinstance(t, list) else [t])
        except Exception:
            ld.append("INVALID_JSON")
    imgs = []
    for im in soup.find_all("img"):
        src = im.get("src") or im.get("data-src") or ""
        imgs.append(
            {
                "src": urljoin(url, src) if src else "",
                "alt": im.get("alt"),
                "width": im.get("width"),
                "height": im.get("height"),
                "loading": im.get("loading"),
            }
        )
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue
        absu = urljoin(url, href)
        links.append(
            {
                "href": absu,
                "text": a.get_text(" ", strip=True)[:120],
                "rel": " ".join(a.get("rel") or []),
                "internal": urlparse(absu).netloc.lower() in HOSTS,
            }
        )
    hreflang = [l.get("hreflang") for l in soup.find_all("link", rel="alternate") if l.get("hreflang")]
    mixed = [u for u in re.findall(r'(?:src|href)="(http://[^"]+)"', r.text)]
    return {
        "url": url,
        "final_url": r.url,
        "status": r.status_code,
        "ms": ms,
        "bytes": len(r.content),
        "content_type": r.headers.get("content-type", ""),
        "x_robots": r.headers.get("x-robots-tag", ""),
        "cache_control": r.headers.get("cache-control", ""),
        "server": r.headers.get("server", ""),
        "security": {h: r.headers.get(h, "") for h in SEC_HEADERS},
        "title": title,
        "meta_description": md.get("content", "").strip() if md else "",
        "meta_robots": robots.get("content", "") if robots else "",
        "canonical": canon.get("href", "") if canon else "",
        "lang": html.get("lang", "") if html else "",
        "viewport": bool(soup.find("meta", attrs={"name": "viewport"})),
        "h1": [h.get_text(" ", strip=True) for h in soup.find_all("h1")],
        "h2": [h.get_text(" ", strip=True) for h in soup.find_all("h2")],
        "h3_count": len(soup.find_all("h3")),
        "word_count": len(text.split()),
        "og": og,
        "twitter": tw,
        "jsonld_types": ld,
        "hreflang": hreflang,
        "images": imgs,
        "links": links,
        "mixed_content": mixed,
        "scripts": len(soup.find_all("script")),
        "stylesheets": len(soup.find_all("link", rel="stylesheet")),
    }


PRIMARY = APEX


def detect_primary():
    global PRIMARY
    for start in START:
        r, _, _ = fetch(start)
        if r is not None and r.status_code < 400 and urlparse(r.url).netloc.lower() in HOSTS:
            PRIMARY = urlparse(r.url).netloc.lower()
            return


def main():
    detect_primary()
    result = {"pages": [], "redirects": {}, "links": {}, "site": {"primary_host": PRIMARY, "alt_host": WWW if PRIMARY == APEX else APEX}}
    seen, q = set(), deque()
    r, _, _ = fetch(f"https://{PRIMARY}/sitemap.xml")
    sitemap_urls = re.findall(r"<loc>([^<]+)</loc>", r.text) if r is not None else []
    result["site"]["sitemap_status"] = r.status_code if r is not None else None
    result["site"]["sitemap_urls"] = sitemap_urls
    for u in START + sitemap_urls:
        n = norm(u)
        if n not in seen:
            seen.add(n)
            q.append(n)
    while q and len(result["pages"]) < MAX_PAGES:
        url = q.popleft()
        r, ms, err = fetch(url)
        if err or r is None:
            result["pages"].append({"url": url, "status": None, "error": err})
            continue
        if "html" not in r.headers.get("content-type", ""):
            result["pages"].append({"url": url, "status": r.status_code, "content_type": r.headers.get("content-type", ""), "non_html": True})
            continue
        page = analyze(url, r, ms)
        page["depth_hint"] = None
        result["pages"].append(page)
        for l in page["links"]:
            if l["internal"]:
                n = norm(l["href"])
                if n not in seen and not re.search(r"\.(pdf|png|jpe?g|gif|svg|webp|zip|mp4)$", n, re.I):
                    seen.add(n)
                    q.append(n)

    for u in [f"http://{APEX}/", f"http://{WWW}/", f"https://{APEX}/", f"https://{WWW}/"] + [
        s for s in sitemap_urls
    ]:
        result["redirects"][u] = chain(u)

    targets = set()
    for p in result["pages"]:
        for l in p.get("links", []):
            targets.add(l["href"])
        for im in p.get("images", []):
            if im["src"]:
                targets.add(im["src"])

    def check(u):
        r, ms, err = fetch(u, method="HEAD")
        if r is not None and r.status_code in (403, 405, 400):
            r, ms, err = fetch(u)
        return u, (r.status_code if r is not None else None), (r.url if r is not None else ""), err, ms

    with ThreadPoolExecutor(8) as ex:
        for u, st, fin, err, ms in ex.map(check, sorted(targets)):
            result["links"][u] = {"status": st, "final": fin, "error": err, "ms": ms}

    site = result["site"]
    for path in ["/robots.txt", "/llms.txt", "/favicon.ico", "/sitemap_index.xml", "/.well-known/security.txt", "/humans.txt"]:
        r, ms, err = fetch(f"https://{PRIMARY}" + path)
        site[path] = {"status": r.status_code if r is not None else None, "body": (r.text[:3000] if r is not None and r.status_code == 200 else ""), "ctype": r.headers.get("content-type", "") if r is not None else ""}
    r, _, _ = fetch(f"https://{PRIMARY}/this-page-should-not-exist-seosorted-404-check")
    site["soft404"] = {"status": r.status_code if r is not None else None, "title": BeautifulSoup(r.text, "html.parser").title.get_text(strip=True) if r is not None and BeautifulSoup(r.text, "html.parser").title else ""}
    bots = {
        "Googlebot": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Bingbot": "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "GPTBot": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.1; +https://openai.com/gptbot",
        "OAI-SearchBot": "Mozilla/5.0 (compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot)",
        "ChatGPT-User": "Mozilla/5.0 (compatible; ChatGPT-User/1.0; +https://openai.com/bot)",
        "ClaudeBot": "Mozilla/5.0 (compatible; ClaudeBot/1.0; +claudebot@anthropic.com)",
        "PerplexityBot": "Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)",
        "Google-Extended": "Mozilla/5.0 (compatible; Google-Extended)",
        "CCBot": "CCBot/2.0 (https://commoncrawl.org/faq/)",
    }
    site["bots"] = {}
    for name, ua in bots.items():
        r, ms, err = fetch(f"https://{PRIMARY}/", ua=ua)
        site["bots"][name] = {"status": r.status_code if r is not None else None, "bytes": len(r.content) if r is not None else 0, "ms": ms, "error": err}

    json.dump(result, open(OUT, "w"), indent=1, default=str)
    print(json.dumps({"primary_host": PRIMARY, "pages": len(result["pages"]), "links": len(result["links"])}))


main()
