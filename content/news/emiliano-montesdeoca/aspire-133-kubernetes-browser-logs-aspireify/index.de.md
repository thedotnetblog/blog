---
title: "Aspire 13.3: Kubernetes-Unterstützung, Browser-Logs und die Aspireify-Funktion"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "Fünf Wochen nach 13.2 erscheint Aspire 13.3 mit 45 neuen Features, darunter erstklassiges AKS-Deployment, eine KI-gestützte Onboarding-Funktion, Browser-Log-Erfassung und strukturierte Befehlsergebnisse."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

Fünf Wochen sind keine lange Zeit für ein Release, aber Aspire 13.3 fühlt sich nicht so an. Die Hauptpunkte sind bedeutsam: erstklassiges Kubernetes- und AKS-Deployment mit Helm, eine agentengestützte Onboarding-Funktion namens Aspireify, Browser-Log-Erfassung direkt im Dashboard und strukturierte Befehlsergebnisse. Dazu 45 neue Features, 134 Verbesserungen und 93 Fehlerbehebungen.

Kommen wir zu den Highlights.

## Aspireify: Agentengestütztes Onboarding

Aspire zu einem bestehenden Projekt hinzuzufügen klingt einfach — AppHost einfügen, fertig. In der Praxis erfordert es viel Recherche: welche Ports wichtig sind, welche Umgebungsvariablen echte Abhängigkeiten sind, welche Docker-Compose-Dienste zu Aspire-Integrationen zugeordnet werden sollen.

Die neue **Aspireify-Funktion** gibt Ihrem Coding-Agenten einen geführten Workflow genau dafür. Wenn `aspire init` einen Skelett-AppHost erstellt, hilft die Aspireify-Funktion dem Agenten, das Repository zu inspizieren, zu verstehen, wie es bereits funktioniert, und den AppHost so zu verdrahten, dass er zur App passt — nicht umgekehrt.

Die Standardhaltung ist "Änderungen an Ihrem Code minimieren." Wenn Ihre App bereits `DATABASE_URL` liest, mappt der Agent das mit `WithEnvironment()` anstatt Sie zu bitten, Ihre Konfiguration neu zu schreiben. Wenn ein Port fest codiert ist, teilt die Funktion dem Agenten mit, wann er ihn beibehalten soll.

Das ist die Art von KI-Tooling, die wirklich Zeit spart, anstatt mehr Arbeit zum Überprüfen zu generieren.

## Erstklassiges Kubernetes- und AKS-Deployment

Dies stand schon eine Weile auf der Wunschliste. Aspire 13.3 liefert **erstklassige Kubernetes- und AKS-Deployment-Unterstützung mit Helm**. Sie können jetzt AKS direkt aus den Aspire-Tools als Deployment-Ziel wählen.

Für Teams, die bereits Produktionsworkloads auf AKS betreiben, schließt dies eine bedeutende Lücke. Ihr Aspire-App-Modell hat jetzt einen sauberen Weg von der lokalen Entwicklung zu Kubernetes ohne manuelle Helm-Chart-Erstellung.

## Browser-Logs im Dashboard

Das ist eine jener Funktionen, die klein erscheinen, bis man ein Frontend-Problem debuggt.

Die neue `WithBrowserLogs()` API hängt eine verfolgte Browser-Ressource an jede endpoint-fähige Ressource an. Aspire startet Chromium mit einer privaten CDP-Pipe und streamt Konsolen-Logs, Netzwerkanfragen und Fehler direkt in den Ressourcen-Log-Stream:

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

Der TypeScript AppHost unterstützt dasselbe:

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

Konsolen-Fehler, fehlgeschlagene Netzwerkanfragen, clientseitige Ausnahmen — alles im selben Dashboard sichtbar, wo Sie bereits Traces und Metriken beobachten. Kein Tab-Wechsel zu Browser DevTools mehr für die Grundlagen.

## Strukturierte Befehlsergebnisse

Ressourcenbefehle haben ein bedeutsames Upgrade erhalten. Bisher gaben Befehle Erfolg/Misserfolg zurück. Jetzt geben sie strukturierte Ergebnisse zurück: Text, JSON oder Markdown, das durch das Modell, die Dashboard-Benutzeroberfläche, die CLI und die MCP-Tools fließt.

Das Dashboard verbindet all das mit einem neuen Benachrichtigungscenter im Header. Befehlsergebnisse erscheinen als zeitgestempelte Benachrichtigungen mit Markdown-Rendering und einer "Antwort anzeigen"-Aktion.

Das macht Ressourcenbefehle wirklich komposierbar. Eine Integration kann jetzt einen Befehl exponieren, der eine bedeutsame Ausgabe zurückgibt — wie eine Tunnel-URL — anstatt nur irgendwo den Zustand zu ändern.

## Fazit

Aspire 13.3 ist das Upgrade wert, allein schon für die Kubernetes-Unterstützung. Die Browser-Logs und strukturierten Befehlsergebnisse fühlen sich wie die Art von Verbesserungen der Lebensqualität an, die sich in einem alltäglichen Entwicklungsworkflow schnell ansammeln.

Vollständige Versionshinweise: [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
