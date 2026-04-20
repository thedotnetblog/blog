---
title: "Azure Smart Tier jest GA — Automatyczna Optymalizacja Kosztów Blob Storage Bez Reguł Cyklu Życia"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Inteligentna warstwa Azure Blob Storage jest teraz ogólnie dostępna, automatycznie przenosząc obiekty między warstwami hot, cool i cold na podstawie rzeczywistych wzorców dostępu."
tags:
  - azure
  - storage
  - blob-storage
  - cost-optimization
  - cloud-native
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "azure-smart-tier-blob-storage-ga" >}}).*

Jeśli kiedykolwiek spędziłeś czas na dostosowywaniu polityk cyklu życia Azure Blob Storage i obserwowałeś ich rozpadanie się, gdy wzorce dostępu się zmieniły, to jest coś dla Ciebie. Microsoft właśnie ogłosił [ogólną dostępność inteligentnej warstwy](https://azure.microsoft.com/en-us/blog/optimize-object-storage-costs-automatically-with-smart-tier-now-generally-available/) dla Azure Blob i Data Lake Storage.

## Co inteligentna warstwa faktycznie robi

Inteligentna warstwa ciągle ocenia czas ostatniego dostępu do każdego obiektu. Często dostępne dane pozostają w hot, nieaktywne dane przechodzą do cool po 30 dniach, następnie do cold po kolejnych 60 dniach. Gdy dane są ponownie dostępne, są natychmiast promowane z powrotem do hot.

Podczas podglądu Microsoft poinformował, że **ponad 50% pojemności zarządzanej przez inteligentną warstwę automatycznie przesunęło się do chłodniejszych warstw**.

## Dlaczego to ważne dla deweloperów .NET

Scenariusze praktyczne:
- **Telemetria i logi aplikacji** — gorące podczas debugowania, rzadko dostępne po kilku tygodniach
- **Pipeline'y danych i wyniki ETL** — intensywnie dostępne podczas przetwarzania, potem głównie zimne
- **Treści generowane przez użytkowników** — nowe przesłania są gorące, starsze treści stopniowo się schładzają

## Konfiguracja

- **Nowe konta**: Wybierz inteligentną warstwę jako domyślną warstwę dostępu podczas tworzenia konta
- **Istniejące konta**: Zmień domyślną warstwę dostępu do blobów na inteligentną

Obiekty mniejsze niż 128 KiB pozostają w hot i nie ponoszą opłaty monitoringowej.
