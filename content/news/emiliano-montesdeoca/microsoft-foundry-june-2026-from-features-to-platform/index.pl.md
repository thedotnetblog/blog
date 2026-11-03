---
title: "Microsoft Foundry Czerwiec 2026: Od Dostarczania Funkcji do Zarządzanej Platformy Agentowej"
date: 2026-07-18
author: Emiliano Montesdeoca
description: "Czerwcowe aktualizacje Foundry sygnalizują przejście platformy: dystrybucja, narzędzia, pamięć, obserwowalność i optymalizacja zbiegają się w gotowy dla przedsiębiorstw stos operacji agentowych."
tags:
  - Microsoft Foundry
  - Agents
  - Toolboxes
  - Observability
  - AI Platform
  - Enterprise AI
---

Czerwcowa fala Foundry 2026 to nie tylko kolejny miesięczny przegląd. Oznacza przejście dojrzałości od „buduj fajnych agentów" do „prowadź agentów jako zarządzane systemy korporacyjne". To rozróżnienie ma znaczenie większe niż jakakolwiek pojedyncza funkcja.

Oryginalne źródło: https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/

Trzy aktualizacje definiują tę zmianę. Po pierwsze, publikowanie agentów do Microsoft 365 Copilot i Teams osiągnęło GA, co przenosi dystrybucję z niestandardowych projektów integracyjnych na opiniowany pas wdrożeniowy. Po drugie, Toolboxes zyskały silniejsze mechanizmy wykrywania i kontroli wykonania, w tym wyszukiwanie narzędzi i rutyny. Po trzecie, obserwowalność plus optymalizacja stały się zamkniętą pętlą, a nie późniejszym dodatkiem.

Moje zdanie: to najważniejszy wzorzec w wydaniu. **Śledzenie, ewaluacja, optymalizacja i kontrolowane wdrożenie** tworzą minimalny opłacalny model operacyjny dla systemów niedeterministycznych. Jeśli masz tylko jeden z tych elementów, masz telemetrię lub strojenie, a nie zarządzanie.

Claude GA wewnątrz Foundry jest również strategiczny, ale nie głównie ze względu na jakość modelu. Większą wartością jest integracja korporacyjna: uwierzytelnianie Entra, RBAC, ciągłość rozliczeń i dopasowanie polityk. Zespoły przechodzące z bezpośrednich endpointów modeli do Foundry powinny postrzegać to jako konsolidację operacyjną, a nie tylko zmianę dostawcy.

Agenci Autopilot są obiecujący, ale organizacje powinny podchodzić do nich z trzeźwymi wyborami architektonicznymi. Współpraca w przestrzeni współdzielonej w Teams może odblokować produktywność, ale szybko podnosi złożoność tożsamości, uprawnień i odpowiedzialności. Zacznij od ograniczonych zakresów i ścisłych punktów zatwierdzeń przed szerokim wdrożeniem.

Praktyczne rekomendacje:

- **Jeśli już jesteś w pilocie**, priorytetem jest instrumentacja przed rozszerzeniem możliwości. Podłącz śledzenie GenAI najpierw. Następnie ustanów zestawy ewaluacyjne powiązane z wynikami biznesowymi, a nie ogólnymi metrykami modeli. Dopiero potem uruchamiaj pętle optymalizacyjne i przepływy promocji.
- **Dla agentów z dużą liczbą toolboxów**, włącz wyszukiwanie narzędzi wcześnie, aby zmniejszyć szum kontekstowy i ryzyko wyboru złego narzędzia w miarę wzrostu katalogów.
- **Dla agentów z pamięcią**, zdefiniuj TTL i politykę przechowywania z góry. Pamięć bez kontroli cyklu życia staje się długiem zgodnościowym.

Najbardziej stanowczy wniosek, jaki mogę wyciągnąć, jest taki: Foundry teraz mniej dotyczy „który model wybrać?" a bardziej **„czy mogę prowadzić zachowanie agenta jako zarządzany cykl życia?"** Zespoły, które dobrze odpowiedzą na drugie pytanie, łatwo dostosują się do rotacji modeli. Zespoły skupione na rankingach modeli będą odbudowywać kruche stosy co kwartał.

Czerwcowe wydanie wyjaśnia jedną rzecz. Foundry staje się **platformą operacyjną dla systemów AI**, a nie tylko zestawem narzędzi programistycznych. To trudniejszy produkt do zbudowania i znacznie bardziej wartościowy do przyjęcia.