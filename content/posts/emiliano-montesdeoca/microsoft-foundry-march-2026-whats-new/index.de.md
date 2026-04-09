---
title: "Microsoft Foundry März 2026 — GPT-5.4, Agent Service GA und das SDK-Refresh, das Alles Verändert"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Das März-2026-Update von Microsoft Foundry ist gewaltig: Agent Service erreicht GA, GPT-5.4 bringt zuverlässiges Reasoning, das azure-ai-projects SDK wird in allen Sprachen stabil, und Fireworks AI bringt offene Modelle nach Azure."
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "microsoft-foundry-march-2026-whats-new.md" >}}).*

Die monatlichen „What's New in Microsoft Foundry"-Posts sind normalerweise eine Mischung aus inkrementellen Verbesserungen und gelegentlichen Highlight-Features. Die [März 2026-Ausgabe](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)? Praktisch nur Highlight-Features. Foundry Agent Service erreicht GA, GPT-5.4 geht in Produktion, das SDK bekommt ein großes stabiles Release, und Fireworks AI bringt Open-Model-Inferenz nach Azure. Schauen wir uns an, was für .NET-Entwickler wichtig ist.

## Foundry Agent Service ist produktionsreif

Das ist die große Neuigkeit. Die Runtime der nächsten Generation für Agenten ist allgemein verfügbar — aufgebaut auf der OpenAI Responses API, draht-kompatibel mit OpenAI-Agenten und offen für Modelle verschiedener Anbieter. Wenn ihr heute mit der Responses API baut, fügt die Migration zu Foundry Enterprise-Sicherheit, privates Networking, Entra RBAC, vollständiges Tracing und Evaluation auf eure bestehende Agentenlogik hinzu.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

Zentrale Neuerungen: End-to-End Private Networking, MCP-Auth-Erweiterung (einschließlich OAuth-Passthrough), Voice Live Preview für Sprach-zu-Sprach-Agenten und gehostete Agenten in 6 neuen Regionen.

## GPT-5.4 — Zuverlässigkeit über reine Intelligenz

Bei GPT-5.4 geht es nicht darum, schlauer zu sein. Es geht um Zuverlässigkeit. Stärkeres Reasoning über lange Interaktionen, bessere Instruktionstreue, weniger Ausfälle mitten im Workflow und integrierte Computer-Use-Fähigkeiten. Für Produktions-Agenten ist diese Zuverlässigkeit viel wichtiger als Benchmark-Scores.

| Modell | Preis (pro M Token) | Ideal für |
|--------|---------------------|-----------|
| GPT-5.4 (≤272K) | $2.50 / $15 Output | Produktions-Agenten, Coding, Dokumenten-Workflows |
| GPT-5.4 Pro | $30 / $180 Output | Tiefgehende Analyse, wissenschaftliches Reasoning |
| GPT-5.4 Mini | Kostengünstig | Klassifikation, Extraktion, leichte Tool-Aufrufe |

Die clevere Strategie ist Routing: GPT-5.4 Mini übernimmt die hochvolumige, latenzarme Arbeit, während GPT-5.4 die reasoning-intensiven Anfragen bearbeitet.

## Das SDK ist endlich stabil

Das `azure-ai-projects` SDK hat stabile Releases in allen Sprachen veröffentlicht — Python 2.0.0, JS/TS 2.0.0, Java 2.0.0 und .NET 2.0.0 (1. April). Die `azure-ai-agents`-Abhängigkeit ist weg — alles lebt unter `AIProjectClient`. Installation mit `pip install azure-ai-projects`, das Paket bündelt `openai` und `azure-identity` als direkte Abhängigkeiten.

Für .NET-Entwickler bedeutet das ein einziges NuGet-Paket für die gesamte Foundry-Oberfläche. Schluss mit dem Jonglieren separater Agent-SDKs.

## Fireworks AI bringt offene Modelle nach Azure

Vielleicht die architektonisch interessanteste Ergänzung: Fireworks AI verarbeitet über 13 Billionen Token täglich bei ~180K Anfragen/Sekunde, jetzt über Foundry verfügbar. DeepSeek V3.2, gpt-oss-120b, Kimi K2.5 und MiniMax M2.5 zum Start.

Die eigentliche Geschichte ist **Bring-Your-Own-Weights** — quantisierte oder feingetunete Gewichte von überall hochladen, ohne den Serving-Stack zu ändern. Deployment über serverloses Pay-per-Token oder provisionierten Durchsatz.

## Weitere Highlights

- **Phi-4 Reasoning Vision 15B** — multimodales Reasoning für Charts, Diagramme und Dokumentlayouts
- **Evaluations GA** — fertige Evaluatoren mit kontinuierlichem Produktions-Monitoring direkt in Azure Monitor
- **Priority Processing** (Preview) — dedizierte Compute-Lane für latenzempfindliche Workloads
- **Voice Live** — Sprach-zu-Sprach-Runtime, die direkt mit Foundry-Agenten verbunden ist
- **Tracing GA** — End-to-End-Inspektion von Agenten-Traces mit Sortierung und Filterung
- **PromptFlow-Deprecation** — Migration zu Microsoft Framework Workflows bis Januar 2027

## Fazit

März 2026 ist ein Wendepunkt für Foundry. Agent Service GA, stabile SDKs in allen Sprachen, GPT-5.4 für zuverlässige Produktions-Agenten und Open-Model-Inferenz über Fireworks AI — die Plattform ist bereit für ernsthafte Workloads.

Lest den [vollständigen Überblick](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) und [baut euren ersten Agenten](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code), um loszulegen.
