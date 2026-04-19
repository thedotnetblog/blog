---
title: "Respostes de fons a Microsoft Agent Framework: no hi ha més ansietat de temps d'espera"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework ara us permet descarregar tasques d'IA de llarga durada amb fitxes de continuació. A continuació s'explica com funcionen les respostes de fons i per què són importants per als vostres agents.NET."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

Si heu creat alguna cosa amb models de raonament com l'o3 o el GPT-5.2, coneixeu el dolor. El vostre agent comença a pensar en una tasca complexa, el client s'asseu allà esperant i en algun lloc entre "això està bé" i "s'ha estavellat?" la vostra connexió s'esgota. Tota aquesta feina? Desaparegut.

Microsoft Agent Framework acaba d'enviar [respostes de fons](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) i, sincerament, aquesta és una d'aquestes característiques que haurien d'haver existit des del primer dia.

## El problema amb el bloqueig de trucades

En un patró de sol·licitud-resposta tradicional, el vostre client es bloqueja fins que l'agent acabi. Això funciona bé per a tasques ràpides. Però quan demaneu a un model de raonament que faci una investigació profunda, una anàlisi en diversos passos o que generi un informe de 20 pàgines? Esteu mirant els minuts del rellotge de paret. Durant aquesta finestra:

- Les connexions HTTP es poden esgotar
- Els blips de xarxa maten tota l'operació
- El vostre usuari mira un spinner preguntant-se si està passant alguna cosa

Les respostes de fons donen la volta a això.

## Com funcionen les fitxes de continuació

En lloc de bloquejar, inicieu la tasca de l'agent i recupereu un **token de continuació**. Penseu-ho com un bitllet de reclamació en un taller de reparacions: no us quedeu al taulell esperant, torneu quan estigui llest.

El flux és senzill:

1. Envieu la vostra sol·licitud amb `AllowBackgroundResponses = true`
2. Si l'agent admet el processament en segon pla, obtindreu un testimoni de continuació
3. Enquesta sobre el teu horari fins que el testimoni torni `null`; això vol dir que el resultat està preparat

Aquí teniu la versió de.NET:

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

// Poll until complete
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

Si l'agent completa immediatament (tasques senzilles, models que no necessiten processament en segon pla), no es retorna cap testimoni de continuació. El vostre codi només funciona, no cal cap manipulació especial.

## Transmissió amb currículum: la veritable màgia

Les enquestes estan bé per als escenaris de foc i oblit, però què passa quan voleu progrés en temps real? Les respostes en segon pla també admeten la transmissió amb la represa integrada.

Cada actualització en streaming porta el seu propi testimoni de continuació. Si la vostra connexió cau a la meitat del flux, repreneu exactament on ho vau deixar:

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
    break; // Simulate a network interruption
}

// Resume from exactly where we left off
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

L'agent continua processant el costat del servidor independentment del que passi amb el vostre client. Això és una tolerància a fallades integrada sense que escriviu la lògica de reintent o els interruptors.

## Quan s'ha d'utilitzar realment

No totes les trucades d'agent necessiten respostes en segon pla. Per completar-les ràpidament, esteu afegint complexitat sense cap motiu. Però aquí és on brillen:

- **Tasques de raonament complexes**: anàlisi en diversos passos, investigació profunda, qualsevol cosa que faci pensar realment a un model de raonament
- **Generació llarga de contingut**: informes detallats, documents de diverses parts, anàlisis exhaustives
- **Xarxes poc fiables**: clients mòbils, desplegaments perifèrics, VPN corporatives descabellades
- **Patrons UX asíncrons**: envieu una tasca, aneu a fer una altra cosa, torneu per obtenir resultats

Per als desenvolupadors de.NET que creem aplicacions empresarials, aquesta última és especialment interessant. Penseu en una aplicació Blazor en què un usuari sol·licita un informe complex: desactiveu la tasca de l'agent, els mostreu un indicador de progrés i deixeu que continuï treballant. Sense gimnàstica WebSocket, sense infraestructura de cua personalitzada, només un testimoni i un bucle d'enquesta.

## Tancant

Les respostes de fons estan disponibles ara tant a.NET com a Python mitjançant Microsoft Agent Framework. Si esteu creant agents que fan alguna cosa més complexa que les simples preguntes i respostes, val la pena afegir-ho al vostre conjunt d'eines. El patró de testimoni de continuació manté les coses senzilles alhora que resol un problema de producció molt real.

Consulteu la [documentació completa](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) per obtenir la referència completa de l'API i més exemples.
