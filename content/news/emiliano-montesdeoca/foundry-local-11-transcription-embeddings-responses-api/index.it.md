---
title: "Foundry Local 1.1: Trascrizione in Tempo Reale, Embeddings e l'API di Risposta"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1 aggiunge la trascrizione live dal microfono, gli embeddings di testo e il supporto per l'API di Risposta — tutto in esecuzione locale senza dipendenza dal cloud, senza latenza di rete, senza costi per token."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 ha dimostrato il concetto: eseguire modelli di IA localmente su Windows, macOS (Apple Silicon) e Linux x64 con un SDK adatto agli sviluppatori. La versione 1.1 aggiunge tre funzionalità che coprono molti casi d'uso reali in produzione.

## Trascrizione Audio in Diretta

La nuova funzionalità più significativa: streaming di riconoscimento vocale in tempo reale direttamente dal microfono. Sottotitoli, interfacce vocali, trascrizione di riunioni, strumenti di accessibilità — tutto eseguito localmente senza alcuna dipendenza dal cloud.

L'API è basata su sessioni e trasmette i risultati man mano che arrivano, con marcatori `is_final` per distinguere il testo intermedio da quello finalizzato. Disponibile per tutti i binding linguistici: JavaScript, C#, Python e Rust.

Carica un modello vocale in streaming dal catalogo, crea una sessione con le impostazioni audio (frequenza di campionamento, canali, lingua), avviala, invia blocchi audio PCM grezzi e consuma lo stream asincrono di risultati. Il post contiene esempi completi in Python e C#.

## Embeddings di Testo

Ricerca semantica, pipeline RAG, clustering, corrispondenza di similarità — tutto questo richiede embeddings. Foundry Local 1.1 aggiunge il supporto per i modelli di embedding così da poter generare vettori localmente dallo stesso SDK, senza inviare dati a un endpoint cloud.

Per le applicazioni in cui la residenza dei dati è importante o dove si elabora contenuto sensibile, la generazione locale di embeddings è una capacità significativa.

## API di Risposta

Foundry Local supporta ora la [API di Risposta](https://platform.openai.com/docs/api-reference/responses) — l'interfaccia strutturata progettata per le interazioni agentiche. Questo aggiunge:

- **Chiamata agli strumenti** — consente ai modelli in esecuzione locale di invocare strumenti che definisci tu
- **Input multimodale visione-linguaggio** — passa immagine + testo a modelli capaci di visione
- Compatibile con la forma API standard, quindi gli agenti esistenti che puntano all'API di Risposta di OpenAI funzionano contro modelli locali

## Miglioramenti alle Dimensioni del Pacchetto

Due modifiche riducono la dimensione del pacchetto JavaScript:
- Il layer FFI `koffi` è stato sostituito con un addon C Node-API personalizzato
- Il provider di esecuzione WebGPU viene distribuito come plugin separato, così le applicazioni che non necessitano di accelerazione GPU non ne pagano il costo in termini di dimensioni

L'SDK C# ora punta a versioni di framework inferiori per una compatibilità .NET più ampia.

## Perché È Importante

Le tre funzionalità insieme — trascrizione, embeddings, chiamata agli strumenti — coprono i blocchi di costruzione fondamentali di molte applicazioni di IA. Eseguirli localmente significa:
- Nessun internet richiesto
- Nessun costo per token
- Nessun dato lascia la macchina
- Latenza costante indipendentemente dalle condizioni di rete

Foundry Local è la scelta giusta per scenari edge, carichi di lavoro sensibili alla privacy, applicazioni offline, o qualsiasi cosa in cui si voglia evitare la dipendenza dal cloud durante lo sviluppo.

Post originale: [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
