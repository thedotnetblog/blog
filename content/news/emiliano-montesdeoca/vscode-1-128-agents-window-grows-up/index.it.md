---
title: "VS Code 1.128 Fa una Scommessa Chiara: La Finestra degli Agenti Sta Diventando la Nuova Superficie di Lavoro"
date: 2026-07-25
author: Emiliano Montesdeoca
description: "VS Code 1.128 trasforma i workflow degli agenti da novità a ergonomia quotidiana con sessioni multi-chat, supporto vision in GA e controlli più profondi di host/sessione."
tags:
  - VS Code
  - AI Agents
  - Copilot
  - Developer Experience
  - Multimodal
  - Productivity
---

Visual Studio Code 1.128 è un rilascio significativo non per una funzionalità killer, ma perché diversi cambiamenti si allineano attorno a una singola direzione: lo sviluppo agent-first all'interno dell'editor sta diventando strutturato, parallelo e operativamente gestibile.

Fonte originale: https://code.visualstudio.com/updates/v1_128

Il punto di spicco è il **comportamento multi-chat più ricco** nelle sessioni host degli agenti, incluse chat peer, fork e turni concorrenti sotto un'unica sessione genitore. Questo è esattamente ciò di cui gli sviluppatori esperti hanno bisogno quando esplorano implementazioni alternative o suddividono compiti attraverso percorsi di verifica. Rispecchia il vero lavoro ingegneristico, che raramente è lineare.

La mia opinione: questo è il primo rilascio di VS Code in cui la finestra degli Agenti sembra meno un pannello chat e più una superficie di orchestrazione del workspace.

Le chat rapide senza un workspace selezionato contano anche più di quanto sembri. Abbattono l'attrito per domande concettuali o architetturali mantenendo distinte le sessioni legate al progetto. Quella separazione può ridurre il disordine e preservare l'integrità del contesto per i workflow di modifica del codice.

**Copilot Vision che raggiunge la GA** è un altro punto di svolta. Una volta che immagini e PDF sono input normali per la chat, i task pesanti di documentazione e UI diventano significativamente più fluidi. I team dovrebbero ora pensare al contesto multimodale come capacità predefinita, non come add-on avanzato.

Ci sono anche implicazioni pratiche per la piattaforma. Il **supporto BYOK** in scenari di host agenti, parametri di campionamento del modello configurabili e impostazioni predefinite del modello utility indicano una maturità crescente per la governance enterprise dei modelli. Le organizzazioni con requisiti stringenti sui provider possono ora modellare il comportamento con controllo più fine invece di impostazioni predefinite one-size-fits-all.

### Raccomandazioni per i team che adottano 1.128

- **Definisci convenzioni per il branching e la denominazione delle chat** nelle sessioni multi-chat in modo che l'esplorazione parallela non diventi rumore conversazionale.
- **Incoraggia gli sviluppatori a tenere una chat per l'implementazione** e una per i test o l'analisi dei fallimenti.
- **Usa le chat rapide intenzionalmente** per domande non legate al repository.
- **Se gestisci endpoint BYOK**, stabilisci profili temperatura/top_p di base per classe di carico di lavoro e documenta le eccezioni.
- **Decidi se i flussi utility** dovrebbero essere eseguiti su modelli forniti da Copilot o BYOK per evitare gap di comportamento silenziosi accidentali.
- **Considera le scorciatoie a livello OS strategicamente.** Essere in grado di attivare comandi VS Code a livello di sistema può migliorare il flusso per utenti avanzati, ma una proliferazione non gestita di keybinding può danneggiare la coerenza tra i team.

## In sintesi

VS Code 1.128 non aggiunge solo funzionalità. Stringe i meccanismi della collaborazione degli agenti nei cicli di sviluppo reali. Gli editor che vinceranno nel prossimo ciclo saranno quelli che trattano le interazioni con gli agenti come **primitive di workflow di prima classe**, non esperimenti di sidebar. Questo rilascio mostra che VS Code capisce quella corsa.