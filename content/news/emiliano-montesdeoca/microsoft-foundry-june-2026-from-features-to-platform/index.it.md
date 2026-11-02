---
title: "Microsoft Foundry Giugno 2026: Da Feature Drop a Piattaforma di Agenti Governata"
date: 2026-07-18
author: Emiliano Montesdeoca
description: "Gli aggiornamenti di Foundry di giugno segnalano una transizione di piattaforma: distribuzione, tooling, memoria, osservabilità e ottimizzazione convergono in uno stack operativo per agenti enterprise."
tags:
  - Microsoft Foundry
  - Agents
  - Toolboxes
  - Observability
  - AI Platform
  - Enterprise AI
---

L'ondata Foundry di giugno 2026 non è solo un altro digest mensile. Segna una transizione di maturità da "costruisci agenti interessanti" a "opera agenti come sistemi enterprise governati." Questa distinzione conta più di qualsiasi singola funzionalità.

Fonte originale: https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/

Tre aggiornamenti definiscono il cambiamento. Primo, la pubblicazione di agenti per Microsoft 365 Copilot e Teams è diventata GA, spostando la distribuzione da progetti di integrazione personalizzati a una corsia di deployment opinionata. Secondo, Toolboxes ha ottenuto controlli di scoperta ed esecuzione più forti, inclusa la ricerca di strumenti e le routine. Terzo, l'osservabilità più l'ottimizzazione sono diventate un ciclo chiuso deliberato, non un ripensamento.

Il mio parere: questo è il pattern più importante del rilascio. **Tracing, valutazione, ottimizzazione e rollout controllato** formano il modello operativo minimo vitale per sistemi non deterministici. Se hai solo uno di questi pezzi, hai telemetria o tuning, non governance.

Claude GA in Foundry è anche strategico, ma non principalmente per la qualità del modello. Il valore più grande è l'integrazione enterprise: auth Entra, RBAC, continuità di fatturazione e allineamento delle policy. I team che passano da endpoint modello diretti a Foundry dovrebbero inquadrarlo come consolidamento operativo, non solo cambio fornitore.

Gli agenti Autopilot sono promettenti, ma le organizzazioni dovrebbero affrontarli con scelte architetturali sobrie. La collaborazione in spazio condiviso in Teams può sbloccare produttività, ma solleva rapidamente complessità di identità, autorizzazioni e responsabilità. Inizia con ambiti limitati e checkpoint di approvazione rigorosi prima del deployment esteso.

Raccomandazioni pratiche:

- **Se sei già in fase pilota**, dai priorità alla strumentazione prima dell'espansione delle capacità. Collega il tracing GenAI prima. Poi stabilisci suite di valutazione legate ai risultati di business, non a metriche generiche del modello. Solo dopo dovresti eseguire cicli di ottimizzazione e workflow di promozione.
- **Per agenti con molti toolbox**, abilita la ricerca degli strumenti presto per ridurre il rumore di contesto e il rischio di selezione dello strumento sbagliato man mano che i cataloghi crescono.
- **Per agenti con memoria**, definisci TTL e policy di conservazione in anticipo. La memoria senza controlli del ciclo di vita diventa debito di conformità.

La conclusione più opinabile che posso trarre è questa: Foundry ora è meno su "quale modello scelgo?" e più su **"posso gestire il comportamento degli agenti come un ciclo di vita gestito?"** I team che rispondono bene alla seconda domanda si adatteranno facilmente al ricambio dei modelli. I team fissati sulle classifiche dei modelli continueranno a ricostruire stack fragili ogni trimestre.

Il rilascio di giugno chiarisce una cosa. Foundry sta diventando **una piattaforma operativa per sistemi AI**, non solo un toolkit di sviluppo. Questo è un prodotto più difficile da costruire, e uno molto più prezioso da adottare.