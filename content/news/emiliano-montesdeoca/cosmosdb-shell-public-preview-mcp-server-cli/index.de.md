---
title: "Cosmos DB Shell Ist in der Öffentlichen Vorschau — Und Es Hat einen Integrierten MCP-Server"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell ist ein neues Open-Source-CLI, das Datenbankbefehle als MCP-Tools bereitstellt. Ihre KI-Agenten können Container navigieren, Abfragen ausführen und Daten verwalten, indem sie dieselbe Schnittstelle verwenden, die Sie benutzen."
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

Wenn Sie jemals zwischen einem Portal-Tab, einem SDK-Beispiel und einem halbfertigen Skript hin- und herspringen mussten, nur um eine Cosmos DB-Frage zu beantworten, kennen Sie bereits die Reibung, die dieses Projekt zu beseitigen versucht.

Azure Cosmos DB Shell ist gerade in die öffentliche Vorschau gestartet. Es ist ein Open-Source-CLI mit bash-ähnlicher Syntax und — der Teil, der es interessant macht — einem integrierten MCP-Server.

## Was Es von Anderen Datenbank-CLIs Unterscheidet

Das CLI selbst ist nützlich: vertraute Befehle, Skript-Unterstützung, CI/CD-Integration. Dieser Teil ist das Mindestmaß für ein entwicklerorientiertes Datenbank-Tool.

Der interessante Teil ist die MCP-Server-Integration. Jeder Befehl, den das CLI bereitstellt, wird als MCP-Tool verfügbar, das Ihre KI-Agenten aufrufen können. Es gibt keine benutzerdefinierte API-Schicht, keinen Integrationscode zu schreiben. Ihr Agent kann:

- Datenbankhierarchien mit `cd`, `ls`, `pwd` navigieren
- SQL-Abfragen mit `query` ausführen und strukturierte Ergebnisse zurückbekommen
- Elemente mit `create item`, `update`, `rm` erstellen und ändern
- Datenbanken und Container mit `mkdb`, `mkcon`, `rmdb`, `rmcon` verwalten
- Den aktuellen Kontext mit `endpoint`, `pwd` inspizieren

Die wichtigste Verschiebung: Ihr Agent spricht nicht mit einer Cosmos DB-API — er spricht mit derselben Shell-Schnittstelle, die Sie verwenden. Die Befehle sind deterministisch, prüfbar und Open Source, sodass Sie genau sehen können, was passiert.

## Die Open-Source-Grundlage Ist Wichtig

Dies ist kein verwalteter Black-Box-Dienst. Die Shell ist Open Source, was bedeutet:

- Sicherheitsteams können die Implementierung prüfen
- Plattformteams können sie forken und für ihre spezifischen Standards erweitern
- Entwickler können Verbesserungen beitragen, die allen zugutekommen

Für Unternehmens-Teams, die KI-Tools einsetzen, ist "können wir genau sehen, wie es funktioniert" zunehmend keine optionale Anforderung. Open Source ist hier ein bedeutsames Unterscheidungsmerkmal.

## Drei Szenarien, Die Einfacher Werden

**Intelligente Datenanalyse** — verbinden Sie einen Agenten mit der Shell, stellen Sie Fragen in natürlicher Sprache, erhalten Sie strukturierte Abfrageergebnisse. Der Agent übernimmt die Abfragekonstruktion; die Shell übernimmt die Ausführung.

**Autonomes Datenmanagement** — Workflows, die Daten in Cosmos DB erstellen, aktualisieren oder entfernen müssen, können dies über die MCP-Tools tun, ohne eine benutzerdefinierte Integration zu benötigen.

**Echtzeit-Überwachung und Warnungen** — ein Agent kann Container periodisch abfragen, Ergebnisse vergleichen und Anomalien über den passenden Benachrichtigungskanal melden.

Die MCP-Schnittstelle macht diese Szenarien mit jeder KI-Plattform, die MCP spricht, kombinierbar — nicht nur mit Microsofts Tools.

## Erste Schritte

Die Shell ist in der öffentlichen Vorschau. Installieren Sie sie, konfigurieren Sie Ihre Cosmos DB-Verbindung und aktivieren Sie den MCP-Server. Von dort aus kann jeder MCP-kompatible Agent-Host die Tools entdecken und verwenden.

Originalbeitrag: [Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
