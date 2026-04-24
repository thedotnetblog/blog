---
title: "Foundry Toolboxes: Ein einziger Endpunkt für alle Agent-Tools"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry hat Toolboxes in der Public Preview veröffentlicht — eine Möglichkeit, KI-Agent-Tools über einen einzigen MCP-kompatiblen Endpunkt zu kuratieren, zu verwalten und bereitzustellen."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [hier klicken]({{< ref "index.md" >}}).*

Hier ist ein Problem, das banal klingt, bis man es selbst erlebt: Die Organisation baut mehrere KI-Agenten, jeder braucht Tools, und jedes Team verkabelt sie von Grund auf neu. Dieselbe Web-Search-Integration, dieselbe Azure AI Search-Konfiguration, dieselbe GitHub-MCP-Server-Verbindung — aber in einem anderen Repository, von einem anderen Team, mit anderen Credentials und ohne gemeinsame Governance.

Microsoft Foundry hat soeben [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) in der Public Preview veröffentlicht — eine direkte Antwort auf dieses Problem.

## Was ist eine Toolbox?

Eine Toolbox ist ein benanntes, wiederverwendbares Tool-Bundle, das man einmal in Foundry definiert und über einen einzigen MCP-kompatiblen Endpunkt bereitstellt. Jede Agent-Runtime, die MCP spricht, kann sie konsumieren — kein Lock-in bei Foundry Agents.

Das Versprechen ist einfach: **build once, consume anywhere**. Tools definieren, Authentifizierung zentral konfigurieren (OAuth passthrough, Entra Managed Identity), Endpunkt veröffentlichen. Jeder Agent, der diese Tools braucht, verbindet sich einmal und bekommt sie alle.

## Die vier Säulen (zwei davon heute verfügbar)

| Säule | Status | Was sie tut |
|-------|--------|-------------|
| **Discover** | Demnächst | Genehmigte Tools finden ohne manuelle Suche |
| **Build** | Heute verfügbar | Tools in ein wiederverwendbares Bundle kuratieren |
| **Consume** | Heute verfügbar | Ein MCP-Endpunkt stellt alle Tools bereit |
| **Govern** | Demnächst | Zentrale Auth + Observability für alle Tool-Calls |

## Praktisches Beispiel

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Dokumentation durchsuchen und auf GitHub-Issues reagieren.",
    tools=[
        {"type": "web_search", "description": "Öffentliche Dokumentation suchen"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Nach der Veröffentlichung liefert Foundry einen einheitlichen Endpunkt. Eine Verbindung, alle Tools.

## Kein Lock-in bei Foundry Agents

Toolboxes werden in Foundry **erstellt und verwaltet**, aber die Konsumfläche ist das offene MCP-Protokoll. Sie können von Custom Agents mit Microsoft Agent Framework oder LangGraph, GitHub Copilot und anderen MCP-fähigen IDEs sowie jeder anderen MCP-Runtime genutzt werden.

## Warum das jetzt wichtig ist

Die Multi-Agenten-Welle kommt in der Produktion an. Jeder neue Agent ist eine neue Fläche für duplizierte Konfiguration, veraltete Credentials und inkonsistentes Verhalten. Die Build + Consume-Grundlage reicht aus, um mit der Zentralisierung zu beginnen. Wenn die Govern-Säule kommt, hat man eine vollständig beobachtbare, zentral gesteuerte Tool-Schicht für die gesamte Agent-Flotte.

## Fazit

Das ist noch früh — Public Preview, Python SDK zuerst, mit Discover und Govern noch ausstehend. Aber das Modell ist solide und das MCP-native Design bedeutet, dass es mit den Tools funktioniert, die man bereits aufbaut. Details im [offiziellen Announcement](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/).
