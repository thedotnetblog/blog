---
title: "La Vera Frontiera per l'SQL Agentico: Verificabilità con OBO in SQL MCP Server"
date: 2026-07-22
author: Emiliano Montesdeoca
description: "L'autenticazione On-Behalf-Of in Data API builder più SQL MCP Server è una tappa di governance importante perché Azure SQL può finalmente verificare l'umano dietro un'azione di un agente."
tags:
  - Azure SQL
  - SQL MCP Server
  - Agentic AI
  - Security
  - Microsoft Entra ID
  - Data API Builder
---

C'è una verità dolorosa nei progetti AI enterprise: molti team sono ossessionati dalla qualità del modello e ignorano la responsabilità. Quando un agente scrive o legge dati di produzione, la prima domanda nella revisione dell'incidente non è "la risposta era buona?" È "chi ha effettivamente fatto questo?"

Fonte originale: https://devblogs.microsoft.com/azure-sql/sql-mcp-server-obo-auth/

Ecco perché il supporto OBO in Data API builder 2.0 con SQL MCP Server è più importante di quanto sembri. Gli approcci con username/password e identità gestita funzionano ancora operativamente, ma entrambi collassano l'identità nel confine del servizio. I log mostrano l'app o il middleware, non l'origine della richiesta umana. Questo è accettabile per automazione semplice. Non è accettabile per workflow agentici regolamentati.

Con OBO, SQL autentica il **contesto utente delegato**, non l'identità dell'host dello strumento. Questo ti dà un modello di audit fondamentalmente migliore: principale utente, azione, contesto dell'istruzione e identificatore dell'app di livello intermedio insieme. Ottieni tracciabilità senza perdere la superficie di controllo degli strumenti MCP e delle autorizzazioni delle entità DAB.

La mia opinione è ferma qui: se il tuo agente può toccare dati SQL sensibili, OBO dovrebbe essere la tua architettura predefinita, non un compito di hardening opzionale. La configurazione è più complessa, ma il debito di identità viene sempre pagato dopo, di solito durante incidenti di sicurezza, audit di conformità o escalation esecutive.

### Guida pratica all'implementazione

- **Inizia validando il flusso di identità** con una vista "WhoAmI" minima e controlli automatizzati nei test di integrazione. Se il principale SQL non corrisponde all'utente autenticato, fermati e correggi prima di spedire.
- **Collega query Log Analytics** per SQLSecurityAuditEvents nei tuoi dashboard SOC e attiva alert per azioni ad alto rischio avviate attraverso percorsi OBO.
- **Allinea RBAC e autorizzazioni DAB** in modo che l'identità a livello utente e l'autorizzazione a livello di azione rimangano coerenti end-to-end.

Un punto di design sottile ma importante nell'annuncio è il comportamento della cache. DAB blocca esplicitamente la memorizzazione nella cache delle risposte quando l'auth delegato dall'utente è abilitato. Quel compromesso è corretto. Trucchi di performance che possono far trapelare risultati con ambito utente non ne valgono la pena in ambienti multi-tenant o regolamentati.

**SQL MCP Server più OBO** è l'inizio di un pattern maturo: agenti come operatori controllati, utenti come principali responsabili, piani dati come sistemi verificabili. Se la tua architettura non può rispondere "chi ha fatto questo" con fiducia, non è AI pronta per la produzione, non importa quanto sia raffinata la demo.