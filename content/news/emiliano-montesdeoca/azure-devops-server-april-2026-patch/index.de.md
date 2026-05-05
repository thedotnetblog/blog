---
title: "Azure DevOps Server April 2026 Patch — Fix für PR-Abschluss und Sicherheitsupdates"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server erhält Patch 3 mit einem Fix für fehlgeschlagene PR-Abschlüsse, verbesserter Abmeldevalidierung und wiederhergestellten GitHub Enterprise Server PAT-Verbindungen."
tags:
  - azure-devops
  - devops
  - patches
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "azure-devops-server-april-2026-patch.md" >}}).*

Kurzer Hinweis für Teams, die selbst gehosteten Azure DevOps Server betreiben: Microsoft hat [Patch 3 für April 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) mit drei gezielten Fixes veröffentlicht.

## Was behoben wurde

- **Fehlgeschlagene Pull-Request-Abschlüsse** — eine Null-Referenz-Ausnahme beim automatischen Abschluss von Work Items konnte dazu führen, dass PR-Merges fehlschlugen. Wenn du auf zufällige Fehler beim PR-Abschluss gestoßen bist, ist das wahrscheinlich die Ursache
- **Validierung der Abmelde-Weiterleitung** — verbesserte Validierung beim Abmelden, um potenziell bösartige Weiterleitungen zu verhindern. Das ist ein Sicherheitsfix, den man zeitnah anwenden sollte
- **GitHub Enterprise Server PAT-Verbindungen** — das Erstellen von Personal-Access-Token-Verbindungen zu GitHub Enterprise Server war defekt, jetzt funktioniert es wieder

## So aktualisierst du

Lade [Patch 3](https://aka.ms/devopsserverpatch3) herunter und starte den Installer. Um zu überprüfen, ob der Patch angewendet wurde:

```bash
<patch-installer>.exe CheckInstall
```

Wenn du Azure DevOps Server on-premises betreibst, empfiehlt Microsoft dringend, immer auf dem neuesten Patch zu bleiben — sowohl für Sicherheit als auch Zuverlässigkeit. Schau dir die [Release Notes](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026) für alle Details an.
