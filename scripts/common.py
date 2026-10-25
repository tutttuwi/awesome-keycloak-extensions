"""Shared helpers for awesome-keycloak-extensions scripts."""
from __future__ import annotations

import datetime as dt
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "projects"

# Fixed genre list (see docs/decisions/002-genres.md). Add new genres only via a decision record.
GENRES = [
    "Authentication",
    "MFA / Passwordless",
    "Event / Webhook / Messaging",
    "Identity Provider",
    "Protocol (CAS / WS-Fed)",
    "Protocol Mapper / Claim",
    "User Storage / Federation",
    "Provisioning (SCIM)",
    "Multi-tenancy / Organization",
    "Policy / Authorization",
    "Email / Notification",
    "Theme / UI",
    "Monitoring / Audit",
    "Storage / Datastore",
    "Security / Bot protection",
    "Config as code / DevOps",
    "Testing / Examples",
]
UNCATEGORIZED = "Uncategorized"
KINDS = ("core", "peripheral")


def file_for(repo: str) -> pathlib.Path:
    return DATA / (repo.replace("/", "__") + ".yml")


def load_all() -> list[dict]:
    items = []
    for path in sorted(DATA.glob("*.yml")):
        d = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        d["_path"] = path
        items.append(d)
    return items


def save(d: dict) -> None:
    out = {k: v for k, v in d.items() if not k.startswith("_")}
    path = d.get("_path") or file_for(out["repo"])
    path.write_text(yaml.safe_dump(out, allow_unicode=True, sort_keys=False), encoding="utf-8")


def _months_between(date_str: str, today: dt.date) -> float:
    d = dt.date.fromisoformat(date_str[:10])
    return (today - d).days / 30.44


def activity(p: dict, today: dt.date | None = None) -> str:
    """Active / Stale / Inactive / Unknown (thresholds: see README)."""
    today = today or dt.date.today()
    if p.get("archived") or p.get("unmaintained"):
        return "Inactive"
    lc = p.get("last_commit")
    if not lc:
        return "Unknown"
    m = _months_between(str(lc), today)
    if m <= 12:
        return "Active"
    if m <= 24:
        return "Stale"
    return "Inactive"
