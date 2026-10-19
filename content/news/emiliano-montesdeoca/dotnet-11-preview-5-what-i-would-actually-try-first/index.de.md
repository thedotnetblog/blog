---
title: ".NET 11 Preview 5: Was ich tatsächlich zuerst testen würde"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 5 liefert Verbesserungen im SDK, Runtime, C#, ASP.NET Core und EF Core. Hier sind die Updates, die ich am meisten für einen frühen Test halte, wenn Sie echte .NET-Apps bauen."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - Entity Framework
---

.NET Preview-Beiträge sind immer vollgepackt.

Das sind gute Nachrichten für die Plattform, aber es bedeutet auch, dass die praktische Frage vergraben wird: **was sollten Sie tatsächlich zuerst testen?**

.NET 11 Preview 5 bringt viel im SDK, Runtime, Libraries, ASP.NET Core, C#, MAUI und EF Core. Anstatt dies in eine riesige Changelog-Zusammenfassung zu verwandeln, möchte ich mich auf die Teile konzentrieren, die meiner Meinung nach jetzt echte Entwickleraufmerksamkeit verdienen.

## Die MCP-Server-Vorlage in `dotnet new` ist ein Signal

Dies ist wahrscheinlich der strategischste Punkt im SDK-Bereich.

Wenn eine Projektvorlage direkt im SDK landet, bedeutet das, dass die Plattform das Szenario nicht mehr als Nische betrachtet. Eine **MCP-Server-Vorlage** in `dotnet new` senkt die Kosten für das Ausprobieren des Musters und sendet eine klare Botschaft, wohin sich das Ökosystem entwickelt.

Wenn Sie Agent-Tooling, interne Assistenten oder KI-integrierte Entwicklerdienstprogramme in .NET bauen, ist dies eines der ersten Dinge, die ich testen würde.

## Build-Zeit-Schwachstellen- und End-of-Life-Prüfungen sind genau die Art von Standardwerten, die ich mag

Sicherheits- und Lebenszyklusbewusstsein sind viel besser, wenn die Plattform Ihnen **während des Builds** hilft, nicht erst hinterher in einem separaten Bericht, den niemand liest.

Die neuen SDK-Prüfungen auf Schwachstellen und End-of-Life-Pakete während des Builds sind die Art von Feature, die ich liebe, weil sie besseres Verhalten zum Standard machen.

Diese sind nicht auffällig, aber sie sind die Art von Verbesserungen, die wirklich gut altern.

## Meine Kurzliste für einen ersten Durchgang

Wenn ich einen halben Tag hätte, um Preview 5 zu erkunden, würde ich Folgendes tun:

1. die MCP-Server-Vorlage ausprobieren
2. Builds ausführen und die neuen Schwachstellen-/EOL-Prüfungen inspizieren
3. jede Codebasis testen, die von den neuen C#-Modellierungsfunktionen profitieren könnte
4. Blazor SSR-Szenarien validieren, wenn Sie auf diesem Stack sind
5. EF Core-lastige Pfade ausführen und auf Warnungsänderungen oder SQL-Unterschiede achten

Dort sehe ich den frühen Wert.

Originalquelle: [.NET 11 Preview 5 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-5/)