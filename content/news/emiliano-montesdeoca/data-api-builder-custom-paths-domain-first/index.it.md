---
title: "I Percorsi Personalizzati di Data API Builder Ti Permettono di Progettare API per Umani, Non per Tabelle"
date: 2026-07-17
author: "Emiliano Montesdeoca"
description: "I percorsi REST composti in DAB sono una piccola funzionalità con un grande impatto architetturale per il design API orientato al dominio."
tags:
  - data-api-builder
  - azure-sql
  - rest-api
  - api-design
  - dotnet
---

Fonte originale: [Compose your API surface with Data API builder custom paths](https://devblogs.microsoft.com/azure-sql/data-api-builder-custom-rest-paths/)

Il nuovo supporto per **percorsi REST composti** in Data API Builder potrebbe sembrare un miglioramento di configurazione minore, ma in realtà risolve una tensione di design API di vecchia data: la topologia del database che si riversa nel design degli endpoint pubblici.

Le route basate su entità predefinite sono ottime per iniziare velocemente. Sono spesso sbagliate per API di prodotto a lungo termine. I sistemi reali hanno bisogno di strutture di route che corrispondano ai concetti di business, ai confini di proprietà e ai modelli mentali dei consumatori.

Ecco perché questo cambiamento di DAB è importante. Puoi mantenere la comodità dell'API generata mentre presenti una superficie domain-first più pulita.

La mia opinione è semplice: **se la struttura del tuo percorso API rispecchia i nomi grezzi delle tabelle in produzione**, di solito stai ottimizzando per la comodità del backend a scapito della chiarezza del client.

Con i percorsi personalizzati, i team possono modellare confini migliori, come superfici specifiche per vendite, fatturazione, supporto o partner. Questo non sostituisce una corretta governance API, ma dà agli utenti di DAB un modo pratico per allineare il design delle route con il linguaggio di prodotto.

### Guida pratica per i team che adottano questa funzionalità

- **Definisci una politica di denominazione** prima di aggiungere percorsi ad hoc. Sottosegmenti inconsistenti diventano zavorra a lungo termine.
- **Mappa gli endpoint a contesti delimitati**, non a organigrammi. I team cambiano; la semantica del dominio dovrebbe essere stabile.
- **Tratta la struttura del percorso come parte della tua strategia di versioning** e documenta esplicitamente le breaking changes.
- **Valida il comportamento dell'autorizzazione** lungo le strutture di percorso personalizzate in modo che la chiarezza delle route sia abbinata alla chiarezza della sicurezza.

Ciò che apprezzo in DAB in generale è il **modello di leva**: ottieni paginazione, filtraggio, proiezione e altri meccanismi di endpoint senza scrivere codice controller ripetitivo. I percorsi personalizzati rendono quella leva più pronta per la produzione riducendo una delle maggiori obiezioni degli architetti API.

C'è un **avvertimento**. Una migliore composizione dei percorsi può tentare i team a esporre troppo troppo velocemente perché la generazione sembra facile. I guardrail contano ancora: mantieni l'esposizione delle entità deliberata, applica le policy centralmente ed evita di costruire contratti pubblici accidentali da esperimenti di schema interni.

Per le organizzazioni .NET sotto pressione di delivery, questa funzionalità è uno sblocco di produttività se usata con disciplina. Puoi muoverti più velocemente dei livelli API artigianali preservando comunque una superficie di endpoint coerente e business-friendly.

**In sintesi:** i percorsi personalizzati di DAB non riguardano l'abbellimento delle URL. Riguardano **recuperare l'intenzione del design API** mantenendo l'efficienza operativa degli endpoint generati.