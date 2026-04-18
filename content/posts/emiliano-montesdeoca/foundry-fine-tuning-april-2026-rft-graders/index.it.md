---
title: "L'RFT di Foundry è ora più economico e intelligente — Ecco cosa è cambiato"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry ha rilasciato tre aggiornamenti RFT questo mese: addestramento globale per o4-mini, nuovi valutatori di modello GPT-4.1 e una guida alle best practice che vi farà risparmiare ore di debugging."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

Se state sviluppando app .NET che si basano su modelli fine-tunati, gli aggiornamenti Foundry di questo mese meritano la vostra attenzione. Il Reinforcement Fine-Tuning è diventato più accessibile e significativamente più economico.

I dettagli completi sono nell'[annuncio ufficiale](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/), ma ecco il riassunto pratico.

## Addestramento Globale per o4-mini

o4-mini è il modello di riferimento per workload pesanti in ragionamento e agentici. La grande notizia: ora potete lanciare job di fine-tuning da più di 13 regioni Azure con tariffe di addestramento per token più basse rispetto all'addestramento Standard. Stessa infrastruttura, stessa qualità, maggiore copertura.

Se il vostro team è distribuito geograficamente, questo conta. Non siete più vincolati a un pugno di regioni per addestrare.

Ecco la chiamata API REST per avviare un job di addestramento globale:

```bash
curl -X POST "https://<your-resource>.openai.azure.com/openai/fine_tuning/jobs?api-version=2025-04-01-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{
    "model": "o4-mini",
    "training_file": "<your-training-file-id>",
    "method": {
      "type": "reinforcement",
      "reinforcement": {
        "grader": {
          "type": "string_check",
          "name": "answer-check",
          "input": "{{sample.output_text}}",
          "reference": "{{item.reference_answer}}",
          "operation": "eq"
        }
      }
    },
    "hyperparameters": {
      "n_epochs": 2,
      "compute_multiplier": 1.0
    },
    "trainingType": "globalstandard"
  }'
```

Quel flag `trainingType: globalstandard` è la differenza chiave.

## Nuovi Valutatori di Modello: Famiglia GPT-4.1

I valutatori definiscono il segnale di ricompensa contro cui il vostro modello ottimizza. Finora, i valutatori basati su modello erano limitati a un insieme più ristretto di modelli. Ora avete tre nuove opzioni: GPT-4.1, GPT-4.1-mini e GPT-4.1-nano.

Quando dovreste usare valutatori di modello invece di quelli deterministici? Quando l'output del vostro task è aperto, quando avete bisogno di punteggio parziale su più dimensioni, o quando state costruendo workflow agentici dove la correttezza delle chiamate agli strumenti dipende dal contesto semantico.

Il punto è che la strategia a livelli è pratica:

- **GPT-4.1-nano** per le iterazioni iniziali. Basso costo, cicli di feedback rapidi.
- **GPT-4.1-mini** una volta che la vostra rubrica di valutazione è stabile e avete bisogno di maggiore fedeltà.
- **GPT-4.1** per la valutazione in produzione o rubriche complesse dove ogni decisione di punteggio conta.

Potete persino mescolare tipi di valutatori in un singolo job RFT. Usate string-match per la dimensione "risposta corretta" e un valutatore di modello per valutare la qualità del ragionamento. Questa flessibilità è onestamente ciò che lo rende utile per workload reali.

## La Trappola del Formato Dati RFT

Questo fa inciampare molti. Il formato dati RFT è diverso da SFT. L'ultimo messaggio in ogni riga deve avere il ruolo User o Developer — non Assistant. La risposta attesa va in una chiave di livello superiore come `reference_answer` che il valutatore referenzia direttamente.

Se stavate facendo supervised fine-tuning e volete passare a RFT, dovete ristrutturare i vostri dati di addestramento. Non saltate questo passaggio o i vostri job falliranno silenziosamente.

## Perché Questo È Importante per gli Sviluppatori .NET

Se state chiamando modelli fine-tunati dalle vostre app .NET tramite l'SDK Azure OpenAI, un addestramento più economico significa che potete iterare in modo più aggressivo. Le opzioni dei valutatori di modello significano che potete fare fine-tuning per task sfumati — non solo scenari di corrispondenza esatta. E la guida alle best practice su [GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) vi farà risparmiare tempo reale di debugging.

Iniziate in piccolo. Da dieci a cento campioni. Valutatore semplice. Validate il ciclo. Poi scalate.
