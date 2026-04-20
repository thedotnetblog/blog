---
title: "Achtergrondreacties in Microsoft Agent Framework: Geen Timeout-angst Meer"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework laat je nu langlopende AI-taken offloaden met vervolgingstokens. Zo werken achtergrondreacties en waarom ze belangrijk zijn voor je .NET-agents."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "background-responses-agent-framework-long-running-tasks" >}}).*

Als je ooit iets hebt gebouwd met redeneermodellen zoals o3 of GPT-5.2, ken je de pijn. Je agent begint een complexe taak te verwerken, de client zit te wachten en ergens treedt een verbindingstime-out op.

Microsoft Agent Framework heeft zojuist [achtergrondreacties](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) uitgebracht — en eerlijk gezegd is dit een van die functies die er vanaf dag één had moeten zijn.

## Hoe vervolgingstokens werken

In plaats van te blokkeren start je de agenttaak en krijg je een **vervolgingstoken** terug. Denk eraan als een klaim-ticket bij een reparatiewinkel:

1. Stuur je verzoek met `AllowBackgroundResponses = true`
2. Als de agent achtergrondverwerking ondersteunt, krijg je een vervolgingstoken
3. Poll op je planning totdat het token `null` terugkeert

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

## Wanneer dit te gebruiken

- **Complexe redeneer taken** — meerstapsanalyse, diepgaand onderzoek
- **Lange contentgeneratie** — gedetailleerde rapporten, meerdelige documenten
- **Onbetrouwbare netwerken** — mobiele clients, edge-implementaties
- **Asynchrone UX-patronen** — taak indienen, iets anders doen, terugkomen voor resultaten

Bekijk de [volledige documentatie](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/).
