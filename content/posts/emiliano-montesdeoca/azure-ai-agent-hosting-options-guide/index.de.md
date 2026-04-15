---
title: "Wo solltest du deine KI-Agenten auf Azure hosten? Ein praktischer Entscheidungsleitfaden"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure bietet sechs Möglichkeiten, KI-Agenten zu hosten — von rohen Containern bis hin zu vollständig verwalteten Foundry Hosted Agents. So wählst du die richtige für deine .NET-Workload."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "azure-ai-agent-hosting-options-guide.md" >}}).*

Wenn du gerade KI-Agenten mit .NET baust, hast du wahrscheinlich etwas bemerkt: Es gibt *viele* Möglichkeiten, sie auf Azure zu hosten. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents — und alle klingen vernünftig, bis du tatsächlich einen auswählen musst. Microsoft hat gerade einen [umfassenden Leitfaden zum Azure KI-Agenten-Hosting](https://devblogs.microsoft.com/all-things-azure/hostedagent/) veröffentlicht, der das klärt, und ich möchte ihn aus der praktischen Perspektive eines .NET-Entwicklers aufschlüsseln.

## Die sechs Optionen auf einen Blick

So würde ich die Landschaft zusammenfassen:

| Option | Am besten für | Du verwaltest |
|--------|--------------|---------------|
| **Container Apps** | Volle Container-Kontrolle ohne K8s-Komplexität | Observability, State, Lifecycle |
| **AKS** | Enterprise-Compliance, Multi-Cluster, Custom Networking | Alles (das ist der Punkt) |
| **Azure Functions** | Event-getriebene, kurzlebige Agenten-Tasks | Kaum etwas — echtes Serverless |
| **App Service** | Einfache HTTP-Agenten, vorhersehbarer Traffic | Deployment, Scaling-Config |
| **Foundry Agents** | Code-optionale Agenten über Portal/SDK | Fast nichts |
| **Foundry Hosted Agents** | Custom-Framework-Agenten mit verwalteter Infra | Nur dein Agenten-Code |

Die ersten vier sind General-Purpose Compute — du *kannst* Agenten darauf ausführen, aber sie wurden nicht dafür entwickelt. Die letzten zwei sind agenten-nativ: Sie verstehen Konversationen, Tool-Aufrufe und Agenten-Lifecycles als First-Class-Konzepte.

## Foundry Hosted Agents — der Sweet Spot für .NET-Agenten-Entwickler

Das hat meine Aufmerksamkeit geweckt. Foundry Hosted Agents sitzen genau in der Mitte: Du bekommst die Flexibilität, deinen eigenen Code auszuführen (Semantic Kernel, Agent Framework, LangGraph — was auch immer), aber die Plattform kümmert sich um Infrastruktur, Observability und Konversationsmanagement.

Das Schlüsselstück ist der **Hosting Adapter** — eine dünne Abstraktionsschicht, die dein Agenten-Framework mit der Foundry-Plattform verbindet. Für Microsoft Agent Framework sieht das so aus:

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

Das ist deine gesamte Hosting-Geschichte. Der Adapter übernimmt Protokollübersetzung, Streaming über Server-Sent Events, Konversationsverlauf und OpenTelemetry-Tracing — alles automatisch. Keine Custom Middleware, kein manuelles Plumbing.

## Deployment ist wirklich einfach

Ich habe vorher Agenten auf Container Apps deployed und es funktioniert, aber man schreibt am Ende viel Glue-Code für State Management und Observability. Mit Hosted Agents und `azd` sieht das Deployment so aus:

```bash
# KI-Agenten-Extension installieren
azd ext install azure.ai.agents

# Von einer Vorlage initialisieren
azd ai agent init

# Bauen, pushen, deployen — fertig
azd up
```

Dieses einzelne `azd up` baut deinen Container, pusht ihn zu ACR, provisioniert das Foundry-Projekt, deployed Model-Endpoints und startet deinen Agenten. Fünf Schritte in einem Befehl zusammengefasst.

## Integriertes Konversationsmanagement

Das ist der Teil, der in der Produktion am meisten Zeit spart. Anstatt deinen eigenen Konversations-State-Store zu bauen, handhaben Hosted Agents das nativ:

```python
# Eine persistente Konversation erstellen
conversation = openai_client.conversations.create()

# Erste Runde
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# Zweite Runde — Kontext bleibt erhalten
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

Kein Redis. Kein Cosmos DB Session Store. Keine Custom Middleware für Nachrichtenserialisierung. Die Plattform kümmert sich einfach darum.

## Mein Entscheidungsframework

Nachdem ich alle sechs Optionen durchgegangen bin, hier mein schnelles mentales Modell:

1. **Brauchst du null Infrastruktur?** → Foundry Agents (Portal/SDK, keine Container)
2. **Hast du Custom-Agenten-Code, willst aber verwaltetes Hosting?** → Foundry Hosted Agents
3. **Brauchst du event-getriebene, kurzlebige Agenten-Tasks?** → Azure Functions
4. **Brauchst du maximale Container-Kontrolle ohne K8s?** → Container Apps
5. **Brauchst du strikte Compliance und Multi-Cluster?** → AKS
6. **Hast du einen einfachen HTTP-Agenten mit vorhersehbarem Traffic?** → App Service

Für die meisten .NET-Entwickler, die mit Semantic Kernel oder Microsoft Agent Framework bauen, sind Hosted Agents wahrscheinlich der richtige Startpunkt. Du bekommst Scale-to-Zero, integriertes OpenTelemetry, Konversationsmanagement und Framework-Flexibilität — ohne Kubernetes zu verwalten oder deinen eigenen Observability-Stack aufzubauen.

## Zum Abschluss

Die Agenten-Hosting-Landschaft auf Azure reift schnell. Wenn du heute ein neues KI-Agenten-Projekt startest, würde ich Foundry Hosted Agents ernsthaft in Betracht ziehen, bevor du aus Gewohnheit zu Container Apps oder AKS greifst. Die verwaltete Infrastruktur spart echte Zeit, und das Hosting-Adapter-Pattern lässt dich deine Framework-Wahl behalten.

Schau dir den [vollständigen Leitfaden von Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/) und das [Foundry Samples Repo](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents) für funktionierende Beispiele an.
