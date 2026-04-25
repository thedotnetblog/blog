---
title: "68 Minut Dziennie na Ponowne Tłumaczenie Kodu Copilotowi? Jest na to Sposób"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Context rot jest realny — twój agent AI zaczyna się gubić po 30 turach, a ty płacisz podatek za kompaktowanie co godzinę. auto-memory daje GitHub Copilot CLI chirurgiczną pamięć bez spalania tysięcy tokenów."
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

Znasz ten moment, gdy Twoja sesja Copilot dochodzi do `/compact`, a agent kompletnie zapomina, nad czym pracowałeś? Przez kolejne pięć minut ponownie tłumaczysz strukturę plików, nieudany test i trzy podejścia, które już wypróbowałeś. Potem dzieje się to znowu. I znowu.

Desi Villanueva zmierzył to: **68 minut dziennie** — tylko na ponowną orientację. Nie na pisanie kodu. Nie na review PR-ów. Tylko na ponowne wprowadzanie AI w to, co już wiedziała.

Okazuje się, że istnieje konkretny powód, dla którego tak się dzieje, i konkretne rozwiązanie.

## Kłamstwo okna kontekstu

Twój agent przychodzi z wielką liczbą na pudełku. 200K tokenów. Brzmi imponująco. W praktyce to sufit, a nie gwarancja.

Oto rzeczywiste obliczenia:

- 200K całkowitego contextu
- Minus około 65K na narzędzia MCP załadowane przy starcie (~33%)
- Minus około 10K na pliki instrukcji, takie jak `AGENTS.md` albo `copilot-instructions.md`

To zostawia Ci około **125K, zanim napiszesz choć jedno słowo**. I jest jeszcze gorzej — LLM-y nie degradują się łagodnie, gdy context się zapełnia. Uderzają w ścianę przy około 60% pojemności. Model zaczyna gubić rzeczy wspomniane 30 tur wcześniej, zaprzecza wcześniejszym odpowiedziom i halucynuje nazwy plików, które 10 minut wcześniej z pełnym przekonaniem podał. Branża nazywa to problemem "lost in the middle".

Efektywny limit: **45K tokenów** zanim jakość zacznie spadać. To może oznaczać 20-30 aktywnych tur rozmowy, zanim agent zacznie dryfować. Dlatego trafiasz na `/compact` co 45 minut — nie dlatego, że zużyłeś 200K tokenów, ale dlatego, że model już przy 120K zaczyna się psuć.

## Podatek kompaktacji

Każdy `/compact` zabiera Ci stan przepływu. Jesteś głęboko w sesji debugowania. Wspólny context budował się przez 30 minut. Agent zna strukturę plików, nieudany test i hipotezę. Potem pojawia się ostrzeżenie.

- Zignoruj je → agent stopniowo głupieje i zaczyna halucynować stary stan
- Uruchom `/compact` → agent dostaje dwuzdaniowe streszczenie 30-minutowego dochodzenia

W obu przypadkach przegrywasz. W obu przypadkach opowiadasz swój projekt tak, jakbyś był nowym pracownikiem pierwszego dnia.

Najgorsze? **Pamięć już istnieje**. Copilot CLI zapisuje każdą sesję do lokalnej bazy SQLite w `~/.copilot/session-store.db` — każdy dotknięty plik, każdą turę, każdy checkpoint. Wszystko leży na dysku. Agent po prostu nie potrafi tego odczytać.

## auto-memory: warstwa recall, nie system pamięci

To jest główna idea stojąca za [auto-memory](https://github.com/dezgit2025/auto-memory): nie buduj nowego systemu pamięci — zbuduj warstwę zapytań tylko do odczytu na tym, co już istnieje.

```bash
pip install auto-memory
```

Około 1,900 linii Pythona. Zero zależności. Instaluje się w 30 sekund.

Zamiast zalewać context wynikami grep, dajesz agentowi chirurgiczny dostęp do tego, co naprawdę ma znaczenie:

| Operacja | Tokeny | Co dostajesz |
|----------|--------|--------------|
| `grep -r "auth" src/` | ~5,000–10,000 | 500 wyników, z których większość jest nieistotna |
| `find . -name "*.py"` | ~2,000 | Wszystkie pliki Pythona, bez kontekstu |
| Ponowna orientacja agenta | ~2,000 | Ty tłumaczysz to, co on już powinien wiedzieć |
| **`auto-memory files --json --limit 10`** | **~50** | **10 plików, nad którymi pracowałeś wczoraj** |

To poprawa 200x. Agent omija wykopaliska archeologiczne i od razu trafia do tego, co ważne.

Rekomendowany przepływ: gdy zbliżasz się do użycia 50-70% contextu, uruchom `/clear`, a potem wpisz: "przejrzyj ostatnie sesje, w których omawialiśmy temat X". Zamiast spalać 12K tokenów na ślepe wyszukiwanie, auto-memory wyciąga odpowiedni context w 50.

## Dlaczego to ma znaczenie dla programistów .NET

Jeśli używasz GitHub Copilot CLI do pracy z .NET — scaffoldowanie usług, debugowanie zapytań EF Core, iterowanie nad komponentami Blazor — problem context rot uderza równie mocno. Złożone rozwiązania z wieloma projektami, współdzielonymi bibliotekami i głębokimi łańcuchami wywołań to dokładnie ten rodzaj codebase'u, w którym agent najszybciej gubi wątek.

Instrukcja instalacji pokazuje, jak skierować na to Copilot CLI. To jednorazowa konfiguracja.

Szczerze? Odzyskanie 68 minut dziennie to nie jest drobny tweak jakości życia. To prawie 6 godzin tygodniowo.

## Podsumowanie

Context rot to realne ograniczenie architektoniczne, a nie bug, który po prostu zostanie załatany. auto-memory omija je, dając agentowi tani i precyzyjny mechanizm recall zamiast kosztownego i hałaśliwego ponownego eksplorowania. Jeśli prowadzisz poważny development wspierany przez AI z GitHub Copilot CLI, ta 30-sekundowa instalacja jest tego warta.

Sprawdź: [auto-memory na GitHubie](https://github.com/dezgit2025/auto-memory). Oryginalny wpis Desi Villanuevy: [I Wasted 68 Minutes a Day Re-Explaining My Code](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/).