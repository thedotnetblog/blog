---
title: "Het Herhalende Migratiewerk Elimineren met Agentic Platform Engineering"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape begeleidt de migratie van een echte AWS Terraform-deployment naar Azure Bicep — door de deployment-intentie te extraheren en de architectuur opnieuw te mappen in plaats van een 1:1 syntaxconversie te doen."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — een stap-voor-stap gids van Git-Ape (git agentisch platform engineering tool) dat een echt AWS Terraform-repo naar Azure migreert, met focus op intentie-extractie in plaats van regel-voor-regel conversie.

## De invoer: contoso-migration

De bron is een echt Terraform-project (`contoso-migration`) dat een Next.js-app op AWS deployt — EC2 voor compute, ALB voor load balancing, S3 voor artefacten, en IAM-sleutels voor identiteit. Kosten: ~$34/maand. Het doel is niet dezelfde infrastructuur op Azure te reproduceren; het is uitzoeken wat de deployment eigenlijk probeert te doen en dat herbouwen met Azure-native services.

## Stap 1: Validatie en authenticatie

Git-Ape begint met het valideren van alle vereiste CLI-tools — `az`, `aws`, `gh`, `jq`, `git` — en het bevestigen van actieve auth-sessies voordat er iets wordt aangeraakt. Geen gedeeltelijke uitvoeringen.

## Stap 2: Intentie-extractie

De agent leest het volledige bronrepository via de GitHub API en extraheert de deployment-intentie: runtime (Node.js), compute-type, ingress-patroon, artefact-verwerking, identiteitsmodel, netwerken en monitoring. Dit is de cruciale stap — het bouwt een semantisch model van wat de deployment doet, niet welke Terraform-sleutelwoorden het gebruikt.

## Stap 3: Service-mapping

AWS-services worden gekoppeld aan Azure-equivalenten:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → Ingebouwde App Service load balancing
- IAM-rollen/sleutels → Managed Identity
- Terraform → Bicep + GitHub Actions

## Stap 4: Criticus-agent

Voordat de uitvoer wordt gegenereerd, voert een criticus-agent uit en detecteert twee blokkerende problemen:

1. **Build-on-startup anti-patroon** — de originele Terraform voerde `npm install && npm run build` uit op EC2 bij het opstarten. Fix: bouw in CI, deploy een gereed artefact.
2. **Onnodige Blob Storage** — S3 werd gebruikt voor artefact-staging die geëlimineerd kon worden met de juiste CI/CD. De criticus-agent verwijderde het volledig.

## Stap 5: Gegenereerde uitvoer

Het resultaat is ~80 regels Bicep in plaats van de originele 200+ regels Terraform. De agent maakte een nieuwe GitHub-repo met `infra/main.bicep` en `.github/workflows/deploy.yml` en verwijderde alle AWS-specifieke bestanden.

## Vergelijking van beveiligingshouding

De migratie leverde ook een betekenisvolle beveiligingsverbetering op:

| AWS origineel | Azure-uitvoer |
|---|---|
| Alleen HTTP | Alleen HTTPS, TLS 1.2 |
| SSH open naar 0.0.0.0/0 | Geen SSH-blootstelling |
| IAM-toegangssleutels | OIDC + Managed Identity |
| Geen monitoring | Application Insights |

Kosten: ~$13/maand vs de originele $34/maand.

## Wat dit onderscheidt van een syntaxisconverter

De criticus-agent stap is wat dit onderscheidt van een mechanische vertaling. Het ving patronen op die op AWS zouden hebben gewerkt maar op Azure fout zouden zijn — en corrigeerde ze in plaats van ze te repliceren. De uitvoer is niet "AWS in Azure-syntaxis"; het is een Azure-native deployment die hetzelfde doel schoner bereikt.

Zie de [volledige gids](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) voor de volledige agent-trace en gegenereerde bestanden.
