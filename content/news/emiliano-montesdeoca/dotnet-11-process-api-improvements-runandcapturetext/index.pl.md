---
title: ".NET 11 w końcu naprawia API Procesów"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process otrzymuje największą aktualizację od lat. RunAndCaptureTextAsync, KillOnParentExit, API SafeProcessHandle i pełna kontrola nad przekierowaniem standardowych uchwytów — koniec z powtarzającym się kodem obsługi deadlocka."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

Każdy deweloper .NET, który kiedykolwiek musiał uruchomić proces i przechwycić jego wynik, napisał jakąś wariację tego samego niebezpiecznego powtarzającego się kodu: asynchroniczny odczyt z stdout, asynchroniczny odczyt z stderr, `WaitForExitAsync`, nie zapomnij opróżnić obu strumieni, albo dostaniesz deadlock. To dobrze znana pułapka, która istnieje od lat.

.NET 11 w końcu naprawia to porządnie.

## RunAndCaptureTextAsync

Kluczowe dodanie: jedna statyczna metoda, która uruchamia proces, przechwytuje stdout i stderr, i czeka na zakończenie bez deadlocka.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

Jedno wywołanie. Bez ręcznego opróżniania strumieni. Bez ostrożnie umieszczonego `WaitForExit`. Jeśli po prostu chcesz uruchomić coś i uzyskać wynik, to jest właśnie to API, którego szukasz.

Jest też `Process.RunAsync` dla przypadku, gdy chcesz czekać na zakończenie bez przechwytywania danych wyjściowych.

## KillOnParentExit

Częsty problem z uruchamianymi procesami: jeśli proces nadrzędny ulega awarii lub zostaje zabity, procesy potomne nadal działają jako sieroty. `KillOnParentExit` pozwala zadeklarować przy uruchamianiu procesu, że proces potomny powinien zostać zakończony, gdy zakończy się proces nadrzędny.

Ta funkcja istniała w specyficznych dla platformy formach (obiekty zadań w Windows, prctl w Linux), ale wymagała p/invoke lub bibliotek zewnętrznych do użycia z .NET. Teraz jest właściwością pierwszej klasy w `ProcessStartInfo`.

## API oparte na SafeProcessHandle

Nowa lekka powierzchnia API jest zbudowana wokół `SafeProcessHandle`, a nie pełnej klasy `Process`. Pełna klasa `Process` niesie ze sobą dużo stanu i trudno ją przycinać — ścieżka `SafeProcessHandle` jest bardziej przyjazna dla trimmera w aplikacjach, które muszą minimalizować rozmiar wyjścia (WASM, natywne AOT).

## Pełna Kontrola nad Dziedziczeniem Uchwytów

Aktualizacja dodaje również szczegółową kontrolę nad tym, które uchwyty dziedziczy proces potomny i jak są przekierowywane standardowe uchwyty. Wcześniej można było przekierowywać stdin/stdout/stderr, ale nie można było określić dokładnie, które uchwyty dziedziczyć na poziomie systemu operacyjnego. Nowe API udostępniają tę kontrolę.

## Dlaczego To Jest Ważne

Klasa `Process` jest używana w toolingu, systemach budowania, uruchomieniach testów i każdej aplikacji, która wywołuje inne pliki wykonywalne. Stara powierzchnia API pochodzi z epoki .NET Framework i pokazywała swój wiek. Nie jest to zmiana łamiąca kompatybilność — stare API nadal działają — ale nowy kod powinien preferować nową powierzchnię.

W przypadku przycinanych aplikacji lub scenariuszy kompilacji AOT, ścieżka `SafeProcessHandle` jest szczególnie mile widziana. Stara klasa `Process` przynosiła dużo kodu z ciężkimi odwołaniami refleksji, który komplikował przycinanie.

Oryginalny post: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
