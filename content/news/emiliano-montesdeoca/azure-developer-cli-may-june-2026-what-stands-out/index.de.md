---
title: "Azure Developer CLI wird immer mehr zu einem besseren Inner-Loop-Tool"
date: 2026-06-28
author: "Emiliano Montesdeoca"
description: "Die Azure-Developer-CLI-Versionen von Mai und Juni 2026 bringen viel, aber der größte Wert liegt darin, wie sie den täglichen Loop verbessern: besseres Tool-Management, sichereres Provisioning, stärkere Erweiterungsunterstützung und praktischere Ausführungsworkflows."
tags:
  - Azure Developer CLI
  - azd
  - Azure
  - Developer Tools
  - .NET
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

Große CLI-Roundups können anstrengend zu lesen sein, weil sie große Workflow-Verbesserungen und winzige Fixes in einer einzigen Textwand vermischen.

Also hier meine Kurzversion: Die neuesten **Azure Developer CLI**-Updates sind wichtig, weil `azd` immer mehr zu einem **besseren Inner-Loop-Tool** wird und nicht nur zu einem Deployment-Wrapping.

Das ist die entscheidende Verschiebung.

## Tool-Management wird Teil des Produkts, nicht zur Nebensache

Eine meiner Lieblingsneuerungen sind die neuen `azd tool`-Befehle.

Alles, was Setup-Reibung reduziert, ist es wert, beachtet zu werden, besonders in Projekten, in denen eine funktionierende Umgebung aus SDKs, CLIs, Docker, Bicep und Erweiterungen besteht.

Wenn das Tool jetzt helfen kann, diese Abhängigkeiten direkt zu entdecken, zu installieren, zu prüfen und zu aktualisieren, entfernt das viele der nervigen Fehlerbilder, die Neulinge oft zuerst treffen.

Das ist echter Wert.

## `azd exec` wirkt auch wichtiger, als es klingt

Auf den ersten Blick kann `azd exec` wie eine kleine Komfortfunktion aussehen.

Das halte ich nicht für richtig.

Befehle mit dem vollständigen `azd`-Umgebungskontext auszuführen, einschließlich Secret-Auflösung, ist genau die Art von Fähigkeit, die lokale Automatisierung und Scripting viel sauberer macht.

Das reduziert den Bedarf an zusätzlichen Glue-Skripten und hilft, Ausführungen über Umgebungen hinweg konsistent zu halten.

Das ist ein praktischer Gewinn.

## Sichereres Provisioning und besseres Abbruchverhalten sind unterschätzte Verbesserungen

Das Release enthält auch Änderungen an Provisioning-Abhängigkeiten, Abbruchbehandlung und Deployment-Verhalten, die vielleicht nicht glamourös aussehen, aber sehr willkommen sind.

Interaktive Abbruchaufforderungen, besseres Abhängigkeitsmodell und klarerer Deployment-Status sind genau die Art von Verbesserungen, die ein CLI vertrauenswürdig wirken lassen, wenn du mit echten Azure-Ressourcen arbeitest.

Und Vertrauen ist bei Werkzeugen wie diesem ein großes Thema.

## Meine Einschätzung

Je mehr sich `azd` bei Setup, Scripting, Deployment-Sicherheit und Erweiterungsunterstützung verbessert, desto mehr fühlt es sich wie etwas an, das du in deinem täglichen Loop behalten kannst, statt es nur kurz vor dem Deployment zu berühren.

Das ist die richtige Richtung.

Für Teams, die cloud-native oder KI-gestützte Anwendungen auf Azure bauen, wird das CLI dort nützlicher, wo es am meisten zählt: während der eigentlichen Entwicklung.

Originalbeitrag: [Azure Developer CLI (azd) – May and June 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/)