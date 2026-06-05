---
title: "Agent Skills w Visual Studio: Naucz Copilota Jak Naprawdę Pracuje Twój Zespół"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio obsługuje teraz Agent Skills — wielokrotnie używane zestawy instrukcji, które uczą Copilota specyficznych przepływów pracy, standardów kodowania i konwencji Twojego zespołu. Zdefiniuj raz, stosuj automatycznie."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

Jedno z trwałych frustracji z asystentami programowania AI: dobrze znają ogólne programowanie, ale nie znają specyficznych konwencji *Twojego* zespołu, Twoich wewnętrznych API ani preferowanych wzorców. W każdej sesji ponownie wyjaśniasz kontekst. Agent Skills w Visual Studio zostało zaprojektowane, aby rozwiązać ten problem.

## Czym Są Agent Skills

Wielokrotnie używane zestawy instrukcji — zdefiniowane w plikach `SKILL.md` — które uczą agentów Copilota jak obsługiwać konkretne zadania. Zdefiniuj skill dla "jak uruchomić nasz pipeline budowania", "jak generować boilerplate dla naszej warstwy usług" lub "nasza checklista przeglądu kodu". Agent stosuje skill automatycznie, kiedy jest to istotne.

To nie jest nowa koncepcja (`.github/copilot-instructions.md` istnieje od jakiegoś czasu), ale integracja z Visual Studio czyni je obiektami pierwszej klasy z interfejsem użytkownika do odkrywania.

## Tworzenie Skills w Visual Studio

Zintegrowany przepływ UI: kliknij ikonę narzędzi w Copilot Chat, otwórz panel skills, kliknij `+`. Wybierasz zakres globalny (osobisty) lub na poziomie rozwiązania, wybierasz nazwę, a Visual Studio generuje szablon. Tryb agenta Copilot może następnie pomóc Ci wypełnić szablon — użyj agenta do napisania skilla dla agenta.

Obecnie w kanale Insiders, wkrótce w Release.

Możesz również tworzyć skills ręcznie:

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## Lokalizacje Odkrywania

Skills są automatycznie odkrywane ze standardowych ścieżek:

**Poziom rozwiązania (współdzielony przez repozytorium):** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**Globalny/osobisty (Twój profil użytkownika, dostępny wszędzie):** `~/.copilot/skills/`, `~/.agents/skills/`

Obsługa wielu lokalizacji oznacza, że ta sama konwencja działa z GitHub Copilot, Claude Code i innymi frameworkami agentów — zdefiniuj swoje skills raz, używaj wszędzie.

## Format

Skills są zgodne z formatem [agentskills.io/specification](https://agentskills.io/specification) — specyfikacją opartą na Markdown, czytelną zarówno dla ludzi, jak i maszyn. Możesz dołączyć skrypty, szablony i przykłady obok `SKILL.md`.

## Wartość Praktyczna

Prawdziwa siła nie leży w pojedynczych funkcjach — lecz w kombinacji skills współdzielonych przez zespół (przez `.github/skills/`) i osobistych skills (przez `~/.agents/skills/`). Skills zespołu kodują sposób działania Twojej organizacji. Osobiste skills kodują to, jak konkretnie pracujesz. Agent automatycznie otrzymuje oba konteksty.

Dla organizacji już intensywnie korzystających z Copilota, to znaczący krok w kierunku uczynienia narzędzia naprawdę świadomym specyficznych konwencji bazy kodu zamiast dawania ogólnych porad.

Oryginalny post: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
