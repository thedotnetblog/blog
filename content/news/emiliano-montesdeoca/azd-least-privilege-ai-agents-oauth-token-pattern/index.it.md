---
title: "Il Tuo Agente IA Ha un Problema di Identità (Ed Ecco il Template che lo Risolve)"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Un nuovo template azd di Curity e Microsoft mostra come costruire agenti IA che usano token OAuth di breve durata con scope a grana fine — in modo che gli agenti non possano mai vedere dati che non dovrebbero vedere."
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

C'è un momento in ogni progetto di agente IA che va più o meno così: la demo funziona perfettamente, l'agente interpreta il linguaggio naturale, chiama le API giuste, restituisce i dati giusti. Poi inizi a pensare agli utenti reali.

Cosa impedisce alla sessione dell'agente di un utente di vedere i dati di un altro utente? E se l'agente viene ingannato tramite prompt injection? E se chiama uno strumento in modo inaspettato?

Questi non sono casi limite. Sono decisioni di design che devi prendere prima di rilasciare.

Un nuovo template `azd` di Curity e Microsoft ti fornisce un riferimento funzionante per esattamente questo problema.

## Il Problema Principale: Autenticazione ≠ Autorizzazione

La maggior parte dei campioni di agenti gestisce bene l'autenticazione degli utenti. Gestisce male l'autorizzazione. Sapere *chi* è l'utente non ti dice *quali dati* dovrebbe vedere.

Un'applicazione client tradizionale fa chiamate API prevedibili. Un agente IA è non deterministico — interpreta il linguaggio naturale e decide cosa chiamare. Può essere creativo. Può anche sbagliare. E se viene manipolato tramite prompt injection, hai bisogno di regole che non dipendano dal buon comportamento dell'IA.

La soluzione dimostrata da questo template: **token di breve durata che trasportano esattamente le informazioni giuste per ogni salto**.

## Come Funziona la Catena di Token

Il template usa token di accesso OAuth 2.0 con scambio di token per restringere i permessi a ogni passo. Un token utente viene scambiato due volte prima di raggiungere il server MCP:

1. **Primo scambio** — restringe lo scope e converte il token opaco in un JWT
2. **Secondo scambio** — aggiunge l'identità dell'agente e un nuovo audience per il salto del server MCP

Come appare il token del server MCP:

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

Il `customer_id` è incorporato nel token dal server di autorizzazione, non passato come parametro che l'agente controlla. L'API controlla il token, non le istruzioni dell'agente.

Questo significa: anche se qualcuno inganna l'agente facendogli tentare di recuperare i dati di un altro cliente, il token non lo autorizzerà.

## Cosa Distribuisce il Template

Con pochi comandi `azd` ottieni:

- Un agente backend su Microsoft Foundry (C#, SDK Microsoft A2A e MCP)
- Un server MCP che espone un'API di portafoglio di esempio
- Curity Identity Server come server di autorizzazione, insieme a Entra ID per l'autenticazione
- Gateway API esterni e interni che gestiscono lo scambio di token e il logging degli audit
- Bicep per tutta l'infrastruttura Azure: Container Apps, VNet, ACR, Azure AI Foundry, Key Vault, Azure SQL Database, storage

L'intero pattern è ispezionabile e personalizzabile.

## Il Principio di Design che Vale la Pena Adottare

Anche se non usi Curity, il pattern è trasferibile: **gli agenti non dovrebbero mai avere accesso permanente all'API**. Ogni azione dovrebbe usare un token di breve durata con il minimo scope necessario per quella specifica chiamata, emesso per la specifica identità dell'agente, con i claim di cui l'API ha bisogno per prendere decisioni di autorizzazione.

Questo regge contro agenti creativi, errori e prompt injection in modi che "assicurati solo che l'agente non faccia cose cattive" non farà mai.

## Conclusione

I pattern di sicurezza per gli agenti IA sono ancora in fase di definizione in tutto il settore. Questo template è una delle implementazioni di riferimento più complete che ho visto — copre il flusso di autorizzazione reale, non solo l'autenticazione.

Post originale: [Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
