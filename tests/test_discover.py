import common
import discover
from conftest import make_project

OFFICIAL_HTML = """
<a href="https://github.com/keycloak/keycloak">Keycloak</a>
<a href="https://github.com/owner/ext-one">one</a>
<a href="https://github.com/owner/ext-one/">dup</a>
<a href="https://github.com/other/ext-two.git">two</a>
<h2>Less active</h2>
<a href="https://github.com/old/ext-three">three</a>
"""


def test_parse_official_skips_site_chrome_and_duplicates_and_flags_less_active():
    assert discover.parse_official(OFFICIAL_HTML) == [
        ("owner/ext-one", False),
        ("other/ext-two", False),
        ("old/ext-three", True),
    ]


def test_guess_genre_detects_protocol_without_matching_cassandra():
    assert discover.guess_genre("jacekkow/keycloak-protocol-cas") == "Protocol (CAS / WS-Fed)"
    assert discover.guess_genre("cloudtrust/keycloak-wsfed") == "Protocol (CAS / WS-Fed)"
    assert discover.guess_genre("opdt/keycloak-cassandra-extension") == "Storage / Datastore"


def test_guess_genre_falls_back_to_uncategorized():
    assert discover.guess_genre("someone/keycloak-something") == common.UNCATEGORIZED


def test_every_guessed_genre_is_a_known_genre():
    for _, genre in discover.GUESS:
        assert genre in common.GENRES


def test_known_repos_include_aliases_case_insensitively():
    p = make_project(repo="New/Repo", aliases=["Old/Repo"])

    known = discover.known_repos([p])

    assert known["new/repo"] is p
    assert known["old/repo"] is p
