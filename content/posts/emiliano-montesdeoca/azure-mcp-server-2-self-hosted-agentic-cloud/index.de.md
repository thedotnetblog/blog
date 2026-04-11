---
title: "Azure MCP Server 2.0 ist da — Self-Hosted Agentic Cloud Automation ist Realität"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 wird stabil mit Self-Hosted Remote Deployments, 276 Tools über 57 Azure-Dienste und Enterprise-Grade-Sicherheit — hier ist das, was für .NET-Entwickler zählt, die Agentic Workflows aufbauen."
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud.md" >}}).*

Falls du in letzter Zeit mit MCP und Azure etwas aufgebaut hast, weißt du wahrscheinlich schon, dass die lokale Erfahrung gut funktioniert. MCP-Server einstöpseln, deinen KI-Agenten mit Azure-Ressourcen kommunizieren lassen, weitermachen. Aber sobald du diese Einrichtung teamübergreifend teilen musst? Da wird es kompliziert.

Nicht mehr. Azure MCP Server [hat gerade 2.0 Stable erreicht](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), und die Hauptfunktion ist genau das, wofür Enterprise-Teams gefragt haben: **Self-Hosted Remote MCP Server Support**.

## Was ist Azure MCP Server?

Kleine Auffrischung. Azure MCP Server implementiert die [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)-Spezifikation und macht Azure-Funktionen als strukturierte, auffindbare Tools verfügbar, die KI-Agenten aufrufen können. Denk daran als standardisierte Brücke zwischen deinem Agenten und Azure — Bereitstellung, Deployment, Monitoring, Diagnostik, alles über eine einheitliche Schnittstelle.

Die Zahlen sprechen für sich: **276 MCP Tools über 57 Azure-Dienste**. Das ist umfangreiche Unterstützung.

## Das Wichtigste: Self-Hosted Remote Deployments

Hier ist die Sache. MCP lokal auf deiner Maschine zu betreiben ist okay für Entwicklung und Experimente. Aber in einem echten Team-Szenario brauchst du:

- Gemeinsamer Zugriff für Entwickler und interne Agent-Systeme
- Zentralisierte Konfiguration (Mandantenkontext, Abonnement-Standards, Telemetrie)
- Enterprise-Netzwerk- und Richtliniengrenzen
- Integration in CI/CD-Pipelines

Azure MCP Server 2.0 adressiert das alles. Du kannst es als zentral verwalteten internen Service mit HTTP-basiertem Transport, ordentlicher Authentifizierung und konsistenter Governance bereitstellen.

Für die Authentifizierung hast du zwei solide Optionen:

1. **Managed Identity** — wenn neben [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry) betrieben
2. **On-Behalf-Of (OBO) Flow** — OpenID Connect Delegation, die Azure APIs mit dem Kontext des angemeldeten Benutzers aufruft

Dieser OBO-Flow ist besonders interessant für uns .NET-Entwickler. Das bedeutet, dass deine Agentic Workflows mit den eigentlichen Berechtigungen des Benutzers arbeiten können, nicht mit einem überberechtigten Service-Account. Principle of Least Privilege, gleich eingebaut.

## Security Hardening

Das ist nicht nur ein Feature-Release — es ist auch eines für Sicherheit. Das 2.0-Release fügt hinzu:

- Stärkere Endpoint-Validierung
- Schutz gegen Injection-Muster in Query-orientierten Tools
- Strengere Isolationskontrollen für Dev-Umgebungen

Falls du MCP als gemeinsamen Service bereitstellen willst, zählen diese Schutzmaßnahmen. Eine Menge.

## Wo kannst du es verwenden?

Die Client-Kompatibilität ist breit. Azure MCP Server 2.0 funktioniert mit:

- **IDEs**: VS Code, Visual Studio, IntelliJ, Eclipse, Cursor
- **CLI Agents**: GitHub Copilot CLI, Claude Code
- **Standalone**: lokaler Server für einfache Setups
- **Self-Hosted Remote**: der neue Star von 2.0

Zusätzlich gibt es Sovereign Cloud Support für Azure US Government und Azure von 21Vianet betrieben, was für regulierte Deployments entscheidend ist.

## Warum das für .NET-Entwickler wichtig ist

Falls du Agentic Anwendungen mit .NET aufbaust — ob das Semantic Kernel, Microsoft Agent Framework oder deine eigene Orchestrierung ist — gibt dir Azure MCP Server 2.0 eine produktionsreife Möglichkeit, deinen Agenten mit Azure-Infrastruktur zu interagieren. Keine benutzerdefinierten REST-Wrapper. Keine Service-spezifischen Integrationsmuster. Einfach MCP.

Kombiniert mit der [Fluent API für MCP Apps](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/), die vor ein paar Tagen kam, reift das .NET MCP-Ökosystem schnell.

## Erste Schritte

Wähle deinen Weg:

- **[GitHub Repo](https://aka.ms/azmcp)** — Quellcode, Docs, alles
- **[Docker Image](https://aka.ms/azmcp/download/docker)** — containerisiertes Deployment
- **[VS Code Extension](https://aka.ms/azmcp/download/vscode)** — IDE-Integration
- **[Self-Hosting Guide](https://aka.ms/azmcp/self-host)** — das Flaggschiff-Feature von 2.0

## Zusammenfassung

Azure MCP Server 2.0 ist genau die Art von Infrastruktur-Upgrade, das in einer Demo nicht glamourös aussieht, aber in der Praxis alles verändert. Self-Hosted Remote MCP mit ordnungsgemäßer Authentifizierung, Security Hardening und Sovereign Cloud Support bedeutet, dass MCP bereit für echte Teams ist, die echte Agentic Workflows auf Azure aufbauen. Falls du auf das „Enterprise-Ready"-Signal gewartet hast — das ist es.
