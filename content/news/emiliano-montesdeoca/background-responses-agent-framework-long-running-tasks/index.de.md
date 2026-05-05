---
title: "Background Responses im Microsoft Agent Framework: Keine Timeout-Angst mehr"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Das Microsoft Agent Framework ermöglicht nun das Auslagern lang laufender KI-Aufgaben mit Continuation Tokens. So funktionieren Background Responses und warum sie für deine .NET-Agenten wichtig sind."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

Wenn du irgendetwas mit Reasoning-Modellen wie o3 oder GPT-5.2 gebaut hast, kennst du den Schmerz. Dein Agent fängt an, über eine komplexe Aufgabe nachzudenken, der Client wartet, und irgendwo zwischen "das ist okay" und "ist das abgestürzt?" bricht deine Verbindung wegen Timeout ab. Die ganze Arbeit? Weg.

Das Microsoft Agent Framework hat gerade [Background Responses](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) ausgeliefert — und ehrlich gesagt, das ist eine dieser Funktionen, die von Anfang an hätte existieren sollen.

## Das Problem mit blockierenden Aufrufen

In einem traditionellen Request-Response-Muster blockiert dein Client, bis der Agent fertig ist. Das funktioniert gut für schnelle Aufgaben. Aber wenn du ein Reasoning-Modell bittest, tiefgehende Recherche, mehrstufige Analyse oder einen 20-seitigen Bericht zu erstellen? Da schaust du auf Minuten realer Wartezeit. Während dieses Zeitfensters:

- HTTP-Verbindungen können ablaufen
- Netzwerkunterbrechungen zerstören die gesamte Operation
- Dein Benutzer starrt auf einen Spinner und fragt sich, ob irgendetwas passiert

Background Responses drehen das Ganze um.

## Wie Continuation Tokens funktionieren

Anstatt zu blockieren, startest du die Agent-Aufgabe und bekommst ein **Continuation Token** zurück. Denk daran wie an einen Abholschein in einer Werkstatt — du stehst nicht an der Theke und wartest, du kommst zurück, wenn es fertig ist.

Der Ablauf ist unkompliziert:

1. Sende deine Anfrage mit `AllowBackgroundResponses = true`
2. Wenn der Agent Hintergrundverarbeitung unterstützt, bekommst du ein Continuation Token
3. Polle nach deinem Zeitplan, bis das Token `null` zurückgibt — das bedeutet, das Ergebnis ist fertig

Hier ist die .NET-Version:

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

// Pollen bis fertig
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

Wenn der Agent sofort fertig wird (einfache Aufgaben, Modelle die keine Hintergrundverarbeitung brauchen), wird kein Continuation Token zurückgegeben. Dein Code funktioniert einfach — keine spezielle Behandlung nötig.

## Streaming mit Wiederaufnahme: die echte Magie

Polling ist gut für Fire-and-Forget-Szenarien, aber was, wenn du Echtzeit-Fortschritt willst? Background Responses unterstützen auch Streaming mit eingebauter Wiederaufnahme.

Jedes gestreamte Update trägt sein eigenes Continuation Token. Wenn deine Verbindung mitten im Stream abbricht, setzt du genau dort fort, wo du aufgehört hast:

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
    break; // Simuliere eine Netzwerkunterbrechung
}

// Genau dort fortsetzen, wo wir aufgehört haben
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

Der Agent verarbeitet serverseitig weiter, unabhängig davon, was mit deinem Client passiert. Das ist eingebaute Fehlertoleranz, ohne dass du Retry-Logik oder Circuit Breaker schreiben musst.

## Wann man das tatsächlich verwenden sollte

Nicht jeder Agent-Aufruf braucht Background Responses. Für schnelle Completions fügst du Komplexität ohne Grund hinzu. Aber hier glänzen sie:

- **Komplexe Reasoning-Aufgaben** — mehrstufige Analyse, tiefgehende Recherche, alles was ein Reasoning-Modell wirklich zum Nachdenken bringt
- **Lange Content-Generierung** — detaillierte Berichte, mehrteilige Dokumente, ausführliche Analysen
- **Unzuverlässige Netzwerke** — mobile Clients, Edge-Deployments, instabile Firmen-VPNs
- **Asynchrone UX-Muster** — Aufgabe absenden, etwas anderes machen, Ergebnisse abholen

Für uns .NET-Entwickler, die Enterprise-Apps bauen, ist der letzte Punkt besonders interessant. Denk an eine Blazor-App, in der ein Benutzer einen komplexen Bericht anfordert — du startest die Agent-Aufgabe, zeigst einen Fortschrittsindikator und lässt sie weiterarbeiten. Keine WebSocket-Akrobatik, keine selbstgebaute Queue-Infrastruktur, nur ein Token und eine Poll-Schleife.

## Zusammenfassung

Background Responses sind jetzt sowohl in .NET als auch in Python über das Microsoft Agent Framework verfügbar. Wenn du Agenten baust, die mehr als einfaches Q&A machen, lohnt es sich, das in dein Toolkit aufzunehmen. Das Continuation-Token-Muster hält die Dinge einfach und löst gleichzeitig ein sehr reales Produktionsproblem.

Schau dir die [vollständige Dokumentation](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) für die komplette API-Referenz und weitere Beispiele an.
