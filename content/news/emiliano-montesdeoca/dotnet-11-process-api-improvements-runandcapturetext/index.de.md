---
title: ".NET 11 behebt endlich die Prozess-API"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process bekommt sein größtes Update seit Jahren. RunAndCaptureTextAsync, KillOnParentExit, SafeProcessHandle-APIs und volle Kontrolle über Standard-Handle-Umleitung — kein Deadlock-Boilerplate mehr."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

Jeder .NET-Entwickler, der jemals einen Prozess starten und seine Ausgabe erfassen musste, hat irgendeine Variante desselben gefährlichen Boilerplate-Codes geschrieben: async-Lesen von stdout, async-Lesen von stderr, `WaitForExitAsync` — und bloß nicht vergessen, beide Streams zu leeren, sonst gibt es einen Deadlock. Es ist eine bekannte Falle, die seit Jahren besteht.

.NET 11 behebt das endlich ordentlich.

## RunAndCaptureTextAsync

Die wichtigste Ergänzung: eine einzelne statische Methode, die einen Prozess startet, stdout und stderr erfasst und auf das Beenden wartet — ohne Deadlock.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

Ein einziger Aufruf. Kein manuelles Leeren der Streams. Kein sorgfältig positioniertes `WaitForExit`. Wenn Sie einfach etwas ausführen und dessen Ausgabe erhalten müssen, ist das die API, die Sie wollen.

Es gibt auch `Process.RunAsync` für den Fall, dass Sie auf das Beenden warten möchten, ohne die Ausgabe zu erfassen.

## KillOnParentExit

Ein häufiges Problem mit gestarteten Prozessen: Wenn der übergeordnete Prozess abstürzt oder beendet wird, laufen die untergeordneten Prozesse als Waisen weiter. `KillOnParentExit` ermöglicht es Ihnen, beim Start des Prozesses anzugeben, dass der untergeordnete Prozess beendet werden soll, wenn der übergeordnete Prozess beendet wird.

Diese Funktion existierte auf plattformspezifische Weise (Job Objects unter Windows, prctl unter Linux), erforderte aber p/invoke oder Drittanbieter-Bibliotheken zur Verwendung aus .NET. Jetzt ist es eine erstklassige Eigenschaft von `ProcessStartInfo`.

## SafeProcessHandle-basierte APIs

Die neue leichtgewichtige API-Oberfläche ist um `SafeProcessHandle` anstelle der vollständigen `Process`-Klasse aufgebaut. Die vollständige `Process`-Klasse trägt viel Zustand und ist schwer zu trimmen — der `SafeProcessHandle`-Pfad ist trimmer-freundlicher für Anwendungen, die die Ausgabegröße minimieren müssen (WASM, native AOT).

## Vollständige Kontrolle über Handle-Vererbung

Das Update fügt auch eine feinkörnige Kontrolle darüber hinzu, welche Handles ein untergeordneter Prozess erbt und wie Standard-Handles umgeleitet werden. Bisher konnte man stdin/stdout/stderr umleiten, aber nicht genau festlegen, welche Handles auf Betriebssystemebene vererbt werden sollen. Die neuen APIs machen diese Kontrolle zugänglich.

## Warum Das Wichtig Ist

Die `Process`-Klasse wird in Tooling, Build-Systemen, Test-Runnern und jeder Anwendung verwendet, die andere Executables aufruft. Die alte API-Oberfläche stammte noch aus .NET Framework und zeigte ihr Alter. Das ist keine Breaking Change — die alten APIs funktionieren weiterhin — aber neuer Code sollte die neue Oberfläche bevorzugen.

Für getrimte Anwendungen oder AOT-Kompilierungsszenarien ist der `SafeProcessHandle`-Pfad besonders willkommen. Die alte `Process`-Klasse brachte viel reflektionslastigen Code mit, der das Trimmen erschwerte.

Original-Post: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
