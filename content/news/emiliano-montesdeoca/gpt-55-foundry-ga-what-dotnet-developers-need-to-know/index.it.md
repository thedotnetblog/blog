---
title: "GPT-5.5 È Arrivato su Azure Foundry — Cosa Devono Sapere i Sviluppatori .NET"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 è generalmente disponibile in Microsoft Foundry. La progressione da GPT-5 a 5.5, cosa è realmente migliorato e come iniziare a usarlo nei tuoi agenti oggi."
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

Microsoft ha appena annunciato che [GPT-5.5 è generalmente disponibile in Microsoft Foundry](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/). Se stai costruendo agenti su Azure, questo è l'aggiornamento che stavi aspettando.

## La progressione di GPT-5

- **GPT-5**: ha unificato ragionamento e velocità in un unico sistema
- **GPT-5.4**: ragionamento multi-step più solido, capacità agentiche per l'enterprise
- **GPT-5.5**: ragionamento in contesto lungo più profondo, esecuzione agentica più affidabile, migliore efficienza dei token

## Cosa è cambiato davvero

**Coding agentico migliorato**: GPT-5.5 mantiene il contesto su grandi codebase, diagnostica guasti architetturali e anticipa i requisiti di test. Il modello ragiona su *cos'altro* influenza una correzione prima di agire.

**Efficienza dei token**: Output di qualità superiore con meno token e meno tentativi. Costo e latenza direttamente inferiori in produzione.

**Analisi in contesto lungo**: Gestisce documenti estesi e cronologie multi-sessione senza perdere il filo.

## Prezzi

| Modello | Input ($/M token) | Input in cache | Output ($/M token) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5,00 | $0,50 | $30,00 |
| GPT-5.5 Pro | $30,00 | $3,00 | $180,00 |

## Perché Foundry è importante

Foundry Agent Service permette di definire agenti in YAML o collegarli con Microsoft Agent Framework, GitHub Copilot SDK, LangGraph o OpenAI Agents SDK — ed eseguirli come agenti ospitati isolati con filesystem persistente, identità Microsoft Entra e prezzi scale-to-zero.

```csharp
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "Sei un assistente utile.", name: "MioAgente");
```

Consulta l'[annuncio completo](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/) per tutti i dettagli.
