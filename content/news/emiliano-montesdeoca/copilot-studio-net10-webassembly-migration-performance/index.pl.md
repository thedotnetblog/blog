---
title: "Jak Copilot Studio Przemigrował do .NET 10 WebAssembly i Stał się 20% Szybszy"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "Ulepszenia .NET 10 WASM nie są tylko dla nowych projektów. Oto co zmierzył Copilot Studio po aktualizacji z .NET 8: automatyczne odciskanie palców, WasmStripILAfterAOT domyślnie i prawdziwe liczby wydajności wykonania."
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

Zespół Copilot Studio zrobił coś, o co ciekawili się wszyscy programiści Blazor WASM: faktycznie zaktualizowali aplikację produkcyjną z .NET 8 do .NET 10 i zmierzyli wyniki. Post dzieli się konkretnymi liczbami, co jest rzadkie i naprawdę przydatne.

## Aktualizacja Była Nudna (To Dobra Rzecz)

Aktualizacja docelowego frameworka, odświeżenie odwołań do pakietów, naprawienie zmian przełomowych. To wszystko. Build .NET 10 teraz działa na produkcji. Sama migracja nie była interesującą częścią — zmiany w .NET 10 są nią.

## Automatyczne Odciski Palców Zasobów

Wcześniej dystrybucja aplikacji WASM oznaczała pisanie niestandardowych skryptów do zmiany nazw opublikowanych zasobów z hashami SHA256 dla cache-bustingu. Copilot Studio miał skrypt PowerShell robiący dokładnie to — zmiana nazw plików, wstrzykiwanie atrybutów `integrity` do loadera JavaScript, zarządzanie wszystkim ręcznie.

W .NET 10 wszystko to jest wbudowane. Opublikowane zasoby są automatycznie oznaczane odciskiem palca, importowane bezpośrednio z `dotnet.js` i weryfikowane pod kątem integralności bez ręcznej interwencji. Zespół usunął skrypt zmiany nazw.

Mała zmiana w zakresie, znaczące zmniejszenie złożoności.

## WasmStripILAfterAOT Jest Teraz Domyślnie Włączony

W .NET 8 usuwanie IL ze skompilowanych AOT zestawów było opt-in. W .NET 10 jest to domyślne. Po kompilacji AOT oryginalny bytecode IL jest usuwany z wyjścia — nie jest potrzebny w czasie wykonywania, a jego zachowanie niepotrzebnie zwiększało rozmiar pakietu.

Copilot Studio używa specyficznej optymalizacji: dostarcza zarówno silnik JIT (szybki start), jak i silnik AOT (maksymalna wydajność w stanie ustalonym), ładując oba równolegle i przekazując z JIT do AOT, gdy jest gotowy. Deduplikuje również pliki identyczne między dwoma silnikami.

Nowe zachowanie usuwania IL oznacza, że zestawy AOT nie pasują już bit po bicie do swoich odpowiedników JIT, więc mniej plików jest deduplikowanych:
- .NET 8: 59 współdzielonych plików
- .NET 10: 22 współdzielone pliki

Wynik netto: rozmiar pakietu około 15% większy dla silnika AOT. Pobieranie AOT jest ~6% wolniejsze na szybkim LAN, ~17% wolniejsze na 4G. Ale wszystko to dzieje się w tle po tym, jak aplikacja jest już interaktywna.

## Liczby Wydajności

To jest ważna część:

- **~20% szybciej** przy pierwszym wywołaniu (zimna ścieżka)
- **~5% szybciej** przy kolejnych wywołaniach (ciepła ścieżka)

Ulepszenia są najbardziej widoczne w "dużych botach" — dużych, złożonych agentach, gdzie dominuje kod skompilowany AOT. Dla prostszych przepływów pracy zysk jest mniejszy.

## Jeśli Nadal Jesteś na .NET 8

Historia migracji jest naprawdę prosta: zaktualizuj `<TargetFramework>`, odśwież odwołania do pakietów, usuń niestandardowe skrypty odciskania palców, a automatycznie skorzystasz z `WasmStripILAfterAOT`. Jeśli kompilujesz AOT, spodziewaj się podobnych zysków wydajności.

Uwaga z posta: jeśli ładujesz środowisko uruchomieniowe .NET WASM wewnątrz `WebWorker`, ustaw `dotnetSidecar = true` podczas inicjalizacji.

Oryginalny post: [Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
