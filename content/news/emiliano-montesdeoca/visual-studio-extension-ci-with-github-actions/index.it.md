---
title: "I Team di Estensioni Visual Studio Dovrebbero Smettere di Rilasciare per Abitudine e Iniziare a Rilasciare per Pipeline"
date: 2026-07-23
author: "Emiliano Montesdeoca"
description: "Un flusso GitHub Actions ripetibile per il versioning e la pubblicazione VSIX è ora abbastanza semplice che i passaggi di rilascio manuali sono difficili da giustificare."
tags:
  - visual-studio
  - vsix
  - github-actions
  - ci-cd
  - developer-tooling
---

Fonte originale: [Automating your Visual Studio extension builds with GitHub Actions](https://devblogs.microsoft.com/visualstudio/automating-your-visual-studio-extension-builds-with-github-actions/)

Se mantieni estensioni Visual Studio e ancora esegui parti significative del rilascio manualmente, questo è il tuo segnale per modernizzare.

Il workflow mostrato in questo post è intenzionalmente pratico: timbra versione, build, pubblica artefatti di test su una galleria, poi pubblica i binari stabili su Marketplace. Nessuna cerimonia di piattaforma pesante, solo comportamento di rilascio deterministico.

Ciò che mi piace di più è che il versioning viene trattato come stato della pipeline, non come elemento di checklist pre-rilascio. Quella singola decisione elimina un numero sorprendente di errori: metadati non corrispondenti, versioni di assembly obsolete e note di rilascio inconsistenti.

La separazione tra pubblicazione su galleria e pubblicazione su Marketplace è anche operativamente matura. I team hanno bisogno di un posto per build di validazione rapide che non portino la semantica del rilascio ufficiale. Spingere tutto direttamente su Marketplace è ad alto attrito e incoraggia scorciatoie rischiose.

### Un pattern di rilascio solido per i team di estensioni

- **Su pull request e commit su main**, produci artefatti VSIX CI e pubblicali sulla galleria per i tester.
- **Su rilasci taggati**, pubblica pacchetti firmati e validati su Marketplace.
- **Mantieni la gestione dei token minima** con segreti dedicati e ambiti di privilegio minimo.

La mia opinione: **gli ecosistemi di estensioni sono in ritardo rispetto agli ecosistemi di app nella disciplina CI** perché i team piccoli presumono che i workflow manuali siano gestibili. Sono gestibili finché non lo sono più. Una patch affrettata, un pacchetto rotto, un aggiornamento del manifest dimenticato, e la fiducia cala.

Queste azioni riutilizzabili sono utili perché codificano la logica di rilascio ripetuta una volta e permettono ai team di concentrarsi sulla qualità dell'estensione invece che sulla meccanica del packaging.

C'è ancora bisogno di giudizio ingegneristico. Dovresti proteggere la pubblicazione su Marketplace con controlli di qualità e trattare i manifest di pubblicazione come artefatti di rilascio verificati. Ma la complessità della pipeline di base è ora abbastanza bassa che i rilasci solo manuali sono per lo più debito tecnico.

Se guidi lo sviluppo di estensioni, **standardizza questo ora tra i repository**. Otterrai migliore tracciabilità, onboarding più facile e meno colli di bottiglia di rilascio con una singola persona.

### Rollout suggerito

- **Inizia con build più pubblicazione su galleria** per un'estensione.
- **Introduci il version stamping** dopo aver validato le convenzioni manifest-source.
- **Aggiungi la pubblicazione su Marketplace** solo dopo che la gestione dei segreti e i gate di rilascio sono in atto.

Non si tratta di inseguire la moda DevOps. Si tratta di affidabilità per le persone che installano il tuo tooling e si aspettano che gli aggiornamenti funzionino.

Gli ecosistemi di estensioni stabili sono costruiti allo stesso modo delle applicazioni stabili: con automazione noiosa e ripetibile che rimuove le congetture umane.