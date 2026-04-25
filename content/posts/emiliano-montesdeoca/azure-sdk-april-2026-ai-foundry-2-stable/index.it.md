---
title: "Azure SDK Aprile 2026: AI Foundry 2.0 e Cosa Devono Sapere gli Sviluppatori .NET"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "La versione Azure SDK di aprile 2026 porta Azure.AI.Projects 2.0.0 stabile con breaking change significativi, correzioni critiche di sicurezza per Cosmos DB e nuove librerie di Provisioning per .NET."
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui](https://thedotnetblog.com/posts/emiliano-montesdeoca/azure-sdk-april-2026-ai-foundry-2-stable/).*

Le versioni mensili dell'SDK sono spesso facili da ignorare. Questa ha alcune cose degne di attenzione — specialmente se stai costruendo con AI Foundry, Cosmos DB in Java, o fai provisioning di infrastruttura da codice .NET.

## Azure.AI.Projects 2.0.0 — Breaking Change che Hanno Senso

Split di namespace, tipi rinominati, e convenzione `Is*` coerente per i booleani.

## Cosmos DB Java: Correzione Critica di Sicurezza (RCE)

La versione 4.79.0 corregge una **vulnerabilità di Remote Code Execution (CWE-502)**. Aggiorna immediatamente.

## Nuove Librerie di Provisioning per .NET

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

Post originale: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).
