---
title: "La valutazione di modernizzazione di GitHub Copilot è il miglior strumento di migrazione che non stai ancora usando"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "L'estensione di modernizzazione di GitHub Copilot non si limita a suggerire modifiche al codice — produce una valutazione completa della migrazione con issue azionabili, confronti tra target Azure e un workflow collaborativo. Ecco perché il documento di valutazione è la chiave di tutto."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "dotnet-modernization-assessment-github-copilot.md" >}}).*

Migrare un'app legacy .NET Framework a .NET moderno è una di quelle attività che tutti sanno di dover fare ma che nessuno vuole iniziare. Non è mai solo "cambiare il target framework." Sono API che sono scomparse, pacchetti che non esistono più, modelli di hosting che funzionano in modo completamente diverso, e un milione di piccole decisioni su cosa containerizzare, cosa riscrivere e cosa lasciare così.

Jeffrey Fritz ha appena pubblicato un [approfondimento sulla valutazione di modernizzazione di GitHub Copilot](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/), e onestamente? È il miglior tooling di migrazione che abbia visto per .NET. Non per la generazione di codice — quello è ormai standard. Per il documento di valutazione che produce.

## Non è solo un motore di suggerimenti di codice

L'estensione VS Code segue un modello **Valuta → Pianifica → Esegui**. La fase di valutazione analizza l'intero codebase e produce un documento strutturato che cattura tutto: cosa deve cambiare, quali risorse Azure provisionare, quale modello di deployment usare. Tutto ciò che segue — infrastructure as code, containerizzazione, manifesti di deployment — deriva da ciò che la valutazione trova.

La valutazione viene salvata in `.github/modernize/assessment/` nel tuo progetto. Ogni esecuzione produce un report indipendente, così accumuli uno storico e puoi monitorare come la tua postura di migrazione evolve man mano che risolvi gli issue.

## Due modi per iniziare

**Valutazione Consigliata** — il percorso veloce. Scegli tra domini curati (Upgrade Java/.NET, Cloud Readiness, Sicurezza) e ottieni risultati significativi senza toccare la configurazione. Ottimo per un primo sguardo a dove si trova la tua app.

**Valutazione Personalizzata** — il percorso mirato. Configura esattamente cosa analizzare: compute target (App Service, AKS, Container Apps), OS target, analisi della containerizzazione. Scegli più target Azure per confrontare gli approcci di migrazione fianco a fianco.

Quella vista di confronto è genuinamente utile. Un'app con 3 issue obbligatori per App Service potrebbe averne 7 per AKS. Vedere entrambi aiuta a guidare la decisione sull'hosting prima di impegnarsi in un percorso di migrazione.

## La suddivisione degli issue è azionabile

Ogni issue viene con un livello di criticità:

- **Obbligatorio** — deve essere risolto o la migrazione fallisce
- **Potenziale** — potrebbe impattare la migrazione, necessita di giudizio umano
- **Opzionale** — miglioramenti raccomandati, non bloccano la migrazione

E ogni issue linka ai file interessati e numeri di riga, fornisce una descrizione dettagliata di cosa c'è che non va e perché conta per la tua piattaforma target, dà passaggi concreti di remediation (non solo "sistema questo"), e include link alla documentazione ufficiale.

Puoi assegnare singoli issue agli sviluppatori e hanno tutto ciò di cui hanno bisogno per agire. Questa è la differenza tra uno strumento che ti dice "c'è un problema" e uno che ti dice come risolverlo.

## I percorsi di upgrade coperti

Per .NET specificamente:
- .NET Framework → .NET 10
- ASP.NET → ASP.NET Core

Ogni percorso di upgrade ha regole di rilevamento che sanno quali API sono state rimosse, quali pattern non hanno un equivalente diretto e quali problemi di sicurezza richiedono attenzione.

Per i team che gestiscono più applicazioni, c'è anche un CLI che supporta valutazioni batch multi-repo — clona tutti i repo, valutali tutti, ottieni report per app più una vista aggregata del portfolio.

## La mia opinione

Se sei seduto su applicazioni legacy .NET Framework (e siamo onesti, la maggior parte dei team enterprise lo è), questo è *lo* strumento con cui iniziare. Il solo documento di valutazione vale il tempo — trasforma un vago "dovremmo modernizzare" in una lista concreta e prioritizzata di elementi di lavoro con percorsi chiari in avanti.

Il workflow collaborativo è intelligente anche: esporta le valutazioni, condividile con il tuo team, importale senza rieseguire. Review di architettura dove chi decide non è chi esegue gli strumenti? Coperto.

## Conclusione

La valutazione di modernizzazione di GitHub Copilot trasforma la migrazione .NET da un progetto spaventoso e indefinito in un processo strutturato e tracciabile. Inizia con una valutazione consigliata per vedere a che punto sei, poi usa valutazioni personalizzate per confrontare i target Azure e costruire il tuo piano di migrazione.

Leggi il [walkthrough completo](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) e scarica l'[estensione VS Code](https://aka.ms/ghcp-appmod/vscode-ext) per provarla sul tuo codebase.
