# Contributing / 掲載申請

Add a project by opening a PR with **one YAML file**: `data/projects/<owner>__<repo>.yml`.
Stars, forks, license, last commit and contributors are filled in automatically by CI — you only need the fields below.

```yaml
name: my-keycloak-extension
repo: owner/my-keycloak-extension
url: https://github.com/owner/my-keycloak-extension
summary: One-line English description.
summary_ja: 日本語の1行説明(任意)
kind: core            # core = SPI implementation / peripheral = tool (Terraform, CLI, testing, ...)
genre: Authentication # must be one of GENRES in scripts/common.py
spi_types: [Authenticator]
official: false
reviewed: true
```

## Inclusion criteria
- An OSS license is declared in the repository
- It implements a Keycloak SPI (`kind: core`) or is a Keycloak companion tool (`kind: peripheral`)
- The README explains how to install it

Inactive projects (no commit for 24+ months, archived, or "no longer maintained") are kept in the Archive table, not removed.
