---
title: ".NET 8 e .NET 9 Fine del Supporto: Trattatelo come una Scadenza di Consegna"
date: 2026-07-19
author: "Emiliano Montesdeoca"
description: "Il 10 novembre 2026 non è solo una data di supporto; è il punto in cui il rischio di aggiornamento rimandato diventa esplicito."
tags:
  - dotnet
  - net10
  - security
  - platform-lifecycle
  - engineering-leadership
---

Fonte originale: [.NET 8 and .NET 9 will reach End of Support on November 10, 2026](https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support/)

Questo annuncio è diretto, e i team dovrebbero rispondere con uguale chiarezza: se prevedi di continuare a spedire su .NET 8 o .NET 9 oltre il 10 novembre 2026, stai prendendo una decisione intenzionale di runtime non supportato.

Le applicazioni continueranno a funzionare. Non è questo il punto. Il punto è che gli aggiornamenti di sicurezza e manutenzione si fermano. Una volta che ciò accade, ogni vulnerabilità nota senza un percorso di backport diventa la tua responsabilità operativa.

La mia opinione: **le organizzazioni spesso trattano gli aggiornamenti del framework come manutenzione opzionale** e poi pagano per quella decisione in finestre di emergenza, risultati di audit e escalation forzate ai vendor. La pianificazione dell'aggiornamento dovrebbe essere una voce della roadmap di prodotto, non una side quest.

Una posizione pratica di migrazione per i team .NET:

- **Imposta il re-targeting a .NET 10 come obiettivo datato**, non come elemento di backlog aperto.
- **Esegui test di compatibilità e regressione** in parallelo con il lavoro sulle funzionalità ora, non in Q4.
- **Traccia la prontezza delle dipendenze e dell'hosting** come flussi di lavoro separati, perché molti fallimenti accadono al di fuori del file di progetto.
- **Usa Upgrade Assistant e la documentazione delle breaking changes** presto per anticipare le sorprese.

Se possiedi librerie condivise usate da più prodotti, pubblica la tua timeline di supporto .NET 10 pubblicamente all'interno della tua organizzazione. I team downstream hanno bisogno di lead time.

La marcatura dei componenti fuori supporto di Visual Studio è anche operativamente importante. Crea un segnale chiaro che la pulizia della toolchain fa parte del rimanere conformi. I team che ignorano questo di solito finiscono in stati SDK misti e comportamento di build inconsistente.

Un dettaglio poco discusso è che .NET 8 e .NET 9 convergono sulla stessa data di fine. Questo comprime le finestre di aggiornamento per le organizzazioni che hanno scaglionato l'adozione aspettandosi più margine. Se sei passato a .NET 9 per l'accesso alle funzionalità, ti trovi comunque sulla stessa scogliera di supporto.

Per i platform lead, la matrice decisionale è semplice: **migra prima della scadenza, o documenta e accetta il rischio non supportato** con controlli compensativi. Non esiste una terza opzione in cui nulla cambia.

La buona notizia è che .NET 10 è un target LTS fino a novembre 2028, il che offre una pista stabile una volta completato il passaggio.

Non aspettare l'ultimo Patch Tuesday per iniziare. Trattalo come una scadenza di consegna con implicazioni di sicurezza, perché è esattamente ciò che è.