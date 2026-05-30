---
title: "Ihr Lokaler MAF-Agent Hat Jetzt ein Produktions-Zuhause"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents verleiht Ihrem Microsoft Agent Framework-Agenten Identität, Skalierung, Sitzungspersistenz und Observabilität ohne zusätzliche Konfiguration. So sieht das in der Praxis aus."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

Einen Agenten lokal zum Laufen zu bringen ist der spaßige Teil. Der knifflige Teil ist alles, was danach kommt: es ohne Nervenzerreißen zu deployen, Sitzungen zu verwalten, Identität einzurichten, Observabilität zu verkabeln. Das bedeutet normalerweise viel benutzerdefinierte Infrastruktur.

Foundry Hosted Agents hat den Großteil dieser Infrastruktur für Microsoft Agent Framework (MAF)-Benutzer gerade beseitigt.

## Was Foundry Hosted Agents Wirklich Tut

Wenn Sie einen MAF-Agenten in Foundry Hosted Agents deployen, übernimmt die Plattform eine überraschend lange Liste von Dingen, die Sie sonst selbst bauen müssten:

- **Skalierung auf null** — Ihr Agent kostet nichts im Leerlauf und fährt automatisch wieder hoch
- **Pro-Sitzung VM-isolierte Sandboxes** — jede Benutzersitzung bekommt ihre eigene Sandbox mit Dateisystempersistenz, die Scale-down-Ereignisse überlebt
- **Eingebautes Entra ID** — jeder Agent erhält seine eigene Identität, um Foundry-Modelle, Toolbox und Azure-Dienste aufzurufen, ohne Geheimnisse im Image
- **Versionierte Deployments** — jedes Deployment ist ein unveränderlicher Snapshot mit Blue/Green- und Canary-Rollout-Unterstützung
- **Observabilität ohne Konfiguration** — `APPLICATIONINSIGHTS_CONNECTION_STRING` wird zur Laufzeit injiziert, sodass MAFs OpenTelemetry-Traces automatisch in App Insights fließen

Letzteres ist wirklich angenehm. Kein zusätzliches Verkabeln, keine zusätzliche Konfiguration. Traces erscheinen einfach.

## Der Code-Unterschied Ist Minimal

Das schätze ich an dieser Integration am meisten. Sie schreiben Ihren Agenten nicht neu. Sie umhüllen ihn einfach:

**In .NET:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**In Python:**

```python
server = ResponsesHostServer(agent)
server.run()
```

Das ist alles. Dieselbe Logik, die Sie lokal getestet haben, läuft in der Produktion. Die Plattform umhüllt sie mit der Infrastruktur für Sitzungsverwaltung, Identität und Skalierung.

## Zwei Protokolle, Ein Agent

Hosted Agents unterstützen zwei Endpoint-Stile:

- **Responses** (`/responses`) — OpenAI-kompatibel, verwaltet Gesprächsverlauf und Streaming. Guter Standard für chat-ähnliche Agenten.
- **Invocations** (`/invocations`) — Sie definieren das Anfrage-/Antwortschema. Gut für nicht-konversationelle Workflows.

Wenn Sie etwas bauen, das wie ein Gespräch aussieht, beginnen Sie mit Responses. Wenn Sie einen API-ähnlichen Agenten bauen, der strukturierte Eingaben nimmt und strukturierte Ausgaben zurückgibt, gibt Ihnen Invocations die Flexibilität.

## Der Deployment-Ablauf mit `azd`

Wenn Sie `azd up` mit einem MAF-Agenten ausführen:

1. Erstellt optional ein Foundry-Projekt und deployed ein Modell
2. Packt Ihren Code und pusht ein Image zu Azure Container Registry
3. Provisioniert Compute aus dem ACR-Image
4. Weist dem Agenten eine dedizierte Entra ID zu
5. Stellt einen stabilen Endpoint bereit (`https://{project_endpoint}/agents/{agent_name}`)
6. Handhabt alles andere von diesem Punkt an

Sitzungen bleiben bis zu 30 Tage bestehen. Inaktives Compute wird nach 15 Minuten deprovisioniert und bei der nächsten Anfrage transparent wiederhergestellt. Aus der Perspektive des Agenten hat sich nichts geändert.

## Fazit

Die Distanz zwischen "lokal funktionierend" und "in der Produktion laufend" war für KI-Agenten historisch lang und schmerzhaft. Foundry Hosted Agents + MAF schließt diese Lücke erheblich. Wenn Sie bereits einen lokalen Agenten mit Agent Framework gebaut haben, lohnt es sich, dies heute auszuprobieren.

Das Team sagt, GA kommt bald — dies ist derzeit in Preview. Schauen Sie sich die [MAF Hosted Agent Integration-Dokumentation](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) und die [.NET-Beispiele](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) an, um loszulegen.

Originalartikel: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
