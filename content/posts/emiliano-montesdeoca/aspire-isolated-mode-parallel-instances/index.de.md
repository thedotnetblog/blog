---
title: "Aspires Isolierter Modus Behebt den Port-Konflikt-Albtraum für Parallele Entwicklung"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 führt den --isolated Modus ein: zufällige Ports, getrennte Secrets und null Kollisionen beim gleichzeitigen Ausführen mehrerer Instanzen desselben AppHosts. Perfekt für KI-Agenten, Worktrees und parallele Workflows."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

Wenn du jemals versucht hast, zwei Instanzen desselben Projekts gleichzeitig zu starten, kennst du den Schmerz. Port 8080 wird bereits verwendet. Port 17370 ist belegt. Etwas killen, neustarten, Umgebungsvariablen jonglieren — ein echter Produktivitätskiller.

Dieses Problem wird schlimmer, nicht besser. KI-Agenten erstellen Git Worktrees um unabhängig zu arbeiten. Hintergrund-Agenten starten separate Umgebungen. Entwickler checken dasselbe Repo zweimal für Feature-Branches aus. Jedes dieser Szenarien läuft gegen dieselbe Wand: Zwei Instanzen derselben App kämpfen um dieselben Ports.

Aspire 13.2 behebt das mit einem einzigen Flag. James Newton-King vom Aspire-Team hat [alle Details aufgeschrieben](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/), und es ist eines dieser „warum hatten wir das nicht schon früher"-Features.

## Die Lösung: `--isolated`

```bash
aspire run --isolated
```

Das war's. Jeder Lauf bekommt:

- **Zufällige Ports** — keine Kollisionen mehr zwischen Instanzen
- **Isolierte User Secrets** — Connection Strings und API Keys bleiben pro Instanz getrennt

Keine manuelle Port-Neuzuweisung. Kein Umgebungsvariablen-Jonglieren. Jeder Lauf bekommt automatisch eine frische, kollisionsfreie Umgebung.

## Reale Szenarien, in denen das glänzt

**Mehrere Checkouts.** Du hast einen Feature-Branch in einem Verzeichnis und einen Bugfix in einem anderen:

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

Beide laufen ohne Konflikte. Das Dashboard zeigt, was wo läuft.

**Hintergrund-Agenten in VS Code.** Wenn der Hintergrund-Agent von Copilot Chat einen Git Worktree erstellt um unabhängig an deinem Code zu arbeiten, muss er möglicherweise deinen Aspire AppHost starten. Ohne `--isolated` ist das ein Port-Konflikt mit deinem primären Worktree. Mit ihm funktionieren einfach beide Instanzen.

Der Aspire-Skill, der mit `aspire agent init` mitkommt, weist Agenten automatisch an, `--isolated` zu verwenden, wenn sie in Worktrees arbeiten. So sollte Copilots Hintergrund-Agent das von Haus aus richtig handhaben.

**Integrationstests parallel zur Entwicklung.** Tests gegen einen laufenden AppHost ausführen während du weiter Features baust? Der isolierte Modus gibt jedem Kontext eigene Ports und Konfiguration.

## Wie es unter der Haube funktioniert

Wenn du `--isolated` übergibst, generiert die CLI eine eindeutige Instanz-ID für den Lauf. Das treibt zwei Verhaltensweisen:

1. **Port-Randomisierung** — statt sich an vorhersagbare Ports aus deiner AppHost-Konfiguration zu binden, wählt der isolierte Modus zufällige verfügbare Ports für alles — das Dashboard, Service-Endpoints, alles. Service Discovery passt sich automatisch an, sodass sich Services gegenseitig finden, unabhängig davon, auf welchen Ports sie landen.

2. **Secret-Isolation** — jeder isolierte Lauf bekommt seinen eigenen User-Secrets-Speicher, der durch die Instanz-ID identifiziert wird. Connection Strings und API Keys eines Laufs lecken nicht in einen anderen.

Dein Code braucht keine Änderungen. Aspires Service Discovery löst Endpoints zur Laufzeit auf, sodass alles korrekt verbunden wird, unabhängig von der Port-Zuweisung.

## Wann man es verwenden sollte

Verwende `--isolated`, wenn du mehrere Instanzen desselben AppHosts gleichzeitig betreibst — sei es für parallele Entwicklung, automatisierte Tests, KI-Agenten oder Git Worktrees. Für Einzelinstanz-Entwicklung, bei der du vorhersagbare Ports bevorzugst, funktioniert das reguläre `aspire run` weiterhin bestens.

## Zusammenfassung

Der isolierte Modus ist ein kleines Feature, das ein reales, zunehmend häufiges Problem löst. Da KI-gestützte Entwicklung uns in Richtung mehr paralleler Workflows drängt — mehrere Agenten, mehrere Worktrees, mehrere Kontexte — ist die Fähigkeit, einfach eine weitere Instanz hochzufahren ohne um Ports zu kämpfen, essentiell.

Lies den [vollständigen Post](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/) für alle technischen Details und probiere es aus mit `aspire update --self` um Version 13.2 zu bekommen.
