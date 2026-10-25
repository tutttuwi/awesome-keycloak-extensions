# 003: Add "Protocol (CAS / WS-Fed)" genre

- Date: 2026-10-25
- Decision: Add `Protocol (CAS / WS-Fed)` to `GENRES` for extensions that implement an additional login protocol (LoginProtocol SPI) such as CAS or WS-Federation.
- Why: the first full discovery run found three such entries (`jacekkow/keycloak-protocol-cas`, `cloudtrust/keycloak-wsfed`, `ChosoMeister/Keycloak-WS-Federation`). None of the existing genres fit: they are not identity providers (Keycloak acts as the IdP) nor protocol mappers.
