---
title: "SQL MCP Server — Der richtige Weg, AI-Agenten Datenbankzugriff zu geben"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "SQL MCP Server von Data API builder gibt AI-Agenten sicheren, deterministischen Datenbankzugriff, ohne Schemas zu exponieren oder auf NL2SQL zu setzen. RBAC, Caching, Multi-Datenbank-Unterstützung — alles integriert."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "sql-mcp-server-data-api-builder.md" >}}).*

Seien wir ehrlich: Die meisten heute verfügbaren Datenbank-MCP-Server sind beängstigend. Sie nehmen eine natürlichsprachliche Abfrage, generieren SQL im laufenden Betrieb und führen es gegen Ihre Produktionsdaten aus. Was könnte schiefgehen? (Alles. Alles könnte schiefgehen.)

Das Azure SQL-Team hat gerade den [SQL MCP Server vorgestellt](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/), und er verfolgt einen grundlegend anderen Ansatz. Als Feature von Data API builder (DAB) 2.0 gebaut, gibt er AI-Agenten strukturierten, deterministischen Zugriff auf Datenbankoperationen — ohne NL2SQL, ohne Schema-Exposition und mit vollständigem RBAC bei jedem Schritt.

## Warum kein NL2SQL?

Das ist die interessanteste Design-Entscheidung. Modelle sind nicht deterministisch, und komplexe Abfragen produzieren am wahrscheinlichsten subtile Fehler. Genau die Abfragen, von denen Benutzer hoffen, dass AI sie generieren kann, sind auch diejenigen, die die meiste Prüfung erfordern, wenn sie nicht-deterministisch erzeugt werden.

Stattdessen verwendet SQL MCP Server einen **NL2DAB**-Ansatz. Der Agent arbeitet mit der Entitäts-Abstraktionsschicht von Data API builder und dem integrierten Query Builder, um akkurates, wohlgeformtes T-SQL deterministisch zu produzieren. Gleiches Ergebnis für den Benutzer, aber ohne das Risiko halluzinierter JOINs oder versehentlicher Datenexposition.

## Sieben Tools, nicht siebenhundert

SQL MCP Server exponiert genau sieben DML-Tools, unabhängig von der Datenbankgröße:

- `describe_entities` — verfügbare Entitäten und Operationen entdecken
- `create_record` — Zeilen einfügen
- `read_records` — Tabellen und Views abfragen
- `update_record` — Zeilen ändern
- `delete_record` — Zeilen entfernen
- `execute_entity` — gespeicherte Prozeduren ausführen
- `aggregate_records` — Aggregationsabfragen

Das ist clever, weil Context Windows der Denkraum des Agenten sind. Sie mit Hunderten von Tool-Definitionen zu überfluten lässt weniger Raum für das Denken. Sieben feste Tools halten den Agenten auf *Denken* statt *Navigieren* fokussiert.

Jedes Tool kann einzeln aktiviert oder deaktiviert werden:

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## In drei Befehlen starten

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

Das ist ein laufender SQL MCP Server, der Ihre Customers-Tabelle exponiert. Die Entitäts-Abstraktionsschicht bedeutet, dass Sie Namen und Spalten aliasieren, Felder pro Rolle beschränken und genau kontrollieren können, was Agenten sehen — ohne interne Schema-Details preiszugeben.

## Die Sicherheitsgeschichte überzeugt

Hier zahlt sich die Reife von Data API builder aus:

- **RBAC auf jeder Ebene** — jede Entität definiert, welche Rollen lesen, erstellen, aktualisieren oder löschen können, und welche Felder sichtbar sind
- **Azure Key Vault-Integration** — Connection Strings und Secrets sicher verwaltet
- **Microsoft Entra + Custom OAuth** — Authentifizierung auf Produktionsniveau
- **Content Security Policy** — Agenten interagieren über einen kontrollierten Vertrag, nicht über rohes SQL

Die Schema-Abstraktion ist besonders wichtig. Ihre internen Tabellen- und Spaltennamen werden niemals dem Agenten exponiert. Sie definieren Entitäten, Aliase und Beschreibungen, die für die AI-Interaktion sinnvoll sind — nicht Ihr Datenbank-ERD.

## Multi-Datenbank und Multi-Protokoll

SQL MCP Server unterstützt Microsoft SQL, PostgreSQL, Azure Cosmos DB und MySQL. Und da es ein DAB-Feature ist, bekommen Sie REST-, GraphQL- und MCP-Endpoints gleichzeitig aus derselben Konfiguration. Gleiche Entitätsdefinitionen, gleiche RBAC-Regeln, gleiche Sicherheit — über alle drei Protokolle.

Die Auto-Konfiguration in DAB 2.0 kann sogar Ihre Datenbank inspizieren und die Konfiguration dynamisch aufbauen, wenn Sie für schnelles Prototyping mit weniger Abstraktion arbeiten möchten.

## Meine Einschätzung

So sollte Enterprise-Datenbankzugriff für AI-Agenten funktionieren. Nicht „Hey LLM, schreib mir SQL und YOLO es gegen Produktion." Stattdessen: eine wohldefinierte Entitätsschicht, deterministische Abfragegenerierung, RBAC bei jedem Schritt, Caching, Monitoring und Telemetrie. Es ist langweilig auf die bestmögliche Art.

Für .NET-Entwickler ist die Integrationsgeschichte sauber — DAB ist ein .NET-Tool, der MCP Server läuft als Container, und er funktioniert mit Azure SQL, das die meisten von uns bereits verwenden. Wenn Sie AI-Agenten bauen, die Datenzugriff brauchen, starten Sie hier.

## Zusammenfassung

SQL MCP Server ist kostenlos, Open Source und läuft überall. Es ist der präskriptive Ansatz von Microsoft, um AI-Agenten sicheren Datenbankzugriff zu geben. Lesen Sie den [vollständigen Beitrag](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) und die [Dokumentation](https://aka.ms/sql/mcp) für den Einstieg.
