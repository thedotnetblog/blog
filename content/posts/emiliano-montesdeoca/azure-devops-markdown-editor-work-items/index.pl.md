---
title: "Azure DevOps W Końcu Naprawia UX Edytora Markdown, na Który Wszyscy Narzekali"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Edytor Markdown Azure DevOps dla elementów roboczych zyskuje wyraźniejsze rozróżnienie między trybem podglądu a trybem edycji. To mała zmiana, która naprawia naprawdę irytujący problem w przepływie pracy."
tags:
  - azure-devops
  - devops
  - productivity
  - developer-tools
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "azure-devops-markdown-editor-work-items" >}}).*

Jeśli używasz Azure Boards, pewnie już to przeżyłeś: czytasz opis elementu roboczego, może przeglądasz kryteria akceptacji, i przypadkowo klikasz dwa razy. Bum — jesteś w trybie edycji. Nie chciałeś niczego edytować. Po prostu czytałeś.

Dan Hellem [ogłosił poprawkę](https://devblogs.microsoft.com/devops/improving-the-markdown-editor-for-work-items/), i to jedna z tych zmian, która brzmi banalnie, ale faktycznie usuwa prawdziwe tarcie z codziennego przepływu pracy.

## Co się zmieniło

Edytor Markdown dla pól tekstowych elementów roboczych otwiera się teraz domyślnie w **trybie podglądu**. Możesz czytać i wchodzić w interakcje z treścią — śledzić linki, przeglądać formatowanie — bez obaw o przypadkowe wejście w tryb edycji.

Kiedy faktycznie chcesz edytować, klikasz ikonę edycji na górze pola. Kiedy skończyłeś, explicite wychodzisz z powrotem do trybu podglądu.

## Dlaczego to ważne bardziej niż brzmi

[Wątek opinii społeczności](https://developercommunity.visualstudio.com/t/Markdown-editor-for-work-item-multi-line/10935496) na ten temat był długi. Zachowanie podwójnego kliknięcia-do-edycji zostało wprowadzone z edytorem Markdown w lipcu 2025, a skargi zaczęły się niemal natychmiast.

Nowe domyślne zachowanie respektuje najbardziej powszechny wzorzec interakcji: czytasz elementy robocze znacznie częściej niż je edytujesz.

## Status wdrożenia

To jest już wdrażane dla podzbioru klientów i rozszerzy się na wszystkich w ciągu najbliższych dwóch do trzech tygodni.
