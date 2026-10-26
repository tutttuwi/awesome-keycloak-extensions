# awesome-keycloak-extensions

A curated, ranked catalog of Keycloak extensions (SPI implementations) and companion tools — official-list entries plus popular community projects.  
Keycloakの拡張(SPI実装)と周辺ツールを、公式掲載分+人気のコミュニティ製も含めてランキング形式でまとめたカタログです。

**Browse / filter / search: https://noccalabs.com/awesome-keycloak-extensions/**

> Data fetched: **2026-10-25** (README generated 2026-10-26). Stars/forks/last commit come from the GitHub API; `unknown` = not fetched yet (never guessed). Official list: <https://www.keycloak.org/extensions>

Activity: **Active** ≤12 months · **Stale** 12–24 months · **Inactive** >24 months / archived / "no longer maintained" · **Unknown** = last commit not fetched yet.

## Top 20 (SPI extensions, by ★)

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-metrics-spi](https://github.com/aerogear/keycloak-metrics-spi)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/aerogear/keycloak-metrics-spi.html) | Exposes Keycloak metrics (Prometheus format) via an SPI.<br>KeycloakのメトリクスをPrometheus形式で公開するSPI | 614 | 2024-11-08 | Stale | 26.0.0 | Apache-2.0 | Official |
| 2 | [keycloak-orgs](https://github.com/p2-inc/keycloak-orgs)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/p2-inc/keycloak-orgs.html) | Organizations / multi-tenancy for Keycloak realms.<br>Keycloakの組織・マルチテナント機能 | 544 | 2026-10-14 | Active | 26.8.0 | Elastic-2.0 | Official |
| 3 | [keycloak-restrict-client-auth](https://github.com/sventorben/keycloak-restrict-client-auth)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/sventorben/keycloak-restrict-client-auth.html) | Restrict which users may access which clients (role/policy based).<br>クライアント単位でユーザーのアクセスを制限 | 440 | 2026-10-14 | Active | 26.8.0 | MIT | Official |
| 4 | [keycloak-extensions-demo](https://github.com/dasniko/keycloak-extensions-demo)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/dasniko/keycloak-extensions-demo.html) | Demo of many SPI types: action token, authenticators, event listener, token mapper, required action, etc.<br>多数のSPI実装例(actiontoken/authenticator/event-listener/tokenmapper/requiredaction等) | 434 | 2026-10-14 | Active | nightly | Apache-2.0 | Official |
| 5 | [keycloak-magic-link](https://github.com/p2-inc/keycloak-magic-link)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/p2-inc/keycloak-magic-link.html) | Passwordless magic-link login.<br>マジックリンク(パスワードレス)認証 | 430 | 2026-10-20 | Active | 26.8.0 | Other (see repo) | Official |
| 6 | [keycloak-home-idp-discovery](https://github.com/sventorben/keycloak-home-idp-discovery)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/sventorben/keycloak-home-idp-discovery.html) | Discover the home IdP from the user's email domain.<br>メールドメインからホームIdPを自動判定 | 341 | 2026-10-02 | Active | 26.8.0 | MIT | Official |
| 7 | [keycloak-events](https://github.com/p2-inc/keycloak-events)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/p2-inc/keycloak-events.html) | Event listeners and webhooks for Keycloak events.<br>Keycloakイベント用のリスナー/Webhook | 317 | 2026-10-15 | Active | 26.8.0 | Other (see repo) | Official |
| 8 | [keycloak-mfa-plugins](https://github.com/netzbegruenung/keycloak-mfa-plugins)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/netzbegruenung/keycloak-mfa-plugins.html) | MFA plugins: SMS, enforced MFA, native-app MFA.<br>MFAプラグイン集(SMS/強制MFA/ネイティブアプリMFA) | 300 | 2026-10-13 | Active | 26.8.0 | Apache-2.0 | Official |
| 9 | [apple-identity-provider-keycloak](https://github.com/klausbetz/apple-identity-provider-keycloak)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/klausbetz/apple-identity-provider-keycloak.html) | Sign in with Apple identity provider.<br>Sign in with Apple用Identity Provider | 297 | 2026-01-18 | Active | unknown | Apache-2.0 | Official |
| 10 | [keycloak-2fa-email-authenticator](https://github.com/mesutpiskin/keycloak-2fa-email-authenticator)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/mesutpiskin/keycloak-2fa-email-authenticator.html) | Email OTP second-factor authenticator.<br>メールOTPによる二要素認証 | 289 | 2026-10-23 | Active | 26.7.3 | Apache-2.0 | Community |
| 11 | [keycloak-multi-tenancy](https://github.com/anarsultanov/keycloak-multi-tenancy)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/anarsultanov/keycloak-multi-tenancy.html) | Multi-tenancy support for Keycloak.<br>Keycloakのマルチテナント対応 | 171 | 2025-12-12 | Active | 26.3.1 | Apache-2.0 | Official |
| 12 | [keycloak-discord](https://github.com/wadahiro/keycloak-discord)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/wadahiro/keycloak-discord.html) | Discord identity provider.<br>Discord用Identity Provider | 158 | 2024-11-02 | Stale | 26.0.5 | Apache-2.0 | Official |
| 13 | [keycloak-protocol-cas](https://github.com/jacekkow/keycloak-protocol-cas)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/jacekkow/keycloak-protocol-cas.html) | CAS protocol support for Keycloak.<br>KeycloakにCASプロトコルを追加 | 131 | 2026-10-13 | Active | unknown | Apache-2.0 | Official |
| 14 | [keycloak-provider](https://github.com/privacyidea/keycloak-provider)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/privacyidea/keycloak-provider.html) | OTP / 2FA via a privacyIDEA server.<br>privacyIDEA連携のOTP二要素認証 | 131 | 2026-07-01 | Active | 26.5.6 | Apache-2.0 | Official |
| 15 | [keycloak-webhook](https://github.com/vymalo/keycloak-webhook)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/vymalo/keycloak-webhook.html) | Send Keycloak events to webhooks (HTTP, AMQP, Syslog).<br>KeycloakイベントをWebhook等へ送信 | 114 | 2026-07-26 | Active | unknown | MIT | Community |
| 16 | [Keycloak-FranceConnect](https://github.com/InseeFr/Keycloak-FranceConnect)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/InseeFr/Keycloak-FranceConnect.html) | FranceConnect / ProConnect identity providers.<br>FranceConnect/ProConnect用Identity Provider | 107 | 2026-09-10 | Active | 26.7.2 | MIT | Official |
| 17 | [keycloak-adaptive-authn](https://github.com/mabartos/keycloak-adaptive-authn)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/mabartos/keycloak-adaptive-authn.html) | Risk-based / adaptive authentication.<br>リスクベース(アダプティブ)認証 | 105 | 2026-07-28 | Active | nightly | Apache-2.0 | Official |
| 18 | [keycloak-scim-server](https://github.com/Metatavu/keycloak-scim-server)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/Metatavu/keycloak-scim-server.html) | SCIM server implemented as a Keycloak extension.<br>KeycloakにSCIMサーバーを追加する拡張 | 95 | 2026-10-07 | Active | unknown | Apache-2.0 | Official |
| 19 | [keycloak-phone-number](https://github.com/vymalo/keycloak-phone-number)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/vymalo/keycloak-phone-number.html) | Log in with a phone number and SMS OTP.<br>電話番号+SMS OTPでログイン | 55 | 2026-07-24 | Active | 26.5.2 | MIT | Community |
| 20 | [keycloak-custom-event-listener](https://github.com/cevheri/keycloak-custom-event-listener)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/cevheri/keycloak-custom-event-listener.html) | Example event listener that forwards user create/register events to an API.<br>ユーザー作成/登録イベントを外部APIへ送るリスナー例 | 55 | 2024-11-05 | Stale | unknown | Apache-2.0 | Community |

## By genre

### Authentication

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-magic-link](https://github.com/p2-inc/keycloak-magic-link)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/p2-inc/keycloak-magic-link.html) | Passwordless magic-link login.<br>マジックリンク(パスワードレス)認証 | 430 | 2026-10-20 | Active | 26.8.0 | Other (see repo) | Official |
| 2 | [keycloak-home-idp-discovery](https://github.com/sventorben/keycloak-home-idp-discovery)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/sventorben/keycloak-home-idp-discovery.html) | Discover the home IdP from the user's email domain.<br>メールドメインからホームIdPを自動判定 | 341 | 2026-10-02 | Active | 26.8.0 | MIT | Official |
| 3 | [keycloak-adaptive-authn](https://github.com/mabartos/keycloak-adaptive-authn)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/mabartos/keycloak-adaptive-authn.html) | Risk-based / adaptive authentication.<br>リスクベース(アダプティブ)認証 | 105 | 2026-07-28 | Active | nightly | Apache-2.0 | Official |
| 4 | [keycloak-phone-number](https://github.com/vymalo/keycloak-phone-number)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/vymalo/keycloak-phone-number.html) | Log in with a phone number and SMS OTP.<br>電話番号+SMS OTPでログイン | 55 | 2026-07-24 | Active | 26.5.2 | MIT | Community |
| 5 | [keycloak-psso-extension](https://github.com/unioslo/keycloak-psso-extension)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/unioslo/keycloak-psso-extension.html) | macOS Platform Single Sign-On (PSSO) support.<br>macOS Platform SSO対応 | 50 | 2026-10-16 | Active | unknown | GPL-2.0 | Official |
| 6 | [keycloak-app-passwords](https://github.com/radicallyopensecurity/keycloak-app-passwords)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/radicallyopensecurity/keycloak-app-passwords.html) | App-specific passwords.<br>アプリ専用パスワードを発行 | 23 | 2026-09-30 | Active | unknown | GPL-3.0 | Official |
| 7 | [keycloak-client-cert-lookup-for-envoy](https://github.com/Nordix/keycloak-client-cert-lookup-for-envoy)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/Nordix/keycloak-client-cert-lookup-for-envoy.html) | X.509 client certificate lookup for Envoy proxies.<br>Envoy経由のX.509クライアント証明書取得 | 9 | 2026-10-19 | Active | 26.8.1 | Apache-2.0 | Official |
| 8 | [keycloak-personal-access-tokens](https://github.com/mrulex-repo/keycloak-personal-access-tokens)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/mrulex-repo/keycloak-personal-access-tokens.html) | Scoped personal access tokens usable as Basic Auth passwords.<br>Basic認証で使えるスコープ付き個人アクセストークン | 4 | 2026-05-20 | Active | unknown | GPL-3.0 | Official |
| 9 | [keycloak-token-auth](https://github.com/mkunz-it/keycloak-token-auth)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/mkunz-it/keycloak-token-auth.html) | Authenticator that logs in with an ID or access token.<br>IDトークン/アクセストークンでログイン | 1 | 2026-06-29 | Active | 26.6.1 | MIT | Official |

### MFA / Passwordless

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-mfa-plugins](https://github.com/netzbegruenung/keycloak-mfa-plugins)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/netzbegruenung/keycloak-mfa-plugins.html) | MFA plugins: SMS, enforced MFA, native-app MFA.<br>MFAプラグイン集(SMS/強制MFA/ネイティブアプリMFA) | 300 | 2026-10-13 | Active | 26.8.0 | Apache-2.0 | Official |
| 2 | [keycloak-2fa-email-authenticator](https://github.com/mesutpiskin/keycloak-2fa-email-authenticator)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/mesutpiskin/keycloak-2fa-email-authenticator.html) | Email OTP second-factor authenticator.<br>メールOTPによる二要素認証 | 289 | 2026-10-23 | Active | 26.7.3 | Apache-2.0 | Community |
| 3 | [keycloak-provider](https://github.com/privacyidea/keycloak-provider)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/privacyidea/keycloak-provider.html) | OTP / 2FA via a privacyIDEA server.<br>privacyIDEA連携のOTP二要素認証 | 131 | 2026-07-01 | Active | 26.5.6 | Apache-2.0 | Official |
| 4 | [keycloak-extension-qr-code-execution](https://github.com/HadleySo/keycloak-extension-qr-code-execution)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/HadleySo/keycloak-extension-qr-code-execution.html) | Sign in from another device by scanning a QR code.<br>QRコードで別端末からサインイン | 14 | 2026-06-13 | Active | unknown | AGPL-3.0 | Official |
| 5 | [keycloak-push-mfa-extension](https://github.com/ba-itsys/keycloak-push-mfa-extension)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/ba-itsys/keycloak-push-mfa-extension.html) | Push-notification MFA.<br>プッシュ通知によるMFA | 12 | 2026-10-19 | Active | 26.8.1 | Apache-2.0 | Official |

### Event / Webhook / Messaging

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-events](https://github.com/p2-inc/keycloak-events)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/p2-inc/keycloak-events.html) | Event listeners and webhooks for Keycloak events.<br>Keycloakイベント用のリスナー/Webhook | 317 | 2026-10-15 | Active | 26.8.0 | Other (see repo) | Official |
| 2 | [keycloak-webhook](https://github.com/vymalo/keycloak-webhook)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/vymalo/keycloak-webhook.html) | Send Keycloak events to webhooks (HTTP, AMQP, Syslog).<br>KeycloakイベントをWebhook等へ送信 | 114 | 2026-07-26 | Active | unknown | MIT | Community |
| 3 | [keycloak-custom-event-listener](https://github.com/cevheri/keycloak-custom-event-listener)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/cevheri/keycloak-custom-event-listener.html) | Example event listener that forwards user create/register events to an API.<br>ユーザー作成/登録イベントを外部APIへ送るリスナー例 | 55 | 2024-11-05 | Stale | unknown | Apache-2.0 | Community |
| 4 | [keycloak-event-enrichment](https://github.com/AdrianIAna/keycloak-event-enrichment)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/AdrianIAna/keycloak-event-enrichment.html) | Enrich authentication events with GeoIP and User-Agent data.<br>認証イベントにGeoIP/User-Agent情報を付与 | 1 | 2026-09-02 | Active | 26.7.2 | Apache-2.0 | Official |

### Identity Provider

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [apple-identity-provider-keycloak](https://github.com/klausbetz/apple-identity-provider-keycloak)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/klausbetz/apple-identity-provider-keycloak.html) | Sign in with Apple identity provider.<br>Sign in with Apple用Identity Provider | 297 | 2026-01-18 | Active | unknown | Apache-2.0 | Official |
| 2 | [keycloak-discord](https://github.com/wadahiro/keycloak-discord)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/wadahiro/keycloak-discord.html) | Discord identity provider.<br>Discord用Identity Provider | 158 | 2024-11-02 | Stale | 26.0.5 | Apache-2.0 | Official |
| 3 | [Keycloak-FranceConnect](https://github.com/InseeFr/Keycloak-FranceConnect)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/InseeFr/Keycloak-FranceConnect.html) | FranceConnect / ProConnect identity providers.<br>FranceConnect/ProConnect用Identity Provider | 107 | 2026-09-10 | Active | 26.7.2 | MIT | Official |
| 4 | [keycloak-extension-bundid](https://github.com/ba-itsys/keycloak-extension-bundid)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/ba-itsys/keycloak-extension-bundid.html) | BundID (German federal ID) SAML identity provider.<br>ドイツBundID用SAML Identity Provider | 40 | 2026-10-23 | Active | unknown | Apache-2.0 | Official |
| 5 | [keycloak-orcid](https://github.com/eosc-kc/keycloak-orcid)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/eosc-kc/keycloak-orcid.html) | ORCID social identity provider.<br>ORCID用Identity Provider | 17 | 2026-07-01 | Active | 26.5.0 | Other (see repo) | Official |
| 6 | [Extended-SAML-IDP](https://github.com/First8/Extended-SAML-IDP)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/First8/Extended-SAML-IDP.html) | SAML identity provider supporting direct (synchronous) SAML responses.<br>同期SAMLレスポンス対応のSAML Identity Provider | 16 | 2026-10-13 | Active | 26.6.4 | Apache-2.0 | Official |
| 7 | [keycloak-tiktok](https://github.com/mpowr-it/keycloak-tiktok)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/mpowr-it/keycloak-tiktok.html) | TikTok social login provider.<br>TikTok用Identity Provider | 6 | 2026-07-24 | Active | unknown | Apache-2.0 | Official |
| 8 | [keycloak-minecraft-idp](https://github.com/groundsgg/keycloak-minecraft-idp)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/groundsgg/keycloak-minecraft-idp.html) | Microsoft / Xbox identity provider that resolves Minecraft profiles.<br>Minecraftプロフィールを解決するMicrosoft/Xbox IdP | 3 | 2026-10-22 | Active | unknown | Other (see repo) | Official |

### Protocol (CAS / WS-Fed)

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-protocol-cas](https://github.com/jacekkow/keycloak-protocol-cas)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/jacekkow/keycloak-protocol-cas.html) | CAS protocol support for Keycloak.<br>KeycloakにCASプロトコルを追加 | 131 | 2026-10-13 | Active | unknown | Apache-2.0 | Official |
| 2 | [Keycloak-WS-Federation](https://github.com/ChosoMeister/Keycloak-WS-Federation)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/ChosoMeister/Keycloak-WS-Federation.html) | WS-Federation 1.2 protocol and identity broker.<br>WS-Federation 1.2プロトコル/ブローカー | 3 | 2026-10-17 | Active | 26.7.0 | AGPL-3.0 | Official |

### Protocol Mapper / Claim

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-external-claim-mapper](https://github.com/zloom/keycloak-external-claim-mapper)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/zloom/keycloak-external-claim-mapper.html) | Protocol mapper that adds data from a remote service to the JWT.<br>外部サービスのデータをJWTに追加 | 15 | 2025-07-03 | Stale | 25.0.0 | Apache-2.0 | Official |
| 2 | [keycloak-rest-claim-mapper](https://github.com/jowe112/keycloak-rest-claim-mapper)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/jowe112/keycloak-rest-claim-mapper.html) | OIDC/SAML mapper that enriches tokens from a REST API.<br>REST APIの値でトークンを拡充するマッパー | 2 | 2026-08-19 | Active | 26.7.1 | Apache-2.0 | Official |
| 3 | [keycloak-filtered-group-membership-mapper](https://github.com/byteworks-ch/keycloak-filtered-group-membership-mapper)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/byteworks-ch/keycloak-filtered-group-membership-mapper.html) | Group membership mapper with filtering.<br>フィルタ付きグループメンバーシップマッパー | 2 | 2026-04-21 | Active | 26.6.0 | Other (see repo) | Official |

### User Storage / Federation

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [Keycloak-PII-Data-Encryption-Provider](https://github.com/MLukman/Keycloak-PII-Data-Encryption-Provider)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/MLukman/Keycloak-PII-Data-Encryption-Provider.html) | Encrypt PII user attributes at rest.<br>ユーザー属性(個人情報)を暗号化して保存 | 39 | 2025-09-02 | Stale | 26.3.3 | Apache-2.0 | Official |

### Provisioning (SCIM)

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-scim-server](https://github.com/Metatavu/keycloak-scim-server)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/Metatavu/keycloak-scim-server.html) | SCIM server implemented as a Keycloak extension.<br>KeycloakにSCIMサーバーを追加する拡張 | 95 | 2026-10-07 | Active | unknown | Apache-2.0 | Official |

### Multi-tenancy / Organization

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-orgs](https://github.com/p2-inc/keycloak-orgs)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/p2-inc/keycloak-orgs.html) | Organizations / multi-tenancy for Keycloak realms.<br>Keycloakの組織・マルチテナント機能 | 544 | 2026-10-14 | Active | 26.8.0 | Elastic-2.0 | Official |
| 2 | [keycloak-multi-tenancy](https://github.com/anarsultanov/keycloak-multi-tenancy)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/anarsultanov/keycloak-multi-tenancy.html) | Multi-tenancy support for Keycloak.<br>Keycloakのマルチテナント対応 | 171 | 2025-12-12 | Active | 26.3.1 | Apache-2.0 | Official |

### Policy / Authorization

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-restrict-client-auth](https://github.com/sventorben/keycloak-restrict-client-auth)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/sventorben/keycloak-restrict-client-auth.html) | Restrict which users may access which clients (role/policy based).<br>クライアント単位でユーザーのアクセスを制限 | 440 | 2026-10-14 | Active | 26.8.0 | MIT | Official |

### Email / Notification

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-login-notification](https://github.com/sea-watch/keycloak-login-notification)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/sea-watch/keycloak-login-notification.html) | Email users when a new login session is created.<br>新規ログイン時にセキュリティ通知メールを送信 | 1 | 2026-07-21 | Active | 26.7.0 | Other (see repo) | Official |

### Theme / UI

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-shadcn](https://github.com/emirhannaneli/keycloak-shadcn)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/emirhannaneli/keycloak-shadcn.html) | Keycloakify + shadcn/ui login theme starter.<br>Keycloakify+shadcn/uiのログインテーマ | 17 | 2026-08-07 | Active | unknown | MIT | Official |
| 2 | [keycloak-configurable-theme](https://github.com/dockndevai/keycloak-configurable-theme)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/dockndevai/keycloak-configurable-theme.html) | One configurable login theme for all realms.<br>全realm共通の設定可能なログインテーマ | 1 | 2026-10-08 | Active | 26.8.0 | Apache-2.0 | Official |

### Monitoring / Audit

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-metrics-spi](https://github.com/aerogear/keycloak-metrics-spi)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/aerogear/keycloak-metrics-spi.html) | Exposes Keycloak metrics (Prometheus format) via an SPI.<br>KeycloakのメトリクスをPrometheus形式で公開するSPI | 614 | 2024-11-08 | Stale | 26.0.0 | Apache-2.0 | Official |
| 2 | [keycloak-account-events](https://github.com/AdrianIAna/keycloak-account-events)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/AdrianIAna/keycloak-account-events.html) | Let users read their own login history.<br>ユーザー自身がログイン履歴を参照できる | 0 | 2026-09-02 | Active | 26.7.2 | Apache-2.0 | Official |

### Storage / Datastore

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-cassandra-extension](https://github.com/ba-itsys/keycloak-cassandra-extension)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/ba-itsys/keycloak-cassandra-extension.html) | Store Keycloak data in Apache Cassandra.<br>KeycloakのデータをApache Cassandraに保存 | 28 | 2026-10-19 | Active | 26.8.1 | Apache-2.0 | Official |
| 2 | [keycloak-secrets-vault-provider](https://github.com/Nordix/keycloak-secrets-vault-provider)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/Nordix/keycloak-secrets-vault-provider.html) | Vault SPI provider for OpenBao / HashiCorp Vault secrets.<br>OpenBao/HashiCorp Vault用Vault SPI | 12 | 2026-10-19 | Active | 26.8.1 | Apache-2.0 | Official |

### Security / Bot protection

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [Keycloak-GeoAware](https://github.com/B2-Code/Keycloak-GeoAware)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/B2-Code/Keycloak-GeoAware.html) | Geolocation-aware login checks and alerts.<br>位置情報に基づくログイン検査・通知 | 22 | 2026-07-22 | Active | 26.7.0 | Apache-2.0 | Official |
| 2 | [keycloak-block-disposable-email](https://github.com/chintanbuch/keycloak-block-disposable-email)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/chintanbuch/keycloak-block-disposable-email.html) | Block registrations with disposable email addresses.<br>使い捨てメールアドレスでの登録をブロック | 12 | 2025-06-16 | Stale | 26.2.5 | Apache-2.0 | Official |
| 3 | [keycloak-alias-guard](https://github.com/it-perspectives/keycloak-alias-guard)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/it-perspectives/keycloak-alias-guard.html) | Block duplicate accounts created via email aliases (+tags, Gmail dots).<br>メールエイリアスによる重複アカウントを防止 | 6 | 2026-06-19 | Active | 26.5.7 | MIT | Official |
| 4 | [cap-captcha-keycloak](https://github.com/schwebke/cap-captcha-keycloak)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/schwebke/cap-captcha-keycloak.html) | Cap (trycap.dev) captcha for the registration flow.<br>登録フローにCap CAPTCHAを追加 | 4 | 2026-10-08 | Active | 26.8.0 | Apache-2.0 | Official |

### Config as code / DevOps

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-atomic-auth-flows](https://github.com/p2-inc/keycloak-atomic-auth-flows)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/p2-inc/keycloak-atomic-auth-flows.html) | Admin REST endpoint to atomically import authentication flows as code.<br>認証フローをアトミックにインポートする管理API | 5 | 2026-10-01 | Active | 26.8.0 | Apache-2.0 | Official |

### Testing / Examples

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-extensions-demo](https://github.com/dasniko/keycloak-extensions-demo)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/dasniko/keycloak-extensions-demo.html) | Demo of many SPI types: action token, authenticators, event listener, token mapper, required action, etc.<br>多数のSPI実装例(actiontoken/authenticator/event-listener/tokenmapper/requiredaction等) | 434 | 2026-10-14 | Active | nightly | Apache-2.0 | Official |

## Companion tools (Terraform, CLI, testing, …)

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-config-cli](https://github.com/adorsys/keycloak-config-cli)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/adorsys/keycloak-config-cli.html) | CLI to manage Keycloak realm configuration as code (YAML/JSON).<br>Keycloakのrealm設定をYAML/JSONでコード管理するCLI | 1,213 | 2026-10-23 | Active | 26.6.2 | Apache-2.0 | Official |
| 2 | [terraform-provider-keycloak](https://github.com/keycloak/terraform-provider-keycloak)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/keycloak/terraform-provider-keycloak.html) | Terraform provider for managing Keycloak resources.<br>Keycloakリソースを管理するTerraform provider | 955 | 2026-10-13 | Active | unknown | Apache-2.0 | Official |
| 3 | [testcontainers-keycloak](https://github.com/dasniko/testcontainers-keycloak)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/dasniko/testcontainers-keycloak.html) | Testcontainers module to run Keycloak in integration tests.<br>Keycloakを統合テストで起動するTestcontainersモジュール | 464 | 2026-10-11 | Active | nightly | Apache-2.0 | Official |
| 4 | [keycloak](https://github.com/ansible-middleware/keycloak)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/ansible-middleware/keycloak.html) | Ansible collection to install and configure Keycloak / Red Hat build of Keycloak.<br>Keycloakを導入・設定するAnsibleコレクション | 139 | 2026-10-16 | Active | unknown | Apache-2.0 | Official |
| 5 | [kcwarden](https://github.com/iteratec/kcwarden)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/iteratec/kcwarden.html) | Security audit tool for Keycloak configuration.<br>Keycloak設定のセキュリティ監査ツール | 135 | 2026-10-16 | Active | unknown | Apache-2.0 | Official |
| 6 | [edp-keycloak-operator](https://github.com/epam/edp-keycloak-operator)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/epam/edp-keycloak-operator.html) | Kubernetes operator that manages Keycloak realms, clients and users as CRs.<br>Keycloakのrealm/client等をCRで管理するKubernetes Operator | 95 | 2026-10-25 | Active | unknown | Apache-2.0 | Official |
| 7 | [provider-keycloak](https://github.com/crossplane-contrib/provider-keycloak)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/crossplane-contrib/provider-keycloak.html) | Crossplane provider to configure Keycloak declaratively.<br>Keycloakを宣言的に設定するCrossplane provider | 73 | 2026-10-19 | Active | unknown | Apache-2.0 | Official |
| 8 | [keycloak-client](https://github.com/keycloak-client/keycloak-client)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/keycloak-client/keycloak-client.html) | Python client for the Keycloak Admin / OIDC APIs.<br>Keycloak用Pythonクライアント | 58 | 2024-12-29 | Stale | unknown | GPL-3.0 | Official |
| 9 | [postgres-keycloak-oauth-validator](https://github.com/cloudnative-pg/postgres-keycloak-oauth-validator)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/cloudnative-pg/postgres-keycloak-oauth-validator.html) | PostgreSQL module that validates Keycloak-issued OAuth2 tokens.<br>Keycloak発行のOAuth2トークンを検証するPostgreSQLモジュール | 30 | 2026-09-15 | Active | unknown | Apache-2.0 | Official |
| 10 | [keycloak-quarkus-extensions](https://github.com/mabartos/keycloak-quarkus-extensions)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/mabartos/keycloak-quarkus-extensions.html) | Add Quarkus extensions or other dependencies to a Keycloak build.<br>KeycloakビルドにQuarkus拡張や依存を追加 | 21 | 2026-10-22 | Active | 26.7.1 | Apache-2.0 | Official |

## Archive (inactive)

Kept for reference; not part of the rankings above.

| # | Name | Summary | ★ | Last commit | Activity | KC | License | Src |
|--:|------|---------|--:|-------------|----------|----|---------|-----|
| 1 | [keycloak-2fa-sms-authenticator](https://github.com/dasniko/keycloak-2fa-sms-authenticator)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/dasniko/keycloak-2fa-sms-authenticator.html) | SMS OTP second-factor authenticator via AWS SNS (demo).<br>AWS SNS経由のSMS OTP二要素認証(デモ) | 377 | 2025-05-07 | Inactive | 24.0.0 | MIT | Community |
| 2 | [keycloak-extensions](https://github.com/zonaut/keycloak-extensions)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/zonaut/keycloak-extensions.html) | Collection of example extensions.<br>拡張のサンプル集 | 230 | 2022-09-19 | Inactive | unknown | Other (see repo) | Official |
| 3 | [keycloak-event-listener-rabbitmq](https://github.com/aznamier/keycloak-event-listener-rabbitmq)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/aznamier/keycloak-event-listener-rabbitmq.html) | Publish Keycloak events to RabbitMQ.<br>KeycloakイベントをRabbitMQへ送信 | 170 | 2024-03-20 | Inactive | 21.1.2 | Apache-2.0 | Official |
| 4 | [keycloak-passport](https://github.com/exlinc/keycloak-passport)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/exlinc/keycloak-passport.html) | Passport.js strategy for multi-realm Keycloak login (Node.js).<br>Node.js(Passport.js)用のKeycloak認証ストラテジー | 104 | 2018-09-07 | Inactive | unknown | Apache-2.0 | Official |
| 5 | [keycloak-user-spi-demo](https://github.com/dasniko/keycloak-user-spi-demo)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/dasniko/keycloak-user-spi-demo.html) | Minimal in-memory User Storage SPI example.<br>インメモリのUser Storage SPI実装例 | 70 | 2024-01-15 | Inactive | 20.0.0 | MIT | Community |
| 6 | [keycloak-openfga-event-publisher](https://github.com/embesozzi/keycloak-openfga-event-publisher)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/embesozzi/keycloak-openfga-event-publisher.html) | Publish Keycloak role/group changes to OpenFGA for fine-grained authorization.<br>ロール/グループ変更をOpenFGAへ連携 | 61 | 2024-07-02 | Inactive | 25.0.1 | Apache-2.0 | Official |
| 7 | [keycloak-json-remote-claim](https://github.com/groupe-sii/keycloak-json-remote-claim)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/groupe-sii/keycloak-json-remote-claim.html) | Protocol mapper that adds claims fetched from a remote JSON endpoint.<br>外部JSON APIから取得した値をクレームに追加 | 56 | 2020-01-08 | Inactive | 8.0.1 | Apache-2.0 | Official |
| 8 | [Keycloak-Federation-ExistingDB](https://github.com/rsatrio/Keycloak-Federation-ExistingDB)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/rsatrio/Keycloak-Federation-ExistingDB.html) | User federation against an existing relational database.<br>既存DBのユーザーをフェデレーション | 53 | 2023-11-21 | Inactive | 21.1.2 | MIT | Community |
| 9 | [keycloak-event-listener-mqtt](https://github.com/softwarefactory-project/keycloak-event-listener-mqtt)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/softwarefactory-project/keycloak-event-listener-mqtt.html) | Publish Keycloak events to an MQTT broker.<br>KeycloakイベントをMQTTブローカーへ送信 | 45 | 2024-05-22 | Inactive | unknown | Apache-2.0 | Community |
| 10 | [keycloak-wsfed](https://github.com/cloudtrust/keycloak-wsfed)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/cloudtrust/keycloak-wsfed.html) | WS-Federation protocol support.<br>WS-Federationプロトコル対応 | 38 | 2020-11-02 | Inactive | unknown | AGPL-3.0 | Official |
| 11 | [verify-keycloak-integration](https://github.com/IBM-Security/verify-keycloak-integration)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/IBM-Security/verify-keycloak-integration.html) | IBM Security Verify authenticators (push / MFA).<br>IBM Security Verify連携の認証器(MFA) | 31 | 2020-06-10 | Inactive | unknown | Apache-2.0 | Official |
| 12 | [keycloak-regex-mapper](https://github.com/LucaFilipozzi/keycloak-regex-mapper)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/LucaFilipozzi/keycloak-regex-mapper.html) | Broker mapper that maps multi-valued claims/attributes by regex.<br>正規表現で多値クレーム/属性をマッピング | 21 | 2021-08-23 | Inactive | 15.0.2 | Apache-2.0 | Official |
| 13 | [keycloak-github-ssh-key-attribute-mapper](https://github.com/softwarefactory-project/keycloak-github-ssh-key-attribute-mapper)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/softwarefactory-project/keycloak-github-ssh-key-attribute-mapper.html) | Mapper that fetches a user's SSH keys from GitHub into an attribute.<br>GitHubのSSH公開鍵をユーザー属性に取り込む | 20 | 2024-02-12 | Inactive | 22.0.0 | Apache-2.0 | Official |
| 14 | [keycloak-impersonation-policy-enforcer](https://github.com/LucaFilipozzi/keycloak-impersonation-policy-enforcer)<br>[can / cannot](https://noccalabs.com/awesome-keycloak-extensions/p/LucaFilipozzi/keycloak-impersonation-policy-enforcer.html) | Authenticator enforcing an impersonation policy.<br>なりすまし(impersonation)ポリシーを強制 | 13 | 2022-12-23 | Inactive | 18.0.2 | Apache-2.0 | Official |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — add a YAML file under `data/projects/` and open a PR. The README and site are regenerated automatically.
