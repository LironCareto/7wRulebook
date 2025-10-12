#!/usr/bin/env python3
"""
Simple Markdown -> HTML converter for this repo.

Usage (PowerShell):
  python -m pip install markdown
  python .\tools\convert_md_to_html.py

The script strips a leading Jekyll YAML front matter block (between '---' lines)
so the output is a standalone HTML file suitable for opening in a browser.
"""
from pathlib import Path
import re
import sys

try:
    import markdown
except Exception:
    print("Missing 'markdown' package. Install with: python -m pip install markdown")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'rulebook.md'
OUT = ROOT / 'rulebook.html'

if not SRC.exists():
    print(f"Source file not found: {SRC}")
    sys.exit(1)

text = SRC.read_text(encoding='utf-8')

# Remove leading YAML front matter if present
fm = re.match(r"\A---\s*\n.*?\n---\s*\n", text, re.S)
if fm:
    body = text[fm.end():]
else:
    body = text

md = markdown.Markdown(extensions=['extra', 'tables', 'fenced_code', 'toc', 'attr_list'])
html_body = md.convert(body)

# Minimal page wrapper. Link to repo's CSS if available.
css_link = 'css/main.css' if (ROOT / 'css' / 'main.scss').exists() or (ROOT / 'css' / 'main.css').exists() else None

head = ['<!doctype html>', '<html>', '<head>', '<meta charset="utf-8">', '<meta name="viewport" content="width=device-width,initial-scale=1">', '<title>Rulebook</title>']
if css_link:
    head.append(f'<link rel="stylesheet" href="{css_link}">')
head.append('</head>')

out_html = '\n'.join(head) + '\n<body>\n' + html_body + '\n</body>\n</html>\n'

OUT.write_text(out_html, encoding='utf-8')
print(f'Wrote: {OUT}')
