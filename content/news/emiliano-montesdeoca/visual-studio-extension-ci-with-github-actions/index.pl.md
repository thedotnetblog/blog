---
title: 'Zespoły Rozszerzeń Visual Studio Powinny Przestać Wydawać z Przyzwyczajenia i Zacząć Wydawać przez Pipeline'
date: 2026-07-23
author: 'Emiliano Montesdeoca'
description: 'Powtarzalny przepływ GitHub Actions dla wersjonowania i publikacji VSIX jest teraz wystarczająco prosty, że ręczne kroki wydania są trudne do uzasadnienia.'
tags:
  - visual-studio
  - vsix
  - github-actions
  - ci-cd
  - developer-tooling
---

Oryginalne źródło: [Automating your Visual Studio extension builds with GitHub Actions](https://devblogs.microsoft.com/visualstudio/automating-your-visual-studio-extension-builds-with-github-actions/)

Jeśli utrzymujesz rozszerzenia Visual Studio i wciąż wykonujesz znaczące części wydania ręcznie, to jest twój sygnał do modernizacji.

Przepływ pracy pokazany w tym wpisie jest celowo praktyczny: stempluj wersję, buduj, publikuj artefakty testowe do galerii, a następnie publikuj stabilne bity do Marketplace. Bez ciężkiej ceremonii platformowej, tylko deterministyczne zachowanie wydania.

To, co lubię najbardziej, to to, że wersjonowanie jest traktowane jako stan pipeline'u, a nie element listy kontrolnej przed wydaniem. Ta jedna decyzja eliminuje zaskakującą liczbę błędów: niedopasowane metadane, nieaktualne wersje assembly i niespójne notatki wydania.

Podział między publikacją do galerii a publikacją do Marketplace jest również operacyjnie dojrzały. Zespoły potrzebują miejsca na szybkie kompilacje walidacyjne, które nie niosą semantyki oficjalnego wydania. Wypychanie wszystkiego bezpośrednio do Marketplace jest wysokotarciowe i zachęca do ryzykownych skrótów.

### Silny wzorzec wydania dla zespołów rozszerzeń

- **Na pull requesty i commity do main**, produkuj artefakty CI VSIX i publikuj do galerii dla testerów.
- **Na oznaczone wydania (tagi)**, publikuj podpisane i zweryfikowane pakiety do Marketplace.
- **Utrzymuj obsługę tokenów minimalną** z dedykowanymi sekretami i zakresami o najmniejszych uprawnieniach.

Moje stanowcze zdanie: **ekosystemy rozszerzeń pozostają w tyle za ekosystemami aplikacji w dyscyplinie CI**, ponieważ małe zespoły zakładają, że ręczne przepływy są do zarządzania. Są do zarządzania, dopóki nie przestaną być. Jedna pospieszna łatka, jeden zepsuty pakiet, jedna zapomniana aktualizacja manifestu i zaufanie spada.

Te wielokrotnego użytku akcje są użyteczne, ponieważ kodują powtarzalną logikę wydania raz i pozwalają zespołom skupić się na jakości rozszerzenia zamiast na mechanice pakowania.

Wciąż wymagany jest osąd inżynieryjny. Powinieneś bramkować publikację do Marketplace za kontrolami jakości i traktować manifesty publikacji jako audytowane artefakty wydania. Ale podstawowa złożoność pipeline'u jest teraz wystarczająco niska, że ręczne wydania to w większości dług techniczny.

Jeśli prowadzisz rozwój rozszerzeń, **ustandaryzuj to teraz we wszystkich repozytoriach**. Zyskasz lepszą identyfikowalność, łatwiejsze wdrożenie i mniej wąskich gardeł zależnych od jednej osoby.

### Sugerowane wdrożenie

- **Zacznij od budowania plus publikacji do galerii** dla jednego rozszerzenia.
- **Wprowadź stemplowanie wersji** po zweryfikowaniu konwencji manifest-źródło.
- **Dodaj publikację do Marketplace** dopiero po wdrożeniu zarządzania sekretami i bram wydania.

Nie chodzi o gonienie za modą DevOps. Chodzi o niezawodność dla ludzi, którzy instalują twoje narzędzia i oczekują, że aktualizacje będą działać.

Stabilne ekosystemy rozszerzeń buduje się tak samo jak stabilne aplikacje: z nudną, powtarzalną automatyzacją, która usuwa ludzkie zgadywanie.