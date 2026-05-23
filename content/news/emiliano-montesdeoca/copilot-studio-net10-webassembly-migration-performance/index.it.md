---
title: "Come Copilot Studio È Migrato a .NET 10 WebAssembly e Si È Velocizzato del 20%"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "I miglioramenti di .NET 10 WASM non sono solo per i nuovi progetti. Ecco cosa ha misurato Copilot Studio dopo l'aggiornamento da .NET 8: fingerprinting automatico, WasmStripILAfterAOT per impostazione predefinita e numeri reali di prestazioni di esecuzione."
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

Il team di Copilot Studio ha fatto qualcosa su cui tutti gli sviluppatori Blazor WASM erano curiosi: hanno effettivamente aggiornato un'applicazione di produzione da .NET 8 a .NET 10 e misurato i risultati. Il post condivide numeri specifici, il che è raro e genuinamente utile.

## La Migrazione È Stata Noiosa (Questo è Positivo)

Aggiornare il framework di destinazione, aggiornare i riferimenti ai pacchetti, correggere le modifiche che causano interruzioni. Tutto qui. La build .NET 10 ora è in esecuzione in produzione. La migrazione stessa non era la parte interessante — le modifiche in .NET 10 lo sono.

## Fingerprinting Automatico degli Asset

In precedenza, distribuire un'app WASM significava scrivere script personalizzati per rinominare gli asset pubblicati con hash SHA256 per l'invalidazione della cache. Copilot Studio aveva uno script PowerShell che faceva esattamente questo — rinominare i file, iniettare attributi `integrity` nel loader JavaScript, gestire tutto manualmente.

In .NET 10, tutto ciò è integrato. Gli asset pubblicati vengono automaticamente contrassegnati con fingerprint, importati direttamente da `dotnet.js` e validati con integrità senza intervento manuale. Il team ha eliminato lo script di rinomina.

Piccolo cambiamento nell'ambito, riduzione significativa della complessità.

## WasmStripILAfterAOT Ora È Abilitato per Impostazione Predefinita

In .NET 8, rimuovere IL dagli assembly compilati AOT era opt-in. In .NET 10 è l'impostazione predefinita. Dopo la compilazione AOT, il bytecode IL originale viene rimosso dall'output — non è necessario in fase di runtime, e mantenerlo gonfiava le dimensioni del pacchetto senza motivo.

Copilot Studio usa un'ottimizzazione specifica: distribuisce sia un motore JIT (avvio rapido) sia un motore AOT (massime prestazioni in stato stazionario), caricandoli entrambi in parallelo e passando da JIT ad AOT una volta pronto. Deduplica anche i file identici tra i due motori.

Il nuovo comportamento di stripping dell'IL significa che gli assembly AOT non corrispondono più bit per bit alle loro controparti JIT, quindi meno file vengono deduplicati:
- .NET 8: 59 file condivisi
- .NET 10: 22 file condivisi

Risultato netto: dimensione del pacchetto circa il 15% maggiore per il motore AOT. Il download AOT è ~6% più lento su LAN veloce, ~17% più lento su 4G. Ma tutto avviene in background dopo che l'app è già interattiva.

## I Numeri delle Prestazioni

Questa è la parte che conta:

- **~20% più veloce** alla prima chiamata (percorso freddo)
- **~5% più veloce** nelle chiamate successive (percorso caldo)

I miglioramenti sono più visibili nei "bot grandi" — agenti grandi e complessi dove domina il codice compilato AOT. Per flussi di lavoro più semplici il guadagno è minore.

## Se Sei Ancora su .NET 8

La storia di migrazione è genuinamente semplice: aggiorna `<TargetFramework>`, aggiorna i riferimenti ai pacchetti, rimuovi eventuali script di fingerprinting personalizzati, e beneficerai automaticamente di `WasmStripILAfterAOT`. Se stai compilando in AOT, aspettati guadagni di prestazioni simili.

Una nota dal post: se carichi il runtime .NET WASM all'interno di un `WebWorker`, imposta `dotnetSidecar = true` all'inizializzazione.

Post originale: [Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
