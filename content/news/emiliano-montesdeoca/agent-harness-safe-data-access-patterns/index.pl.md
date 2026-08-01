---
title: 'Prawdziwym Zwycięstwem UX dla Agentów Jest Bezpieczna Autonomia, Nie Maksymalna Autonomia'
date: 2026-07-11
author: 'Emiliano Montesdeoca'
description: 'Dostęp do plików, zatwierdzenia i projekt pamięci to praktyczna triada dla godnego zaufania zachowania agentów w produkcji.'
tags:
  - microsoft-agent-framework
  - ai-agents
  - approvals
  - security
  - dotnet
  - python
---

Oryginalne źródło: [Agent Harness: Working with your data, safely](https://devblogs.microsoft.com/agent-framework/agent-harness-working-with-your-data-safely/)

To jeden z bardziej użytecznych wpisów inżynieryjnych o agentach w tym roku, ponieważ odrzuca powszechną pułapkę autonomii na pokaz. Zamiast tego skupia się na tym, jak agenci powinni operować wokół prawdziwych danych użytkownika i rzeczywistych konsekwencji.

Trzy bloki konstrukcyjne podkreślone tutaj są dokładnie właściwe.

- **Dostęp do plików** daje agentom użyteczne ugruntowanie w danych należących do użytkownika.
- **Bramkowanie zatwierdzeniami** zapobiega cichemu wykonywaniu działań o konsekwencjach.
- **Trwała pamięć** unika powtarzalnych interakcji bez poświęcania kontroli.

Większość zespołów przesadnie inwestuje w szerokość narzędzi i niedoinwestowuje w semantykę uprawnień. To odwrotność właściwego podejścia. Agent z dziesięcioma narzędziami i słabymi granicami zatwierdzeń jest mniej wartościowy niż agent z trzema narzędziami i przewidywalnymi punktami kontroli.

Najlepszym praktycznym wzorcem w tym artykule jest **warstwowa strategia zatwierdzeń**:

- **Zawsze wymagaj zatwierdzenia** dla narzędzi wysokiego ryzyka, takich jak transakcje czy operacje niszczące.
- **Automatycznie zatwierdzaj** odczyty niskiego ryzyka, aby zachować płynność.
- **Używaj zakresowych stałych zatwierdzeń** dla powtarzalnych, zaufanych działań w ramach sesji.

Tworzy to zdrowy gradient ryzyka. Użytkownicy nie są przerywani dla nieszkodliwych odczytów, ale wciąż są w pętli, gdy konsekwencje stają się kosztowne lub nieodwracalne.

Podoba mi się też wyraźny podział między **pamięcią plikową** a **pamięcią Foundry**. Zespoły powinny przestać próbować zmuszać jeden model pamięci do rozwiązywania każdego problemu. Surowe, jawne artefakty plikowe są doskonałe dla widocznych dla użytkownika stanów, takich jak raporty i listy obserwowane. Ekstrakcja pamięci na poziomie faktów jest lepsza dla preferencji i kontekstu konwersacyjnego. Połączenie obu daje lepsze wyniki niż udawanie, że którykolwiek z nich jest wystarczający.

Moje stanowcze zdanie: przyszłość jakości agentów będzie mierzona mniej sprytnymi promptami, a bardziej **ergonomią bezpieczeństwa**. Jeśli twoje prośby o zatwierdzenie są hałaśliwe, użytkownicy klikają je na ślepo. Jeśli granice pamięci są niejasne, użytkownicy przestają ufać asystentowi. Jeśli domyślne uprawnienia dostępu do danych są permisywne, zespoły bezpieczeństwa zamkną projekt.

Dla zespołów .NET i Python przyjmujących ten wzorzec, kluczowym ruchem jest **traktowanie callbacków polityk i reguł zatwierdzania jako podstawowej logiki biznesowej**, wersjonowanej i testowanej jak każdy inny krytyczny kod. Nie zostawiaj ich jako ad-hoc lambd pogrzebanych w przykładach.

## Konkluzja

Systemy agentowe, które zdobywają zaufanie, to nie te, które robią najwięcej. To te, które robią dokładnie to, co zamierzał użytkownik, ni mniej, ni więcej, z jasnymi punktami przerwania, gdy ryzyko wzrasta.

To jest różnica między imponującym demem a oprogramowaniem, któremu ludzie są skłonni powierzyć prawdziwą pracę.