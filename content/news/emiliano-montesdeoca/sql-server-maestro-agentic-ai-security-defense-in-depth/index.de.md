---
title: "MAESTRO, Defense-in-Depth und Warum SQL Server jetzt eine Sicherheitsgrenze für KI ist"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "Agentische KI führt Bedrohungen ein, für die traditionelle STRIDE-Modelle nicht konzipiert wurden. So mappt Microsoft SQL auf das MAESTRO-Framework, um eine regulierte Ausführungsgrenze bereitzustellen."
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

Sicherheits-Bedrohungsmodelle werden auf Annahmen darüber aufgebaut, wer oder was die Anfragen stellt. STRIDE geht von menschlichen Akteuren aus, die über definierte Schnittstellen mit Systemen interagieren. KI-Agenten funktionieren nicht so.

## STRIDE Wurde Nicht für KI-Agenten Entworfen

Agentische Systeme operieren autonom, verketten Werkzeuge über API-Aufrufe, treffen Entscheidungen darüber, welche Daten abgerufen und welche Aktionen ausgeführt werden, und können Anweisungen aus mehreren Quellen erhalten — Benutzer-Prompts, Werkzeugergebnisse, abgerufene Daten. Das STRIDE-Bedrohungsmodell (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) erfasst agentenspezifische Angriffsvektoren wie Prompt-Injektion, Kontextvergiftung oder Werkzeugmissbrauch nicht angemessen.

Die Cloud Security Alliance veröffentlichte das MAESTRO-Framework speziell für das Risiko von KI-Agenten.

## Das MAESTRO-Framework

MAESTRO organisiert agentisches KI-Risiko in sieben Schichten:

1. **Foundation Models** — die zugrunde liegenden LLMs und ihre Trainingsvulnerabilitäten
2. **Data Operations** — Datenabruf, -speicherung und -manipulation
3. **Agent Frameworks** — die Orchestrierungs- und Koordinationsmiddleware für Agenten
4. **Deployment & Infrastructure** — wo Agenten ausgeführt werden und wie sie konfiguriert sind
5. **Evaluation & Observability** — Überwachung des Agentenverhaltens im Zeitverlauf
6. **Security & Compliance** — Zugriffskontrollen, Prüfung und regulatorische Compliance
7. **Agent Ecosystem** — wie Agenten miteinander und mit externen Werkzeugen interagieren

Jede Schicht hat spezifische Angriffsvektoren, die traditionelle Sicherheitskontrollen nicht direkt ansprechen.

## Microsoft SQL als Regulierte Ausführungsgrenze

SQL Server 2025 mappt auf konkrete Weise auf MAESTRO-Schichten:

**Data Operations-Schicht**: Das in T-SQL integrierte `AI_GENERATE_EMBEDDINGS` hält Vektoroperationen innerhalb der regulierten Datenbankgrenze. Daten müssen nicht für die Embedding-Verarbeitung zum Modelldienst verlassen.

**Security & Compliance-Schichten**: Row-Level Security (RLS) und Dynamic Data Masking (DDM) gelten unabhängig davon, wie die Anfrage ankam — ob von einem menschlichen Benutzer oder einem KI-Agenten. Der Agent kann keine Kontrollen umgehen, die von der Datenbank selbst durchgesetzt werden.

**Agent Frameworks-Schicht**: Gespeicherte Prozeduren dienen als Werkzeuggrenzen. Statt Agenten willkürlichen SQL-Zugriff zu geben, definieren Sie erlaubte Operationen als Prozeduren und stellen sie als Agentenwerkzeuge bereit. Parametrisierte Abfragen verhindern Injektion auf Ausführungsebene.

**Evaluation & Observability-Schicht**: Audit-Logging und Query Store erfassen, was jeder Agent tatsächlich ausgeführt hat — nicht nur, wozu er aufgefordert wurde. Diese Nachverfolgbarkeit ist bei Vorfallsuntersuchungen in agentischen Systemen, bei denen die Zuordnung komplex ist, von entscheidender Bedeutung.

## Defense-in-Depth für Agentische KI

Das Prinzip bleibt dasselbe wie bei traditioneller Sicherheit: Keine einzelne Kontrolle ist ausreichend. Was sich ändert, ist, welche Kontrollen für Agenten am wichtigsten sind:

**Explosionsradius reduzieren**: Werkzeuggrenzen durch gespeicherte Prozeduren bedeuten, dass ein kompromittierter Agent nur vordefinierte Operationen ausführen kann. Er kann nicht zu willkürlichen Abfragen wechseln.

**Observierbarkeit**: Sie müssen nach einem Vorfall die Frage beantworten können: "Was hat dieser Agent genau getan?" Agentische KI-Systeme ohne Nachverfolgbarkeit auf Datenbankebene haben blinde Flecken, die Anwendungsprotokollierung nicht abdeckt.

**Eingeschränkte Ausführung**: Parametrisierung, RLS und DDM sind Sicherheitseigenschaften unabhängig davon, ob der Aufrufer menschlich ist. Schwächen Sie diese nicht ab, um Agenten zu akkommodieren.

**Rechenschaftspflicht**: SQL Server-Audit-Logging erstellt eine Aufzeichnung, wer (welcher Agent, mit welchen Anmeldedaten) was zu welchem Zeitpunkt ausgeführt hat. Das ist wichtig, wenn agentische Systeme Aktionen mit realen Konsequenzen durchführen.

SQL Server 2025 wurde nicht gebaut, um agentisches Risiko abstrakt zu lösen — es wurde gebaut, um eine relationale Datenbank zu sein. Aber die Governance, die eine Enterprise-Datenbank vertrauenswürdig macht, erweist sich genau als das, was eine Agenten-Ausführungsgrenze sicher macht.

Originalpost: [Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
