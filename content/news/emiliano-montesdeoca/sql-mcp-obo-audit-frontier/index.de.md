---
title: "Die wahre Grenze für agentisches SQL: Prüfbarkeit mit OBO im SQL MCP Server"
date: 2026-07-22
author: Emiliano Montesdeoca
description: "On-Behalf-Of-Authentifizierung in Data API builder plus SQL MCP Server ist ein bedeutender Governance-Meilenstein, weil Azure SQL endlich den Menschen hinter einer Agentenaktion prüfen kann."
tags:
  - Azure SQL
  - SQL MCP Server
  - Agentic AI
  - Security
  - Microsoft Entra ID
  - Data API Builder
---

Es gibt eine schmerzhafte Wahrheit in Enterprise-KI-Projekten: Viele Teams besessen von Modellqualität und ignorieren Verantwortlichkeit. Wenn ein Agent Produktionsdaten schreibt oder liest, ist die erste Incident-Review-Frage nicht "war die Antwort gut?" Es ist "wer hat das tatsächlich getan?"

Originalquelle: https://devblogs.microsoft.com/azure-sql/sql-mcp-server-obo-auth/

Deshalb ist OBO-Unterstützung in Data API builder 2.0 mit SQL MCP Server eine größere Sache, als es zunächst scheint. Benutzername/Passwort- und Managed Identity-Ansätze funktionieren operativ noch, aber beide kollabieren Identität in die Dienstgrenze. Logs zeigen die App oder Middleware, nicht den menschlichen Anforderungsursprung. Das ist für einfache Automatisierung akzeptabel. Es ist nicht akzeptabel für regulierte agentische Workflows.

Mit OBO authentifiziert SQL den **delegierten Benutzerkontext**, nicht die Tool-Host-Identität. Das gibt Ihnen ein grundlegend besseres Audit-Modell: Benutzerprinzipal, Aktion, Anweisungskontext und Middle-Tier-App-Identifikator zusammen. Sie erhalten Rückverfolgbarkeit, ohne die Kontrollfläche von MCP-Tools und DAB-Entitätsberechtigungen zu verlieren.

Meine Meinung ist fest: Wenn Ihr Agent sensible SQL-Daten berühren kann, sollte OBO Ihre Standardarchitektur sein, keine optionale Härtungsaufgabe. Das Setup ist aufwändiger, aber Identitätsschulden werden immer später bezahlt, normalerweise während Sicherheitsvorfällen, Compliance-Audits oder Führungskräfte-Eskalationen.