"""Build site/data.json (for the Pages UI) and README.md (ranking tables) from data/projects/*.yml."""
from __future__ import annotations

import datetime as dt
import json
import os

import common

SITE_URL = os.environ.get("SITE_URL", "")
TOP_N = 20


def sort_key(p: dict):
    # stars desc (unknown last), then newer last_commit first
    return (-(p.get("stars") or -1), "".join(chr(255 - ord(c)) for c in str(p.get("last_commit") or "")))


def fmt_stars(p: dict) -> str:
    s = p.get("stars")
    if s is None:
        return "unknown"
    return f"~{s:,}" if p.get("stars_approx") else f"{s:,}"


def row(rank: int, p: dict) -> str:
    desc = (p.get("summary") or "").replace("|", "\\|")
    ja = p.get("summary_ja")
    if ja:
        desc += f"<br>{ja}".replace("|", "\\|")
    src = "Official" if p.get("official") else "Community"
    return (
        f"| {rank} | [{p['name']}]({p['url']}) | {desc} | {fmt_stars(p)} | {p.get('last_commit') or 'unknown'} "
        f"| {p['_activity']} | {p.get('kc_versions') or 'unknown'} | {p.get('license') or 'unknown'} | {src} |"
    )


HEAD = (
    "| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |\n"
    "|--:|------|---------|--:|-------------|----------|----|---------|-----|\n"
)


def table(items: list[dict]) -> str:
    if not items:
        return "_None yet._\n"
    return HEAD + "\n".join(row(i, p) for i, p in enumerate(items, 1)) + "\n"


def main() -> None:
    today = dt.date.today()
    projects = [p for p in common.load_all() if p.get("kind") in ("core", "peripheral")]
    for p in projects:
        p["_activity"] = common.activity(p, today)

    fetched = [p["fetched_at"] for p in projects if p.get("fetched_at")]
    data_date = max(fetched) if fetched else "unknown"

    live = [p for p in projects if p["_activity"] != "Inactive"]
    archive = sorted((p for p in projects if p["_activity"] == "Inactive"), key=sort_key)
    core = sorted((p for p in live if p["kind"] == "core"), key=sort_key)
    periph = sorted((p for p in live if p["kind"] == "peripheral"), key=sort_key)

    # ---- data.json for the UI
    out = []
    for p in sorted(projects, key=sort_key):
        d = {k: v for k, v in p.items() if not k.startswith("_")}
        d["activity"] = p["_activity"]
        out.append(d)
    (common.ROOT / "site").mkdir(exist_ok=True)
    (common.ROOT / "site" / "data.json").write_text(
        json.dumps({"generated_at": today.isoformat(), "data_date": data_date,
                    "genres": common.GENRES + [common.UNCATEGORIZED], "projects": out},
                   ensure_ascii=False, indent=1, default=str),
        encoding="utf-8",
    )

    # ---- README.md
    L = []
    L.append("# awesome-keycloak-spi\n")
    L.append("A curated, ranked catalog of Keycloak extensions (SPI implementations) and companion tools — "
             "official-list entries plus popular community projects.  \n"
             "Keycloakの拡張(SPI実装)と周辺ツールを、公式掲載分+人気のコミュニティ製も含めてランキング形式でまとめたカタログです。\n")
    if SITE_URL:
        L.append(f"**Browse / filter / search: {SITE_URL}**\n")
    L.append(f"> Data fetched: **{data_date}** (README generated {today.isoformat()}). "
             "Stars/forks/last commit come from the GitHub API; `unknown` = not fetched yet (never guessed). "
             "Official list: <https://www.keycloak.org/extensions>\n")
    L.append("Activity: **Active** ≤12 months · **Stale** 12–24 months · **Inactive** >24 months / archived / "
             "\"no longer maintained\" · **Unknown** = last commit not fetched yet.\n")
    L.append(f"## Top {TOP_N} (SPI extensions, by ★)\n")
    L.append(table(core[:TOP_N]))
    L.append("## By genre\n")
    for g in common.GENRES + [common.UNCATEGORIZED]:
        items = [p for p in core if p.get("genre") == g]
        if not items:
            continue
        L.append(f"### {g}\n")
        L.append(table(items))
    L.append("## Companion tools (Terraform, CLI, testing, …)\n")
    L.append(table(periph))
    L.append("## Archive (inactive)\n")
    L.append("Kept for reference; not part of the rankings above.\n")
    L.append(table(archive))
    L.append("## Contributing\n\nSee [CONTRIBUTING.md](CONTRIBUTING.md) — add a YAML file under `data/projects/` and open a PR. "
             "The README and site are regenerated automatically.\n")
    (common.ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")
    print(f"built: {len(projects)} projects ({len(core)} core / {len(periph)} peripheral / {len(archive)} archive)")


if __name__ == "__main__":
    main()
