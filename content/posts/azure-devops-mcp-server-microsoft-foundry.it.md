---
title: "Azure DevOps MCP Server arriva in Microsoft Foundry: cosa significa per i tuoi agenti IA"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "L'Azure DevOps MCP Server è ora disponibile in Microsoft Foundry. Collega i tuoi agenti IA direttamente ai workflow DevOps — work item, repo, pipeline — con pochi clic."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

MCP (Model Context Protocol) sta avendo il suo momento. Se hai seguito l'ecosistema degli agenti IA, probabilmente hai notato che i server MCP stanno spuntando ovunque — dando agli agenti la capacità di interagire con strumenti e servizi esterni attraverso un protocollo standardizzato.

Ora l'[Azure DevOps MCP Server è disponibile in Microsoft Foundry](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), e questa è una di quelle integrazioni che ti fa pensare alle possibilità pratiche.

## Cosa sta succedendo realmente qui

Microsoft ha già rilasciato l'Azure DevOps MCP Server come [public preview](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview) — quello è il server MCP stesso. La novità è l'integrazione con Foundry. Ora puoi aggiungere l'Azure DevOps MCP Server ai tuoi agenti Foundry direttamente dal catalogo degli strumenti.

Per chi non conosce ancora Foundry: è la piattaforma unificata di Microsoft per costruire e gestire applicazioni e agenti alimentati dall'IA su larga scala. Accesso ai modelli, orchestrazione, valutazione, deployment — tutto in un unico posto.

## La configurazione

La configurazione è sorprendentemente semplice:

1. Nel tuo agente Foundry, vai su **Add Tools** > **Catalog**
2. Cerca "Azure DevOps"
3. Seleziona l'Azure DevOps MCP Server (preview) e clicca su **Create**
4. Inserisci il nome della tua organizzazione e connetti

Tutto qui. Il tuo agente ora ha accesso agli strumenti Azure DevOps.

## Controllare a cosa può accedere il tuo agente

Questa è la parte che apprezzo: non sei bloccato con un approccio tutto-o-niente. Puoi specificare quali strumenti sono disponibili per il tuo agente. Quindi se vuoi che legga solo i work item ma non tocchi le pipeline, puoi configurarlo. Principio del minimo privilegio, applicato ai tuoi agenti IA.

Questo conta per gli scenari enterprise dove non vuoi che un agente attivi accidentalmente una pipeline di deployment perché qualcuno gli ha chiesto di "aiutare con il release."

## Perché è interessante per i team .NET

Pensa a cosa abilita nella pratica:

- **Assistenti per la pianificazione degli sprint** — agenti che possono recuperare work item, analizzare dati di velocità e suggerire la capacità dello sprint
- **Bot di code review** — agenti che capiscono il contesto della tua PR perché possono effettivamente leggere i tuoi repo e work item collegati
- **Risposta agli incidenti** — agenti che possono creare work item, interrogare i deployment recenti e correlare bug con modifiche recenti
- **Onboarding degli sviluppatori** — "Su cosa dovrei lavorare?" ottiene una risposta reale basata su dati reali del progetto

Per i team .NET che già usano Azure DevOps per le loro pipeline CI/CD e la gestione dei progetti, avere un agente IA che può interagire direttamente con questi sistemi è un passo significativo verso un'automazione utile.

## Il quadro più ampio di MCP

Questo fa parte di una tendenza più ampia: i server MCP stanno diventando il modo standard in cui gli agenti IA interagiscono con il mondo esterno. Li vediamo per GitHub, Azure DevOps, database, API SaaS — e Foundry sta diventando l'hub dove tutte queste connessioni convergono.

Se stai costruendo agenti nell'ecosistema .NET, vale la pena tenere d'occhio MCP. Il protocollo è standardizzato, gli strumenti stanno maturando, e l'integrazione Foundry lo rende accessibile senza dover configurare manualmente le connessioni server.

## Per concludere

L'Azure DevOps MCP Server in Foundry è in preview, quindi aspettati che si evolva. Ma il workflow principale è solido: connettere, configurare l'accesso agli strumenti e lasciare che i tuoi agenti lavorino con i tuoi dati DevOps. Se sei già nell'ecosistema Foundry, è a pochi clic. Provalo e vedi quali workflow puoi costruire.

Consulta l'[annuncio completo](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) per la configurazione passo per passo e maggiori dettagli.
