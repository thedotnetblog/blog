---
title: ".NET Aprile 2026 Servicing — Patch di sicurezza da applicare oggi"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "L'aggiornamento di servicing di aprile 2026 corregge 6 CVE in .NET 10, .NET 9, .NET 8 e .NET Framework — incluse due vulnerabilità di esecuzione di codice remoto."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "dotnet-april-2026-servicing-security-patches.md" >}}).*

Gli [aggiornamenti di servicing di aprile 2026](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) per .NET e .NET Framework sono disponibili, e questo include correzioni di sicurezza che vorrai applicare presto. Sei CVE corrette, incluse due vulnerabilità di esecuzione di codice remoto (RCE).

## Cosa è stato corretto

Ecco il riepilogo rapido:

| CVE | Tipo | Interessa |
|-----|------|-----------|
| CVE-2026-26171 | Bypass delle funzionalità di sicurezza | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Esecuzione di codice remoto** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Esecuzione di codice remoto** | .NET 10, 9, 8 |
| CVE-2026-32203 | Denial of Service | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Denial of Service | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Denial of Service | .NET Framework 2.0–4.8.1 |

Le due CVE RCE (CVE-2026-32178 e CVE-2026-33116) interessano la gamma più ampia di versioni .NET e dovrebbero essere la priorità.

## Versioni aggiornate

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

Tutte sono disponibili attraverso i canali abituali — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0), immagini container su MCR e gestori di pacchetti Linux.

## Cosa fare

Aggiorna i tuoi progetti e le pipeline CI/CD alle ultime versioni con patch. Se stai usando container, scarica le immagini più recenti. Se sei su .NET Framework, controlla le [note di rilascio di .NET Framework](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes) per le patch corrispondenti.

Per chi sta eseguendo .NET 10 in produzione (è la versione corrente), 10.0.6 è un aggiornamento obbligatorio. Lo stesso vale per .NET 9.0.15 e .NET 8.0.26 se sei su quelle versioni LTS. Due vulnerabilità RCE non sono qualcosa che si rimanda.
