---
title: "VS Code 1.128 Stawia Jasną Tezę: Okno Agentów Staje Się Nową Powierzchnią Roboczą"
date: 2026-07-25
author: Emiliano Montesdeoca
description: "VS Code 1.128 zamienia przepływy agentowe z nowości w codzienną ergonomię dzięki sesjom wieloczatowym, wsparciu wizji GA i głębszym kontrolom hosta/sesji."
tags:
  - VS Code
  - AI Agents
  - Copilot
  - Developer Experience
  - Multimodal
  - Productivity
---

Visual Studio Code 1.128 to znaczące wydanie nie z powodu jednej zabójczej funkcji, ale dlatego, że kilka zmian zbiega się w jednym kierunku: rozwój agentowy wewnątrz edytora staje się ustrukturyzowany, równoległy i operacyjnie zarządzalny.

Oryginalne źródło: https://code.visualstudio.com/updates/v1_128

Najważniejsze jest **bogatsze zachowanie multi-chat** w sesjach hosta agenta, w tym czaty peerskie, forki i równoczesne tury w ramach jednej sesji nadrzędnej. To dokładnie to, czego doświadczeni programiści potrzebują podczas eksploracji alternatywnych implementacji lub dzielenia zadań na ścieżki weryfikacji. Odzwierciedla prawdziwą pracę inżynieryjną, która rzadko jest liniowa.

Moje zdanie: to pierwsze wydanie VS Code, w którym okno Agentów wydaje się mniej panelem czatu, a bardziej powierzchnią orkiestracji przestrzeni roboczej.

Szybkie czaty bez wybranego obszaru roboczego również mają większe znaczenie, niż się wydaje. Obniżają tarcie dla pytań koncepcyjnych lub architektonicznych, jednocześnie utrzymując sesje związane z projektem odrębne. To rozdzielenie może zmniejszyć bałagan i zachować integralność kontekstu dla przepływów modyfikujących kod.

**Copilot Vision osiągające GA** to kolejny punkt zwrotny. Gdy obrazy i PDF-y są normalnymi danymi wejściowymi do czatu, zadania obciążone dokumentacją i UI stają się znacznie płynniejsze. Zespoły powinny teraz myśleć o multimodalnym kontekście jako domyślnej możliwości, a nie zaawansowanym dodatku.

Są też praktyczne implikacje platformowe. **Wsparcie BYOK** w scenariuszach hosta agenta, konfigurowalne parametry próbkowania modeli i domyślne ustawienia modeli narzędziowych wskazują na rosnącą dojrzałość dla korporacyjnego zarządzania modelami. Organizacje z rygorystycznymi wymaganiami dostawców mogą teraz kształtować zachowanie z drobniejszą kontrolą zamiast domyślnych ustawień jeden-rozmiar-dla-wszystkich.

### Rekomendacje dla zespołów wdrażających 1.128

- **Zdefiniuj konwencje dla rozgałęzień czatu i nazewnictwa** w sesjach wieloczatowych, aby równoległa eksploracja nie stała się szumem konwersacyjnym.
- **Zachęcaj programistów do utrzymywania jednego czatu dla implementacji** i jednego dla testów lub analizy awarii.
- **Używaj szybkich czatów celowo** do pytań niezwiązanych z repozytorium.
- **Jeśli prowadzisz endpointy BYOK**, ustanów bazowe profile temperatura/top_p na klasę obciążenia i udokumentuj wyjątki.
- **Zdecyduj, czy przepływy narzędziowe** powinny działać na modelach dostarczonych przez Copilot czy BYOK, aby uniknąć przypadkowych luk w zachowaniu.
- **Rozważ skróty na poziomie systemu operacyjnego strategicznie.** Możliwość wyzwalania poleceń VS Code w całym systemie może poprawić przepływ dla zaawansowanych użytkowników, ale niezarządzany rozrost skrótów może zaszkodzić spójności między zespołami.

## Konkluzja

VS Code 1.128 nie tylko dodaje funkcje. Zacieśnia mechanikę współpracy agentowej w prawdziwych pętlach programistycznych. Edytory, które wygrają w następnym cyklu, będą tymi, które traktują interakcje agentowe jako **pierwszorzędne prymitywy przepływu pracy**, a nie eksperymenty na pasku bocznym. To wydanie pokazuje, że VS Code rozumie ten wyścig.