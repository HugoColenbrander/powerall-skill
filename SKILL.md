---
name: powerall
description: "Powerall ERP: gebruikersdocumentatie, Connect API, en bedrijfsprocessen (work orders, service, sales, warehouse, finance, inkoop, verhuur)."
version: 1.0.0
author: Hugo Colenbrander
metadata:
  hermes:
    tags: [powerall, erp, api, business, work-orders, service, sales, warehouse, finance]
---

# Powerall ERP

Powerall is een Nederlands ERP-systeem voor bedrijven in techniek, installatie, handel en service. Deze skill bevat de volledige gebruikersdocumentatie + Connect API reference.

**Wanneer te laden:**
- Vragen over Powerall functionaliteit (werkaanvragen, serviceverzoeken, verkoop, inkoop, voorraad, facturatie, etc.)
- Vragen over de Powerall Connect API (endpoints, authenticatie, data modellen)
- Powerall gerelateerde integraties of automatisering

## Referentie-bestanden

Laad alleen de relevante references via `skill_view(name='powerall', file_path='references/...')`:

### Gebruikersdocumentatie (Markdown, Nederlands)
| Bestand | Onderwerp | Grootte |
| --- | --- | --- |
| `references/work.md` | Werkaanvragen, uren registratie, materialen | 156 KB |
| `references/service.md` | Serviceverzoeken, service objecten, contracten | 25 KB |
| `references/sales.md` | Verkooporders, offertes, leveringen | 102 KB |
| `references/purchase.md` | Inkooporders, goederenontvangsten, inkoopfacturen | 64 KB |
| `references/warehouse.md` | Voorraadbeheer, magazijnen, picklijsten, tellingen | 76 KB |
| `references/finance.md` | Facturatie, dagboeken, grootboek, BTW, betalingen | 201 KB |
| `references/customer.md` | Relaties, contactpersonen, afleveradressen | 98 KB |
| `references/article.md` | Artikelen, producten, productgroepen, prijzen | 106 KB |
| `references/machine.md` | Objecten, service objecten, service historie | 129 KB |
| `references/rental.md` | Verhuur, huurcontracten | 30 KB |
| `references/general.md` | Algemene instellingen, gebruikers, rechten | 100 KB |
| `references/dashboard.md` | Dashboard, widgets, KPI's | 1.5 KB |
| `references/layout.md` | Schermlayout, velden, weergave | 10 KB |
| `references/faq.md` | Veelgestelde vragen (alle modules) | 473 KB |

### API & Developer docs
| Bestand | Onderwerp | Grootte |
| --- | --- | --- |
| `references/powerall-api-reference.md` | Connect API: 108 endpoints + 395 data modellen in Markdown | 206 KB |
| `references/powerall-api-swagger.json` | Originele Swagger 2.0 spec (machine-readable) | 505 KB |

### Scripts
| Bestand | Functie |
| --- | --- |
| `scripts/powerall-api.sh` | curl wrapper voor Connect API calls |

## Connect API Quick Reference

**Base URL:** `https://connect.powerall.io`
**Auth:** Basic Authentication (tenant name + API token)
**Format:** JSON

### API-script gebruiken
```bash
export POWERALL_TENANT="jouw_tenant"
export POWERALL_TOKEN="jouw_token"
bash ~/.hermes/skills/powerall/scripts/powerall-api.sh GET /v1/relations
bash ~/.hermes/skills/powerall/scripts/powerall-api.sh GET "/v1/products?limit=10&include=Supplier"
bash ~/.hermes/skills/powerall/scripts/powerall-api.sh POST /v1/service-messages '{"field":"value"}'
```

### Belangrijkste endpoints
| Endpoint | Methoden | Omschrijving |
| --- | --- | --- |
| `/v1/relations` | GET, POST | Relaties (klanten/leveranciers) |
| `/v1/relations/{id}/delivery-addresses` | GET, POST | Afleveradressen |
| `/v1/work-orders` | GET | Werkaanvragen |
| `/v1/work-orders/{rc}:{nr}/hours` | GET, POST | Uren per werkaanvraag |
| `/v1/work-orders/{rc}:{nr}/lines` | POST | Materiaalregels |
| `/v1/service-messages` | GET, POST | Serviceverzoeken |
| `/v1/service-objects` | GET | Service objecten (machines) |
| `/v1/sales-orders` | GET, POST | Verkooporders |
| `/v1/sales-orders/lines` | GET | Verkooporderregels |
| `/v1/purchase-orders` | GET | Inkooporders |
| `/v1/products` | GET | Producten/artikelen |
| `/v1/products/{code}` | GET, PATCH | Specifiek product |
| `/v1/invoices` | GET | Facturen |
| `/v1/deliveries` | GET, POST | Leveringen |
| `/v1/employees` | GET | Medewerkers |
| `/v1/warehouses` | GET | Magazijnen |
| `/v1/permissions` | GET | Permissies |

### Query parameters
- `filters` — veldnaam:operator:waarde (bijv. `relationCode:eq:10001`). Operatoren: eq, ne, gt, lt, ge, le, like, in, notIn, isNull, isNotNull
- `include` — gerelateerde data meeladen (bijv. `include=Lines,Relation`)
- `orderBy` — veldnaam:ASC of veldnaam:DESC
- `limit` / `offset` — paginering
- `includeTotalItems` — totaalaantal meegeven

### Scope per endpoint
Elk endpoint vereist een scope (bijv. `relations.read`, `work-orders.write`). De scope staat in de endpoint-documentatie. Vraag de API-token aan bij je Powerall leverancier met de juiste scopes.

## Query-strategie

1. **Hoe werkt X in Powerall?** → Laad de relevante module reference (work.md, sales.md, etc.)
2. **Hoe configureer ik X?** → general.md of het relevante module-bestand
3. **API endpoint voor X?** → Laad `references/powerall-api-reference.md`
4. **Foutmelding / probleem?** → faq.md (473 KB met oplossingen)
5. **Data model / velden?** → powerall-api-reference.md heeft alle 395 modellen met veldbeschrijvingen
6. **API call doen?** → scripts/powerall-api.sh + powerall-api-reference.md voor parameters

## Valkuilen

- Alle decimalen zijn strings in de API (bijv. `"amount": "123.45"`) om precisieverlies te voorkomen
- Relaties worden geidentificeerd door `relationCode` (niet ID) in veel endpoints
- Werkaanvragen en verkooporders gebruiken composite keys: `{relationCode}:{entryNumber}`
- De API ondersteunt geen webhooks — alleen polling via `last-modified-rules` endpoint
- Geen rate limiting, maar wees respectvol met call-frequentie
- De Nederlandse documentatie gebruikt Powerall-specifieke terminologie (zie faq.md voor definities)
