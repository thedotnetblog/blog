---
title: "Azure Developer CLI continua a diventare uno strumento migliore per l'inner loop"
date: 2026-06-28
author: "Emiliano Montesdeoca"
description: "Le release di maggio e giugno 2026 di Azure Developer CLI aggiungono molto, ma il valore più grande è in come migliorano il ciclo quotidiano: migliore gestione degli strumenti, provisioning più sicuro, supporto più forte per le estensioni e flussi di esecuzione più pratici."
tags:
  - Azure Developer CLI
  - azd
  - Azure
  - Developer Tools
  - .NET
---

*Questo articolo è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

I grandi riepiloghi di CLI possono essere estenuanti da leggere perché mescolano grandi miglioramenti del workflow e piccoli fix in un unico muro di testo.

Quindi ecco la mia versione breve: gli ultimi aggiornamenti di **Azure Developer CLI** contano perché `azd` continua a diventare un **miglior strumento per l'inner loop**, non solo un wrapper di deployment.

Questo è il vero cambiamento.

## La gestione degli strumenti sta diventando parte del prodotto, non un compito laterale

Una delle mie aggiunte preferite sono i nuovi comandi `azd tool`.

Qualsiasi cosa che riduca l'attrito della configurazione merita attenzione, soprattutto nei progetti in cui un ambiente funzionante dipende da un mix di SDK, CLI, Docker, Bicep ed estensioni.

Se lo strumento ora può aiutare a scoprire, installare, verificare e aggiornare direttamente queste dipendenze, elimina molti dei fastidiosi failure mode che colpiscono per primi i nuovi arrivati.

Questo sì che è valore reale.

## `azd exec` sembra anche più importante di quanto suggerisca il nome

A prima vista, `azd exec` può sembrare una piccola comodità.

Io non la penso così.

Eseguire comandi con tutto il contesto dell'ambiente `azd`, inclusa la risoluzione dei secret, è esattamente il tipo di capacità che rende l'automazione locale e lo scripting molto più puliti.

Riduce la necessità di ulteriori script di collegamento e aiuta a mantenere l'esecuzione coerente tra ambienti diversi.

Questo è un vantaggio pratico.

## Provisioning più sicuro e comportamento di cancellazione migliore sono miglioramenti sottovalutati

La release include anche modifiche alle dipendenze di provisioning, alla gestione della cancellazione e al comportamento del deployment, cose che magari non sembrano glamour ma sono molto benvenute.

I prompt di annullamento interattivi, una migliore modellazione delle dipendenze e uno stato del deployment più chiaro sono esattamente il tipo di miglioramenti che fanno sembrare un CLI affidabile quando lavori con risorse Azure reali.

E la fiducia è un tema enorme per strumenti come questo.

## La mia lettura

Più `azd` migliora in configurazione, scripting, sicurezza del deployment e supporto alle estensioni, più sembra qualcosa che puoi tenere nel tuo ciclo quotidiano invece di toccare solo subito prima del deployment.

È la direzione giusta.

Per i team che costruiscono app cloud-native o guidate dall'AI su Azure, questo rende il CLI più utile dove conta di più: durante lo sviluppo reale.

Articolo originale: [Azure Developer CLI (azd) – May and June 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/)