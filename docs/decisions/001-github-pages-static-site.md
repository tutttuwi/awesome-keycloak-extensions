# 001: Static GitHub Pages site fed by YAML + GitHub API

- Date: 2026-10-22
- Decision: One YAML file per project is the source of truth. GitHub Actions (weekly) discovers new entries, refreshes numbers via the GitHub API, regenerates `README.md` and `site/data.json`, and deploys `site/` to GitHub Pages.
- Why: no server/DB, Git-reviewable data, numbers always carry a fetch date, unknown values stay `null` and are shown as unknown (never guessed).
- "Official" = linked from https://www.keycloak.org/extensions. "Community" = found via GitHub topics with stars >= 50 (`MIN_STARS`).
- Auto-discovered entries are `reviewed: false` with a keyword-guessed genre until a human confirms.
