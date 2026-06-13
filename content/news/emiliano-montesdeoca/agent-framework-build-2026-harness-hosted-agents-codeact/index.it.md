---
title: "Agent Harness, Hosted Agents e CodeAct: questo è l'aggiornamento di Agent Framework su cui mi concentrerei"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "L'annuncio di Agent Framework a Build 2026 è ricchissimo, ma i fili più importanti sono il modello di harness, gli hosted agents su Foundry e CodeAct per ridurre il sovraccarico di orchestrazione."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

Il grande annuncio di Agent Framework a Build copre molto, ma tre temi saltano subito all'occhio:

- **il fatto che l'harness stia diventando una parte di runtime più centrale**
- **gli hosted agents di Foundry che offrono una strada verso la produzione**
- **CodeAct che riduce il sovraccarico di orchestrazione multi-step**

Sono questi gli elementi su cui terrei alta l'attenzione.

## L'harness sta diventando il vero centro di gravità

Il post di origine descrive l'harness come il livello in cui il ragionamento del modello incontra l'esecuzione reale.

È la descrizione giusta, ed è anche il motivo per cui penso che questo aspetto conti più di molti singoli punti elenco di funzionalità.

Nel momento in cui un agente ha bisogno di:

- accesso ai file
- esecuzione shell
- modalità di pianificazione
- to-do
- memoria di sessione
- flussi di approvazione

non stai più parlando di un prompt più un modello.

Stai parlando di comportamento a runtime.

È lì che i framework diventano davvero utili o finiscono per essere giocattoli.

E Microsoft Agent Framework sta chiaramente cercando di diventare più utile proprio in quel livello.

## Gli hosted agents sono il punto in cui la storia dal locale alla produzione diventa reale

Penso anche che la parte degli hosted agents sia una delle più importanti strategicamente nell'annuncio.

Il post di origine dice esplicitamente che è il modo più semplice per dare a quell'agente una casa in produzione.

Questa frase conta perché la maggior parte dei framework per agent è ancora molto più forte nell'esperimento locale che nel deployment operativo.

Se gli hosted agents di Foundry rendono molto più facile passare dallo sviluppo locale a:

- scaling
- observability
- managed identity
- session handling
- versioning

allora si chiude una delle lacune più grandi dell'ecosistema attuale degli agent.

Sarebbe un miglioramento significativo.

## CodeAct è l'idea tecnica più interessante dell'aggiornamento

Se dovessi scegliere il concetto tecnico più interessante del post, sceglierei probabilmente CodeAct.

Il problema che cerca di risolvere è molto reale: troppi workflow agent multi-step diventano costosi perché il ciclo di orchestrazione consuma troppe iterazioni del modello.

Quindi, quando il post di origine mostra un risultato come questo:

- 52.4% più veloce
- 63.9% di token in meno

la mia attenzione si accende subito.

Naturalmente, sono numeri da benchmark legati a un carico di lavoro rappresentativo, non una legge universale. Ma l'idea più ampia resta comunque convincente.

Se il modello può comprimere una catena di chiamate agli strumenti in una forma di esecuzione più efficiente, l'economia dei sistemi agent può cambiare parecchio.

## Quello che penso dovrebbero davvero cogliere gli sviluppatori da questo aggiornamento

La lezione importante non è quante funzionalità siano state rilasciate.

La lezione è che il framework si sta rafforzando nei punti che le applicazioni reali richiedono di più:

- runtime shell
- percorso di deploy
- efficienza di esecuzione
- pattern operativi incorporati

Questo è il tipo di segnale di maturità che mi interessa molto più di un'altra checklist superficiale di funzionalità AI.

## La mia lettura

Questo aggiornamento conta perché non sta solo aggiungendo più superficie.

Sta rafforzando la storia di runtime e deployment attorno agli agent in modi che dovrebbero contare per le applicazioni reali, soprattutto per i team che vogliono passare dagli esperimenti locali a sistemi che possano davvero eseguire e mantenere.

È lì che il framework diventa più convincente.

E se seguissi da vicino questo rilascio, harness, hosted agents e CodeAct sarebbero senza dubbio le aree su cui concentrerei la mia attenzione principale.

Articolo originale: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
