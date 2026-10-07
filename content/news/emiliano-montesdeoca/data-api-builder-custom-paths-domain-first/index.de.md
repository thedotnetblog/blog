---
title: 'Data API Builder Custom Paths lassen Sie APIs für Menschen entwerfen, nicht für Tabellen'
date: 2026-07-17
author: 'Emiliano Montesdeoca'
description: 'Zusammengesetzte REST-Pfade in DAB sind eine kleine Funktion mit großer architektonischer Wirkung für domänenorientiertes API-Design.'
tags:
  - data-api-builder
  - azure-sql
  - rest-api
  - api-design
  - dotnet
---

Originalquelle: [Compose your API surface with Data API builder custom paths](https://devblogs.microsoft.com/azure-sql/data-api-builder-custom-rest-paths/)

Die neue Unterstützung für zusammengesetzte REST-Pfade in Data API Builder mag wie eine kleine Konfigurationsverbesserung aussehen, aber sie löst tatsächlich eine langjährige API-Design-Spannung: Datenbanktopologie, die in das öffentliche Endpunkt-Design durchsickert.

Standard-Entity-basierte Routen sind großartig für schnelle Starts. Sie sind oft falsch für langfristige Produkt-APIs. Echte Systeme benötigen Routenstrukturen, die Geschäftskonzepten, Eigentumsgrenzen und Verbraucher-Denkmodellen entsprechen.

Deshalb ist diese DAB-Änderung wichtig. Sie können den Komfort generierter APIs behalten, während Sie eine sauberere domänenorientierte Oberfläche präsentieren.

Meine Meinung ist einfach: Wenn Ihre API-Pfadstruktur in der Produktion rohe Tabellennamen widerspiegelt, optimieren Sie normalerweise für Backend-Komfort auf Kosten der Client-Klarheit.

Mit benutzerdefinierten Pfaden können Teams bessere Grenzen modellieren, wie Vertrieb, Abrechnung, Support oder partnerspezifische Oberflächen. Dies ersetzt keine ordnungsgemäße API-Governance, gibt DAB-Benutzern aber einen praktischen Weg, das Routen-Design an der Produktsprache auszurichten.

Praktische Richtlinien für Teams, die diese Funktion einführen:

Definieren Sie eine Namensrichtlinie, bevor Sie Pfade ad hoc hinzufügen. Inkonsistente Untersegmente werden zu langfristigem Chaos.

Ordnen Sie Endpunkte begrenzten Kontexten zu, nicht Organigrammen. Teams ändern sich; Domänensemantik sollte stabil sein.

Behandeln Sie die Pfadstruktur als Teil Ihrer Versionierungsstrategie und dokumentieren Sie breaking changes explizit.

Validieren Sie das Autorisierungsverhalten entlang benutzerdefinierter Routenstrukturen, damit Routenklarheit mit Sicherheitsklarheit einhergeht.