"""Render one static "can / cannot" page per project (site/p/<owner>/<repo>.html).

All text comes from YAML that ultimately summarises third-party READMEs, so every value is
HTML-escaped and only https:// links are emitted.
"""
from __future__ import annotations

import html
import pathlib
import re

import common

ASSET_PREFIX = "../../"  # pages live two levels below the site root


def _e(s) -> str:
    return html.escape(str(s if s is not None else ""), quote=True)


def _url(u) -> str:
    u = str(u or "")
    return _e(u) if u.startswith("https://") else "#"


def _rich(s) -> str:
    """Escape, then render `inline code` (safe: runs on already-escaped text)."""
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", _e(s))


def _bi(en: str, ja: str) -> str:
    """Bilingual span pair; CSS shows one depending on html[data-lang]."""
    return f'<span class="l-en">{_rich(en)}</span><span class="l-ja">{_rich(ja)}</span>'


def _items(items: list[dict], cls: str, empty_en: str, empty_ja: str) -> str:
    if not items:
        return f'<p class="empty">{_bi(empty_en, empty_ja)}</p>'
    lis = "".join(f'<li class="{cls}">{_bi(it.get("en", ""), it.get("ja", ""))}</li>' for it in items)
    return f'<ul class="items">{lis}</ul>'


def _fmt(n) -> str:
    return "—" if n is None else f"{n:,}"


def _stats(p: dict) -> str:
    stars = ("~" if p.get("stars_approx") and p.get("stars") is not None else "") + _fmt(p.get("stars"))
    rows = [
        ("★", stars), ("Forks", _fmt(p.get("forks"))), ("Contributors", _fmt(p.get("contributors"))),
        ("Updated", p.get("last_commit") or "—"), ("KC", p.get("kc_versions") or "—"),
        ("License", p.get("license") or "—"),
    ]
    return "".join(f"<div><dt>{_e(k)}</dt><dd>{_e(v)}</dd></div>" for k, v in rows)


def _badges(p: dict) -> str:
    act = p.get("_activity") or p.get("activity") or "Unknown"
    b = [
        ('b off' if p.get("official") else 'b', "Official" if p.get("official") else "Community"),
        ("b", "Tool" if p.get("kind") == "peripheral" else "SPI"),
        ("b", p.get("genre")),
        (f"b {act}", act),
    ]
    return "".join(f'<span class="{_e(c)}">{_e(t)}</span>' for c, t in b)


def render_detail(p: dict, d: dict) -> str:
    name, repo = p["name"], p["repo"]
    can, cannot, req = d.get("can") or [], d.get("cannot") or [], d.get("requires") or []
    sources = "".join(f'<li><a href="{_url(s)}" rel="noopener">{_e(s)}</a></li>' for s in d.get("sources") or [])
    note = f'<p class="note">{_e(p["note"])}</p>' if p.get("note") else ""
    summary_ja = p.get("summary_ja") or p.get("summary") or ""
    req_html = (
        f'<section class="req" aria-labelledby="req-h"><h2 id="req-h">{_bi("Requirements", "前提条件")}</h2>'
        f'{_items(req, "r", "", "")}</section>' if req else ""
    )
    return f"""<!doctype html>
<html lang="en" data-lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_e(name)} — Awesome Keycloak Extensions</title>
<meta name="description" content="{_e(p.get('summary'))}">
<link rel="stylesheet" href="{ASSET_PREFIX}assets/detail.css">
</head>
<body>
<header class="top">
  <nav aria-label="Breadcrumb"><a href="{ASSET_PREFIX}">← {_bi("All extensions", "一覧へ戻る")}</a></nav>
  <div class="seg" id="lang" role="group" aria-label="Language">
    <button data-v="en" aria-pressed="true">EN</button><button data-v="ja" aria-pressed="false">日本語</button>
  </div>
</header>
<main>
  <section class="hero" aria-labelledby="name">
    <p class="badges">{_badges(p)}</p>
    <h1 id="name">{_e(name)}</h1>
    <p class="repo"><a href="{_url(p.get('url'))}" rel="noopener">{_e(repo)} ↗</a></p>
    <p class="lead">{_bi(p.get("summary") or "", summary_ja)}</p>
    {note}
    <dl class="stats">{_stats(p)}</dl>
  </section>

  <div class="verdict">
    <section class="panel can" aria-labelledby="can-h">
      <h2 id="can-h"><span class="mark" aria-hidden="true">✓</span>{_bi("What it can do", "できること")}<span class="n">{len(can)}</span></h2>
      {_items(can, "c", "", "")}
    </section>
    <section class="panel cannot" aria-labelledby="cannot-h">
      <h2 id="cannot-h"><span class="mark" aria-hidden="true">✕</span>{_bi("What it cannot do / limits", "できないこと・制約")}<span class="n">{len(cannot)}</span></h2>
      {_items(cannot, "x", "No limitations are stated in the documentation.", "ドキュメントに明記された制約はありません。")}
    </section>
  </div>

  {req_html}

  <footer class="src">
    <p>{_bi(f"Researched {d.get('researched_at')} from the project's own documentation. Summaries may lag behind the project — check the source before adopting.",
            f"{d.get('researched_at')} 時点のプロジェクト公式ドキュメントを基に要約。最新情報は採用前に原典で確認してください。")}</p>
    <ul>{sources}</ul>
  </footer>
</main>
<script>
(() => {{
  const root = document.documentElement, KEY = "akx-lang";
  let lang = null;
  try {{ lang = localStorage.getItem(KEY); }} catch (e) {{}}
  if (lang !== "en" && lang !== "ja") lang = (navigator.language || "en").startsWith("ja") ? "ja" : "en";
  const set = v => {{
    root.dataset.lang = v; root.lang = v;
    document.querySelectorAll("#lang button").forEach(b => b.setAttribute("aria-pressed", b.dataset.v === v));
    try {{ localStorage.setItem(KEY, v); }} catch (e) {{}}
  }};
  document.getElementById("lang").addEventListener("click", ev => {{
    const b = ev.target.closest("button"); if (b) set(b.dataset.v);
  }});
  set(lang);
}})();
</script>
</body>
</html>
"""


def write_detail_pages(projects: list[dict], details: dict[str, dict], out_dir: pathlib.Path) -> int:
    """Write a page for every project that has details; delete pages whose details are gone."""
    out_dir.mkdir(parents=True, exist_ok=True)
    wanted = set()
    for p in projects:
        d = details.get(p["repo"].lower())
        if not d:
            continue
        page = out_dir / page_path(p["repo"])
        page.parent.mkdir(exist_ok=True)
        page.write_text(render_detail(p, d), encoding="utf-8")
        wanted.add(page)
    for old in out_dir.glob("*/*.html"):
        if old not in wanted:
            old.unlink()
    for owner_dir in out_dir.iterdir():
        if owner_dir.is_dir() and not any(owner_dir.iterdir()):
            owner_dir.rmdir()
    return len(wanted)


def page_path(repo: str) -> str:
    """Path of a project's page relative to site/p/."""
    return f"{repo}.html"
