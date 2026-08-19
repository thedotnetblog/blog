---
title: "Aspire in VS Code 13.4 zieht die Entwicklerschleife in genau der richtigen Weise an"
date: 2026-06-16
author: "Emiliano Montesdeoca"
description: "Aspire in VS Code 13.4 ist nicht nur ein Feature-Update. Es ist eine echte Verbesserung der täglichen Entwicklungsschleife mit besserem Debugging, besserer Ressourcensichtbarkeit, Panel-Integration und TypeScript AppHost-Unterstützung."
tags:
  - Aspire
  - VS Code
  - .NET
  - Developer Experience
  - TypeScript
---

Die besten Tooling-Updates sind die, die man nach ein paar Tagen spürt, nicht die, die nur in Release-Notes gut aussehen.

So liest sich **Aspire in VS Code 13.4** für mich.

Bei diesem Update geht es ganz um die Straffung der inneren Schleife: Projekte schneller erstellen, Debugging gemischtsprachiger Ressourcen natürlicher gestalten, Health und Befehle direkt im Editor anzeigen und das Dashboard nahe halten, ohne es zum einzigen Arbeitsort zu machen.

Das ist eine sehr gute Richtung.

## Der große Gewinn ist weniger Kontextwechsel

Wenn Sie Aspire ernsthaft nutzen, bewegen Sie sich normalerweise über mehrere Oberflächen:

- AppHost-Code
- Terminal
- Dashboard
- Logs
- Debug-Sessions
- Service-Endpunkte

Was 13.4 gut macht, ist die Reibung zwischen diesen Oberflächen zu reduzieren.

Die neue VS Code-Erfahrung macht mehr vom App-Status genau dort sichtbar, wo Sie bereits arbeiten:

- Ressourcen-Health im Editor
- Befehle neben Ressourcendeklarationen
- einfacherer Dashboard-Zugriff
- Log-Zugriff aus dem AppHost-Kontext
- ein Panel, das auch vor vollständigem Debugging-Start nützlich bleibt

Das klingt klein, bis man es jeden Tag tut.

## Debugging gemischter Stacks ist wichtiger als man denkt

Einer der stärksten Teile dieses Updates ist die natürlichere Geschichte zum Debuggen von **C#, TypeScript, Python, Go, Browser-Apps und Azure Functions** in einem einzigen Aspire-gesteuerten Flow.

Das spiegelt die reale Form moderner Apps viel besser wider, als so zu tun, als ob alles in einer einzigen Laufzeit lebt.

Besonders für .NET-Entwickler ist das wertvoll, weil viele von uns jetzt Systeme bauen, die API-Projekte, Frontends, Worker und KI-bezogene Dienste in verschiedenen Sprachen mischen.

Die Tatsache, dass Aspire dies in VS Code einheitlicher gestaltet, ist eine sehr praktische Verbesserung.

## Meine Meinung

Aspire 13.4 in VS Code dreht sich nicht um eine Killer-Feature. Es geht darum, die rauen Kanten in der täglichen Schleife zu glätten:

- schneller starten
- mehr Status dort sehen, wo Sie codieren
- natürlicher debuggen
- nur bei Bedarf zu Logs und Dashboard springen

Genau so sollte sich gutes Tooling weiterentwickeln.

Originalquelle: [Aspire in VS Code: the 13.4 developer loop](https://devblogs.microsoft.com/aspire/aspire-vscode-extension-13-4/)