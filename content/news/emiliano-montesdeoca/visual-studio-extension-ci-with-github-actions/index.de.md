---
title: 'Visual Studio Extension-Teams sollten aufhören, aus Gewohnheit zu releasen, und anfangen, per Pipeline zu releasen'
date: 2026-07-23
author: 'Emiliano Montesdeoca'
description: 'Ein wiederholbarer GitHub Actions-Ablauf für VSIX-Versionierung und Veröffentlichung ist jetzt einfach genug, dass manuelle Release-Schritte schwer zu rechtfertigen sind.'
tags:
  - visual-studio
  - vsix
  - github-actions
  - ci-cd
  - developer-tooling
---

Originalquelle: [Automating your Visual Studio extension builds with GitHub Actions](https://devblogs.microsoft.com/visualstudio/automating-your-visual-studio-extension-builds-with-github-actions/)

Wenn Sie Visual Studio-Erweiterungen warten und immer noch wesentliche Teile des Releases manuell ausführen, ist dies Ihr Signal zur Modernisierung.

Der in diesem Beitrag gezeigte Workflow ist bewusst praktisch: Version stempeln, bauen, Testartefakte in einer Galerie veröffentlichen, dann stabile Bits im Marketplace veröffentlichen. Keine schwere Plattformzeremonie, nur deterministisches Release-Verhalten.

Was mir am besten gefällt, ist, dass Versionierung als Pipeline-Zustand behandelt wird, nicht als Pre-Release-Checklistenelement. Diese eine Entscheidung eliminiert eine überraschende Anzahl von Fehlern: nicht übereinstimmende Metadaten, veraltete Assembly-Versionen und inkonsistente Release-Notes.

Die Trennung zwischen Galerie-Veröffentlichung und Marketplace-Veröffentlichung ist auch operativ ausgereift. Teams brauchen einen Ort für schnelle Validierungs-Builds, die keine offizielle Release-Semantik tragen. Alles direkt in den Marketplace zu pushen, ist aufwendig und ermutigt zu riskanten Abkürzungen.

Ein starkes Release-Muster für Extension-Teams:

Bei Pull-Requests und Main-Commits CI-VSIX-Artefakte produzieren und für Tester in der Galerie veröffentlichen.

Bei getaggten Releases signierte und validierte Pakete im Marketplace veröffentlichen.

Token-Handling mit dedizierten Secrets und Least-Privilege-Bereichen minimal halten.