"""Refresh stars / forks / license / last commit / contributors for every data/projects/*.yml.

Requires GITHUB_TOKEN (the Actions built-in token is enough). Without it the script exits
without changing anything, so the site can still be built from the committed data.
Values that cannot be fetched are left as-is (never guessed).
"""
from __future__ import annotations

import base64
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

import common

API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN")
NOT_FOUND_NOTE = "Repository not found on last fetch."


def gh(path: str, want_headers: bool = False):
    req = urllib.request.Request(
        API + path,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "awesome-keycloak-extensions",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.load(r)
        return (body, r.headers) if want_headers else body


def contributors(repo: str) -> int | None:
    try:
        body, headers = gh(f"/repos/{repo}/contributors?per_page=1&anon=true", True)
    except urllib.error.HTTPError:
        return None
    link = headers.get("Link", "")
    m = re.search(r'[?&]page=(\d+)>; rel="last"', link)
    if m:
        return int(m.group(1))
    return len(body)


def kc_version(repo: str, branch: str) -> str | None:
    """Best effort: read <keycloak.version> from pom.xml."""
    try:
        f = gh(f"/repos/{repo}/contents/pom.xml?ref={branch}")
        xml = base64.b64decode(f["content"]).decode("utf-8", "replace")
    except Exception:
        return None
    return parse_kc_version(xml)


def parse_kc_version(xml: str) -> str | None:
    m = re.search(r"<(?:keycloak|keycloak\.version|version\.keycloak)>\s*([\d.]+)", xml)
    if not m:
        return None
    # Keycloak nightly builds are published as 999.0.0-SNAPSHOT
    return "nightly" if m.group(1).startswith("999.") else m.group(1)


def refresh(p: dict) -> bool:
    repo = p["repo"]
    try:
        info = gh(f"/repos/{repo}")
    except urllib.error.HTTPError as e:
        print(f"  ! {repo}: HTTP {e.code} (kept previous values)")
        if e.code == 404 and NOT_FOUND_NOTE not in (p.get("note") or ""):
            p["note"] = f"{p['note']} {NOT_FOUND_NOTE}" if p.get("note") else NOT_FOUND_NOTE
        return False

    if info["full_name"].lower() != repo.lower():
        p["_moved_to"] = info["full_name"]  # renamed/transferred; merged in merge_moved()
    p["stars"] = info["stargazers_count"]
    p["stars_approx"] = False
    p["forks"] = info["forks_count"]
    p["archived"] = bool(info["archived"])
    p["language"] = info.get("language") or p.get("language")
    lic = (info.get("license") or {}).get("spdx_id")
    if lic and lic != "NOASSERTION":
        p["license"] = lic
    elif not p.get("license"):
        p["license"] = "Other (see repo)"
    if not p.get("summary") and info.get("description"):
        p["summary"] = info["description"].strip()

    branch = info.get("default_branch", "main")
    try:
        commits = gh(f"/repos/{repo}/commits?per_page=1&sha={branch}")
        p["last_commit"] = commits[0]["commit"]["committer"]["date"][:10]
    except Exception:
        p["last_commit"] = (info.get("pushed_at") or "")[:10] or p.get("last_commit")

    c = contributors(repo)
    if c is not None:
        p["contributors"] = c
    v = kc_version(repo, branch)
    if v:
        p["kc_versions"] = v

    p["fetched_at"] = dt.date.today().isoformat()
    p["source"] = f"{API}/repos/{repo}"
    return True


def merge_moved(projects: list[dict]) -> None:
    """Fold entries whose repo was renamed/transferred into the canonical name.

    If a file for the new name already exists, the old file is a duplicate and is removed
    (the old name is kept in `aliases` so discover.py does not re-add it). Otherwise the
    file is renamed to the new name.
    """
    by_repo = {p["repo"].lower(): p for p in projects}
    for p in projects:
        new = p.get("_moved_to")
        if not new:
            continue
        old_path = p["_path"]
        target = by_repo.get(new.lower())
        if target is None:
            target = {**p, "repo": new, "url": f"https://github.com/{new}", "_path": common.file_for(new)}
            by_repo[new.lower()] = target
        target["aliases"] = sorted(set(target.get("aliases") or []) | set(p.get("aliases") or []) | {p["repo"]})
        target.pop("_moved_to", None)
        common.save(target)
        if old_path != target["_path"]:
            old_path.unlink()
        print(f"  ~ {p['repo']} moved to {new} (merged)")


def main() -> int:
    if not TOKEN:
        print("GITHUB_TOKEN not set: skipping fetch (committed data is used as-is).")
        return 0
    ok = fail = 0
    projects = common.load_all()
    for p in projects:
        print(f"- {p['repo']}")
        if refresh(p):
            ok += 1
        else:
            fail += 1
        common.save(p)
        time.sleep(0.2)
    merge_moved(projects)
    print(f"done: {ok} updated, {fail} failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
