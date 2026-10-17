import json
import os
import sys
from collections import Counter, defaultdict
from datetime import date
from urllib.parse import urlparse

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

D, OUT = sys.argv[1], sys.argv[2]
audit = json.load(open(f"{D}/audit.json")) if os.path.exists(f"{D}/audit.json") else {}
crawl = json.load(open(f"{D}/crawl.json"))

BRAND = "FF4D00"
INK = "1E1E1E"
HDR = PatternFill("solid", fgColor=INK)
HFONT = Font(bold=True, color="FFFFFF")
SEV = {
    "Critical": PatternFill("solid", fgColor="F8D7DA"),
    "High": PatternFill("solid", fgColor="FDE2CF"),
    "Medium": PatternFill("solid", fgColor="FFF3CD"),
    "Low": PatternFill("solid", fgColor="E2F0D9"),
    "Info": PatternFill("solid", fgColor="E7EEF8"),
}
THIN = Border(bottom=Side(style="thin", color="DDDDDD"))
WRAP = Alignment(wrap_text=True, vertical="top")

pages = [p for p in crawl["pages"] if p.get("status") == 200 and not p.get("non_html")]
by_url = {}
for p in pages:
    by_url.setdefault(p["url"], p)
pages = list(by_url.values())
links = crawl["links"]
psi = crawl.get("psi", {})
site = crawl["site"]
sitemap_urls = site.get("sitemap_urls", [])
_first = urlparse(crawl["pages"][0]["url"]).netloc.lower() if crawl.get("pages") else ""
PRIMARY = site.get("primary_host") or _first
ALT = site.get("alt_host") or (PRIMARY[4:] if PRIMARY.startswith("www.") else "www." + PRIMARY)
BASE = f"https://{PRIMARY}"
NAME = sys.argv[3] if len(sys.argv) > 3 else PRIMARY


def host(u):
    return urlparse(u).netloc.lower()


def sheet(wb, title, headers, rows, widths=None, sev_col=None, tab=None):
    ws = wb.create_sheet(title)
    if tab:
        ws.sheet_properties.tabColor = tab
    ws.append(headers)
    for r in rows:
        ws.append(["" if v is None else v for v in r])
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c)
        cell.fill, cell.font = HDR, HFONT
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(c)].width = (widths or {}).get(c, 18)
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = WRAP
            cell.border = THIN
    if sev_col and rows:
        for r in range(2, len(rows) + 2):
            v = ws.cell(row=r, column=sev_col).value
            if v in SEV:
                ws.cell(row=r, column=sev_col).fill = SEV[v]
                ws.cell(row=r, column=sev_col).font = Font(bold=True)
    ws.freeze_panes = "B2" if len(headers) > 3 else "A2"
    if rows:
        ref = f"A1:{get_column_letter(len(headers))}{len(rows) + 1}"
        t = Table(displayName="T_" + "".join(ch for ch in title if ch.isalnum()), ref=ref)
        t.tableStyleInfo = TableStyleInfo(name="TableStyleLight1", showRowStripes=True)
        ws.add_table(t)
    ws.row_dimensions[1].height = 30
    return ws


issues = []


def add(sev, cat, title, detail, affected, fix, effort, impact, evidence=""):
    issues.append([sev, cat, title, detail, affected, fix, effort, impact, evidence])


canon_targets = Counter(p.get("canonical", "") for p in pages)
canon_www = [p for p in pages if host(p.get("canonical", "")) == ALT]
canon_home = [p for p in pages if p.get("canonical", "").rstrip("/") in (f"https://{ALT}", BASE) and p["url"].rstrip("/") not in (BASE,)]
www_chain = crawl["redirects"].get(f"https://{ALT}/", [])
http_chain = crawl["redirects"].get(f"http://{ALT}/", [])

if canon_www:
    add(
        "Critical",
        "Indexing / Canonicals",
        "Canonical tags point to www, but www redirects to the non-www site",
        f"{len(canon_www)} of {len(pages)} pages declare a canonical on https://{ALT}, yet that host returns {www_chain[0].get('status') if www_chain else 'a redirect'} → {BASE}. Google sees the canonical URL redirecting away, so it has to guess which URL is real; this splits signals and can delay or prevent indexing.",
        len(canon_www),
        f"Pick ONE host (recommended: keep {BASE}, since that is what the server already serves). Set every canonical, sitemap <loc>, robots.txt Sitemap line, Open Graph og:url and internal link to that host. In Next.js set metadataBase to the chosen host.",
        "Low (config)",
        "High",
        "; ".join(f"{p['url']} → {p['canonical']}" for p in canon_www[:8]),
    )
if canon_home:
    add(
        "Critical",
        "Indexing / Canonicals",
        "Inner pages canonicalise to the homepage",
        f"{len(canon_home)} inner pages set their canonical to the homepage, which tells Google they are duplicates of it. These pages will likely never rank in their own right.",
        len(canon_home),
        "Give every page a self-referencing canonical (its own URL on the chosen host). In the Next.js App Router, set alternates.canonical per page in generateMetadata, not once in the root layout.",
        "Low",
        "High",
        "; ".join(f"{p['url']} → {p['canonical']}" for p in canon_home[:8]),
    )
if www_chain and www_chain[0].get("status") in (302, 303, 307):
    add(
        "High",
        "Redirects",
        f"{ALT} → {PRIMARY} uses a temporary {www_chain[0].get('status')} redirect",
        "Temporary redirects (302/307) tell search engines the move is not permanent, so link equity and indexing signals are not consolidated as reliably as with a 301/308.",
        1,
        f"In your host/CDN domain settings (e.g. Vercel → Project → Domains, Cloudflare redirect rules), make {ALT} redirect to {PRIMARY} with a permanent 301/308 redirect.",
        "Low (config)",
        "Medium",
        " → ".join(f"{h['url']} [{h.get('status')}]" for h in www_chain),
    )
sm_www = [u for u in sitemap_urls if host(u) == ALT]
if sm_www:
    add(
        "High",
        "Sitemap",
        ("Every sitemap URL redirects" if len(sm_www) == len(sitemap_urls) else "Sitemap URLs that redirect"),
        f"{len(sm_www)} of {len(sitemap_urls)} URLs in sitemap.xml use https://{ALT}, which redirects. Sitemaps should list only final, 200-status, canonical URLs; redirecting entries are reported in Search Console as 'Page with redirect' and are deprioritised.",
        len(sm_www),
        "Generate sitemap.xml with the chosen host (non-www). Also update lastmod to the real modification date per page instead of one shared timestamp.",
        "Low",
        "Medium",
        ", ".join(sm_www[:10]),
    )
robots_body = site.get("/robots.txt", {}).get("body", "")
if f"{ALT}/sitemap.xml" in robots_body:
    add("Medium", "Robots.txt", f"robots.txt Sitemap line points at the redirecting host {ALT}", "Crawlers follow the redirect, but the directive should name the canonical sitemap URL.", 1, f"Change to: Sitemap: {BASE}/sitemap.xml", "Low", "Low", robots_body.strip()[:300])
def _path(u):
    q = urlparse(u)
    return (q.path.rstrip("/") or "/") + (f"?{q.query}" if q.query else "")


sm_paths = {_path(u) for u in sitemap_urls if host(u) in (PRIMARY, ALT)}
real_missing = [p["url"] for p in pages if _path(p["url"]) not in sm_paths]
if real_missing:
    add("Medium", "Sitemap", "Indexable pages not listed in the sitemap", "These pages were reachable through internal links but are not in sitemap.xml at all (on either host).", len(real_missing), "Add them to the sitemap generator.", "Low", "Medium", ", ".join(real_missing))

titles = defaultdict(list)
descs = defaultdict(list)
for p in pages:
    titles[p.get("title", "")].append(p["url"])
    descs[p.get("meta_description", "")].append(p["url"])
dup_t = {t: u for t, u in titles.items() if t and len(u) > 1}
dup_d = {t: u for t, u in descs.items() if t and len(u) > 1}
if dup_t:
    add("High", "On-page", "Duplicate title tags", f"{sum(len(u) for u in dup_t.values())} pages share {len(dup_t)} titles.", sum(len(u) for u in dup_t.values()), "Write a unique, descriptive title for each page.", "Low", "Medium", " | ".join(f"'{t}': {', '.join(u)}" for t, u in dup_t.items()))
if dup_d:
    add("Medium", "On-page", "Duplicate meta descriptions", f"{sum(len(u) for u in dup_d.values())} pages share {len(dup_d)} descriptions.", sum(len(u) for u in dup_d.values()), "Write a unique description (120–155 chars) per page.", "Low", "Medium", " | ".join(f"'{t[:60]}…': {', '.join(u)}" for t, u in dup_d.items()))
no_desc = [p["url"] for p in pages if not p.get("meta_description")]
if no_desc:
    add("High", "On-page", "Missing meta description", "Google will auto-generate a snippet, usually less compelling.", len(no_desc), "Add a 120–155 character description summarising the page and its value.", "Low", "Medium", ", ".join(no_desc))
long_t = [f"{p['url']} ({len(p.get('title',''))})" for p in pages if len(p.get("title", "")) > 60]
short_t = [f"{p['url']} ({len(p.get('title',''))})" for p in pages if 0 < len(p.get("title", "")) < 30]
if long_t:
    add("Low", "On-page", "Title tags longer than ~60 characters", "Long titles get truncated in search results, often cutting the brand or key message.", len(long_t), "Keep titles to 50–60 characters; put the primary keyword first and the brand last.", "Low", "Low", "; ".join(long_t))
if short_t:
    add("Low", "On-page", "Title tags shorter than 30 characters", "Short titles waste ranking and click-through opportunity.", len(short_t), "Expand with a descriptive keyword phrase.", "Low", "Low", "; ".join(short_t))
bad_d = [f"{p['url']} ({len(p.get('meta_description',''))})" for p in pages if p.get("meta_description") and not 70 <= len(p["meta_description"]) <= 160]
if bad_d:
    add("Low", "On-page", "Meta descriptions outside 70–160 characters", "Too long gets truncated; too short under-sells the page.", len(bad_d), "Aim for 120–155 characters.", "Low", "Low", "; ".join(bad_d))
h1_issues = [f"{p['url']} (H1 count {len(p.get('h1', []))})" for p in pages if len(p.get("h1", [])) != 1]
if h1_issues:
    add("Medium", "On-page", "Pages without exactly one H1", "Each page should have one clear H1 describing its topic.", len(h1_issues), "Ensure a single, keyword-led H1 per page; demote extra H1s to H2.", "Low", "Medium", "; ".join(h1_issues))
thin = [f"{p['url']} ({p.get('word_count')} words)" for p in pages if p.get("word_count", 0) < 300]
if thin:
    add("Medium", "Content", "Thin pages (under 300 words of visible text)", "Little text gives search and AI engines little to understand or quote.", len(thin), "Expand with problem/solution copy, FAQs and examples relevant to the page's query.", "Medium", "Medium", "; ".join(thin))
no_lang = [p["url"] for p in pages if not p.get("lang")]
if no_lang:
    add("Low", "Technical", "Missing <html lang>", "Helps search engines and screen readers.", len(no_lang), 'Set <html lang="en">.', "Low", "Low", ", ".join(no_lang))
no_vp = [p["url"] for p in pages if not p.get("viewport")]
if no_vp:
    add("High", "Mobile", "Missing viewport meta tag", "Pages may not render correctly on mobile (mobile-first indexing).", len(no_vp), 'Add <meta name="viewport" content="width=device-width, initial-scale=1">.', "Low", "High", ", ".join(no_vp))

no_og = [p["url"] for p in pages if not p.get("og", {}).get("og:title") or not p.get("og", {}).get("og:image")]
if no_og:
    add("Medium", "Social / Sharing", "Missing Open Graph title or image", "Links shared on LinkedIn, Slack, X etc. render without a proper preview card.", len(no_og), "Add og:title, og:description, og:image (1200×630) and og:url (canonical host) on every page.", "Low", "Medium", ", ".join(no_og))
og_www = [p["url"] for p in pages if host(p.get("og", {}).get("og:url", "") or "") == ALT]
if og_www:
    add("Low", "Social / Sharing", f"og:url uses the redirecting host {ALT}", "Should match the canonical host.", len(og_www), f"Set og:url to the {PRIMARY} URL of each page.", "Low", "Low", ", ".join(og_www))
no_tw = [p["url"] for p in pages if not p.get("twitter", {}).get("twitter:card")]
if no_tw:
    add("Low", "Social / Sharing", "Missing Twitter/X card tags", "X falls back to Open Graph but twitter:card controls the layout.", len(no_tw), "Add twitter:card = summary_large_image.", "Low", "Low", ", ".join(no_tw))

types = Counter(t for p in pages for t in p.get("jsonld_types", []) if t)
no_ld = [p["url"] for p in pages if not p.get("jsonld_types")]
if "Organization" not in types:
    add("Medium", "Structured data", "No Organization schema", "Organization markup (name, logo, sameAs links) feeds Google's knowledge panel and helps AI engines identify the brand.", 1, "Add Organization JSON-LD on the homepage with name, url, logo and sameAs (LinkedIn, X).", "Low", "Medium", f"Types found: {dict(types) or 'none'}")
if "BreadcrumbList" not in types:
    add("Low", "Structured data", "No BreadcrumbList schema", "Breadcrumb markup gives richer search snippets and clarifies site hierarchy.", len(pages) - 1, "Add BreadcrumbList JSON-LD to inner pages (Home › Section › Page).", "Low", "Low", "")
if no_ld:
    add("Low", "Structured data", "Pages with no structured data", "Consider WebPage/Article/Product/SoftwareApplication or FAQPage where appropriate.", len(no_ld), "Add relevant JSON-LD per page type.", "Low", "Low", ", ".join(no_ld))
if "INVALID_JSON" in types:
    add("High", "Structured data", "Invalid JSON-LD", "Malformed JSON-LD is ignored by Google.", types["INVALID_JSON"], "Validate with https://validator.schema.org and fix syntax.", "Low", "Medium", "")

broken = {u: v for u, v in links.items() if (v.get("status") is None or (v.get("status") or 0) >= 400) and v.get("status") != 999}
internal_broken = {u: v for u, v in broken.items() if host(u) in (PRIMARY, ALT)}
external_broken = {u: v for u, v in broken.items() if u not in internal_broken}
src_map = defaultdict(set)
for p in pages:
    for l in p.get("links", []):
        src_map[l["href"]].add(p["url"])
    for im in p.get("images", []):
        if im["src"]:
            src_map[im["src"]].add(p["url"])
if internal_broken:
    add("Critical", "Links", "Broken internal links / resources", "Internal URLs returning errors waste crawl budget and frustrate visitors.", len(internal_broken), "Fix or remove the links; 301-redirect removed pages to the closest equivalent.", "Low", "High", "; ".join(f"{u} [{v.get('status') or v.get('error')}] on {', '.join(sorted(src_map[u]))[:120]}" for u, v in list(internal_broken.items())[:20]))
if external_broken:
    add("Medium", "Links", "Broken outbound links", "Outbound links to dead pages look unmaintained to users and quality raters.", len(external_broken), "Update or remove the links.", "Low", "Low", "; ".join(f"{u} [{v.get('status') or v.get('error')}]" for u, v in list(external_broken.items())[:20]))
int_www = sorted({l["href"] for p in pages for l in p.get("links", []) if host(l["href"]) == ALT})
if int_www:
    add("Medium", "Links", f"Internal links point to the redirecting host {ALT}", "Every such click/crawl goes through an extra redirect hop.", len(int_www), "Use relative links or the canonical host in navigation and content.", "Low", "Low", ", ".join(int_www[:15]))

imgs = [(p["url"], im) for p in pages for im in p.get("images", [])]
no_alt = [(u, im) for u, im in imgs if im.get("alt") is None]
empty_alt = [(u, im) for u, im in imgs if im.get("alt") == ""]
no_dim = [(u, im) for u, im in imgs if not (im.get("width") and im.get("height"))]
if no_alt:
    add("Medium", "Images / Accessibility", "Images missing alt attribute", "Alt text is an accessibility requirement and an image-search signal.", len(no_alt), "Add descriptive alt text; use alt=\"\" only for purely decorative images.", "Low", "Medium", "; ".join(f"{im['src']} on {u}" for u, im in no_alt[:15]))
if no_dim:
    add("Low", "Performance", "Images without width/height", "Missing dimensions cause layout shift (CLS) while images load.", len(no_dim), "Use next/image or set explicit width and height.", "Low", "Low", "; ".join(f"{im['src']} on {u}" for u, im in no_dim[:15]))

sec = pages[0].get("security", {}) if pages else {}
missing_sec = [h for h, v in sec.items() if not v]
if missing_sec:
    add("Medium", "Security headers", "Missing recommended security headers", "Not a direct ranking factor, but part of Lighthouse Best Practices and enterprise security reviews.", len(missing_sec), "Add in next.config.js headers(): " + ", ".join(missing_sec), "Low", "Low", ", ".join(missing_sec))
mixed = sorted({m for p in pages for m in p.get("mixed_content", [])})
if mixed:
    add("Medium", "Security", "Insecure http:// references (mixed content)", "Browsers may block or warn.", len(mixed), "Change to https://.", "Low", "Medium", ", ".join(mixed[:15]))

llms = site.get("/llms.txt", {})
if llms.get("status") != 200:
    add("Medium", "AI search (GEO)", "No /llms.txt", "llms.txt gives AI assistants (ChatGPT, Claude, Perplexity) a concise, curated map of your product and key pages.", 1, "Publish /llms.txt with a one-paragraph product summary and links to your key pages and docs.", "Low", "Medium", f"status {llms.get('status')}")
blocked_bots = {b: v for b, v in site.get("bots", {}).items() if (v.get("status") or 0) >= 400 or v.get("status") is None}
if blocked_bots:
    add("High", "AI search (GEO)", "Crawlers blocked at the server/CDN", "These user-agents received an error, so the site cannot appear in their search/answers.", len(blocked_bots), "Allow them in Vercel Firewall / bot protection unless intentionally blocked.", "Low", "High", ", ".join(f"{b} [{v.get('status')}]" for b, v in blocked_bots.items()))
s404 = site.get("soft404", {})
if s404.get("status") == 200:
    add("High", "Technical", "Soft 404 — unknown URLs return 200", "Non-existent pages should return 404 so Google doesn't index junk URLs.", 1, "Ensure the not-found route returns HTTP 404 (Next.js notFound()).", "Low", "Medium", f"status 200, title '{s404.get('title')}'")
sectxt = site.get("/.well-known/security.txt", {})
if sectxt.get("status") != 200:
    add("Info", "Security", "No /.well-known/security.txt", "Lets researchers report vulnerabilities; expected by many enterprise buyers.", 1, "Publish security.txt with a security contact.", "Low", "Low", "")

slow = [(u, d) for u, d in psi.items() for s, x in d.items() if s == "mobile" and x.get("scores", {}).get("performance", 100) < 90]
home = psi.get(BASE + "/", {}).get("mobile", {})
if home.get("scores") and home["scores"].get("performance", 100) < 90:
    add("High" if home["scores"]["performance"] < 50 else "Medium", "Performance (Core Web Vitals)", f"Homepage mobile performance {home['scores']['performance']}/100 — LCP {home.get('lcp')}", f"The largest element takes {home.get('lcp')} to render on a mid-range phone (Google's 'good' threshold is 2.5 s); TBT {home.get('tbt')}, CLS {home.get('cls')}. The homepage is the main landing page for brand and paid traffic.", 1, "Preload/priority-load the hero image or animation, serve it as AVIF/WebP at mobile size, defer non-critical JavaScript (map/graph libraries) until after first paint, and lazy-load below-the-fold visuals. Details in the 'Lighthouse opportunities' tab.", "Medium", "High", BASE + "/")
inner = {u: d.get("mobile", {}) for u, d in psi.items() if u != BASE + "/" and d.get("mobile", {}).get("scores")}
slow_inner = {u: m for u, m in inner.items() if m["scores"].get("performance", 100) < 90}
if slow_inner:
    lo = min(m["scores"]["performance"] for m in slow_inner.values()); hi = max(m["scores"]["performance"] for m in slow_inner.values())
    add("Low", "Performance (Core Web Vitals)", f"Inner pages score {lo}–{hi} on mobile", "Close to Google's 90+ 'good' band; mostly LCP on mobile. Desktop scores are 89–92.", len(slow_inner), "Same fixes as the homepage, applied to the shared page template.", "Low", "Medium", "; ".join(f"{urlparse(u).path} {m['scores']['performance']} (LCP {m.get('lcp')})" for u, m in sorted(slow_inner.items())))
acc = [(u, d["mobile"]["scores"]["accessibility"]) for u, d in psi.items() if d.get("mobile", {}).get("scores", {}).get("accessibility", 100) < 100]
if acc:
    add("Low", "Accessibility", (f"Accessibility {min(a for _, a in acc)}/100 on all pages" if min(a for _, a in acc) == max(a for _, a in acc) else f"Accessibility {min(a for _, a in acc)}–{max(a for _, a in acc)}/100 across pages"), "Small Lighthouse accessibility failures shared by the template (see 'Lighthouse opportunities').", len(acc), "Fix the listed contrast / label items in the shared layout.", "Low", "Low", "")

seo_issue_score = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "Info": 4}
issues.sort(key=lambda r: (seo_issue_score[r[0]], r[1]))

wb = Workbook()
ws = wb.active
ws.title = "Summary"
ws.sheet_properties.tabColor = BRAND
ws.column_dimensions["A"].width = 34
ws.column_dimensions["B"].width = 70
ws["A1"] = f"{NAME} — Technical SEO Audit"
ws["A1"].font = Font(bold=True, size=18, color=INK)
ws["A2"] = f"Site: {BASE}   ·   Prepared by SEOsorted   ·   {date.today().strftime('%d %B %Y')}"
ws["A2"].font = Font(italic=True, color="666666")
sev_counts = Counter(r[0] for r in issues)
mob = [d.get("mobile", {}).get("scores", {}) for d in psi.values() if d.get("mobile", {}).get("scores")]
desk = [d.get("desktop", {}).get("scores", {}) for d in psi.values() if d.get("desktop", {}).get("scores")]
avg = lambda xs, k: round(sum(x.get(k, 0) for x in xs) / len(xs)) if xs else "n/a"
rows = [
    ("Unique pages crawled", len(pages)),
    ("URLs in sitemap.xml", len(sitemap_urls)),
    ("Links & resources checked", len(links)),
    ("Broken internal / external", f"{len(internal_broken)} / {len(external_broken)}"),
    *([("Keywords ranking (Google)", f"{audit.get('keywordsRanking')}  ·  avg position {audit.get('avgPosition')}")] if audit.get("keywordsRanking") is not None else []),
    ("Avg Lighthouse — mobile", f"Performance {avg(mob,'performance')} · Accessibility {avg(mob,'accessibility')} · Best practices {avg(mob,'best-practices')} · SEO {avg(mob,'seo')}"),
    ("Avg Lighthouse — desktop", f"Performance {avg(desk,'performance')} · Accessibility {avg(desk,'accessibility')} · Best practices {avg(desk,'best-practices')} · SEO {avg(desk,'seo')}"),
    ("Hosting", pages[0].get("server", "") if pages else ""),
    ("Issues found", "  ·  ".join(f"{k}: {sev_counts.get(k,0)}" for k in ["Critical", "High", "Medium", "Low", "Info"])),
]
r = 4
for k, v in rows:
    ws.cell(row=r, column=1, value=k).font = Font(bold=True)
    ws.cell(row=r, column=2, value=v).alignment = WRAP
    r += 1
r += 1
ws.cell(row=r, column=1, value="Top priorities").font = Font(bold=True, size=13, color=BRAND)
r += 1
for i, row in enumerate([x for x in issues if x[0] in ("Critical", "High")][:8], 1):
    ws.cell(row=r, column=1, value=f"{i}. [{row[0]}] {row[1]}").font = Font(bold=True)
    ws.cell(row=r, column=2, value=f"{row[2]} — {row[5]}").alignment = WRAP
    ws.row_dimensions[r].height = 45
    r += 1
r += 1
ws.cell(row=r, column=1, value="How to read this workbook").font = Font(bold=True, size=13, color=BRAND)
r += 1
for k, v in [
    ("Issues", "Every finding, prioritised, with the fix, effort and expected impact."),
    ("Pages", "One row per page: status, speed, title/description, canonical, headings, word count, schema."),
    ("Performance", "Google PageSpeed (Lighthouse) scores and Core Web Vitals for mobile and desktop."),
    ("Lighthouse opportunities", "The specific failing Lighthouse audits per page."),
    ("Links", "Every internal and outbound link with its HTTP status."),
    ("Images", "Every image with alt text and dimension checks."),
    ("Redirects", "Redirect chains for http/https and www/non-www variants and every sitemap URL."),
    ("Crawlability & AI", "robots.txt, sitemap, llms.txt, soft-404 test and access for Google, Bing and AI crawlers."),
    ("Security headers", "HTTP security headers present/missing."),
    ("Structured data", "JSON-LD schema types per page."),
]:
    ws.cell(row=r, column=1, value=k).font = Font(bold=True)
    ws.cell(row=r, column=2, value=v).alignment = WRAP
    r += 1

sheet(
    wb,
    "Issues",
    ["Priority", "Area", "Issue", "Why it matters", "Pages / items affected", "How to fix", "Effort", "Impact", "Evidence"],
    issues,
    {1: 11, 2: 20, 3: 42, 4: 60, 5: 12, 6: 60, 7: 12, 8: 10, 9: 70},
    sev_col=1,
    tab="C00000",
)

prow = []
for p in sorted(pages, key=lambda x: x["url"]):
    m = psi.get(p["url"], {}).get("mobile", {}).get("scores", {})
    prow.append(
        [
            p["url"], p["status"], p.get("ms"), round(p.get("bytes", 0) / 1024, 1), p.get("title"), len(p.get("title", "")),
            p.get("meta_description"), len(p.get("meta_description", "")), p.get("canonical"),
            "Yes" if p.get("canonical", "").rstrip("/") == p["url"].rstrip("/") else "No",
            p.get("meta_robots") or p.get("x_robots") or "index, follow (default)", len(p.get("h1", [])), " | ".join(p.get("h1", []))[:200],
            len(p.get("h2", [])), p.get("word_count"), len([l for l in p.get("links", []) if l["internal"]]), len([l for l in p.get("links", []) if not l["internal"]]),
            len(p.get("images", [])), len([i for i in p.get("images", []) if i.get("alt") is None]), ", ".join(t for t in p.get("jsonld_types", []) if t) or "—",
            "Yes" if p.get("og", {}).get("og:image") else "No", p.get("lang"), "Yes" if any(p["url"].rstrip("/").replace("https://", "") == s.replace("https://www.", "").replace("https://", "").rstrip("/") for s in sitemap_urls) else "No",
            m.get("performance"), m.get("seo"),
        ]
    )
sheet(
    wb,
    "Pages",
    ["URL", "Status", "Response ms", "HTML KB", "Title", "Title len", "Meta description", "Desc len", "Canonical", "Self-canonical", "Robots", "H1 count", "H1 text", "H2 count", "Words", "Internal links", "External links", "Images", "Images no alt", "Schema types", "OG image", "lang", "In sitemap", "Mobile perf", "Mobile SEO"],
    prow,
    {1: 45, 5: 40, 7: 50, 9: 38, 11: 22, 13: 40, 20: 26},
    tab="2E75B6",
)

perf = []
opps = []
for u, d in sorted(psi.items()):
    for strat in ("mobile", "desktop"):
        x = d.get(strat, {})
        sc = x.get("scores", {})
        perf.append([u, strat.title(), sc.get("performance"), sc.get("accessibility"), sc.get("best-practices"), sc.get("seo"), x.get("lcp"), x.get("fcp"), x.get("tbt"), x.get("cls"), x.get("si"), x.get("tti"), ", ".join(f"{k}: {v}" for k, v in (x.get("field") or {}).items()) or "Not enough real-user data", x.get("error") or (f"Median of runs {x['runs']}" if x.get("runs") and len(x["runs"]) > 1 else "")])
        for f in x.get("failing", []):
            opps.append([u, strat.title(), f.get("title"), f.get("display"), round((f.get("score") or 0) * 100), f.get("savings_ms")])
ws = sheet(wb, "Performance", ["URL", "Device", "Performance", "Accessibility", "Best practices", "SEO", "LCP", "FCP", "TBT", "CLS", "Speed index", "TTI", "Real-user (CrUX) field data", "Note"], perf, {1: 45, 13: 40}, tab="70AD47")
for col in "CDEF":
    ws.conditional_formatting.add(f"{col}2:{col}{len(perf)+1}", CellIsRule(operator="lessThan", formula=["50"], fill=SEV["Critical"]))
    ws.conditional_formatting.add(f"{col}2:{col}{len(perf)+1}", CellIsRule(operator="between", formula=["50", "89"], fill=SEV["Medium"]))
    ws.conditional_formatting.add(f"{col}2:{col}{len(perf)+1}", CellIsRule(operator="greaterThanOrEqual", formula=["90"], fill=SEV["Low"]))
sheet(wb, "Lighthouse opportunities", ["URL", "Device", "Audit", "Value", "Score", "Est. savings (ms)"], sorted(opps, key=lambda r: (r[0], r[1], -(r[5] or 0))), {1: 45, 3: 50, 4: 30}, tab="70AD47")

lrows = []
for u, v in sorted(links.items()):
    kind = "Internal" if host(u) in (PRIMARY, ALT) else "External"
    lrows.append([u, kind, ("999 (LinkedIn blocks bots — link works in a browser)" if v.get("status") == 999 else (v.get("status") or "ERROR")), v.get("final") if v.get("final") and v.get("final") != u else "", v.get("ms"), v.get("error") or "", ", ".join(sorted(src_map[u]))[:300]])
ws = sheet(wb, "Links", ["URL", "Type", "Status", "Redirects to", "ms", "Error", "Found on"], lrows, {1: 60, 4: 45, 7: 60}, tab="7030A0")

irows = [[im["src"], u, "MISSING" if im.get("alt") is None else ("(empty)" if im.get("alt") == "" else im.get("alt")), im.get("width") or "", im.get("height") or "", im.get("loading") or "", links.get(im["src"], {}).get("status", "")] for u, im in imgs]
sheet(wb, "Images", ["Image", "Page", "Alt text", "Width", "Height", "loading", "Status"], irows, {1: 60, 2: 40, 3: 40}, tab="7030A0")

rrows = []
for start, hops in crawl["redirects"].items():
    rrows.append([start, len(hops) - 1, " → ".join(f"{h['url']} [{h.get('status')}]" for h in hops), hops[-1].get("status") if hops else ""])
sheet(wb, "Redirects", ["Start URL", "Hops", "Chain", "Final status"], rrows, {1: 45, 3: 110}, tab="BF8F00")

crows = []
for path in ["/robots.txt", "/sitemap_index.xml", "/llms.txt", "/favicon.ico", "/.well-known/security.txt", "/humans.txt"]:
    v = site.get(path, {})
    crows.append(["File", path, v.get("status"), (v.get("body") or "").strip()[:500]])
crows.append(["File", "/sitemap.xml", site.get("sitemap_status"), f"{len(sitemap_urls)} URLs: " + ", ".join(sitemap_urls)])
crows.append(["Test", "Unknown URL (soft-404 check)", s404.get("status"), s404.get("title")])
for b, v in site.get("bots", {}).items():
    crows.append(["Crawler access", b, v.get("status"), f"{v.get('bytes')} bytes in {v.get('ms')} ms" + (f" — {v.get('error')}" if v.get("error") else "")])
sheet(wb, "Crawlability & AI", ["Check", "Item", "HTTP status", "Detail"], crows, {2: 32, 4: 110}, tab="BF8F00")

srows = [[h, v or "MISSING", "OK" if v else "Add"] for h, v in sec.items()]
srows += [["server", pages[0].get("server") if pages else "", "Info"], ["cache-control (HTML)", pages[0].get("cache_control") if pages else "", "Info"]]
sheet(wb, "Security headers", ["Header", "Value", "Status"], srows, {1: 30, 2: 80}, tab="595959")

ld_rows = [[p["url"], ", ".join(t for t in p.get("jsonld_types", []) if t) or "None", ", ".join(p.get("hreflang", [])) or "—", p.get("og", {}).get("og:type", ""), p.get("og", {}).get("og:url", ""), p.get("twitter", {}).get("twitter:card", "")] for p in sorted(pages, key=lambda x: x["url"])]
sheet(wb, "Structured data", ["URL", "JSON-LD types", "hreflang", "og:type", "og:url", "twitter:card"], ld_rows, {1: 45, 2: 40, 5: 45}, tab="595959")

wb.save(OUT)
print("saved", OUT, "issues", len(issues), dict(sev_counts))
