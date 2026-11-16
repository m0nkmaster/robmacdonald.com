"""Build the article pages and writing index from writing/_src/*.md.

Run: uv run --with markdown python build.py
"""
import html
import re
from datetime import date
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
SRC = ROOT / "writing" / "_src"
SITE = "https://robmacdonald.com"

PAGE = """<!DOCTYPE html>
<html lang="en-GB">
<head>
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-M8LV8Z5P');</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Rob MacDonald</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta name="twitter:card" content="summary">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/writing/article.css">
</head>
<body>
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-M8LV8Z5P" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <header class="top">
    <a href="/" class="home">Rob<span class="accent">.</span>MacDonald</a>
    <a href="/writing/" class="nav">Writing</a>
  </header>
  <main>
{content}
  </main>
  <footer class="footer"><a href="/">&larr; robmacdonald.com</a> &middot; &copy; {year}</footer>
</body>
</html>
"""


def parse(path):
    _, fm, body = path.read_text().split("---", 2)
    meta = {}
    for line in fm.strip().splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    meta["slug"] = path.stem
    meta["body"] = body
    return meta


def nice_date(iso):
    return date.fromisoformat(iso).strftime("%-d %B %Y")


def read_time(body):
    return max(1, round(len(re.findall(r"\w+", body)) / 230))


def render(content, title, desc, url):
    esc = lambda s: html.escape(s, quote=True)
    return PAGE.format(content=content, year=date.today().year,
                       title=esc(title), desc=esc(desc), url=esc(url))


posts = sorted((parse(p) for p in SRC.glob("*.md")), key=lambda m: m["date"], reverse=True)

for p in posts:
    body = markdown.markdown(p["body"], extensions=["fenced_code", "sane_lists", "md_in_html"])
    orig = (f'<p class="orig">Originally published on '
            f'<a href="{html.escape(p["original"])}" rel="noopener">LinkedIn</a>.</p>'
            if p["original"] else "")
    content = f"""    <article>
      <p class="meta"><time datetime="{p['date']}">{nice_date(p['date'])}</time> &middot; {read_time(p['body'])} min read</p>
      <h1>{html.escape(p['title'])}</h1>
      <p class="lede">{html.escape(p['description'])}</p>
      <div class="prose">
{body}
      </div>
      {orig}
    </article>"""
    out = ROOT / "writing" / p["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(content, p["title"], p["description"], f"{SITE}/writing/{p['slug']}/"))

items = "\n".join(
    f"""      <a class="item" href="/writing/{p['slug']}/">
        <time datetime="{p['date']}">{nice_date(p['date'])}</time>
        <h2>{html.escape(p['title'])}</h2>
        <p>{html.escape(p['description'])}</p>
      </a>""" for p in posts)
(ROOT / "writing" / "index.html").write_text(render(
    f'    <h1 class="index-title">Writing</h1>\n    <nav class="list">\n{items}\n    </nav>',
    "Writing", "Articles by Rob MacDonald on engineering, leadership and AI.", f"{SITE}/writing/"))

print(f"Built {len(posts)} articles")
