---
title: "Agent Skills in Visual Studio: Leer Copilot Hoe Jouw Team Echt Werkt"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio ondersteunt nu Agent Skills — herbruikbare instructiesets die Copilot de specifieke workflows, coderingsnormen en conventies van jouw team bijbrengen. Eén keer definiëren, automatisch toepassen."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

Een van de aanhoudende frustraties met AI-codeerassistenten: ze kennen algemeen programmeren goed maar kennen niet de specifieke conventies van *jouw* team, je interne API's of je favoriete patronen. Elke sessie leg je de context opnieuw uit. Agent Skills in Visual Studio is ontworpen om dit te verhelpen.

## Wat Agent Skills Zijn

Herbruikbare instructiesets — gedefinieerd in `SKILL.md`-bestanden — die Copilot-agents leren hoe ze specifieke taken moeten afhandelen. Definieer een skill voor "hoe we onze buildpipeline uitvoeren", "hoe we boilerplate genereren voor onze servicelaag" of "onze code review checklist". De agent past de skill automatisch toe wanneer dat relevant is.

Dit is geen nieuw concept (`.github/copilot-instructions.md` bestaat al een tijdje), maar de Visual Studio-integratie maakt ze tot eersteklas objecten met een discovery-gebruikersinterface.

## Skills Aanmaken in Visual Studio

De geïntegreerde UI-stroom: klik op het gereedschapspictogram in Copilot Chat, open het skillspaneel, klik op `+`. Je kiest globaal (persoonlijk) of oplossingsbreed bereik, kiest een naam en Visual Studio genereert een sjabloon. De Copilot Agent-modus kan je dan helpen het sjabloon in te vullen — gebruik de agent om de skill voor de agent te schrijven.

Momenteel in het Insiders-kanaal, binnenkort beschikbaar in Release.

Je kunt ook handmatig skills aanmaken:

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

## Discovery-Locaties

Skills worden automatisch ontdekt vanuit standaardpaden:

**Oplossingsbreed (gedeeld via repo):** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**Globaal/persoonlijk (jouw gebruikersprofiel, overal beschikbaar):** `~/.copilot/skills/`, `~/.agents/skills/`

De multi-locatie ondersteuning betekent dat dezelfde conventie werkt met GitHub Copilot, Claude Code en andere agent-frameworks — definieer je skills eenmaal, gebruik ze overal.

## Het Formaat

Skills volgen het [agentskills.io/specification](https://agentskills.io/specification)-formaat — een op Markdown gebaseerde specificatie die zowel leesbaar is voor mensen als parseerbaar door machines. Je kunt scripts, sjablonen en voorbeelden opnemen naast de `SKILL.md`.

## Praktische Waarde

De echte kracht ligt niet in de afzonderlijke functies — maar in de combinatie van team-gedeelde skills (via `.github/skills/`) en persoonlijke skills (via `~/.agents/skills/`). Teamskills coderen hoe jouw organisatie dingen doet. Persoonlijke skills coderen hoe jij specifiek werkt. De agent krijgt automatisch beide contexten.

Voor organisaties die Copilot al intensief gebruiken, is dit een betekenisvolle stap om het hulpmiddel daadwerkelijk bewust te maken van de specifieke codebase-conventies in plaats van generiek advies te geven.

Originele post: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
