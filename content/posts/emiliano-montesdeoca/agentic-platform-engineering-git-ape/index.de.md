---
title: "Agentisches Platform Engineering Wird Realität — Git-APE Zeigt Wie"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Microsofts Git-APE-Projekt setzt agentisches Platform Engineering in die Praxis um — mit GitHub Copilot Agents und Azure MCP, um natürlichsprachliche Anfragen in validierte Cloud-Infrastruktur umzuwandeln."
tags:
  - azure
  - github-copilot
  - platform-engineering
  - agents
  - mcp
  - devops
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "agentic-platform-engineering-git-ape" >}}).*

Platform Engineering war einer dieser Begriffe, die auf Konferenzen toll klingen, aber normalerweise bedeuten: „Wir haben ein internes Portal und einen Terraform-Wrapper gebaut." Das eigentliche Versprechen — Self-Service-Infrastruktur, die wirklich sicher, kontrolliert und schnell ist — war immer noch ein paar Schritte entfernt.

Das Azure-Team hat gerade [Teil 2 ihrer Serie über agentisches Platform Engineering](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) veröffentlicht, und in diesem Teil geht es um die praktische Umsetzung. Sie nennen es **Git-APE** (ja, das Akronym ist beabsichtigt), und es ist ein Open-Source-Projekt, das GitHub Copilot Agents plus Azure MCP Server nutzt, um natürlichsprachliche Anfragen in validierte, deployed Infrastruktur umzuwandeln.

## Was Git-APE tatsächlich macht

Die Kernidee: Anstatt dass Entwickler Terraform-Module lernen, durch Portal-UIs navigieren oder Tickets beim Platform-Team einreichen, sprechen sie mit einem Copilot-Agenten. Der Agent interpretiert die Absicht, generiert Infrastructure-as-Code, validiert sie gegen Richtlinien und deployt — alles innerhalb von VS Code.

Hier ist das Setup:

```bash
git clone https://github.com/Azure/git-ape
cd git-ape
```

Öffne den Workspace in VS Code, und die Agent-Konfigurationsdateien werden automatisch von GitHub Copilot erkannt. Du interagierst direkt mit dem Agenten:

```
@git-ape deploy a function app with storage in West Europe
```

Der Agent nutzt Azure MCP Server unter der Haube, um mit Azure-Diensten zu interagieren. Die MCP-Konfiguration in den VS Code-Einstellungen aktiviert spezifische Fähigkeiten:

```json
{
  "azureMcp.serverMode": "namespace",
  "azureMcp.enabledServices": [
    "deploy", "bestpractices", "group",
    "subscription", "functionapp", "storage",
    "sql", "monitor"
  ],
  "azureMcp.readOnly": false
}
```

## Warum das wichtig ist

Für diejenigen von uns, die auf Azure bauen, verschiebt dies die Platform-Engineering-Diskussion von „wie bauen wir ein Portal" zu „wie beschreiben wir unsere Leitplanken als APIs." Wenn die Schnittstelle deiner Plattform ein KI-Agent ist, wird die Qualität deiner Einschränkungen und Richtlinien zum Produkt.

Der Blog von Teil 1 legte die Theorie dar: gut beschriebene APIs, Kontrollschemata und explizite Leitplanken machen Plattformen agent-ready. Teil 2 beweist, dass es funktioniert, indem tatsächliche Werkzeuge ausgeliefert werden. Der Agent generiert nicht blind Ressourcen — er validiert gegen Best Practices, respektiert Namenskonventionen und wendet die Richtlinien deiner Organisation an.

Das Aufräumen ist genauso einfach:

```
@git-ape destroy my-resource-group
```

## Meine Einschätzung

Ich bin ehrlich — hier geht es mehr um das Muster als um das spezifische Tool. Git-APE selbst ist eine Demo/Referenzarchitektur. Aber die zugrundeliegende Idee — Agenten als Interface zu deiner Plattform, MCP als Protokoll, GitHub Copilot als Host — ist die Richtung, in die sich die Enterprise-Developer-Experience bewegt.

Wenn du ein Platform-Team bist, das darüber nachdenkt, wie man interne Werkzeuge agent-freundlich macht, gibt es keinen besseren Startpunkt. Und wenn du ein .NET-Entwickler bist, der sich fragt, wie das mit deiner Welt zusammenhängt: Der Azure MCP Server und GitHub Copilot Agents funktionieren mit jedem Azure-Workload. Deine ASP.NET Core API, dein .NET Aspire Stack, deine containerisierten Microservices — all das kann Ziel eines agentischen Deployment-Flows sein.

## Zusammenfassung

Git-APE ist ein früher, aber konkreter Blick auf agentisches Platform Engineering in der Praxis. Klone das [Repo](https://github.com/Azure/git-ape), probiere die Demo aus und fange an darüber nachzudenken, wie die APIs und Richtlinien deiner Plattform aussehen müssten, damit ein Agent sie sicher nutzen kann.

Lies den [vollständigen Post](https://devblogs.microsoft.com/all-things-azure/putting-agentic-platform-engineering-to-the-test/) für den Walkthrough und Video-Demos.
