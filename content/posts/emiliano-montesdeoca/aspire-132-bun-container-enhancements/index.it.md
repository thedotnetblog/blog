---
title: "Aspire 13.2: Supporto Bun, Contenitori Migliori e Meno Attrito nel Debug"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 aggiunge supporto Bun di prima classe per le app Vite, corregge l'affidabilità di Yarn e porta miglioramenti ai container che rendono il comportamento locale più prevedibile."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui](https://thedotnetblog.com/posts/emiliano-montesdeoca/aspire-132-bun-container-enhancements/).*

Se stai costruendo backend .NET con frontend JavaScript in Aspire, la 13.2 è l'aggiornamento che migliora silenziosamente la tua giornata.

## Bun è Ora di Prima Classe

```typescript
await builder
  .addViteApp("frontend", "./frontend")
  .withBun();
```

Se il tuo team usa già Bun, Aspire non ti costringe più a nuotare controcorrente.

## Yarn Più Affidabile

Gli utenti Yarn ottengono meno errori misteriosi con `withYarn()` e `addViteApp()`.

## Miglioramenti ai Container

`ImagePullPolicy.Never` per usare l'immagine locale senza andare al registry. PostgreSQL 18+ con volumi di dati ora funziona correttamente.

## Miglioramenti al Debug

- `DebuggerDisplayAttribute` sui tipi core
- Messaggi di errore migliori per `WaitFor`
- `BeforeResourceStartedEvent` si attiva al momento giusto

Post originale di David Pine: [Aspire 13.2: Bun Support and Container Enhancements](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/).
