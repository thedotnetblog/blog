---
title: "68 Minuten täglich damit verbracht, Code neu zu erklären? Es gibt eine Lösung"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Context Rot ist real — dein KI-Agent verliert nach 30 Runden den Faden, und du zahlst stündlich die Kompaktierungssteuer. auto-memory gibt GitHub Copilot CLI chirurgische Erinnerungsfähigkeit ohne tausende Tokens zu verbrennen."
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken](https://thedotnetblog.com/posts/emiliano-montesdeoca/auto-memory-stop-re-explaining-code-to-copilot/).*

Kennst du den Moment, wenn deine Copilot-Sitzung `/compact` trifft und der Agent komplett vergisst, woran du gearbeitet hast? Die nächsten fünf Minuten verbringst du damit, die Dateistruktur, den fehlschlagenden Test und die drei Ansätze, die du bereits versucht hast, neu zu erklären. Dann passiert es wieder. Und wieder.

Desi Villanueva hat es gemessen: **68 Minuten pro Tag** — nur für Neuorientierung. Kein Code schreiben. Keine PRs reviewen. Nur die KI über Dinge auf den neuesten Stand bringen, die sie bereits wusste.

Es stellt sich heraus, dass es dafür einen konkreten Grund gibt — und eine konkrete Lösung.

## Die Kontextfenster-Lüge

Dein Agent kommt mit einer großen Zahl auf der Verpackung. 200K Tokens. Klingt riesig. In der Praxis ist es eine Obergrenze, keine Garantie.

Hier ist die tatsächliche Rechnung:

- 200K Gesamtkontext
- Minus ~65K für MCP-Tools beim Start (~33%)
- Minus ~10K für Instruktionsdateien wie `AGENTS.md` oder `copilot-instructions.md`

Das hinterlässt dir etwa **125K bevor du ein einziges Wort schreibst**. Und es wird schlimmer — LLMs degradieren nicht graceful wenn der Kontext voll wird. Sie stoßen an eine Wand bei etwa 60% Auslastung. Das Modell verliert Dinge, die vor 30 Runden erwähnt wurden, widerspricht früheren Antworten und halluziniert Dateinamen, die es vor 10 Minuten noch selbstsicher angegeben hatte.

Effektives Limit: **45K Tokens** bevor die Qualität degradiert. Das sind vielleicht 20-30 Runden aktiver Konversation bevor der Agent anfängt abzudriften.

## Die Kompaktierungssteuer

Jedes `/compact` kostet dich deinen Flow-Zustand. Du bist tief in einer Debugging-Sitzung. Gemeinsamer Kontext über 30 Minuten aufgebaut. Der Agent kennt die Dateistruktur, den fehlschlagenden Test, die Hypothese. Dann kommt die Warnung.

- Ignorieren → Agent wird progressiv dümmer
- `/compact` ausführen → Agent hat eine 2-Absatz-Zusammenfassung einer 30-minütigen Untersuchung

So oder so verlierst du. So oder so erzählst du dein eigenes Projekt einem neuen Mitarbeiter am ersten Tag nach.

Das Grausame: **Die Erinnerung existiert bereits.** Copilot CLI schreibt jede Sitzung in eine lokale SQLite-Datenbank bei `~/.copilot/session-store.db`. Der Agent kann sie nur nicht lesen.

## auto-memory: Eine Recall-Schicht, Kein Gedächtnissystem

```bash
pip install auto-memory
```

~1.900 Zeilen Python. Null Abhängigkeiten. In 30 Sekunden installiert.

Anstatt den Kontext mit Grep-Ergebnissen zu fluten, gibst du dem Agenten chirurgischen Zugriff auf das, was wirklich wichtig ist — **50 Tokens statt 10.000**.

## Fazit

Context Rot ist eine reale architektonische Einschränkung. auto-memory umgeht sie, indem es deinem Agenten einen günstigen, präzisen Recall-Mechanismus gibt. Wenn du ernsthaftes KI-unterstütztes Entwickeln mit GitHub Copilot CLI machst, ist die 30-Sekunden-Installation es wert.

Schau es dir an: [auto-memory auf GitHub](https://github.com/dezgit2025/auto-memory). Original-Post von Desi Villanueva: [I Wasted 68 Minutes a Day](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/).
