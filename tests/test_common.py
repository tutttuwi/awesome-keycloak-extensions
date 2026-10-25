import datetime as dt

import common
from conftest import make_project

TODAY = dt.date(2026, 10, 25)


def test_activity_is_active_within_12_months():
    assert common.activity(make_project(last_commit="2026-01-01"), TODAY) == "Active"


def test_activity_is_stale_between_12_and_24_months():
    assert common.activity(make_project(last_commit="2025-05-01"), TODAY) == "Stale"


def test_activity_is_inactive_after_24_months():
    assert common.activity(make_project(last_commit="2024-01-01"), TODAY) == "Inactive"


def test_activity_is_inactive_when_archived_even_if_recent():
    assert common.activity(make_project(last_commit="2026-10-01", archived=True), TODAY) == "Inactive"


def test_activity_is_inactive_when_marked_unmaintained():
    assert common.activity(make_project(unmaintained=True), TODAY) == "Inactive"


def test_activity_is_unknown_without_last_commit():
    assert common.activity(make_project(last_commit=None), TODAY) == "Unknown"


def test_save_and_load_round_trip_drops_private_keys(data_dir):
    p = make_project(_activity="Active")
    common.save(p)

    loaded = common.load_all()

    assert len(loaded) == 1
    assert loaded[0]["repo"] == "owner/keycloak-foo"
    assert "_activity" not in loaded[0]
    assert loaded[0]["_path"] == data_dir / "owner__keycloak-foo.yml"
