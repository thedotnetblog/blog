---
title: "azd update — Ein Befehl für alle deine Paketmanager"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Die Azure Developer CLI hat jetzt einen universellen Update-Befehl, der unabhängig von der Installationsmethode funktioniert — winget, Homebrew, Chocolatey oder Installationsskript."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "azd-update-universal-upgrade-command.md" >}}).*

Kennst du diese Meldung „Eine neue Version von azd ist verfügbar", die alle paar Wochen auftaucht? Die, die du wegklickst, weil du dich nicht mehr erinnerst, ob du `azd` über winget, Homebrew oder dieses curl-Skript installiert hast, das du vor sechs Monaten ausgeführt hast? Ja, das ist jetzt endlich gelöst.

Microsoft hat [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) veröffentlicht — ein einziger Befehl, der die Azure Developer CLI auf die neueste Version aktualisiert, unabhängig davon, wie du sie ursprünglich installiert hast. Windows, macOS, Linux — egal. Ein Befehl.

## So funktioniert's

```bash
azd update
```

Das war's. Wenn du frühen Zugang zu neuen Features möchtest, kannst du auf den täglichen Insiders-Build wechseln:

```bash
azd update --channel daily
azd update --channel stable
```

Der Befehl erkennt deine aktuelle Installationsmethode und nutzt im Hintergrund den passenden Update-Mechanismus. Kein „Moment, habe ich auf diesem Rechner winget oder choco benutzt?" mehr.

## Der kleine Haken

`azd update` ist ab Version 1.23.x verfügbar. Wenn du eine ältere Version hast, musst du ein letztes manuelles Update mit deiner ursprünglichen Installationsmethode durchführen. Danach übernimmt `azd update` alles Weitere.

Prüfe deine aktuelle Version mit `azd version`. Falls du eine Neuinstallation brauchst, hilft dir die [Installationsdokumentation](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) weiter.

## Warum das wichtig ist

Es ist eine kleine Verbesserung der Lebensqualität, aber für diejenigen von uns, die `azd` täglich zum Deployen von KI-Agenten und Aspire-Apps auf Azure nutzen, bedeutet auf dem neuesten Stand zu sein weniger „dieser Bug war schon in der letzten Version behoben"-Momente. Eine Sache weniger, über die man nachdenken muss.

Lies die [vollständige Ankündigung](https://devblogs.microsoft.com/azure-sdk/azd-update/) und Jon Gallants [tiefergehende Analyse](https://blog.jongallant.com/2026/04/azd-update) für mehr Kontext.
