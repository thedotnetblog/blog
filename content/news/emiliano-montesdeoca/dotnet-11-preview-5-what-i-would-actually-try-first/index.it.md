---
title: ".NET 11 Preview 5: Cosa Proverei Davvero per Primo"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 5 porta miglioramenti in SDK, runtime, C#, ASP.NET Core ed EF Core. Ecco gli aggiornamenti che secondo me vale più la pena testare presto se costruisci app .NET reali."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - Entity Framework
---

I post di preview di .NET sono sempre ricchi.

Questa è una buona notizia per la piattaforma, ma significa anche che la domanda pratica viene sepolta: **cosa dovresti effettivamente testare per primo?**

.NET 11 Preview 5 porta molto in SDK, runtime, librerie, ASP.NET Core, C#, MAUI e EF Core. Invece di trasformarlo in un enorme riepilogo di changelog, voglio concentrarmi sulle parti che secondo me meritano l'attenzione degli sviluppatori ora.

## Il template MCP server in `dotnet new` è un segnale

Questo è probabilmente l'elemento più strategico nella sezione SDK.

Quando un template di progetto arriva direttamente nell'SDK, significa che la piattaforma non sta più trattando lo scenario come di nicchia. Avere un **template MCP Server** integrato in `dotnet new` abbassa il costo di provare il pattern e invia un messaggio chiaro su dove sta andando l'ecosistema.

Se stai costruendo agent tooling, assistenti interni o utility di sviluppo integrate con l'AI in .NET, questa è una delle prime cose che testerei.

## I controlli di vulnerabilità e fine-vita al build sono esattamente il tipo di impostazioni predefinite che mi piacciono

La consapevolezza di sicurezza e ciclo di vita è molto meglio quando la piattaforma ti aiuta *durante il build*, non dopo in un report separato che nessuno legge.

I nuovi controlli SDK per vulnerabilità e pacchetti a fine vita durante il build sono il tipo di funzionalità che amo perché rendono il comportamento migliore l'impostazione predefinita.

Non sono appariscenti, ma sono il tipo di miglioramenti che invecchiano molto bene.

## C# continua a diventare più espressivo nei punti giusti

Gli elementi C# di Preview 5 sono interessanti, specialmente:

- gerarchie di classi chiuse
- dichiarazioni union e pattern union
- lavoro continuo sull'evoluzione unsafe

Non adotterei ciecamente tutto questo in produzione ancora, perché le funzionalità linguistiche in preview meritano sempre un ciclo di test sobrio. Ma la direzione è buona. C# continua a muoversi verso una modellazione più ricca senza perdere la sua identità.

## ASP.NET Core e EF Core hanno aggiornamenti pratici che vale la pena testare presto

Due aree che metterei sicuramente attraverso uno spike:

### Miglioramenti Blazor

La validazione lato client per Blazor SSR e i miglioramenti di QuickGrid senza interattività sono entrambi il tipo di funzionalità di qualità della vita che possono semplificare app reali.

### Impostazioni predefinite e warning di EF Core

EF Core che sposta la compatibilità SQL Server 2022 come predefinita e aggiunge warning per query EF asincrone eseguite in modo sincrono sono esattamente il tipo di cambiamenti che possono far emergere problemi nascosti in codebase reali.

Questo significa che vale la pena testarlo prima possibile.

## La mia breve lista per un primo passaggio

Se avessi mezza giornata per esplorare Preview 5, farei questo:

1. provare il template MCP server
2. eseguire build e ispezionare i nuovi controlli vulnerabilità/EOL
3. testare qualsiasi codebase che potrebbe beneficiare delle nuove funzionalità di modellazione C#
4. validare scenari Blazor SSR se sei su quello stack
5. eseguire percorsi pesanti di EF Core e osservare cambiamenti di warning o differenze SQL

È lì che vedo il valore iniziale.

## Il mio parere

.NET 11 Preview 5 sembra uno di quei rilasci in cui la piattaforma continua a spingere in due direzioni contemporaneamente:

- capacità di sviluppo più ambiziose
- impostazioni predefinite migliori per team orientati alla produzione

Quella combinazione è ciò che voglio da un ciclo di preview.

Provalo, ma provalo con proposito.

Post originale: [.NET 11 Preview 5 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-5/)