---
title: ".NET 11 Preview 4: Template Server MCP, Librerie Runtime-Async, API Processi"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 è disponibile. I punti salienti: il template del server MCP nell'SDK, le librerie runtime compilate con runtime-async, dotnet watch per mobile e una significativa espansione dell'API Processi."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 è disponibile. Ogni versione di una preview principale di .NET aggiunge un lungo elenco di elementi per runtime, SDK, librerie, ASP.NET Core, MAUI, C# ed Entity Framework. Invece di ripetere la lista completa, ecco le cose che hanno attirato la mia attenzione.

## Il Template del Server MCP Arriva nell'SDK di .NET

L'elemento più interessante: un template di progetto server MCP è ora incluso nell'SDK. Questo significa che `dotnet new mcp-server` (o come finirà per chiamarsi il comando) funziona direttamente. Per chiunque stia costruendo tooling MCP in .NET, questo riduce considerevolmente la frizione iniziale. L'integrazione MCP nella toolchain della piattaforma segnala la direzione in cui si sta muovendo l'ecosistema.

## Librerie Runtime Compilate con Runtime-Async

Il runtime stesso ora compila le sue librerie standard usando la funzionalità runtime-async. È un cambiamento interno che influisce sulle prestazioni — le macchine a stati async nel runtime diventano più efficienti. L'importanza qui non riguarda cambiamenti visibili nell'API; è che runtime-async è abbastanza maturo da essere usato per la BCL stessa, il che è un segnale significativo sulla maturità della funzionalità.

## Ottimizzazioni JIT e Intrinseci Hardware

Preview 4 continua il lavoro sul JIT. Miglioramenti agli intrinseci hardware e alla generazione del codice arrivano qui — i dettagli si trovano nelle note di rilascio del runtime. Questi tipi di cambiamenti migliorano tipicamente il throughput nei cicli di calcolo intensivi senza modifiche al tuo codice.

## Espansione dell'API Processi

Un aggiornamento importante a `System.Diagnostics.Process` arriva in Preview 4:

- `Process.RunAndCaptureTextAsync` — avvia un processo, cattura stdout/stderr, attendi l'uscita, il tutto in una chiamata senza rischio di deadlock
- `KillOnParentExit` — accoppiamento leggero del ciclo di vita tra processo padre e figlio
- API basate su `SafeProcessHandle` più compatibili con il trimmer

Se hai mai scritto codice ripetitivo per catturare l'output di un processo senza causare deadlock (lettura async di stdout *e* stderr contemporaneamente), `RunAndCaptureTextAsync` è l'API che mancava.

## dotnet watch per Android e iOS

`dotnet watch` ora supporta la selezione del dispositivo per i progetti .NET MAUI Android e iOS. Iterazione più rapida su mobile senza gestire manualmente le connessioni ai dispositivi nel ciclo di build.

## API di Compressione Basate su Span

Nuove API di encoder/decoder Deflate, ZLib e GZip basate su span arrivano nelle librerie. Meno allocazioni quando si lavora con dati compressi — rilevante se si effettua elaborazione dati ad alto throughput.

## Provalo

[Scarica .NET 11 Preview 4](https://dotnet.microsoft.com/download/dotnet/11.0) — è una preview, non pronta per la produzione, ma vale la pena eseguirla sui tuoi progetti per individuare eventuali problemi in anticipo prima del ciclo RC.

Post originale: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
