---
title: "NuGet package pruning w .NET 10 to taki rodzaj usprawnienia, który czuć wszędzie"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "Nowe NuGet package pruning w .NET 10 zmniejsza liczbę fałszywie pozytywnych raportów o podatnościach, upraszcza graf restore i poprawia wydajność restore. To jedna z tych zmian platformowych, które po cichu sprawiają, że codzienna praca staje się lepsza."
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

*Ten artykuł został przetłumaczony automatycznie. Oryginał znajdziesz [tutaj]({{< ref "index.md" >}}).*

Niektóre usprawnienia platformowe ekscytują, bo otwierają nowe scenariusze.

Inne ekscytują, bo sprawiają, że istniejące workflow są mniej hałaśliwe, mniej kruche i mniej irytujące.

**NuGet package pruning w .NET 10** zdecydowanie należy do drugiej kategorii, i mówię to jako komplement.

## Dlaczego to ma znaczenie

Jeśli kiedykolwiek mierzyłeś się z szumem związanym z podatnościami transitive, zbyt dużymi grafami restore albo pakietami, które technicznie istnieją, ale nie są naprawdę istotne dla runtime, z którego korzysta twoja aplikacja, ta zmiana trafia w prawdziwy problem.

Pruning pomaga, usuwając z efektywnego grafu zależności pakiety dostarczane przez platformę, gdy runtime już je zapewnia.

To oznacza:

- mniej fałszywie pozytywnych raportów o podatnościach
- czystsze grafy zależności transitive
- mniejszy narzut restore
- bardziej użyteczne wyniki audytu

## Moja opinia

To dokładnie taki rodzaj usprawnienia .NET, który lubię.

Sprawia, że domyślne ustawienia są lepsze, zmniejsza obciążenie mentalne i poprawia zarówno jakość sygnału bezpieczeństwa, jak i codzienne zachowanie tooling.

To zwycięstwo, nawet jeśli nigdy nie trafi na slajd keynote.

Oryginalny wpis: [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
