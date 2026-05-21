---
title: "Die MSSQL-Erweiterung für VS Code wird still und leise zu einer viel größeren Plattform"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "Das neueste Update der MSSQL-Erweiterung bringt Azure-SQL-Provisioning, von Copilot unterstütztes Schema-Design, Data API Builder und Notebooks. Das Spannende ist, wie viel Datenbankarbeit jetzt in VS Code bleiben kann."
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

Die MSSQL-Erweiterung für VS Code wächst schon seit einer Weile, aber dieses neueste Update macht die Richtung viel klarer.

Es ist nicht mehr nur „verbinden und ein paar Abfragen ausführen“.

Mit **Azure-SQL-Provisioning**, **Schema Designer mit Copilot**, **SQL Notebooks** und **Data API Builder**, die alle in einem Release vorangebracht werden, entwickelt sich die Erweiterung zu einer deutlich vollständigeren Arbeitsumgebung für datenbankzentrierte Entwicklung.

## Der praktische Haken ist das Provisioning direkt aus dem Editor

Der Quellbeitrag sagt, dass man jetzt eine vollständig verwaltete Cloud-Datenbank „direkt aus dem Editor und ohne Kosten“ über die Free-Tier erstellen kann.

Das ist die Art von Funktion, die klein klingt, bis man merkt, wie viel Einrichtungsaufwand sie entfernt.

Für viele Entwickler liegt der nervige Teil datenintensiver Experimente nicht in SQL selbst. Es ist die Umgebungslücke zwischen:

- Idee
- Datenbank
- Schema
- API
- testbarem Backend

Wenn diese Lücke in einem einzigen Tool kleiner wird, wird der ganze Workflow attraktiver.

## So sieht ein stärkerer inner loop für Datenarbeit aus

Was ich an diesem Release mag, ist, dass es mehr vom Datenbank-Workflow an einem Ort hält:

- Datenbank provisionieren
- Schema entwerfen
- Änderungen überprüfen
- ORM-Skripte erzeugen
- APIs bereitstellen
- Endpunkte testen
- per Notebooks dokumentieren und abfragen

Das ist eine wesentlich überzeugendere Geschichte, als SQL als getrenntes Nebentool im Stack zu behandeln.

## Der von Copilot unterstützte Schema-Workflow ist der Punkt, an dem sich der KI-Wert echt anfühlt

Die Ergänzungen im Schema-Designer sind besonders interessant, weil sie einen guten Mittelweg zu treffen scheinen.

Der Wert ist nicht „KI entwirft dein Datenmodell und du vertraust blind darauf“.

Der Wert ist:

- schnellere Startpunkte
- visuelle Prüfung
- Änderungsverfolgung
- migrationsorientierte Ausgabe
- explizite Akzeptieren/Rückgängig-Optionen

Das ist ein deutlich gesünderer KI-Workflow als vollständige Auto-Generierung ohne Prüfmöglichkeit.

Und bei Datenbankarbeit ist Nachvollziehbarkeit enorm wichtig.

## Data API Builder ist ein stiller Verstärker

Die andere Funktion, die ich nicht übersehen würde, ist die Integration von Data API Builder.

Wenn du vom Schema zu Folgendem kommen kannst:

- REST
- GraphQL
- MCP-Endpunkten

und zwar innerhalb derselben Umgebung, dann schafft das einen sehr effizienten Weg für Backend-Prototypen und interne Tools.

Das ersetzt keine tiefere Backend-Entwicklung. Aber es verkürzt den Weg von der Datenbankidee zur funktionierenden Oberfläche erheblich.

## Meine Einschätzung

Dieses Release lässt die MSSQL-Erweiterung eher wie eine kleine Plattform innerhalb von VS Code wirken als wie ein einfaches Add-on.

Für Entwickler, die APIs, Datentools, Admin-Tools oder SQL-gestützte Prototypen bauen, ist das eine bedeutende Verschiebung.

Und wenn Microsoft diesen Loop weiter verdichtet, wird die Erweiterung viel strategisch nützlicher, als viele Leute heute noch annehmen.

Originalbeitrag: [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)