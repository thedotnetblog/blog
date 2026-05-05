---
title: "Hör auf, dein Terminal zu babysitzen: Aspires Detached Mode verändert den Workflow"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 lässt dich deinen AppHost im Hintergrund ausführen und gibt dir dein Terminal zurück. Kombiniert mit neuen CLI-Befehlen und Agent-Unterstützung ist das wichtiger als es klingt."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

Jedes Mal, wenn du einen Aspire AppHost startest, ist dein Terminal weg. Gesperrt. Belegt, bis du Ctrl+C drückst. Musst du schnell einen Befehl ausführen? Öffne einen neuen Tab. Willst du Logs prüfen? Noch ein Tab. Es ist eine kleine Reibung, die sich schnell summiert.

Aspire 13.2 behebt das. James Newton-King hat [alle Details aufgeschrieben](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), und ehrlich gesagt ist das eines dieser Features, das sofort verändert, wie man arbeitet.

## Detached Mode: ein Befehl, Terminal zurück

```bash
aspire start
```

Das ist die Kurzform für `aspire run --detach`. Dein AppHost startet im Hintergrund und du bekommst dein Terminal sofort zurück. Keine Extra-Tabs. Kein Terminal-Multiplexer. Einfach dein Prompt, bereit loszulegen.

## Laufende Prozesse verwalten

Die Sache ist — im Hintergrund laufen lassen ist nur nützlich, wenn man auch verwalten kann, was da draußen läuft. Aspire 13.2 liefert einen vollständigen Satz an CLI-Befehlen genau dafür:

```bash
# List all running AppHosts
aspire ps

# Inspect the state of a specific AppHost
aspire describe

# Stream logs from a running AppHost
aspire logs

# Stop a specific AppHost
aspire stop
```

Das macht die Aspire CLI zu einem echten Prozessmanager. Du kannst mehrere AppHosts starten, ihren Status prüfen, ihre Logs verfolgen und sie herunterfahren — alles aus einer einzigen Terminal-Sitzung.

## Kombiniere es mit dem isolierten Modus

Der Detached Mode passt natürlich zum isolierten Modus. Willst du zwei Instanzen desselben Projekts im Hintergrund ohne Port-Konflikte laufen lassen?

```bash
aspire start --isolated
aspire start --isolated
```

Jede bekommt zufällige Ports, separate Secrets und ihren eigenen Lebenszyklus. Verwende `aspire ps`, um beide zu sehen, `aspire stop`, um den zu beenden, den du nicht mehr brauchst.

## Warum das für Coding-Agents riesig ist

Hier wird es richtig interessant. Ein Coding-Agent, der in deinem Terminal arbeitet, kann jetzt:

1. Die App mit `aspire start` starten
2. Ihren Zustand mit `aspire describe` abfragen
3. Logs mit `aspire logs` prüfen, um Probleme zu diagnostizieren
4. Sie mit `aspire stop` beenden, wenn er fertig ist

Alles ohne die Terminal-Sitzung zu verlieren. Vor dem Detached Mode hätte sich ein Agent, der deinen AppHost ausführt, aus seinem eigenen Terminal ausgesperrt. Jetzt kann er starten, beobachten, iterieren und aufräumen — genau so, wie man es von einem autonomen Agenten erwartet.

Das Aspire-Team hat hier bewusst investiert. `aspire agent init` richtet eine Aspire-Skill-Datei ein, die Agents diese Befehle beibringt. So können Tools wie Copilots Coding-Agent deine Aspire-Workloads direkt verwalten.

## Fazit

Der Detached Mode ist ein Workflow-Upgrade, das sich als einfaches Flag tarnt. Du hörst auf, zwischen Terminals zu wechseln, Agents blockieren sich nicht mehr selbst, und die neuen CLI-Befehle geben dir echte Sichtbarkeit über das, was läuft. Es ist praktisch, es ist sauber, und es macht den täglichen Entwicklungszyklus spürbar flüssiger.

Lies den [vollständigen Beitrag](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) für alle Details und hole dir Aspire 13.2 mit `aspire update --self`.
