---
title: "Wie Copilot Studio auf .NET 10 WebAssembly Migrierte und 20% Schneller Wurde"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "Die Verbesserungen von .NET 10 WASM sind nicht nur für neue Projekte. Hier ist, was Copilot Studio nach dem Upgrade von .NET 8 gemessen hat: automatisches Fingerprinting, WasmStripILAfterAOT standardmäßig und echte Ausführungsleistungszahlen."
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

Das Copilot Studio-Team hat etwas getan, worüber alle Blazor WASM-Entwickler neugierig waren: Sie haben tatsächlich eine Produktionsanwendung von .NET 8 auf .NET 10 aktualisiert und die Ergebnisse gemessen. Der Beitrag teilt spezifische Zahlen, was selten und wirklich nützlich ist.

## Das Upgrade War Langweilig (Das ist eine Gute Sache)

Ziel-Framework aktualisieren, Paketreferenzen auffrischen, Breaking Changes beheben. Das ist alles. Der .NET 10-Build läuft jetzt in der Produktion. Die Migration selbst war nicht der interessante Teil — die Änderungen in .NET 10 sind es.

## Automatisches Asset-Fingerprinting

Früher bedeutete das Bereitstellen einer WASM-App das Schreiben benutzerdefinierter Skripte zum Umbenennen veröffentlichter Assets mit SHA256-Hashes für Cache-Busting. Copilot Studio hatte ein PowerShell-Skript, das genau das tat — Dateien umbenennen, `integrity`-Attribute in den JavaScript-Loader injizieren, alles manuell verwalten.

In .NET 10 ist all das integriert. Veröffentlichte Assets werden automatisch mit Fingerprint versehen, direkt aus `dotnet.js` importiert und ohne manuelle Eingriffe mit Integrität validiert. Das Team löschte das Umbenennungsskript.

Kleine Änderung im Umfang, deutliche Reduzierung der Komplexität.

## WasmStripILAfterAOT Ist Jetzt Standardmäßig Aktiviert

In .NET 8 war das Entfernen von IL aus AOT-kompilierten Assemblys opt-in. In .NET 10 ist es der Standard. Nach der AOT-Kompilierung wird der ursprüngliche IL-Bytecode aus der Ausgabe entfernt — er wird zur Laufzeit nicht benötigt, und ihn zu behalten blähte die Paketgröße grundlos auf.

Copilot Studio verwendet eine spezifische Optimierung: Es liefert sowohl eine JIT-Engine (schneller Start) als auch eine AOT-Engine (maximale Steady-State-Leistung), lädt beide parallel und übergibt von JIT an AOT, sobald sie bereit ist. Es dedupliziert auch Dateien, die zwischen den beiden Engines identisch sind.

Das neue IL-Stripping-Verhalten bedeutet, dass AOT-Assemblys nicht mehr Bit-für-Bit mit ihren JIT-Gegenstücken übereinstimmen, sodass weniger Dateien dedupliziert werden:
- .NET 8: 59 gemeinsame Dateien
- .NET 10: 22 gemeinsame Dateien

Nettoergebnis: etwa 15% größere Paketgröße für die AOT-Engine. Der AOT-Download ist ~6% langsamer auf schnellem LAN, ~17% langsamer auf 4G. Aber das alles passiert im Hintergrund, nachdem die App bereits interaktiv ist.

## Die Leistungszahlen

Das ist der wichtige Teil:

- **~20% schneller** beim ersten Aufruf (kalter Pfad)
- **~5% schneller** bei nachfolgenden Aufrufen (warmer Pfad)

Die Verbesserungen sind am sichtbarsten bei "großen Bots" — großen, komplexen Agenten, bei denen AOT-kompilierter Code dominiert. Für einfachere Workflows ist der Gewinn kleiner.

## Wenn Sie Noch auf .NET 8 Sind

Die Migrationsgeschichte ist wirklich einfach: Aktualisieren Sie `<TargetFramework>`, aktualisieren Sie Paketreferenzen, entfernen Sie benutzerdefinierte Fingerprinting-Skripte, und Sie profitieren automatisch von `WasmStripILAfterAOT`. Wenn Sie AOT kompilieren, erwarten Sie ähnliche Leistungsgewinne.

Ein Hinweis aus dem Beitrag: Wenn Sie die .NET WASM-Laufzeitumgebung in einem `WebWorker` laden, setzen Sie `dotnetSidecar = true` bei der Initialisierung.

Originalbeitrag: [Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
