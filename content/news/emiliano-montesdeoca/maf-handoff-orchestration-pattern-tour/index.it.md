---
title: "Il Pattern Handoff: Quando Un Agente Non Basta"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Il pattern di orchestrazione Handoff di Microsoft Agent Framework consente agli agenti di decidere chi gestisce il prossimo turno — senza perdere il contesto della conversazione o violare le regole di topologia."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

A un certo punto ogni sistema multi-agente supera un semplice router. Il primo segnale è di solito quando un agente specialista deve fare una domanda di follow-up, o si rende conto a metà turno che un altro agente dovrebbe continuare. Una pipeline fissa fallisce lì. Un router a singolo passaggio fallisce lì.

È esattamente il problema per cui il pattern di orchestrazione Handoff in Microsoft Agent Framework è progettato.

## Come Funziona Handoff

Lo sviluppatore dichiara un grafo: ecco gli agenti, ecco i bordi tra di loro. Il framework fa il resto — sintetizza uno strumento handoff per ogni bordo in uscita e lo inietta in ogni agente. Quando un agente decide di cedere il controllo, chiama lo strumento. Il framework applica la topologia.

Tre cose rendono questo diverso dal semplice fare in modo che gli agenti si chiamino tra di loro:

1. **Una trascrizione condivisa** — l'agente ricevente vede l'intera cronologia della conversazione. Senza ricominciare da zero.
2. **Applicazione della topologia** — un agente può fare handoff solo a destinazioni dichiarate. I bug di routing vengono rilevati in fase di authoring, non in produzione.
3. **Terminazione naturale** — quando l'agente attivo finisce il suo turno senza chiamare uno strumento handoff, il workflow cede all'utente. Senza polling, senza condizioni di uscita esplicite.

## Un Esempio Minimale

In .NET, costruire un workflow handoff appare così:

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triage può inviare a entrambi i specialisti. Entrambi i specialisti possono rimandare a triage. Il grafo è compatibile con l'aciclico ma supporta bordi posteriori quando ne hai bisogno ("ho bisogno di più informazioni" → torna alla ricerca).

## Quando Usare Handoff (e Quando No)

Handoff è una buona scelta quando:

- **La proprietà può cambiare a metà conversazione** — un agente può rendersi conto di essere lo specialista sbagliato
- **I bordi posteriori contano** — potresti dover rivisitare un passo precedente senza ricominciare
- **Le decisioni di routing sono sfumate** — la decisione di fare handoff è contestuale e meglio presa dal modello che da predicati tipizzati

*Non* è la scelta giusta quando:

- La tua pipeline è fissa e sequenziale — usa il workflow `Sequential` per quello
- Ogni passo è indipendente — agenti che condividono una trascrizione dove solo uno di loro ne aveva bisogno è solo rumore
- Hai bisogno di garanzie di elaborazione rigorose — il non-determinismo del routing guidato dal modello non è ciò che vuoi

## Bordi Posteriori e Human-in-the-Loop

Una delle forme più interessanti che Handoff consente sono i veri bordi posteriori. Un agente può decidere "non ho abbastanza informazioni" e tornare a un passo di ricerca, non con un loop codificato, ma perché il modello decide che è la scelta giusta.

Le interazioni human-in-the-loop si compongono naturalmente. Quando uno specialista ha bisogno dell'input dell'utente, il workflow cede all'utente tramite il loop di turno predefinito, raccoglie la risposta e riprende con il contesto completo. L'agente non ha mai perso la conversazione.

## Conclusione

Handoff è uno di quei pattern che sembra semplice ma permette molto una volta interiorizzato: routing decentralizzato, contesto condiviso, topologia applicata, terminazione naturale. È il giusto passo successivo quando i tuoi agenti cominciano a dire "in realtà, qualcun altro dovrebbe gestire questo."

Leggi il percorso completo nel post originale: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
