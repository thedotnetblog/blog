---
title: "Ihr KI-Agent Hat ein Identitätsproblem (Und Hier ist die Vorlage, die Es Löst)"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Eine neue azd-Vorlage von Curity und Microsoft zeigt, wie man KI-Agenten erstellt, die kurzlebige OAuth-Token mit feingranularen Scopes verwenden — damit Agenten niemals Daten sehen können, die sie nicht sehen sollten."
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

Es gibt einen Moment in jedem KI-Agenten-Projekt, der ungefähr so läuft: Die Demo funktioniert perfekt, der Agent interpretiert natürliche Sprache, ruft die richtigen APIs auf, gibt die richtigen Daten zurück. Dann fangen Sie an, über echte Benutzer nachzudenken.

Was hindert die Agenten-Session eines Benutzers daran, die Daten eines anderen Benutzers zu sehen? Was passiert, wenn der Agent durch Prompt-Injektion ausgetrickst wird? Was passiert, wenn er ein Tool auf unerwartete Weise aufruft?

Das sind keine Randfälle. Das sind Designentscheidungen, die Sie vor dem Deployment treffen müssen.

Eine neue `azd`-Vorlage von Curity und Microsoft gibt Ihnen eine funktionsfähige Referenz für genau dieses Problem.

## Das Kernproblem: Authentifizierung ≠ Autorisierung

Die meisten Agenten-Beispiele behandeln die Benutzerauthentifizierung gut. Sie behandeln die Autorisierung schlecht. Zu wissen, *wer* der Benutzer ist, sagt Ihnen nicht, *welche Daten* er sehen sollte.

Eine traditionelle Client-Anwendung macht vorhersehbare API-Aufrufe. Ein KI-Agent ist nicht-deterministisch — er interpretiert natürliche Sprache und entscheidet, was er aufruft. Er kann kreativ sein. Er kann auch falsch liegen. Und wenn er durch Prompt-Injektion manipuliert wird, brauchen Sie Regeln, die nicht davon abhängen, dass die KI sich gut verhält.

Die Lösung, die diese Vorlage demonstriert: **Kurzlebige Token, die genau die richtigen Informationen für jeden Hop tragen**.

## Wie die Token-Kette Funktioniert

Die Vorlage verwendet OAuth 2.0-Zugriffstoken mit Token-Austausch, um Berechtigungen bei jedem Schritt einzuschränken. Ein Benutzer-Token wird zweimal ausgetauscht, bevor es den MCP-Server erreicht:

1. **Erster Austausch** — schränkt den Scope ein und konvertiert das opake Token in ein JWT
2. **Zweiter Austausch** — fügt die Agenten-Identität und eine neue Zielgruppe für den MCP-Server-Hop hinzu

So sieht das MCP-Server-Token aus:

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

Die `customer_id` ist vom Autorisierungsserver in das Token eingebettet, nicht als Parameter übergeben, den der Agent kontrolliert. Die API prüft das Token, nicht die Anweisungen des Agenten.

Das bedeutet: Selbst wenn jemand den Agenten dazu verleitet, die Daten eines anderen Kunden abzurufen, wird das Token dies nicht autorisieren.

## Was die Vorlage Deployt

Mit ein paar `azd`-Befehlen erhalten Sie:

- Einen Backend-Agenten auf Microsoft Foundry (C#, Microsoft A2A und MCP SDKs)
- Einen MCP-Server, der eine Beispiel-Portfolio-API exponiert
- Curity Identity Server als Autorisierungsserver, zusammen mit Entra ID für die Authentifizierung
- Externe und interne API-Gateways, die Token-Austausch und Audit-Logging verwalten
- Bicep für die gesamte Azure-Infrastruktur: Container Apps, VNet, ACR, Azure AI Foundry, Key Vault, Azure SQL Database, Speicher

Das gesamte Muster ist inspizierbar und anpassbar.

## Das Designprinzip, das Es Wert Ist, Übernommen zu Werden

Auch wenn Sie Curity nicht verwenden, ist das Muster übertragbar: **Agenten sollten niemals permanenten API-Zugriff haben**. Jede Aktion sollte ein kurzlebiges Token mit dem minimalen Scope verwenden, der für diesen spezifischen Aufruf benötigt wird, ausgestellt für die spezifische Agenten-Identität, mit den Claims, die die API benötigt, um Autorisierungsentscheidungen zu treffen.

Das hält gegen kreative Agenten, Fehler und Prompt-Injektion stand, wie es "Stellen Sie einfach sicher, dass der Agent keine schlechten Dinge tut" niemals tun wird.

## Fazit

Sicherheitsmuster für KI-Agenten werden in der Industrie noch ausgearbeitet. Diese Vorlage ist eine der vollständigsten Referenzimplementierungen, die ich gesehen habe — sie deckt den tatsächlichen Autorisierungsfluss ab, nicht nur die Authentifizierung.

Originalbeitrag: [Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
