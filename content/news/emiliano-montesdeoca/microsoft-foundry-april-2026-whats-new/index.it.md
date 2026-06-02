---
title: "Microsoft Foundry Aprile 2026: Foundry Local GA, GPT-5.5, CodeAct con Hyperlight"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "Il riepilogo di Foundry di aprile è ricco: Foundry Local raggiunge la GA, arriva GPT-5.5, Agent Framework ottiene il tracing OpenTelemetry, CodeAct esegue Python in micro-VM Hyperlight, e arriva il Dashboard di Monitoraggio degli Agenti."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Un mese impegnativo per Microsoft Foundry. Ecco gli annunci più importanti.

## Foundry Local è Generalmente Disponibile

Foundry Local — il runtime AI locale multipiattaforma di Microsoft — passa dalla preview alla GA su Windows, macOS (Apple Silicon) e Linux x64. Inferenza di modelli locali pronta per la produzione con un SDK orientato agli sviluppatori. La versione 1.1 aggiunge il supporto per trascrizione, embeddings e API Responses.

## GPT-5.5

L'ultimo modello della famiglia GPT-5 è ora disponibile in Foundry. Quota predefinita per gli abbonamenti Tier 5 e Tier 6. Se hai lavorato con varianti precedenti di GPT-5, vale la pena valutarlo per i tuoi casi d'uso.

## Tracing di Agent Framework in Foundry

Due funzionalità di tracing vengono rilasciate in anteprima questo mese:

**Tracing di Microsoft Agent Framework** — Gli agenti MAF possono ora emettere trace OpenTelemetry in Foundry. Esegui il debug del comportamento degli agenti, traccia l'esecuzione in più passaggi, individua latenza ed errori nelle chiamate agli strumenti. Questo colma una lacuna reale: sapere *cosa ha effettivamente fatto il tuo agente* in produzione, non solo cosa ha restituito.

**Tracing degli agenti ospitati** — Sessioni, chiamate agli strumenti e passaggi di esecuzione degli agenti ospitati appaiono anche nelle trace di Foundry. La stessa storia di osservabilità estesa al livello ospitato.

## CodeAct con Hyperlight (Alpha)

Questa è l'aggiunta tecnicamente più interessante: Agent Framework può ora eseguire codice Python all'interno di micro-macchine virtuali [Hyperlight](https://github.com/hyperlight-dev/hyperlight).

CodeAct è il pattern in cui un agente genera ed esegue codice Python come strumento. La preoccupazione ovvia è la sicurezza — stai eseguendo codice generato dal modello. Le micro-VM di Hyperlight forniscono isolamento a livello di processo con tempi di avvio vicini al nativo, rendendo pratica l'esecuzione di codice in sandbox senza il sovraccarico di container o VM completi.

Per i flussi di lavoro agentici dove l'esecuzione di codice è necessaria, questo è un miglioramento significativo della sicurezza rispetto all'esecuzione di codice nel processo host.

## Dashboard di Monitoraggio degli Agenti (Anteprima)

Un dashboard operativo unificato che combina l'utilizzo dei token, la latenza, il tasso di successo delle esecuzioni e i punteggi degli evaluator in un'unica vista. La distinzione dai normali dashboard di osservabilità: include i risultati di valutazione insieme alle metriche operative, così puoi correlare "l'agente è più lento" con "i punteggi dell'evaluator sono scesi" — o confermare che non sono correlati.

## Evaluator Personalizzati per la Valutazione Continua (Anteprima)

Ora puoi portare i tuoi evaluator basati su codice o prompt nelle pipeline di valutazione continua. In precedenza, la valutazione continua era limitata agli evaluator integrati. Gli evaluator personalizzati ti permettono di applicare criteri di qualità specifici del team nel tuo ciclo di monitoraggio in produzione.

## Inventario degli Agenti nel Piano di Controllo

La vista Operate del Piano di Controllo di Foundry mostra ora tutti gli agenti supportati in un abbonamento: agenti Foundry, Azure SRE Agent, cicli di agenti Logic Apps e agenti personalizzati registrati. Una vista per capire cosa è distribuito e dove.

Post originale: [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
