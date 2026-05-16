---
title: "Eliminare il Lavoro Ripetitivo della Migrazione con l'Agentic Platform Engineering"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape illustra la migrazione di un deployment Terraform AWS reale verso Azure Bicep — estraendo l'intenzione del deployment e rimappando l'architettura invece di fare una conversione sintattica 1:1."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — una guida passo per passo di Git-Ape (strumento git di ingegneria di piattaforma agentiva) che migra un vero repository Terraform AWS verso Azure, concentrandosi sull'estrazione dell'intenzione piuttosto che sulla conversione riga per riga.

## L'input: contoso-migration

La fonte è un vero progetto Terraform (`contoso-migration`) che distribuisce un'app Next.js su AWS — EC2 per il computing, ALB per il bilanciamento del carico, S3 per gli artefatti e chiavi IAM per l'identità. Costo: ~34 $/mese. L'obiettivo non è riprodurre la stessa infrastruttura su Azure; è capire cosa il deployment sta effettivamente cercando di fare e ricostruirlo con servizi nativi Azure.

## Passo 1: Validazione e autenticazione

Git-Ape inizia validando tutti gli strumenti CLI richiesti — `az`, `aws`, `gh`, `jq`, `git` — e confermando le sessioni di autenticazione attive prima di toccare qualsiasi cosa. Nessuna esecuzione parziale.

## Passo 2: Estrazione dell'intenzione

L'agente legge l'intero repository sorgente tramite l'API GitHub ed estrae l'intenzione del deployment: runtime (Node.js), tipo di computing, modello di ingress, gestione degli artefatti, modello di identità, rete e monitoraggio. Questo è il passaggio chiave — sta costruendo un modello semantico di cosa fa il deployment, non quali parole chiave Terraform usa.

## Passo 3: Mappatura dei servizi

I servizi AWS vengono mappati agli equivalenti Azure:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → Bilanciamento del carico integrato di App Service
- Ruoli/chiavi IAM → Managed Identity
- Terraform → Bicep + GitHub Actions

## Passo 4: Agente critico

Prima di generare l'output, viene eseguito un agente critico che individua due problemi bloccanti:

1. **Anti-pattern di build all'avvio** — il Terraform originale eseguiva `npm install && npm run build` su EC2 all'avvio. Fix: costruire in CI, distribuire un artefatto pronto.
2. **Blob Storage non necessario** — S3 veniva usato per lo staging degli artefatti che poteva essere eliminato con un CI/CD appropriato. L'agente critico lo ha rimosso completamente.

## Passo 5: Output generato

Il risultato è ~80 righe di Bicep invece delle 200+ righe originali di Terraform. L'agente ha creato un nuovo repository GitHub con `infra/main.bicep` e `.github/workflows/deploy.yml` e rimosso tutti i file specifici di AWS.

## Confronto della postura di sicurezza

La migrazione ha anche prodotto un significativo miglioramento della sicurezza:

| AWS originale | Output Azure |
|---|---|
| Solo HTTP | Solo HTTPS, TLS 1.2 |
| SSH aperto a 0.0.0.0/0 | Nessuna esposizione SSH |
| Chiavi di accesso IAM | OIDC + Managed Identity |
| Nessun monitoraggio | Application Insights |

Costo: ~13 $/mese vs i 34 $/mese originali.

## Cosa lo differenzia da un convertitore di sintassi

Il passaggio dell'agente critico è ciò che separa questo da una traduzione meccanica. Ha individuato pattern che avrebbero funzionato su AWS ma sarebbero stati sbagliati su Azure — e li ha corretti invece di replicarli. L'output non è "AWS in sintassi Azure"; è un deployment nativo Azure che raggiunge lo stesso obiettivo in modo più pulito.

Vedi la [guida completa](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) per la traccia completa dell'agente e i file generati.
