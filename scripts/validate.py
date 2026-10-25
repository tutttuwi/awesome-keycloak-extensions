"""Validate data/projects/*.yml (run in CI on every PR). Exits 1 if any entry is invalid."""
from __future__ import annotations

import datetime as dt
import re
import sys

import common

REQUIRED = ("name", "repo", "url", "summary", "kind", "genre", "official", "reviewed")
COUNTS = ("stars", "forks", "contributors")
REPO_RE = re.compile(r"^[\w.-]+/[\w.-]+$")


def _is_iso_date(v) -> bool:
    if isinstance(v, dt.date):
        return True
    try:
        dt.date.fromisoformat(str(v))
        return True
    except ValueError:
        return False


def check_project(p: dict, filename: str) -> list[str]:
    errs = [f"missing required field '{k}'" for k in REQUIRED if p.get(k) in (None, "") and k not in ("official", "reviewed")]
    errs += [f"'{k}' must be true/false" for k in ("official", "reviewed") if not isinstance(p.get(k), bool)]

    repo = p.get("repo") or ""
    if not REPO_RE.match(repo):
        errs.append(f"repo '{repo}' must look like owner/name")
    else:
        if filename != repo.replace("/", "__") + ".yml":
            errs.append(f"file name must be {repo.replace('/', '__')}.yml")
        if p.get("url") != f"https://github.com/{repo}":
            errs.append(f"url must be https://github.com/{repo}")

    if p.get("kind") not in common.KINDS:
        errs.append(f"kind must be one of {list(common.KINDS)}")
    genre = p.get("genre")
    if genre not in common.GENRES and genre != common.UNCATEGORIZED:
        errs.append(f"genre '{genre}' is not in GENRES (scripts/common.py)")
    if p.get("reviewed") is True and genre == common.UNCATEGORIZED:
        errs.append("reviewed entries must not be Uncategorized")

    for k in COUNTS:
        v = p.get(k)
        if v is not None and (not isinstance(v, int) or isinstance(v, bool) or v < 0):
            errs.append(f"'{k}' must be a non-negative integer or null")
    for k in ("last_commit", "fetched_at"):
        v = p.get(k)
        if v is not None and not _is_iso_date(v):
            errs.append(f"'{k}' must be an ISO date (YYYY-MM-DD) or null")
    if not isinstance(p.get("spi_types", []), list):
        errs.append("'spi_types' must be a list")
    return errs


def check_duplicates(projects: list[dict]) -> list[str]:
    seen: dict[str, str] = {}
    errs = []
    for p in projects:
        for name in [p.get("repo") or ""] + list(p.get("aliases") or []):
            key = name.lower()
            if key in seen:
                errs.append(f"{name}: duplicate of {seen[key]}")
            else:
                seen[key] = p.get("repo")
    return errs


def _check_items(d: dict, key: str, min_items: int) -> list[str]:
    items = d.get(key)
    if not isinstance(items, list):
        return [f"'{key}' must be a list"]
    errs = [f"'{key}' needs at least {min_items} item(s)"] if len(items) < min_items else []
    for i, it in enumerate(items):
        for lang in ("en", "ja"):
            if not isinstance(it, dict) or not str(it.get(lang) or "").strip():
                errs.append(f"{key}[{i}] needs a non-empty '{lang}' text")
    return errs


def check_details(d: dict, filename: str, repos: set[str]) -> list[str]:
    repo = str(d.get("repo") or "")
    errs = []
    if repo.lower() not in {r.lower() for r in repos}:
        errs.append(f"no project file for repo '{repo}'")
    if filename != f"{repo}.yml":
        errs.append(f"file name must be data/details/{repo}.yml")
    if not _is_iso_date(d.get("researched_at") or "x"):
        errs.append("'researched_at' must be an ISO date")
    sources = d.get("sources")
    if not isinstance(sources, list) or not sources or not all(str(s).startswith("https://") for s in sources):
        errs.append("'sources' must be a non-empty list of https:// URLs")
    errs += _check_items(d, "can", 1)
    errs += _check_items(d, "cannot", 0)
    errs += _check_items(d, "requires", 0)
    return errs


def main() -> int:
    projects = common.load_all()
    errs = []
    for p in projects:
        errs += [f"{p['_path'].name}: {e}" for e in check_project(p, p["_path"].name)]
    errs += check_duplicates(projects)
    repos = {p["repo"] for p in projects}
    for d in common.load_details().values():
        rel = d["_path"].relative_to(common.DETAILS).as_posix()
        errs += [f"details/{rel}: {e}" for e in check_details(d, rel, repos)]
    for e in errs:
        print(f"::error::{e}")
    print(f"validated {len(projects)} file(s): {len(errs)} error(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
