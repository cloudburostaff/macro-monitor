#!/usr/bin/env python3
"""Render any Markdown file into a styled Macro Monitor page (nav + content + footer).
Usage: build_page.py SRC OUT KICKER TITLE SUBTITLE BACK_HREF BACK_LABEL"""
import sys, re, markdown

SRC, OUT   = sys.argv[1], sys.argv[2]
KICKER     = sys.argv[3] if len(sys.argv) > 3 else "Reference"
TITLE      = sys.argv[4] if len(sys.argv) > 4 else "Document"
SUBTITLE   = sys.argv[5] if len(sys.argv) > 5 else ""
BACK_HREF  = sys.argv[6] if len(sys.argv) > 6 else "index.html"
BACK_LABEL = sys.argv[7] if len(sys.argv) > 7 else "← Back to Macro Monitor"

body = markdown.markdown(open(SRC, encoding="utf-8").read(),
                         extensions=["tables", "sane_lists", "fenced_code"])
body = re.sub(r'<a href="(https?://[^"]+)"',
              r'<a href="\1" target="_blank" rel="noopener noreferrer"', body)
body = body.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")

TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Macro Monitor — __TITLE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root{--navy:#0f2a4a;--blue:#1f5fa8;--ink:#1a2230;--muted:#5b6776;--line:#e2e7ee;--soft:#f4f6f9;--bg:#e7eaef;}
  *{box-sizing:border-box;} html,body{margin:0;padding:0;}
  body{background:var(--bg);color:var(--ink);font-family:'Inter',-apple-system,system-ui,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased;}
  .nav{background:var(--navy);color:#fff;}
  .nav .in{width:min(1000px,94vw);margin:0 auto;padding:14px 0;display:flex;align-items:center;justify-content:space-between;}
  .nav .brand{display:flex;align-items:center;gap:11px;}
  .nav .dot{width:30px;height:30px;border-radius:7px;background:#fff;color:var(--navy);display:flex;align-items:center;justify-content:center;font-size:16px;}
  .nav .nm{font-weight:700;font-size:15px;letter-spacing:-.01em;}
  .nav a.back{color:#9fc0e6;text-decoration:none;font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.04em;}
  .nav a.back:hover{color:#fff;}
  .page{width:min(1000px,94vw);background:#fff;margin:30px auto 0;padding:48px 60px 52px;border-top:4px solid var(--navy);box-shadow:0 2px 26px rgba(15,42,74,.11);}
  @media(max-width:640px){.page{padding:32px 22px 40px;}}
  .kicker{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--blue);}
  .head{padding-bottom:22px;border-bottom:1px solid var(--line);margin-bottom:6px;}
  .head h1{font-size:36px;font-weight:800;color:var(--navy);margin:10px 0 0;letter-spacing:-.02em;}
  .head .sub{margin-top:12px;font-size:15px;color:var(--muted);}
  .content h2{font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.01em;margin:34px 0 8px;padding-bottom:8px;border-bottom:2px solid var(--navy);}
  .content h2:first-of-type{margin-top:20px;}
  .content p{font-size:14.5px;color:#2b3543;margin:0 0 13px;}
  .content a{color:var(--blue);}
  .content strong{color:var(--ink);}
  .content ul,.content ol{margin:0 0 14px;padding-left:22px;}
  .content li{font-size:14px;color:#2b3543;margin:5px 0;}
  .content pre{background:var(--navy);color:#dce7f2;border-radius:9px;padding:16px 18px;overflow-x:auto;font-family:'IBM Plex Mono',monospace;font-size:12px;line-height:1.5;margin:6px 0 16px;}
  .content code{font-family:'IBM Plex Mono',monospace;font-size:12.5px;background:#eef1f4;padding:1px 5px;border-radius:4px;color:var(--navy);}
  .content pre code{background:none;padding:0;color:inherit;font-size:12px;}
  .tbl{overflow-x:auto;margin:6px 0 16px;border:1px solid var(--line);border-radius:8px;}
  table{width:100%;border-collapse:collapse;font-size:13px;min-width:540px;}
  thead th{background:var(--navy);color:#fff;text-align:left;padding:9px 11px;font-weight:600;font-family:'IBM Plex Mono',monospace;font-size:10.5px;letter-spacing:.04em;text-transform:uppercase;}
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
  <a class="back" href="__BACK_HREF__">__BACK_LABEL__</a>
</div></nav>
<main class="page">
  <div class="head">
    <div class="kicker">__KICKER__</div>
    <h1>__TITLE__</h1>
    __SUB__
  </div>
  <div class="content">
__BODY__
  </div>
</main>
<footer class="site-footer">
  <p class="attrib">Service offered by <a href="https://atnode.ai" target="_blank" rel="noopener noreferrer">atnode.ai</a> using the awesome <a href="https://hyperagent.com" target="_blank" rel="noopener noreferrer">hyperagent platform</a>.</p>
  <p class="gl">Internal monitoring summary — not investment advice.</p>
</footer>
</body>
</html>
"""

sub_html = f'<div class="sub">{SUBTITLE}</div>' if SUBTITLE else ""
out = (TPL.replace("__TITLE__", TITLE).replace("__KICKER__", KICKER)
          .replace("__SUB__", sub_html).replace("__BACK_HREF__", BACK_HREF)
          .replace("__BACK_LABEL__", BACK_LABEL).replace("__BODY__", body))
open(OUT, "w", encoding="utf-8").write(out)
print("wrote", OUT, len(out), "bytes")
