---
title: "Azure DevOps MCP Server landet in Microsoft Foundry: Was das für deine KI-Agenten bedeutet"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Der Azure DevOps MCP Server ist jetzt in Microsoft Foundry verfügbar. Verbinde deine KI-Agenten direkt mit DevOps-Workflows — Work Items, Repos, Pipelines — mit wenigen Klicks."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

MCP (Model Context Protocol) hat gerade seinen Moment. Wenn du das KI-Agenten-Ökosystem verfolgst, hast du wahrscheinlich bemerkt, dass MCP-Server überall auftauchen — sie geben Agenten die Fähigkeit, über ein standardisiertes Protokoll mit externen Tools und Diensten zu interagieren.

Jetzt ist der [Azure DevOps MCP Server in Microsoft Foundry verfügbar](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), und das ist eine dieser Integrationen, die einen über die praktischen Möglichkeiten nachdenken lässt.

## Was hier tatsächlich passiert

Microsoft hat den Azure DevOps MCP Server bereits als [Public Preview](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview) veröffentlicht — das ist der MCP-Server selbst. Neu ist die Foundry-Integration. Du kannst den Azure DevOps MCP Server jetzt direkt aus dem Tool-Katalog zu deinen Foundry-Agenten hinzufügen.

Für diejenigen, die Foundry noch nicht kennen: Es ist Microsofts einheitliche Plattform zum Erstellen und Verwalten von KI-gestützten Anwendungen und Agenten im großen Maßstab. Modellzugriff, Orchestrierung, Evaluierung, Deployment — alles an einem Ort.

## Die Einrichtung

Die Einrichtung ist überraschend unkompliziert:

1. Gehe in deinem Foundry-Agenten zu **Add Tools** > **Catalog**
2. Suche nach "Azure DevOps"
3. Wähle den Azure DevOps MCP Server (Preview) und klicke auf **Create**
4. Gib deinen Organisationsnamen ein und verbinde

Das war's. Dein Agent hat jetzt Zugriff auf Azure DevOps-Tools.

## Kontrollieren, worauf dein Agent zugreifen kann

Das ist der Teil, den ich schätze: Du bist nicht auf einen Alles-oder-Nichts-Ansatz festgelegt. Du kannst festlegen, welche Tools deinem Agenten zur Verfügung stehen. Wenn du also willst, dass er nur Work Items lesen, aber keine Pipelines anfassen darf, kannst du das konfigurieren. Prinzip der minimalen Berechtigung, angewandt auf deine KI-Agenten.

Das ist wichtig für Enterprise-Szenarien, in denen du nicht willst, dass ein Agent versehentlich eine Deployment-Pipeline auslöst, weil jemand ihn gebeten hat, "beim Release zu helfen."

## Warum das für .NET-Teams interessant ist

Denk darüber nach, was das in der Praxis ermöglicht:

- **Sprint-Planungsassistenten** — Agenten, die Work Items abrufen, Velocity-Daten analysieren und Sprint-Kapazität vorschlagen können
- **Code-Review-Bots** — Agenten, die deinen PR-Kontext verstehen, weil sie tatsächlich deine Repos und verknüpften Work Items lesen können
- **Incident Response** — Agenten, die Work Items erstellen, kürzliche Deployments abfragen und Bugs mit kürzlichen Änderungen korrelieren können
- **Entwickler-Onboarding** — "Woran sollte ich arbeiten?" bekommt eine echte Antwort, gestützt auf tatsächliche Projektdaten

Für .NET-Teams, die Azure DevOps bereits für ihre CI/CD-Pipelines und Projektverwaltung nutzen, ist ein KI-Agent, der direkt mit diesen Systemen interagieren kann, ein bedeutender Schritt in Richtung nützlicher Automatisierung.

## Das größere MCP-Bild

Das ist Teil eines breiteren Trends: MCP-Server werden zum Standard, wie KI-Agenten mit der Außenwelt interagieren. Wir sehen sie für GitHub, Azure DevOps, Datenbanken, SaaS-APIs — und Foundry wird zum Hub, wo all diese Verbindungen zusammenkommen.

Wenn du Agenten im .NET-Ökosystem baust, lohnt es sich, MCP im Auge zu behalten. Das Protokoll ist standardisiert, das Tooling reift heran, und die Foundry-Integration macht es zugänglich, ohne Server-Verbindungen manuell einrichten zu müssen.

## Zusammenfassung

Der Azure DevOps MCP Server in Foundry ist in der Preview, also rechne damit, dass er sich weiterentwickelt. Aber der Kern-Workflow ist solide: verbinden, Tool-Zugriff konfigurieren und deine Agenten mit deinen DevOps-Daten arbeiten lassen. Wenn du bereits im Foundry-Ökosystem bist, ist das nur ein paar Klicks entfernt. Probier es aus und schau, welche Workflows du bauen kannst.

Schau dir die [vollständige Ankündigung](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) für die Schritt-für-Schritt-Einrichtung und weitere Details an.
