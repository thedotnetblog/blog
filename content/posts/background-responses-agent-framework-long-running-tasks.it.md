---
title: "Risposte in background nel Microsoft Agent Framework: basta ansia da timeout"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework ora permette di scaricare attività IA di lunga durata con token di continuazione. Ecco come funzionano le risposte in background e perché contano per i tuoi agenti .NET."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

Se hai costruito qualcosa con modelli di ragionamento come o3 o GPT-5.2, conosci il dolore. Il tuo agente inizia a ragionare su un compito complesso, il client resta in attesa, e da qualche parte tra "va tutto bene" e "si sarà bloccato?" la tua connessione va in timeout. Tutto quel lavoro? Perso.

Microsoft Agent Framework ha appena rilasciato le [risposte in background](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) — e onestamente, questa è una di quelle funzionalità che avrebbero dovuto esistere dal primo giorno.

## Il problema con le chiamate bloccanti

In un pattern tradizionale richiesta-risposta, il tuo client si blocca finché l'agente non finisce. Funziona bene per i compiti veloci. Ma quando chiedi a un modello di ragionamento di fare ricerca approfondita, analisi multi-step, o generare un report di 20 pagine? Stai guardando minuti di tempo reale. Durante quella finestra:

- Le connessioni HTTP possono scadere
- I problemi di rete uccidono l'intera operazione
- Il tuo utente fissa uno spinner chiedendosi se sta succedendo qualcosa

Le risposte in background ribaltano tutto questo.

## Come funzionano i token di continuazione

Invece di bloccare, lanci il compito dell'agente e ottieni un **token di continuazione**. Pensalo come un biglietto di ritiro in un'officina — non resti al bancone ad aspettare, torni quando è pronto.

Il flusso è diretto:

1. Invia la tua richiesta con `AllowBackgroundResponses = true`
2. Se l'agente supporta l'elaborazione in background, ricevi un token di continuazione
3. Interroga al tuo ritmo finché il token non torna `null` — significa che il risultato è pronto

Ecco la versione .NET:

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri("https://<myresource>.openai.azure.com"),
    new DefaultAzureCredential())
    .GetResponsesClient("<deployment-name>")
    .AsAIAgent();

AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();

AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

// Interrogare fino al completamento
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

Se l'agente completa immediatamente (compiti semplici, modelli che non necessitano di elaborazione in background), nessun token viene restituito. Il tuo codice funziona e basta — nessuna gestione speciale necessaria.

## Streaming con ripresa: la vera magia

Il polling va bene per scenari fire-and-forget, ma cosa succede quando vuoi il progresso in tempo reale? Le risposte in background supportano anche lo streaming con ripresa integrata.

Ogni aggiornamento dello stream porta il suo token di continuazione. Se la tua connessione cade a metà stream, riprendi esattamente da dove avevi lasciato:

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponseUpdate? latestUpdate = null;

await foreach (var update in agent.RunStreamingAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options))
{
    Console.Write(update.Text);
    latestUpdate = update;
    break; // Simulare un'interruzione di rete
}

// Riprendere esattamente da dove avevamo lasciato
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

L'agente continua a elaborare lato server indipendentemente da cosa succede al tuo client. È tolleranza ai guasti integrata senza che tu scriva logica di retry o circuit breaker.

## Quando usare questo concretamente

Non ogni chiamata all'agente ha bisogno di risposte in background. Per completamenti veloci, stai aggiungendo complessità senza motivo. Ma ecco dove brillano:

- **Compiti di ragionamento complesso** — analisi multi-step, ricerca approfondita, qualsiasi cosa che faccia davvero pensare un modello di ragionamento
- **Generazione di contenuti lunghi** — report dettagliati, documenti multi-parte, analisi estese
- **Reti poco affidabili** — client mobili, deployment edge, VPN aziendali instabili
- **Pattern UX asincroni** — invia un compito, vai a fare altro, torna per i risultati

Per noi sviluppatori .NET che costruiamo app enterprise, l'ultimo punto è particolarmente interessante. Pensa a un'app Blazor dove un utente richiede un report complesso — lanci il compito dell'agente, mostri un indicatore di progresso, e li lasci continuare a lavorare. Niente acrobazie WebSocket, niente infrastruttura di code personalizzata, solo un token e un loop di polling.

## Per concludere

Le risposte in background sono disponibili ora sia in .NET che in Python attraverso Microsoft Agent Framework. Se stai costruendo agenti che fanno qualcosa di più complesso del semplice Q&A, vale la pena aggiungerlo al tuo toolkit. Il pattern del token di continuazione mantiene le cose semplici risolvendo un problema di produzione molto reale.

Consulta la [documentazione completa](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) per il riferimento completo dell'API e altri esempi.
