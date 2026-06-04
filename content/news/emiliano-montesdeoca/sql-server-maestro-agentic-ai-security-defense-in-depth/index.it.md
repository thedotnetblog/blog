---
title: "MAESTRO, Difesa in Profondità e Perché SQL Server È Ora un Confine di Sicurezza per l'IA"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "L'IA agentiva introduce minacce per cui i modelli STRIDE tradizionali non erano progettati. Ecco come Microsoft SQL si mappa al framework MAESTRO per fornire un confine di esecuzione governato."
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

I modelli di minacce alla sicurezza sono costruiti su ipotesi su chi o cosa sta facendo le richieste. STRIDE assume attori umani che interagiscono con i sistemi attraverso interfacce definite. Gli agenti di IA non funzionano in questo modo.

## STRIDE Non È Stato Progettato per gli Agenti di IA

I sistemi agentici operano autonomamente, concatenano strumenti tramite chiamate API, prendono decisioni su quali dati recuperare e quali azioni eseguire, e possono ricevere istruzioni da più fonti — prompt dell'utente, risultati degli strumenti, dati recuperati. Il modello di minacce STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) non cattura adeguatamente i vettori di attacco specifici degli agenti come l'iniezione di prompt, l'avvelenamento del contesto o l'abuso degli strumenti.

La Cloud Security Alliance ha pubblicato il framework MAESTRO specificamente per il rischio degli agenti di IA.

## Il Framework MAESTRO

MAESTRO organizza il rischio dell'IA agentiva in sette livelli:

1. **Foundation Models** — gli LLM sottostanti e le loro vulnerabilità di addestramento
2. **Data Operations** — recupero, archiviazione e manipolazione dei dati
3. **Agent Frameworks** — il middleware di orchestrazione e coordinazione degli agenti
4. **Deployment & Infrastructure** — dove gli agenti vengono eseguiti e come sono configurati
5. **Evaluation & Observability** — monitoraggio del comportamento degli agenti nel tempo
6. **Security & Compliance** — controlli di accesso, audit e conformità normativa
7. **Agent Ecosystem** — come gli agenti interagiscono tra loro e con strumenti esterni

Ogni livello ha vettori di attacco specifici che i controlli di sicurezza tradizionali non affrontano direttamente.

## Microsoft SQL Come Confine di Esecuzione Governato

SQL Server 2025 si mappa sui livelli MAESTRO in modi concreti:

**Livello Data Operations**: `AI_GENERATE_EMBEDDINGS` integrato in T-SQL mantiene le operazioni vettoriali all'interno del confine governato del database. I dati non devono uscire verso il servizio del modello per l'elaborazione degli embedding.

**Livelli Security & Compliance**: La sicurezza a livello di riga (RLS) e il mascheramento dinamico dei dati (DDM) si applicano indipendentemente da come è arrivata la richiesta — che provenga da un utente umano o da un agente di IA. L'agente non può aggirare i controlli che sono imposti dal database stesso.

**Livello Agent Frameworks**: Le stored procedure fungono da confini degli strumenti. Invece di dare agli agenti accesso SQL arbitrario, definisci le operazioni consentite come procedure e le esponi come strumenti agente. Le query parametrizzate prevengono l'iniezione a livello di esecuzione.

**Livello Evaluation & Observability**: Il logging di audit e Query Store catturano ciò che ogni agente ha effettivamente eseguito — non solo ciò che gli è stato chiesto di fare. Questa tracciabilità è critica per le indagini sugli incidenti nei sistemi agentici dove l'attribuzione è complessa.

## Difesa in Profondità per l'IA Agentiva

Il principio rimane lo stesso della sicurezza tradizionale: nessun singolo controllo è sufficiente. Ciò che cambia è quali controlli contano di più per gli agenti:

**Ridurre il raggio d'impatto**: i confini degli strumenti delle stored procedure significano che un agente compromesso può eseguire solo operazioni predefinite. Non può passare a query arbitrarie.

**Osservabilità**: devi essere in grado di rispondere "cosa ha fatto esattamente questo agente?" dopo un incidente. I sistemi di IA agentiva senza tracciabilità a livello di database hanno punti ciechi che il logging applicativo non copre.

**Esecuzione vincolata**: parametrizzazione, RLS e DDM sono asset di sicurezza indipendentemente dal fatto che il chiamante sia umano. Non indebolirli per accomodare gli agenti.

**Responsabilità**: il logging di audit di SQL Server crea un registro di chi (quale agente, con quali credenziali) ha eseguito cosa in quale momento. Questo conta quando i sistemi agentici compiono azioni con conseguenze reali nel mondo.

SQL Server 2025 non è stato costruito per risolvere il rischio agentivo in astratto — è stato costruito per essere un database relazionale. Ma la governance che rende affidabile un database enterprise si rivela essere esattamente ciò che rende sicuro un confine di esecuzione degli agenti.

Post originale: [Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
