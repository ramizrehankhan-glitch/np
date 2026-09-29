#!/usr/bin/env python3
"""Assemble index.html from sections/*.html and css/*.css (in filename order)."""
from pathlib import Path

ROOT = Path(__file__).parent
sections = sorted((ROOT / "sections").glob("*.html"))
styles = ["css/fonts.css", "css/base.css"] + [f"css/{p.name}" for p in sorted((ROOT / "css").glob("[0-9]*.css"))]

head = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI Guardian — Enterprise AI Governance Software</title>
  <meta name="description" content="AI Guardian gives every employee one approved path to AI, with identity, policy, security, cost, and audit controls on every request.">
"""
head += "".join(f'  <link rel="stylesheet" href="{s}">\n' for s in styles)
head += "</head>\n<body>\n<main class=\"page\">\n"
body = "\n".join(p.read_text().rstrip() for p in sections)
tail = "\n</main>\n</body>\n</html>\n"
tmp = ROOT / ".index.html.tmp"
tmp.write_text(head + body + tail)
tmp.replace(ROOT / "index.html")  # atomic, so concurrent builds never leave a partial file
print(f"index.html: {len(sections)} sections, {len(styles)} stylesheets")
