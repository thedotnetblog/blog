---
title: "Verbinde deine MCP-Server auf Azure Functions mit Foundry Agents — So geht's"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Baue deinen MCP-Server einmal, deploye ihn auf Azure Functions und verbinde ihn mit Microsoft Foundry-Agenten mit korrekter Authentifizierung. Deine Tools funktionieren überall — VS Code, Cursor und jetzt auch Enterprise-AI-Agenten."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "foundry-agents-mcp-servers-azure-functions.md" >}}).*

Das liebe ich am MCP-Ökosystem: Du baust deinen Server einmal, und er funktioniert überall. VS Code, Visual Studio, Cursor, ChatGPT — jeder MCP-Client kann deine Tools entdecken und nutzen. Jetzt fügt Microsoft einen weiteren Konsumenten zu dieser Liste hinzu: Foundry-Agenten.

Lily Ma vom Azure SDK-Team [hat einen praktischen Leitfaden veröffentlicht](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) zur Verbindung von MCP-Servern auf Azure Functions mit Microsoft Foundry-Agenten. Wenn du bereits einen MCP-Server hast, ist das reiner Mehrwert — kein Neuaufbau nötig.

## Warum diese Kombination Sinn macht

Azure Functions bietet dir skalierbare Infrastruktur, integrierte Authentifizierung und Serverless-Abrechnung für das Hosting von MCP-Servern. Microsoft Foundry bietet dir AI-Agenten, die denken, planen und handeln können. Beides zu verbinden bedeutet, dass deine benutzerdefinierten Tools — Datenbankabfragen, Business-API-Aufrufe, Validierungslogik — zu Fähigkeiten werden, die Enterprise-AI-Agenten autonom entdecken und nutzen können.

Der Kernpunkt: Dein MCP-Server bleibt gleich. Du fügst einfach Foundry als weiteren Konsumenten hinzu. Die gleichen Tools, die in deinem VS Code-Setup funktionieren, treiben jetzt einen AI-Agenten an, mit dem dein Team oder deine Kunden interagieren.

## Authentifizierungsoptionen

Hier liefert der Post echten Mehrwert. Vier Authentifizierungsmethoden je nach Szenario:

| Methode | Anwendungsfall |
|---------|---------------|
| **Schlüsselbasiert** (Standard) | Entwicklung oder Server ohne Entra-Auth |
| **Microsoft Entra** | Produktion mit verwalteten Identitäten |
| **OAuth Identity Passthrough** | Produktion, bei der sich jeder Benutzer einzeln authentifiziert |
| **Ohne Authentifizierung** | Entwicklung/Tests oder nur öffentliche Daten |

Für die Produktion ist Microsoft Entra mit Agentenidentität der empfohlene Weg. OAuth Identity Passthrough ist für Fälle, in denen der Benutzerkontext wichtig ist — der Agent fordert Benutzer zur Anmeldung auf, und jede Anfrage trägt das eigene Token des Benutzers.

## Einrichtung

Der allgemeine Ablauf:

1. **Deploye deinen MCP-Server auf Azure Functions** — Beispiele verfügbar für [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet), Python, TypeScript und Java
2. **Aktiviere die integrierte MCP-Authentifizierung** auf deiner Function App
3. **Hole deine Endpoint-URL** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Füge den MCP-Server als Tool in Foundry hinzu** — navigiere zu deinem Agenten im Portal, füge ein neues MCP-Tool hinzu, gib Endpoint und Credentials an

Dann teste es im Agent Builder Playground, indem du einen Prompt sendest, der eines deiner Tools auslöst.

## Meine Einschätzung

Die Composability-Geschichte wird hier richtig stark. Baue deinen MCP-Server einmal in .NET (oder Python, TypeScript, Java), deploye ihn auf Azure Functions, und jeder MCP-kompatible Client kann ihn nutzen — Coding-Tools, Chat-Apps und jetzt Enterprise-AI-Agenten. Das ist ein „einmal schreiben, überall nutzen"-Muster, das tatsächlich funktioniert.

Speziell für .NET-Entwickler macht die [Azure Functions MCP-Erweiterung](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) das unkompliziert. Du definierst deine Tools als Azure Functions, deployest sie, und du hast einen produktionsreifen MCP-Server mit der gesamten Sicherheit und Skalierung, die Azure Functions bietet.

## Zusammenfassung

Wenn du MCP-Tools auf Azure Functions betreibst, ist die Verbindung mit Foundry-Agenten ein schneller Gewinn — deine benutzerdefinierten Tools werden zu Enterprise-AI-Fähigkeiten mit korrekter Authentifizierung und ohne Code-Änderungen am Server selbst.

Lies den [vollständigen Leitfaden](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) für Schritt-für-Schritt-Anleitungen zu jeder Authentifizierungsmethode, und sieh dir die [detaillierte Dokumentation](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry) für Produktions-Setups an.
