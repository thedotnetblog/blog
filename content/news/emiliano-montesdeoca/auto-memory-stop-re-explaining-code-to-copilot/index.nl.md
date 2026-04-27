---
title: "68 Minuten per Dag Code Opnieuw Uitleggen aan Copilot? Daar is een Oplossing voor"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Context rot is echt — je AI-agent raakt na 30 turns de draad kwijt, en je betaalt elk uur de compactiebelasting. auto-memory geeft GitHub Copilot CLI chirurgisch geheugen zonder duizenden tokens te verbranden."
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

Ken je dat moment waarop je Copilot-sessie `/compact` bereikt en de agent compleet vergeet waar je mee bezig was? De volgende vijf minuten leg je opnieuw de mapstructuur, de mislukte test en de drie benaderingen die je al hebt geprobeerd uit. Daarna gebeurt het weer. En weer.

Desi Villanueva timede het: **68 minuten per dag** — alleen al aan heroriëntatie. Niet aan code schrijven. Niet aan PR's reviewen. Alleen de AI weer bijpraten over wat hij al wist.

Blijkt dat daar een concrete reden voor is, en een concrete oplossing.

## De leugen van het contextvenster

Je agent komt met een groot getal op de doos. 200K tokens. Klinkt enorm. In de praktijk is het een bovengrens, geen garantie.

Dit is de echte rekensom:

- 200K totale context
- Minus ongeveer 65K voor MCP-tools die bij startup worden geladen (~33%)
- Minus ongeveer 10K voor instructiebestanden zoals `AGENTS.md` of `copilot-instructions.md`

Dat laat je ongeveer **125K over voordat je ook maar een woord typt**. En het wordt erger — LLM's degraderen niet netjes terwijl de context volloopt. Ze lopen vast rond 60% van de capaciteit. Het model begint dingen te verliezen die 30 turns geleden zijn genoemd, spreekt eerdere antwoorden tegen en hallucineert bestandsnamen die het 10 minuten eerder nog vol vertrouwen noemde. De industrie noemt dit het "lost in the middle"-probleem.

Effectieve limiet: **45K tokens** voordat de kwaliteit inzakt. Dat zijn misschien 20-30 actieve gespreksbeurten voordat de agent begint af te dwalen. Daarom zit je elke 45 minuten op `/compact` — niet omdat je 200K tokens hebt volgepropt, maar omdat het model al bij 120K begint te verpieteren.

## De compactiebelasting

Elke `/compact` kost je flow state. Je zit diep in een debugsessie. De gedeelde context is in 30 minuten opgebouwd. De agent kent de mapstructuur, de mislukte test en de hypothese. Dan verschijnt de waarschuwing.

- Negeer het → de agent wordt geleidelijk dommer en gaat oude state hallucinerend invullen
- Draai `/compact` → de agent krijgt een samenvatting van twee alinea's van een onderzoek van 30 minuten

In beide gevallen verlies je. In beide gevallen ben je je eigen project aan het navertellen alsof je een nieuwe collega op dag één bent.

Het venijnige deel? **Het geheugen bestaat al**. Copilot CLI schrijft elke sessie weg naar een lokale SQLite-database op `~/.copilot/session-store.db` — elk aangeraakt bestand, elke turn, elk checkpoint. Alles staat op schijf. De agent kan het alleen niet lezen.

## auto-memory: een recall-laag, geen geheugensysteem

Dat is het kernidee achter [auto-memory](https://github.com/dezgit2025/auto-memory): bouw geen nieuw geheugensysteem — bouw een read-only querylaag bovenop wat er al is.

```bash
pip install auto-memory
```

Ongeveer 1.900 regels Python. Geen afhankelijkheden. Installeert in 30 seconden.

In plaats van de context te overspoelen met grep-resultaten, geef je de agent chirurgische toegang tot wat echt belangrijk is:

| Operatie | Tokens | Wat je krijgt |
|----------|--------|---------------|
| `grep -r "auth" src/` | ~5,000–10,000 | 500 resultaten, waarvan de meeste irrelevant zijn |
| `find . -name "*.py"` | ~2,000 | Alle Python-bestanden, zonder context |
| Heroriëntatie van de agent | ~2,000 | Jij legt uit wat hij eigenlijk al had moeten weten |
| **`auto-memory files --json --limit 10`** | **~50** | **De 10 bestanden waaraan je gisteren hebt gewerkt** |

Dat is een verbetering van 200x. De agent slaat het archeologische graafwerk over en gaat meteen naar wat ertoe doet.

De aanbevolen flow: als je richting 50-70% contextgebruik gaat, draai dan `/clear` en prompt vervolgens met: "bekijk de laatste sessies waarin we onderwerp X bespraken". In plaats van 12K tokens te verbranden aan blinde zoekopdrachten, haalt auto-memory de relevante context in 50 tokens op.

## Waarom dit belangrijk is voor .NET-ontwikkelaars

Als je GitHub Copilot CLI gebruikt voor .NET-werk — services scaffolden, EF Core-queries debuggen, itereren op Blazor-componenten — dan raakt het context rot-probleem je net zo hard. Complexe oplossingen met meerdere projecten, gedeelde libraries en diepe call chains zijn precies het soort codebase waar de agent het snelst de draad kwijt raakt.

De installgids legt uit hoe je Copilot CLI erop laat wijzen. Het is een eenmalige setup.

Eerlijk? 68 minuten per dag terugkrijgen is geen klein quality-of-life-tweak. Dat is bijna 6 uur per week.

## Afsluiting

Context rot is een echte architecturale beperking, geen bug die zomaar gepatcht gaat worden. auto-memory omzeilt dat door je agent een goedkope, precieze recall-mechaniek te geven in plaats van een dure, lawaaierige herverkenning. Als je serieus AI-ondersteund ontwikkelt met GitHub Copilot CLI, is die installatie van 30 seconden het waard.

Bekijk het: [auto-memory op GitHub](https://github.com/dezgit2025/auto-memory). Oorspronkelijke post van Desi Villanueva: [I Wasted 68 Minutes a Day Re-Explaining My Code](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/).