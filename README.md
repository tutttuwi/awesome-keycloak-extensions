# awesome-keycloak-spi

A curated, ranked catalog of Keycloak extensions (SPI implementations) and companion tools — official-list entries plus popular community projects.  
Keycloakの拡張(SPI実装)と周辺ツールを、公式掲載分+人気のコミュニティ製も含めてランキング形式でまとめたカタログです。

> Data fetched: **2026-10-22** (README generated 2026-10-22). Stars/forks/last commit come from the GitHub API; `unknown` = not fetched yet (never guessed). Official list: <https://www.keycloak.org/extensions>

Activity: **Active** ≤12 months · **Stale** 12–24 months · **Inactive** >24 months / archived / "no longer maintained" · **Unknown** = last commit not fetched yet.

## Top 20 (SPI extensions, by ★)

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-metrics-spi](https://github.com/aerogear/keycloak-metrics-spi) | Exposes Keycloak metrics (Prometheus format) via an SPI.<br>KeycloakのメトリクスをPrometheus形式で公開するSPI | 616 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 2 | [keycloak-orgs](https://github.com/p2-inc/keycloak-orgs) | Organizations / multi-tenancy for Keycloak realms.<br>Keycloakの組織・マルチテナント機能 | 541 | unknown | Unknown | unknown | Elastic-2.0 | Official |
| 3 | [keycloak-extensions-demo](https://github.com/dasniko/keycloak-extensions-demo) | Demo of many SPI types: action token, authenticators, event listener, token mapper, required action, etc.<br>多数のSPI実装例(actiontoken/authenticator/event-listener/tokenmapper/requiredaction等) | 429 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 4 | [keycloak-magic-link](https://github.com/p2-inc/keycloak-magic-link) | Passwordless magic-link login.<br>マジックリンク(パスワードレス)認証 | 425 | unknown | Unknown | unknown | unknown | Official |
| 5 | [keycloak-home-idp-discovery](https://github.com/sventorben/keycloak-home-idp-discovery) | Discover the home IdP from the user's email domain.<br>メールドメインからホームIdPを自動判定 | 341 | unknown | Unknown | unknown | MIT | Official |
| 6 | [keycloak-events](https://github.com/p2-inc/keycloak-events) | Event listeners and webhooks for Keycloak events.<br>Keycloakイベント用のリスナー/Webhook | 314 | unknown | Unknown | unknown | unknown | Official |
| 7 | [keycloak-mfa-plugins](https://github.com/netzbegruenung/keycloak-mfa-plugins) | MFA plugins: SMS, enforced MFA, native-app MFA.<br>MFAプラグイン集(SMS/強制MFA/ネイティブアプリMFA) | 297 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 8 | [apple-identity-provider-keycloak](https://github.com/klausbetz/apple-identity-provider-keycloak) | Sign in with Apple identity provider.<br>Sign in with Apple用Identity Provider | 295 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 9 | [keycloak-multi-tenancy](https://github.com/anarsultanov/keycloak-multi-tenancy) | Multi-tenancy support for Keycloak.<br>Keycloakのマルチテナント対応 | 171 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 10 | [keycloak-event-listener-rabbitmq](https://github.com/aznamier/keycloak-event-listener-rabbitmq) | Publish Keycloak events to RabbitMQ.<br>KeycloakイベントをRabbitMQへ送信 | 170 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 11 | [keycloak-discord](https://github.com/wadahiro/keycloak-discord) | Discord identity provider.<br>Discord用Identity Provider | 158 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 12 | [keycloak-adaptive-authn](https://github.com/mabartos/keycloak-adaptive-authn) | Risk-based / adaptive authentication.<br>リスクベース(アダプティブ)認証 | 102 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 13 | [keycloak-scim-server](https://github.com/Metatavu/keycloak-scim-server) | SCIM server implemented as a Keycloak extension.<br>KeycloakにSCIMサーバーを追加する拡張 | 95 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 14 | [keycloak-event-listener-mqtt](https://github.com/softwarefactory-project/keycloak-event-listener-mqtt) | Publish Keycloak events to an MQTT broker.<br>KeycloakイベントをMQTTブローカーへ送信 | 46 | unknown | Unknown | unknown | Apache-2.0 | Community |

## By genre

### Authentication

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-magic-link](https://github.com/p2-inc/keycloak-magic-link) | Passwordless magic-link login.<br>マジックリンク(パスワードレス)認証 | 425 | unknown | Unknown | unknown | unknown | Official |
| 2 | [keycloak-home-idp-discovery](https://github.com/sventorben/keycloak-home-idp-discovery) | Discover the home IdP from the user's email domain.<br>メールドメインからホームIdPを自動判定 | 341 | unknown | Unknown | unknown | MIT | Official |
| 3 | [keycloak-adaptive-authn](https://github.com/mabartos/keycloak-adaptive-authn) | Risk-based / adaptive authentication.<br>リスクベース(アダプティブ)認証 | 102 | unknown | Unknown | unknown | Apache-2.0 | Official |

### MFA / Passwordless

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-mfa-plugins](https://github.com/netzbegruenung/keycloak-mfa-plugins) | MFA plugins: SMS, enforced MFA, native-app MFA.<br>MFAプラグイン集(SMS/強制MFA/ネイティブアプリMFA) | 297 | unknown | Unknown | unknown | Apache-2.0 | Official |

### Event / Webhook / Messaging

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-events](https://github.com/p2-inc/keycloak-events) | Event listeners and webhooks for Keycloak events.<br>Keycloakイベント用のリスナー/Webhook | 314 | unknown | Unknown | unknown | unknown | Official |
| 2 | [keycloak-event-listener-rabbitmq](https://github.com/aznamier/keycloak-event-listener-rabbitmq) | Publish Keycloak events to RabbitMQ.<br>KeycloakイベントをRabbitMQへ送信 | 170 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 3 | [keycloak-event-listener-mqtt](https://github.com/softwarefactory-project/keycloak-event-listener-mqtt) | Publish Keycloak events to an MQTT broker.<br>KeycloakイベントをMQTTブローカーへ送信 | 46 | unknown | Unknown | unknown | Apache-2.0 | Community |

### Identity Provider

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [apple-identity-provider-keycloak](https://github.com/klausbetz/apple-identity-provider-keycloak) | Sign in with Apple identity provider.<br>Sign in with Apple用Identity Provider | 295 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 2 | [keycloak-discord](https://github.com/wadahiro/keycloak-discord) | Discord identity provider.<br>Discord用Identity Provider | 158 | unknown | Unknown | unknown | Apache-2.0 | Official |

### Provisioning (SCIM)

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-scim-server](https://github.com/Metatavu/keycloak-scim-server) | SCIM server implemented as a Keycloak extension.<br>KeycloakにSCIMサーバーを追加する拡張 | 95 | unknown | Unknown | unknown | Apache-2.0 | Official |

### Multi-tenancy / Organization

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-orgs](https://github.com/p2-inc/keycloak-orgs) | Organizations / multi-tenancy for Keycloak realms.<br>Keycloakの組織・マルチテナント機能 | 541 | unknown | Unknown | unknown | Elastic-2.0 | Official |
| 2 | [keycloak-multi-tenancy](https://github.com/anarsultanov/keycloak-multi-tenancy) | Multi-tenancy support for Keycloak.<br>Keycloakのマルチテナント対応 | 171 | unknown | Unknown | unknown | Apache-2.0 | Official |

### Monitoring / Audit

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-metrics-spi](https://github.com/aerogear/keycloak-metrics-spi) | Exposes Keycloak metrics (Prometheus format) via an SPI.<br>KeycloakのメトリクスをPrometheus形式で公開するSPI | 616 | unknown | Unknown | unknown | Apache-2.0 | Official |

### Testing / Examples

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-extensions-demo](https://github.com/dasniko/keycloak-extensions-demo) | Demo of many SPI types: action token, authenticators, event listener, token mapper, required action, etc.<br>多数のSPI実装例(actiontoken/authenticator/event-listener/tokenmapper/requiredaction等) | 429 | unknown | Unknown | unknown | Apache-2.0 | Official |

## Companion tools (Terraform, CLI, testing, …)

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-config-cli](https://github.com/adorsys/keycloak-config-cli) | CLI to manage Keycloak realm configuration as code (YAML/JSON).<br>Keycloakのrealm設定をYAML/JSONでコード管理するCLI | ~1,200 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 2 | [terraform-provider-keycloak](https://github.com/keycloak/terraform-provider-keycloak) | Terraform provider for managing Keycloak resources.<br>Keycloakリソースを管理するTerraform provider | 951 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 3 | [testcontainers-keycloak](https://github.com/dasniko/testcontainers-keycloak) | Testcontainers module to run Keycloak in integration tests.<br>Keycloakを統合テストで起動するTestcontainersモジュール | 458 | unknown | Unknown | unknown | Apache-2.0 | Official |
| 4 | [kcwarden](https://github.com/iteratec/kcwarden) | Security audit tool for Keycloak configuration.<br>Keycloak設定のセキュリティ監査ツール | 132 | unknown | Unknown | unknown | Apache-2.0 | Official |

## Archive (inactive)

Kept for reference; not part of the rankings above.

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-extensions](https://github.com/zonaut/keycloak-extensions) | Collection of example extensions.<br>拡張のサンプル集 | 230 | unknown | Inactive | unknown | unknown | Official |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — add a YAML file under `data/projects/` and open a PR. The README and site are regenerated automatically.
