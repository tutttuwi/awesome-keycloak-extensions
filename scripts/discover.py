"""Discover new extensions and create stub YAML files (never overwrites curated fields).

Sources:
  1. https://www.keycloak.org/extensions  -> official entries (+ "Less active" section)
  2. GitHub topic search (keycloak-spi / keycloak-extension / keycloak-provider), stars >= MIN_STARS
     -> community entries (needs GITHUB_TOKEN)

Stubs get genre "Uncategorized" and reviewed: false. Review them and set kind/genre/summary_ja.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse
import urllib.request

import common

OFFICIAL_URL = "https://www.keycloak.org/extensions"
TOPICS = ["keycloak-spi", "keycloak-extension", "keycloak-provider"]
MIN_STARS = int(os.environ.get("MIN_STARS", "50"))
TOKEN = os.environ.get("GITHUB_TOKEN")
# Links on the page that are site chrome, not extensions.
CHROME = {"keycloak/keycloak", "keycloak/keycloak-web", "keycloak/keycloak-community"}

# Very rough keyword guess; always marked reviewed:false so a human confirms.
GUESS = [
    (r"event.?listener|webhook|rabbit|mqtt|kafka|sns|sqs", "Event / Webhook / Messaging"),
    (r"mapper|claim", "Protocol Mapper / Claim"),
    (r"scim", "Provisioning (SCIM)"),
    (r"mfa|otp|2fa|webauthn|passkey|passwordless|magic.?link", "MFA / Passwordless"),
    (r"idp|identity.?provider|social|oidc.?provider|saml", "Identity Provider"),
    (r"theme|keycloakify|login.?theme", "Theme / UI"),
    (r"tenan|organi[sz]ation", "Multi-tenancy / Organization"),
    (r"metrics|audit|monitor", "Monitoring / Audit"),
    (r"terraform|ansible|helm|operator|config", "Config as code / DevOps"),
    (r"captcha|bot|rate.?limit", "Security / Bot protection"),
    (r"user.?(storage|federation)|ldap|federation", "User Storage / Federation"),
    (r"mail|sms|notif", "Email / Notification"),
    (r"auth", "Authentication"),
]


def guess_genre(text: str) -> str:
    t = text.lower()
    for pat, genre in GUESS:
        if re.search(pat, t):
            return genre
    return common.UNCATEGORIZED


def http_get(url: str, headers: dict | None = None) -> bytes:
    h = {"User-Agent": "awesome-keycloak-spi"}
    h.update(headers or {})
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=30) as r:
        return r.read()


def parse_official(html: str) -> list[tuple[str, bool]]:
    idx = html.rfind("Less active")
    pat = re.compile(r'href="https://github\.com/([\w.-]+/[\w.-]+?)(?:\.git)?/?"')
    out, seen = [], set()
    for m in pat.finditer(html):
        repo = m.group(1)
        if repo.lower() in CHROME or repo.lower() in seen:
            continue
        seen.add(repo.lower())
        out.append((repo, idx != -1 and m.start() > idx))
    return out


def topic_search() -> list[dict]:
    if not TOKEN:
        print("GITHUB_TOKEN not set: skipping topic search.")
        return []
    found = {}
    for topic in TOPICS:
        q = urllib.parse.quote(f"topic:{topic} stars:>={MIN_STARS}")
        url = f"https://api.github.com/search/repositories?q={q}&sort=stars&per_page=50"
        data = json.loads(
            http_get(url, {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"})
        )
        for it in data.get("items", []):
            found[it["full_name"].lower()] = it
    return list(found.values())


def stub(repo: str, **kw) -> dict:
    d = {
        "name": repo.split("/")[1], "repo": repo, "url": f"https://github.com/{repo}",
        "summary": kw.get("summary", ""), "summary_ja": None,
        "kind": "core", "genre": kw.get("genre", common.UNCATEGORIZED), "spi_types": [],
        "language": None, "license": None, "stars": None, "stars_approx": False, "forks": None,
        "contributors": None, "last_commit": None, "archived": None, "kc_versions": None,
        "official": kw.get("official", False),
        "less_active_in_official": kw.get("less_active", False),
        "unmaintained": False, "reviewed": False, "note": None,
        "fetched_at": None, "source": kw.get("source"),
    }
    return d


def main() -> int:
    existing = {p["repo"].lower(): p for p in common.load_all()}
    added = 0

    try:
        pairs = parse_official(http_get(OFFICIAL_URL).decode("utf-8", "replace"))
        print(f"official page: {len(pairs)} GitHub links")
        if not pairs:
            print("  ! parsed 0 links - page structure may have changed")
    except Exception as e:  # network failure must not break the pipeline
        print(f"official page fetch failed: {e}")
        pairs = []

    for repo, less in pairs:
        cur = existing.get(repo.lower())
        if cur:
            cur["official"] = True
            cur["less_active_in_official"] = less
            common.save(cur)
        else:
            d = stub(repo, official=True, less_active=less, genre=guess_genre(repo), source=OFFICIAL_URL)
            common.save(d)
            existing[repo.lower()] = d
            added += 1
            print(f"  + official: {repo}")

    for it in topic_search():
        repo = it["full_name"]
        if repo.lower() in existing or it.get("fork"):
            continue
        desc = it.get("description") or ""
        d = stub(repo, summary=desc, genre=guess_genre(repo + " " + desc),
                 source="GitHub topic search")
        common.save(d)
        existing[repo.lower()] = d
        added += 1
        print(f"  + community: {repo} ({it['stargazers_count']}*)")

    print(f"added {added} stub(s). Run fetch_github.py, then review genre/kind/summary_ja.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
