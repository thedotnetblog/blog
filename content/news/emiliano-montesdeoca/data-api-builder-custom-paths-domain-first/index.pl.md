---
title: 'Niestandardowe Ścieżki Data API Builder Pozwalają Projektować API dla Ludzi, a Nie Tabel'
date: 2026-07-17
author: 'Emiliano Montesdeoca'
description: 'Złożone ścieżki REST w DAB to mała funkcja o dużym wpływie architektonicznym dla projektowania API zorientowanego domenowo.'
tags:
  - data-api-builder
  - azure-sql
  - rest-api
  - api-design
  - dotnet
---

Oryginalne źródło: [Compose your API surface with Data API builder custom paths](https://devblogs.microsoft.com/azure-sql/data-api-builder-custom-rest-paths/)

Nowe wsparcie **złożonych ścieżek REST** w Data API Builder może wyglądać jak drobne ulepszenie konfiguracyjne, ale w rzeczywistości rozwiązuje długotrwałe napięcie w projektowaniu API: przeciekanie topologii bazy danych do projektu publicznych endpointów.

Domyślne trasy oparte na encjach są świetne do szybkiego startu. Często są błędne dla długoterminowych API produktowych. Prawdziwe systemy potrzebują struktur tras, które pasują do koncepcji biznesowych, granic własności i modeli mentalnych konsumentów.

Dlatego ta zmiana DAB ma znaczenie. Możesz zachować wygodę generowanego API, prezentując czystszą powierzchnię zorientowaną domenowo.

Moje stanowcze zdanie jest proste: **jeśli struktura ścieżek twojego API odzwierciedla surowe nazwy tabel w produkcji**, zwykle optymalizujesz pod wygodę backendu kosztem klarowności dla klienta.

Dzięki niestandardowym ścieżkom zespoły mogą modelować lepsze granice, takie jak powierzchnie sprzedażowe, rozliczeniowe, wsparcia lub specyficzne dla partnera. To nie zastępuje właściwego zarządzania API, ale daje użytkownikom DAB praktyczny sposób na dopasowanie projektu tras do języka produktu.

### Praktyczne wskazówki dla zespołów wdrażających tę funkcję

- **Zdefiniuj politykę nazewnictwa** przed dodawaniem ścieżek ad-hoc. Niespójne podsegmenty stają się długoterminowym bałaganem.
- **Mapuj endpointy na konteksty ograniczone**, a nie schematy organizacyjne. Zespoły się zmieniają; semantyka domeny powinna być stabilna.
- **Traktuj strukturę ścieżek jako część strategii wersjonowania** i dokumentuj przełomowe zmiany jawnie.
- **Waliduj zachowanie autoryzacji** wzdłuż niestandardowych struktur tras, aby klarowność tras szła w parze z klarownością bezpieczeństwa.

Doceniam w DAB ogólnie **model dźwigni**: dostajesz paginację, filtrowanie, projekcję i inne mechanizmy endpointów bez pisania powtarzalnego kodu kontrolerów. Niestandardowe ścieżki czynią tę dźwignię bardziej gotową do produkcji, redukując jeden z największych zarzutów architektów API.

Jest jeden **zastrzeżenie**. Lepsza kompozycja ścieżek może kusić zespoły do ujawniania zbyt wiele zbyt szybko, ponieważ generowanie wydaje się łatwe. Bariery ochronne wciąż mają znaczenie: utrzymuj celowe ujawnianie encji, stosuj politykę centralnie i unikaj budowania przypadkowych publicznych kontraktów z wewnętrznych eksperymentów schematów.

Dla organizacji .NET pod presją dostarczania, ta funkcja jest odblokowaniem produktywności, jeśli używana z dyscypliną. Możesz działać szybciej niż ręcznie wykonane warstwy API, zachowując spójną i przyjazną biznesowo powierzchnię endpointów.

**Konkluzja:** Niestandardowe ścieżki DAB nie polegają na upiększaniu URL-i. Chodzi o **odzyskanie intencji projektowej API** przy zachowaniu wydajności operacyjnej generowanych endpointów.