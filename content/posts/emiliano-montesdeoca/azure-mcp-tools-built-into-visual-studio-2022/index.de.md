---
title: "Azure MCP Tools sind jetzt in Visual Studio 2022 integriert — Keine Erweiterung erforderlich"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Azure MCP Tools werden als Teil der Azure-Entwicklungsworkload in Visual Studio 2022 ausgeliefert. Über 230 Tools, 45 Azure-Dienste, keine Erweiterungen zu installieren."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [hier klicken]({{< ref "azure-mcp-tools-built-into-visual-studio-2022.md" >}}).*

Wenn du die Azure MCP Tools in Visual Studio über die separate Erweiterung benutzt hast, kennst du das Spiel — VSIX installieren, neustarten, hoffen dass nichts kaputtgeht, Versionskonflikte managen. Diese Reibung ist vorbei.

Yun Jung Choi hat [angekündigt](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/), dass Azure MCP Tools jetzt direkt als Teil der Azure-Entwicklungsworkload in Visual Studio 2022 ausgeliefert werden. Keine Erweiterung. Kein VSIX. Kein Neustart-Tanz.

## Was das konkret bedeutet

Ab Visual Studio 2022 Version 17.14.30 ist der Azure MCP Server in der Azure-Entwicklungsworkload enthalten. Wenn du diese Workload bereits installiert hast, musst du ihn nur in GitHub Copilot Chat aktivieren und fertig.

Über 230 Tools für 45 Azure-Dienste — direkt aus dem Chat-Fenster zugänglich. Storage Accounts auflisten, eine ASP.NET Core App deployen, App Service Probleme diagnostizieren, Log Analytics abfragen — alles ohne einen Browser-Tab zu öffnen.

## Warum das wichtiger ist als es klingt

Die Sache mit Entwickler-Tooling ist: Jeder zusätzliche Schritt ist Reibung, und Reibung tötet die Akzeptanz. MCP als separate Erweiterung bedeutete Versionskonflikte, Installationsfehler und eine weitere Sache, die aktuell gehalten werden musste. Die Integration in die Workload bedeutet:

- **Ein einziger Update-Pfad** über den Visual Studio Installer
- **Kein Versionsabweichung** zwischen der Erweiterung und der IDE
- **Immer aktuell** — der MCP Server wird mit den regulären VS-Releases aktualisiert

Für Teams, die auf Azure standardisieren, ist das ein großer Gewinn. Du installierst die Workload einmal, aktivierst die Tools, und sie sind in jeder Sitzung verfügbar.

## Was du damit machen kannst

Die Tools decken den gesamten Entwicklungslebenszyklus über Copilot Chat ab:

- **Lernen** — frage nach Azure-Diensten, Best Practices, Architekturmustern
- **Entwerfen & Entwickeln** — erhalte Service-Empfehlungen, konfiguriere App-Code
- **Deployen** — provisioniere Ressourcen und deploye direkt aus der IDE
- **Fehlerbehebung** — frage Logs ab, prüfe den Ressourcenzustand, diagnostiziere Produktionsprobleme

Ein schnelles Beispiel — tippe das in Copilot Chat:

```
List my storage accounts in my current subscription.
```

Copilot ruft die Azure MCP Tools im Hintergrund auf, fragt deine Subscriptions ab und liefert eine formatierte Liste mit Namen, Standorten und SKUs. Kein Portal nötig.

## So aktivierst du es

1. Update auf Visual Studio 2022 **17.14.30** oder höher
2. Stelle sicher, dass die **Azure development** Workload installiert ist
3. Öffne GitHub Copilot Chat
4. Klicke auf den **Select tools** Button (das Schraubenschlüssel-Symbol)
5. Schalte **Azure MCP Server** ein

Das war's. Es bleibt über Sitzungen hinweg aktiviert.

## Ein Hinweis

Die Tools sind standardmäßig deaktiviert — du musst sie manuell einschalten. Und VS 2026-spezifische Tools sind in VS 2022 nicht verfügbar. Die Verfügbarkeit der Tools hängt auch von deinen Azure-Subscription-Berechtigungen ab, genau wie im Portal.

## Das große Bild

Das ist Teil eines klaren Trends: MCP wird zum Standard, um Cloud-Tools in Entwickler-IDEs verfügbar zu machen. Wir haben bereits das [stabile Release von Azure MCP Server 2.0](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) und MCP-Integrationen in VS Code und anderen Editoren gesehen. Die Integration in Visual Studios Workload-System ist die natürliche Weiterentwicklung.

Für uns .NET-Entwickler, die in Visual Studio leben, entfällt damit ein weiterer Grund, zum Azure Portal zu wechseln. Und ehrlich gesagt, je weniger Tab-Wechsel, desto besser.
