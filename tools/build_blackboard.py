#!/usr/bin/env python3
"""Render a Macro Monitor weekly blackboard snapshot (markdown) into a styled HTML page."""
import sys, re, markdown

SRC = sys.argv[1] if len(sys.argv) > 1 else "/agent/workspace/site/blackboard_src/2026-W24.md"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/agent/workspace/site/blackboard/2026-W24.html"
WEEK_LABEL   = sys.argv[3] if len(sys.argv) > 3 else "2026 · W24"
WEEK_ENDING  = sys.argv[4] if len(sys.argv) > 4 else "Week ending 12 June 2026"
DATA_ASOF    = sys.argv[5] if len(sys.argv) > 5 else "12 Jun 2026"
REPORT_HREF  = sys.argv[6] if len(sys.argv) > 6 else "../reports/2026-W24.html"

md_text = open(SRC, encoding="utf-8").read()
body = markdown.markdown(md_text, extensions=["tables", "sane_lists"])

# every external link opens in a new tab
body = re.sub(r'<a href="(https?://[^"]+)"',
              r'<a href="\1" target="_blank" rel="noopener noreferrer"', body)
# make wide tables horizontally scrollable on small screens
body = body.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Macro Monitor — Detailed Blackboard · __WEEK__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{--navy:#0f2a4a;--blue:#1f5fa8;--ink:#1a2230;--muted:#5b6776;--line:#e2e7ee;--soft:#f4f6f9;--bg:#e7eaef;}
  *{box-sizing:border-box;} html,body{margin:0;padding:0;}
  body{background:var(--bg);color:var(--ink);font-family:'Inter',-apple-system,system-ui,sans-serif;
    line-height:1.55;-webkit-font-smoothing:antialiased;padding:0 0 0;}
  .nav{background:var(--navy);color:#fff;}
  .nav .in{width:min(1000px,94vw);margin:0 auto;padding:14px 0;display:flex;align-items:center;justify-content:space-between;}
  .nav .brand{display:flex;align-items:center;gap:11px;}
  .nav .dot{width:30px;height:30px;border-radius:7px;background:#fff;color:var(--navy);display:flex;align-items:center;justify-content:center;font-size:16px;}
  .nav .nm{font-weight:700;font-size:15px;letter-spacing:-.01em;}
  .nav a.back{color:#9fc0e6;text-decoration:none;font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.04em;}
  .nav a.back:hover{color:#fff;}
  .page{width:min(1000px,94vw);background:#fff;margin:30px auto 0;padding:48px 60px 52px;
    border-top:4px solid var(--navy);box-shadow:0 2px 26px rgba(15,42,74,.11);}
  @media(max-width:640px){.page{padding:32px 22px 40px;}}
  .kicker{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--blue);}
  .head h1{font-size:36px;font-weight:800;color:var(--navy);margin:10px 0 0;letter-spacing:-.02em;}
  .head .meta{font-family:'IBM Plex Mono',monospace;font-size:12px;color:var(--muted);margin-top:12px;letter-spacing:.02em;}
  .head .lead{margin-top:14px;font-size:15px;color:#2b3543;}
  .head .lead a{color:var(--blue);font-weight:600;text-decoration:none;}
  .head{padding-bottom:22px;border-bottom:1px solid var(--line);margin-bottom:8px;}
  .content h2{font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.01em;
    margin:34px 0 6px;padding-bottom:8px;border-bottom:2px solid var(--navy);}
  .content h2:first-of-type{margin-top:18px;}
  .content p{font-size:14px;color:#2b3543;margin:0 0 12px;}
  .content a{color:var(--blue);}
  .content strong{color:var(--ink);}
  .content blockquote{background:#fbfaf4;border:1px solid #ece3c9;border-left:4px solid #b87211;
    border-radius:0 8px 8px 0;padding:12px 18px;margin:0 0 14px;font-size:13px;color:#3a4250;}
  .content ul{margin:0 0 14px;padding-left:20px;}
  .content li{font-size:13.5px;color:#2b3543;margin:4px 0;}
  .tbl{overflow-x:auto;margin:6px 0 16px;border:1px solid var(--line);border-radius:8px;}
  table{width:100%;border-collapse:collapse;font-size:12.5px;min-width:560px;}
  thead th{background:var(--navy);color:#fff;text-align:left;padding:9px 11px;font-weight:600;
    font-family:'IBM Plex Mono',monospace;font-size:10.5px;letter-spacing:.04em;text-transform:uppercase;}
  tbody td{padding:9px 11px;border-bottom:1px solid var(--line);vertical-align:top;color:#2b3543;}
  tbody tr:nth-child(even){background:var(--soft);}
  tbody tr:last-child td{border-bottom:none;}
  .site-footer{width:min(1000px,94vw);margin:26px auto 40px;text-align:center;font-size:13px;color:var(--muted);}
  .site-footer .attrib a{color:var(--blue);font-weight:600;text-decoration:none;}
  .site-footer .attrib a:hover{text-decoration:underline;}
  .site-footer .gl{font-family:'IBM Plex Mono',monospace;font-size:10.5px;color:#7a8694;margin-top:8px;}
</style>
</head>
<body>
<nav class="nav"><div class="in">
  <div class="brand"><span class="dot">📡</span><span class="nm">Macro Monitor</span></div>
  <a class="back" href="../index.html">← All reports</a>
</div></nav>
<main class="page">
  <div class="head">
    <div class="kicker">Detailed Blackboard</div>
    <h1>Weekly Detailed Blackboard</h1>
    <div class="meta">__WEEK_ENDING__ &nbsp;·&nbsp; DATA SNAPSHOT AS OF __DATA_ASOF__</div>
    <p class="lead">The full swarm data snapshot — every domain's release tables, current stance and the cross-indicator synthesis — that served as the source for the <a href="__REPORT_HREF__">W24 business report →</a></p>
  </div>
  <div class="content">
__BODY__
  </div>
</main>
<footer class="site-footer">
  <p class="attrib">Service offered by <a href="https://atnode.ai" target="_blank" rel="noopener noreferrer">atnode.ai</a> using the awesome <a href="https://hyperagent.com" target="_blank" rel="noopener noreferrer">hyperagent platform</a>.</p>
  <p class="gl">Published automatically every Saturday · Internal monitoring summary — not investment advice.</p>
</footer>
</body>
</html>
"""

HTML = (HTML.replace("__WEEK__", WEEK_LABEL)
            .replace("__WEEK_ENDING__", WEEK_ENDING)
            .replace("__DATA_ASOF__", DATA_ASOF)
            .replace("__REPORT_HREF__", REPORT_HREF)
            .replace("__BODY__", body))

open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, len(HTML), "bytes")
