---
title: "Vom Laptop in die Produktion: KI-Agenten mit zwei Befehlen auf Microsoft Foundry deployen"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Das Azure Developer CLI hat jetzt 'azd ai agent'-Befehle, die deinen KI-Agenten in Minuten vom lokalen Entwicklungsrechner zu einem Live-Foundry-Endpoint bringen. Hier ist der komplette Workflow."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

Du kennst diese Lücke zwischen "es funktioniert auf meinem Rechner" und "es ist deployed und bedient Traffic"? Für KI-Agenten war diese Lücke schmerzhaft groß. Du musst Ressourcen bereitstellen, Modelle deployen, Identität einrichten, Monitoring aufsetzen — und das ist bevor jemand deinen Agenten überhaupt aufrufen kann.

Das Azure Developer CLI hat das gerade zu einer [Zwei-Befehle-Angelegenheit](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) gemacht.

## Der neue `azd ai agent` Workflow

Lass mich durchgehen, wie das tatsächlich aussieht. Du hast ein KI-Agenten-Projekt — sagen wir einen Hotel-Concierge-Agenten. Er funktioniert lokal. Du willst ihn auf Microsoft Foundry laufen lassen.

```bash
azd ai agent init
azd up
```

Das war's. Zwei Befehle. `azd ai agent init` generiert die Infrastructure-as-Code in deinem Repo, und `azd up` provisioniert alles auf Azure und veröffentlicht deinen Agenten. Du bekommst einen direkten Link zu deinem Agenten im Foundry-Portal.

## Was unter der Haube passiert

Der `init`-Befehl generiert echte, inspizierbare Bicep-Templates in deinem Repo:

- Eine **Foundry Resource** (Top-Level-Container)
- Ein **Foundry Project** (wo dein Agent lebt)
- **Modell-Deployment**-Konfiguration (GPT-4o, etc.)
- **Managed Identity** mit korrekten RBAC-Rollenzuweisungen
- `azure.yaml` für die Service-Map
- `agent.yaml` mit Agent-Metadaten und Umgebungsvariablen

Hier der entscheidende Punkt: all das gehört dir. Es ist versioniertes Bicep in deinem Repo. Du kannst es inspizieren, anpassen und zusammen mit deinem Agenten-Code committen. Keine magischen Black Boxes.

## Die innere Entwicklungsschleife

Was mir wirklich gefällt, ist die lokale Entwicklungsgeschichte. Wenn du an der Agenten-Logik iterierst, willst du nicht bei jeder Prompt-Änderung neu deployen:

```bash
azd ai agent run
```

Das startet deinen Agenten lokal. Kombiniere es mit `azd ai agent invoke` um Test-Prompts zu senden, und du hast eine enge Feedback-Schleife. Code bearbeiten, neu starten, aufrufen, wiederholen.

Der `invoke`-Befehl ist auch clever beim Routing — wenn ein lokaler Agent läuft, zielt er automatisch darauf. Wenn nicht, geht er an den Remote-Endpoint.

## Echtzeit-Monitoring

Das ist die Funktion, die mich überzeugt hat. Sobald dein Agent deployed ist:

```bash
azd ai agent monitor --follow
```

Jede Anfrage und Antwort, die durch deinen Agenten fließt, wird in Echtzeit in dein Terminal gestreamt. Für das Debugging von Produktionsproblemen ist das unbezahlbar. Kein Durchsuchen von Log Analytics, kein Warten auf Metrik-Aggregation — du siehst, was gerade passiert.

## Der komplette Befehlssatz

Hier die Kurzreferenz:

| Befehl | Was er tut |
|--------|-----------|
| `azd ai agent init` | Scaffolding eines Foundry-Agent-Projekts mit IaC |
| `azd up` | Azure-Ressourcen bereitstellen und Agent deployen |
| `azd ai agent invoke` | Prompts an den Remote- oder lokalen Agent senden |
| `azd ai agent run` | Agent lokal für Entwicklung ausführen |
| `azd ai agent monitor` | Echtzeit-Logs vom veröffentlichten Agent streamen |
| `azd ai agent show` | Agent-Gesundheit und -Status prüfen |
| `azd down` | Alle Azure-Ressourcen aufräumen |

## Warum das für .NET-Entwickler wichtig ist

Auch wenn das Beispiel in der Ankündigung Python-basiert ist, ist die Infrastruktur-Geschichte sprachunabhängig. Dein .NET-Agent bekommt das gleiche Bicep-Scaffolding, das gleiche Managed-Identity-Setup, die gleiche Monitoring-Pipeline. Und wenn du `azd` bereits für deine .NET Aspire-Apps oder Azure-Deployments nutzt, passt das direkt in deinen bestehenden Workflow.

Die Deployment-Lücke für KI-Agenten war einer der größten Reibungspunkte im Ökosystem. Von einem funktionierenden Prototyp zu einem Produktions-Endpoint mit korrekter Identität, Networking und Monitoring zu kommen, sollte keine Woche DevOps-Arbeit erfordern. Jetzt braucht es zwei Befehle und ein paar Minuten.

## Zusammenfassung

`azd ai agent` ist jetzt verfügbar. Wenn du das Deployment deiner KI-Agenten aufgeschoben hast, weil das Infrastruktur-Setup nach zu viel Arbeit aussah, probier es aus. Schau dir den [vollständigen Walkthrough](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) für die komplette Schritt-für-Schritt-Anleitung inklusive Frontend-Chat-App-Integration an.
