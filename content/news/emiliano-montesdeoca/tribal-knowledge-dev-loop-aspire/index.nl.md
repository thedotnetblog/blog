---
title: "Je dev loop zit vol tribal knowledge, en Aspire geeft het juiste antwoord"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Een nieuwe Aspire-post maakt een sterk punt: veel teams missen niet tools, maar een consistent applicatiemodel dat verborgen operationele kennis omzet in iets dat mensen, scripts en agents echt kunnen gebruiken."
tags:
  - Aspire
  - Developer Experience
  - AI
  - Dev Loop
  - .NET
---

> *Dit artikel is automatisch vertaald. Lees het origineel [hier]({{< ref "tribal-knowledge-dev-loop-aspire.md" >}}).* 

Dit is misschien wel een van de belangrijkste Aspire-posts om te begrijpen *waarom* het product ertoe doet.

Niet omdat het een grote nieuwe feature aankondigt.

Maar omdat het een probleem benoemt dat bijna elk engineeringteam heeft gevoeld, en niet elk team goed heeft beschreven:

**de dev loop zit vol tribal knowledge.**

Die uitspraak komt aan omdat hij waar is.

## Het probleem is niet een gebrek aan tools

De kern van het originele artikel is uitstekend: teams missen vaak geen infrastructuur, scripts, dashboards of commands.

Wat ze missen is een samenhangend model dat alle verborgen operationele kennis rond de applicatie omzet in iets zichtbaars en herhaalbaars.

De echte architectuur van veel apps leeft in:

- shell history
- verspreide scripts
- README-fragmenten
- Slack-threads
- die ene senior engineer die de volgorde van handelingen kent

Dat is geen duurzame dev loop voor mensen.

En zeker niet voor agents.

## De quote die voor mij de hele post samenvat

Er staat één zin in het originele artikel die de bredere boodschap heel goed vangt:

> "**Applications already exist as systems. Aspire makes those systems explicit, because explicit systems scale better than tribal knowledge.**"

Dat is de hele case in één regel.

En eerlijk gezegd is het een van de sterkste éénregelige verklaringen van Aspire die ik tot nu toe heb gezien.

## Waarom dit nu meer telt dan een jaar geleden

Ik denk dat deze post vooral goed landt in het huidige moment omdat AI-assisted development de kosten van ambiguïteit verandert.

Mensen kunnen onvolledige systemen verrassend goed compenseren.

We onthouden:

- welk script eerst moet draaien
- welke environment variable stiekem nodig is
- welk terminal meestal de nuttige logs laat zien
- welke service twee keer opnieuw gestart moet worden om redenen die niemand heeft gedocumenteerd

Agents zijn veel slechter in dat soort verborgen operationele folklore.

Dus als we willen dat agents echt nuttig worden in echte repositories, moeten we het systeem explicieter maken, niet minder.

Daarom vind ik de Aspire-insteek belangrijk.

## De echte waarde van Aspire is niet alleen orchestration

Een veelgemaakte fout is Aspire alleen zien als distributed app launcher of lokale orchestration-helper.

Dat is te klein gedacht.

De sterkere waardepropositie is dat Aspire de applicatie geeft:

- een model
- een shape
- named resources
- expliciete dependencies
- health- en operations-surface
- commands die zowel mensen als automation kunnen begrijpen

Dat verandert de dev loop meer dan mensen soms beseffen.

Want zodra de app geen stapel impliciete conventies meer is en een systeem met een echt model wordt, worden meerdere dingen tegelijk makkelijker:

- onboarding
- debugging
- herhaalbare setup
- CI-consistentie
- AI-assisted workflows

Dat is veel leverage uit één designkeuze.

## Ik vind vooral de "commands as first-class operations" invalshoek sterk

Een ander punt uit het originele artikel dat meer aandacht verdient, is de overgang van README-instructies naar resource-attached commands.

Dat is een deceptief grote verschuiving.

In plaats van te zeggen:

> voer dit script uit, dan dat, en misschien nog iets anders als het eerste faalt

kun je operations direct in de context van de app modelleren.

Dat maakt ze voor mensen makkelijker te ontdekken.

En het betekent dat agents intentie niet uit proza hoeven te raden.

Dat is het soort ding dat een applicatie verandert van "operable als je hem al kent" naar "operable by design".

## Wat ik hieruit zou halen als team lead

Als ik de dev loop van mijn eigen team door deze lens zou bekijken, zou ik een paar directe vragen stellen:

- hoe afhankelijk is onze setup van geheugen?
- hoeveel kritieke dev-acties bestaan alleen in docs of chat-threads?
- hoe vaak lopen nieuwe contributors vast op onzichtbaar systeemgedrag?
- zou een automation tool of coding agent onze app-topologie uit de repo zelf kunnen begrijpen?

Als het antwoord op die laatste vraag "bij lange na niet" is, dan moet deze post een nuttige snaar raken.

## Mijn mening

Dit is een heel sterk kader voor de echte waarde van Aspire.

Niet alleen orchestration.

Het is het app-model expliciet genoeg maken zodat het systeem makkelijker te bedienen, te begrijpen en te automatiseren is.

Dat is belangrijk voor mensen.
Het is belangrijk voor teams.
En het is nog belangrijker nu zoveel moderne development richting agent-assisted workflows beweegt.

Dit is precies het soort artikel dat helpt uitleggen waarom Aspire steeds relevanter aanvoelt dan alleen het .NET-marketinglabel.

Originele post: [Je dev loop zit vol tribal knowledge](https://devblogs.microsoft.com/aspire/dev-loop-tribal-knowledge/)---
title: "Je dev-loop zit vol impliciete kennis, en Aspire heeft het juiste antwoord"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Een nieuwe Aspire-post maakt een sterk punt: veel teams missen geen tooling, ze missen een consistent applicatiemodel dat verborgen operationele kennis omzet in iets dat mensen, scripts en agents echt kunnen gebruiken."
tags:
  - Aspire
  - Developer Experience
  - AI
  - Dev Loop
  - .NET
---

> *Dit artikel is automatisch vertaald. Lees het origineel [hier]({{< ref "tribal-knowledge-dev-loop-aspire.md" >}}).* 

Dit is misschien wel een van de belangrijkste Aspire-posts om te begrijpen *waarom* het product ertoe doet.

Niet omdat het een enorme nieuwe functie aankondigt.

Maar omdat het een probleem benoemt dat bijna elk engineeringteam heeft gevoeld en niet elk team goed heeft beschreven:

**de dev-loop zit vol impliciete kennis.**

Die zin blijft hangen omdat hij waar is.

## Het probleem is niet een gebrek aan tools

De kern van het originele artikel is uitstekend: teams missen vaak geen infrastructuur, scripts, dashboards of commands.

Wat ze missen, is een coherent model dat alle verborgen operationele kennis rond de applicatie omzet in iets zichtbaars en herhaalbaars.

De echte architectuur van veel apps leeft in:

- shell history
- verspreide scripts
- README-fragmenten
- Slack-threads
- die ene senior engineer die de volgorde van handelingen kent

Dat is geen duurzame dev-loop voor mensen.

En zeker ook niet voor agents.

## Het citaat dat volgens mij de hele post samenvat

Er staat één zin in het bronartikel die de bredere boodschap heel goed vangt:

> "**Applicaties bestaan al als systemen. Aspire maakt die systemen expliciet, omdat expliciete systemen beter schalen dan impliciete kennis.**"

Dat is de hele case in één regel.

En eerlijk gezegd is het een van de sterkste uitleggen in één zin van Aspire die ik tot nu toe heb gezien.

## Waarom dit nu belangrijker is dan een jaar geleden

Ik denk dat deze post vooral nu goed landt, omdat AI-assisted development de kosten van ambiguïteit verandert.

Mensen kunnen verrassend goed omgaan met onvolledige systemen.

We onthouden:

- welk script eerst moet draaien
- welke environment variable stiekem nodig is
- welke terminal meestal de nuttige logs laat zien
- welke service twee keer opnieuw gestart moet worden om redenen die niemand heeft gedocumenteerd

Agents zijn veel slechter in dit soort verborgen operationele folklore.

Dus als we willen dat agents echt nuttig worden in echte repositories, moeten we het systeem explicieter maken, niet minder.

Daarom vind ik deze Aspire-framing belangrijk.

## De echte waarde van Aspire is niet alleen orchestration

Een veelgemaakte fout met Aspire is dat het alleen wordt gezien als een distributed app launcher of een lokale orchestration-helper.

Dat is te klein gedacht.

De sterkere value proposition is dat Aspire de applicatie geeft:

- een model
- een vorm
- benoemde resources
- expliciete afhankelijkheden
- health- en operations-oppervlakken
- commands die zowel mensen als automation kunnen begrijpen

Dat verandert de dev-loop meer dan mensen soms doorhebben.

Want zodra de app geen stapel impliciete conventies meer is en een systeem met een echt model wordt, worden meerdere dingen in één keer makkelijker:

- onboarding
- debugging
- herhaalbare setup
- CI-consistentie
- AI-assisted workflows

Dat is veel hefboomwerking uit één ontwerpkeuze.

## Ik vind vooral de invalshoek "commands als first-class operations" sterk

Een ander punt uit de oorspronkelijke post dat volgens mij meer aandacht verdient, is de stap van README-instructies naar aan resources gekoppelde commands.

Dat is een misleidend grote verschuiving.

In plaats van te zeggen:

> draai dit script, daarna dat, en misschien dit andere als het eerste faalt

kun je operaties direct in de applicatiecontext modelleren.

Dat betekent dat mensen ze makkelijker kunnen ontdekken.

En het betekent dat agents intentie niet uit proza hoeven te raden.

Dat is precies het soort ding dat een applicatie verandert van "operable als je het al kent" naar "operable by design".

## Wat ik hieruit zou meenemen als team lead

Als ik mijn eigen dev-loop door deze lens zou bekijken, zou ik een paar directe vragen stellen:

- hoeveel van onze setup hangt af van geheugen?
- hoeveel kritieke dev-acties bestaan alleen in docs of chat-threads?
- hoe vaak lopen nieuwe contributors vast op onzichtbaar systeemgedrag?
- zou een automation-tool of coding agent onze app-topologie uit de repo zelf kunnen begrijpen?

Als het antwoord op die laatste vraag "zeker niet" is, dan moet deze post op een nuttige plek raken.

## Mijn mening

Dit is een zeer sterke framing van Aspire's echte waarde.

Het gaat niet alleen om orchestration.

Het gaat erom het applicatiemodel expliciet genoeg te maken zodat het systeem makkelijker te bedienen, te begrijpen en te automatiseren is.

Dat is belangrijk voor mensen.
Het is belangrijk voor teams.
En het is nog belangrijker nu zoveel moderne ontwikkeling richting agent-assisted workflows beweegt.

Dit is precies het soort artikel dat helpt uitleggen waarom Aspire steeds relevanter aanvoelt dan alleen het .NET-marketinglabel.

Originele publicatie: [Je dev-loop zit vol impliciete kennis](https://devblogs.microsoft.com/aspire/dev-loop-tribal-knowledge/)