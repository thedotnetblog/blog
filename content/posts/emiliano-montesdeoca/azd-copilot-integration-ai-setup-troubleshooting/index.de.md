---
title: "azd + GitHub Copilot: KI-gestütztes Projekt-Setup und intelligente Fehlerbehandlung"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Die Azure Developer CLI integriert sich jetzt mit GitHub Copilot, um dein Projekt zu scaffolden und Deployment-Fehler zu beheben — alles ohne das Terminal zu verlassen."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *Dieser Beitrag wurde automatisch übersetzt. Die englische Originalversion findest du [hier]({{< ref "index.md" >}}).*

Du kennst diesen Moment, wenn du eine bestehende App in Azure deployen möchtest und plötzlich auf eine leere `azure.yaml` starrst und versuchst zu erinnern, ob deine Express-API Container Apps oder App Service verwenden sollte? Genau dieser Moment wird jetzt deutlich kürzer.

Die Azure Developer CLI (`azd`) integriert sich jetzt mit GitHub Copilot auf zwei sinnvolle Arten: KI-gestütztes Projekt-Scaffolding während `azd init` und intelligente Fehlerbehebung, wenn Deployments schiefgehen. Beide Funktionen bleiben vollständig im Terminal — genau dort, wo ich sie haben möchte.

## Setup mit Copilot während azd init

Wenn du `azd init` ausführst, gibt es jetzt die Option "Set up with GitHub Copilot (Preview)". Wähle sie aus, und Copilot analysiert deine Codebasis, um die `azure.yaml`, Infrastruktur-Templates und Bicep-Module zu generieren — basierend auf deinem tatsächlichen Code.

```
azd init
# Wähle: "Set up with GitHub Copilot (Preview)"
```

Voraussetzungen:

- **azd 1.23.11 oder neuer** — prüfe mit `azd version` oder aktualisiere mit `azd update`
- **Aktives GitHub Copilot-Abonnement** (Individual, Business oder Enterprise)
- **GitHub CLI (`gh`)** — `azd` fragt bei Bedarf nach dem Login

Was ich dabei wirklich nützlich finde: Es funktioniert in beide Richtungen. Baust du von Grund auf neu? Copilot hilft dir, von Anfang an die richtigen Azure-Services einzurichten. Hast du eine bestehende App, die du schon länger deployen wolltest? Zeig Copilot auf sie, und er generiert die Konfiguration, ohne dass du irgendetwas umstrukturieren musst.

### Was es wirklich macht

Angenommen, du hast eine Node.js Express-API mit PostgreSQL-Abhängigkeit. Statt manuell zwischen Container Apps und App Service zu entscheiden und dann Bicep von Grund auf zu schreiben, erkennt Copilot deinen Stack und generiert:

- Eine `azure.yaml` mit den richtigen `language`-, `host`- und `build`-Einstellungen
- Ein Bicep-Modul für Azure Container Apps
- Ein Bicep-Modul für Azure Database for PostgreSQL

Vor jeder Änderung werden Vorab-Prüfungen durchgeführt — das Git-Arbeitsverzeichnis wird auf Sauberkeit geprüft, und MCP-Server-Tool-Zustimmung wird im Voraus eingeholt. Nichts passiert, ohne dass du genau weißt, was sich ändert.

## Copilot-gestützte Fehlerbehebung

Deployment-Fehler sind unvermeidlich. Fehlende Parameter, Berechtigungsprobleme, SKU-Verfügbarkeitsprobleme — und die Fehlermeldung sagt dir selten das eine, was du wirklich wissen musst: *wie du es behebst*.

Ohne Copilot sieht die Schleife so aus: Fehler kopieren → Docs durchsuchen → drei irrelevante Stack-Overflow-Antworten lesen → einige `az`-CLI-Befehle ausführen → nochmal versuchen und hoffen. Mit Copilot, der in `azd` integriert ist, kollabiert diese Schleife. Wenn ein `azd`-Befehl fehlschlägt, bietet er sofort vier Optionen an:

- **Explain** — Klartextbeschreibung, was schiefgelaufen ist
- **Guidance** — Schritt-für-Schritt-Anweisungen zur Behebung
- **Diagnose and Guide** — vollständige Analyse + Copilot wendet die Lösung an (mit deiner Genehmigung) + optionaler Retry
- **Skip** — selbst lösen

Das Entscheidende: Copilot hat bereits Kontext über dein Projekt, den fehlgeschlagenen Befehl und die Fehlerausgabe. Seine Vorschläge sind spezifisch für *deine Situation*, keine generischen Docs.

### Typische Fehler, bei denen das glänzt

**Ressourcenanbieter nicht registriert:**
```
ERROR: deployment failed: MissingSubscriptionRegistration:
The subscription is not registered to use namespace 'Microsoft.App'.
```
Das trifft jeden bei einem ersten Deployment in einem neuen Abonnement. Copilot kann den Provider registrieren und das Deployment automatisch neu starten.

**SKU nicht verfügbar:**
```
ERROR: deployment failed: SkuNotAvailable:
The requested VM size 'Standard_D2s_v3' is not available in location 'westus'.
```
Copilot erklärt, welche VM-Größe oder Region blockiert ist, und schlägt verfügbare Alternativen vor.

**Speicherkontoname bereits vergeben:**
```
ERROR: deployment failed: StorageAccountAlreadyTaken:
The storage account named 'myappstorage' is already taken.
```
Globale Eindeutigkeit erwischt jeden mindestens einmal. Copilot schlägt vor, deinen Umgebungsnamen oder ein zufälliges Suffix zu deinen Bicep-Parametern hinzuzufügen.

### Standardverhalten konfigurieren

Wenn du immer die gleiche Option willst, überspringe den interaktiven Prompt:

```
azd config set copilot.errorHandling.category troubleshoot
```

Werte: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. Du kannst auch Auto-Fix und Retry aktivieren:

```
azd config set copilot.errorHandling.fix allow
```

Zurück zum interaktiven Modus jederzeit:

```
azd config unset copilot.errorHandling.category
```

## Fazit

Das ist genau die Art von Copilot-Integration, die echten Mehrwert bringt. Probiere es aus, indem du `azd update` für die neueste Version ausführst, und verwende dann `azd init` für dein nächstes Projekt.

Den [originalen Ankündigungsbeitrag findest du hier](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
