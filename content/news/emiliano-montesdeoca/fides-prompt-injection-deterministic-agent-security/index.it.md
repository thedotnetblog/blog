---
title: "FIDES è il tipo di storia sulla sicurezza deterministica degli agenti che vorrei vedere più spesso"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Le nuove capacità di FIDES in Agent Framework contano perché spostano la difesa contro il prompt injection dalle euristiche verso una policy applicabile basata su contenuti etichettati e controlli middleware."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *Questo articolo è stato tradotto automaticamente. Per la versione originale, [fai clic qui]({{< ref "index.md" >}}).*

Le difese contro il prompt injection spesso sembrano poggiare su un terreno instabile.

Aggiungi un system prompt più forte. Aggiungi un filtro. Aggiungi qualche allowlist. E speri che il prossimo input strano non rompa le assunzioni.

Ecco perché **FIDES** è interessante.

La parte forte della storia è che sposta la sicurezza verso qualcosa di più deterministico:

- etichette sul contenuto
- propagazione delle etichette attraverso il workflow
- applicazione tramite middleware prima che vengano eseguiti strumenti privilegiati
- confini di policy chiari su ciò che il contesto non affidabile può influenzare

## L'articolo sorgente è diretto nel modo giusto

Si apre dicendo che il prompt injection è "**il rischio numero 1 nell'OWASP LLM Top 10**".

Bene.

Mi piace questo tipo di franchezza qui, perché troppi team trattano ancora la sicurezza degli agenti come se fosse una preoccupazione futura invece che un problema di design runtime attuale.

E l'articolo prosegue con un forte contrasto pratico: la maggior parte delle difese attuali è euristica, mentre FIDES cerca di spostare il sistema verso policy ed enforcement.

Questo è esattamente il cambiamento giusto.

## Cosa lo rende più convincente di un altro whitepaper di sicurezza

Molti testi sulla sicurezza dell'AI restano astratti.

Questo articolo fa di meglio. Passa attraverso un esempio molto concreto: un agente di triage di issue GitHub, un body di issue malevolo, una lettura di file privilegiata e un tentativo di fuga tramite commento pubblico.

È utile perché radica tutta la discussione in un workflow reale.

E una volta visto quello scenario, il valore dei controlli deterministici diventa molto più facile da capire.

## L'idea chiave non è "rendi il modello più intelligente"

La cosa più importante qui è che FIDES non chiede al modello di diventare magicamente migliore nel rilevare gli attacchi.

Sta cambiando il contratto del runtime.

Questo significa:

- il contenuto viene etichettato
- le etichette si propagano
- gli strumenti dichiarano cosa accettano
- il middleware blocca i percorsi non sicuri prima dell'esecuzione

È un approccio molto più sano.

Perché, una volta che l'agente può chiamare strumenti con conseguenze reali, la sicurezza non può dipendere solo dal fatto che il modello abbia una buona giornata o meno.

## La mia opinione

È esattamente il tipo di direzione nella sicurezza degli agenti che vorrei vedere più spesso.

Non "fidati del modello perché ignori le istruzioni sbagliate", ma "costruisci la barriera di policy dentro il runtime".

È un modello molto più sano.

E se i framework per agenti vogliono essere presi sul serio in produzione, avranno bisogno di più storie come questa.

Articolo originale: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)