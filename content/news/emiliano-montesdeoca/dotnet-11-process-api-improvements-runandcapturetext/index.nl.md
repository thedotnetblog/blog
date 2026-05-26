---
title: ".NET 11 repareert eindelijk de Proces-API"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process krijgt zijn grootste update in jaren. RunAndCaptureTextAsync, KillOnParentExit, SafeProcessHandle-API's en volledige controle over standaard handle-omleiding — geen deadlock-boilerplate meer."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

Elke .NET-ontwikkelaar die ooit een proces moest starten en de uitvoer ervan moest vastleggen, heeft een variatie op dezelfde gevaarlijke boilerplate geschreven: async lezen van stdout, async lezen van stderr, `WaitForExitAsync`, vergeet niet beide streams te leegmaken of je krijgt een deadlock. Het is een bekende val die al jaren bestaat.

.NET 11 lost dit eindelijk goed op.

## RunAndCaptureTextAsync

De belangrijkste toevoeging: één enkele statische methode die een proces start, stdout en stderr vastlegt, en wacht op beëindiging zonder deadlock.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

Één aanroep. Geen handmatig leegmaken van streams. Geen zorgvuldig geplaatste `WaitForExit`. Als u gewoon iets wilt uitvoeren en de uitvoer wilt ontvangen, is dit de API die u wilt.

Er is ook `Process.RunAsync` voor het geval u wilt wachten op beëindiging zonder de uitvoer te vastleggen.

## KillOnParentExit

Een veelvoorkomend probleem met gestarte processen: als het bovenliggende proces crasht of wordt beëindigd, blijven de onderliggende processen als wezen draaien. `KillOnParentExit` stelt u in staat om bij het starten van het proces te declareren dat het onderliggende proces beëindigd moet worden wanneer het bovenliggende proces wordt beëindigd.

Dit is een functie die op platformspecifieke manieren bestond (job objects op Windows, prctl op Linux) maar p/invoke of externe bibliotheken vereiste voor gebruik vanuit .NET. Nu is het een eersteklas eigenschap op `ProcessStartInfo`.

## SafeProcessHandle-gebaseerde API's

Het nieuwe lichtgewicht API-oppervlak is gebouwd rond `SafeProcessHandle` in plaats van de volledige klasse `Process`. De volledige klasse `Process` draagt veel toestand met zich mee en is moeilijk te trimmen — het `SafeProcessHandle`-pad is trimmer-vriendelijker voor toepassingen die de uitvoergrootte moeten minimaliseren (WASM, native AOT).

## Volledige Controle over Handle-erfenis

De update voegt ook gedetailleerde controle toe over welke handles een onderliggend proces erft en hoe standaard handles worden omgeleid. Voorheen kon u stdin/stdout/stderr omleiden, maar kon u niet precies specificeren welke handles op OS-niveau geërfd worden. De nieuwe API's stellen die controle bloot.

## Waarom Dit Belangrijk Is

De klasse `Process` wordt gebruikt in tooling, buildsystemen, testrunners en elke toepassing die andere uitvoerbare bestanden aanroept. Het oude API-oppervlak dateerde uit het .NET Framework-tijdperk en toonde zijn leeftijd. Dit is geen afbrekende wijziging — de oude API's werken nog steeds — maar nieuwe code moet de voorkeur geven aan het nieuwe oppervlak.

Voor getrimde toepassingen of AOT-compilatiescenario's is het `SafeProcessHandle`-pad bijzonder welkom. De oude klasse `Process` bracht veel reflection-zwaar code mee dat het trimmen bemoeilijkte.

Originele post: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
