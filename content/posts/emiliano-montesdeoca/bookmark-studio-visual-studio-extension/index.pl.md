---
title: "Bookmark Studio Wprowadza Nawigację Opartą na Slotach i Udostępnianie do Zakładek Visual Studio"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Nowe rozszerzenie Bookmark Studio Madsa Kristensena dodaje do zakładek Visual Studio nawigację po slotach za pomocą klawiatury, menedżer zakładek, kolory, etykiety i możliwości eksportu/udostępniania."
tags:
  - visual-studio
  - extensions
  - productivity
  - developer-tools
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "bookmark-studio-visual-studio-extension" >}}).*

Zakładki w Visual Studio zawsze były... w porządku. Ustawiasz jedną, przechodzisz do następnej, zapominasz która jest która.

Mads Kristensen właśnie [wydał Bookmark Studio](https://devblogs.microsoft.com/visualstudio/bookmark-studio-evolving-bookmarks-in-visual-studio/), eksperymentalne rozszerzenie wypełniające luki, na które pewnie natknąłeś się regularnie używając zakładek.

## Nawigacja oparta na slotach

Główna nowość: zakładki można teraz przypisywać do slotów 1–9 i bezpośrednio do nich skakać za pomocą `Alt+Shift+1` do `Alt+Shift+9`. To zmienia zakładki z "mam gdzieś jakieś zakładki" na "Slot 3 to mój kontroler API, Slot 5 to warstwa serwisów, Slot 7 to testy."

## Menedżer zakładek

Nowe okno narzędziowe pokazuje wszystkie zakładki w jednym miejscu z filtrowaniem po nazwie, pliku, lokalizacji, kolorze lub slocie.

## Organizacja z etykietami, kolorami i folderami

Zakładki mogą opcjonalnie mieć etykiety i kolory oraz być grupowane w foldery. Wszystkie metadane są przechowywane per solucja.

## Eksport i udostępnianie

Bookmark Studio pozwala eksportować zakładki jako zwykły tekst, Markdown lub CSV:
- Dołączanie ścieżek zakładek do opisów pull requestów
- Udostępnianie śladów dochodzenia współpracownikom
- Przenoszenie zestawów zakładek między repozytoriami

Pobierz ze [sklepu Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.BookmarkStudio).
