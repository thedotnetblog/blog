---
title: 'Cosmos DB-Zugriff ohne Secrets ist die neue Baseline'
date: 2026-07-16
author: 'Emiliano Montesdeoca'
description: 'Wenn Ihre Cosmos DB-App immer noch von Schlüsseln abhängt, sind Sie bei der Betriebssicherheit bereits zurück.'
tags:
  - azure-cosmos-db
  - dotnet
  - managed-identity
  - rbac
  - cloud-security
---

Originalquelle: [Which Azure Cosmos DB Role Does My App Need?](https://devblogs.microsoft.com/cosmosdb/which-azure-cosmos-db-role-does-my-app-need/)

Die wichtigste Idee in dieser Cosmos DB-Anleitung ist nicht ein Befehl, eine Rollen-ID oder ein CLI-Trick. Sie ist architektonisch: **Hören Sie auf, Anmeldeinformationen als App-Konfiguration zu behandeln** und beginnen Sie, Identität als Laufzeitzustand zu betrachten.

Zu viele Teams liefern immer noch mit Verbindungszeichenfolgen aus, weil es sich schnell anfühlt. Es ist nicht schnell. Es ist aufgeschobenes Risiko. Jeder Schlüssel in einer Konfigurationsdatei wird zu einem Vorfall, der auf einen überstürzten Commit, eine kopierte Pipeline-Variable oder ein durchgesickertes Log wartet. Managed Identity plus Data-Plane-RBAC entfernt diese Fehlerklasse fast vollständig.

Die praktische Herausforderung ist die Verwirrung zwischen **Control-Plane-** und **Data-Plane-Autorisierung**. Hier verlieren viele sonst starke Teams Tage. Azure RBAC-Rollen auf Ressourcen gewähren nicht automatisch Dokumentenzugriff, und Cosmos-Data-Plane-Rollen gewähren keine Kontoverwaltung. Wenn Ihr Team diese Trennt nicht explizit in Ihren Runbooks dokumentiert, werden Sie weiterhin fragile Deployments und schwer zu debuggende 403s erhalten.

### Meine Meinung für Produktionsteams

- **Beginnen Sie mit Data Reader** für Lesepfade und Data Contributor nur, wo Schreibvorgänge wirklich erforderlich sind.
- **Weit eingrenzen nur**, wenn Sie eine einzige Anwendungsgrenze pro Konto haben.
- **Wenn Sie ein Konto über Dienste hinweg teilen**, grenzen Sie den Bereich früh auf Datenbank- oder Container-Grenzen ein, anstatt auf Audit-Druck zu warten.

Dies ist eine dieser Entscheidungen, die sich **verstärken**. Wenn Sie Ihre .NET-App mit `DefaultAzureCredential` und reiner Endpunkt-Konfiguration verdrahten, wird jede Umgebung sauberer: lokal, CI, Staging und Produktion. Sie machen auch die Incident-Reaktion schneller, weil Sie über Berechtigungen durch Rollenzuweisungen nachdenken können, anstatt mysteriöse Schlüssel zu jagen.

Wenn Sie nur eines aus diesem Beitrag übernehmen, machen Sie dies: **Entfernen Sie zuerst Secrets, optimieren Sie dann Rollen**. Teams, die diese Reihenfolge umkehren, bleiben normalerweise in Meetings stecken. Teams, die zuerst Secrets entfernen, liefern normalerweise aus und härten dann nach.