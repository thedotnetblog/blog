---
title: "Missiecontrole voor coderingagenten: een geïntegreerde ervaring in VS Code"
description: "VS Code brengt lokale, cloud-, CLI- en externe coderingagenten samen in Agent Sessions zodat ontwikkelaars autonoom werk kunnen volgen, onderbreken en coördineren."
date: 2026-08-07
author: Emiliano Montesdeoca
tags: [agents, orchestration, multi-agent, VS Code, automation, Codex]
slug: unified-agent-experience-mission-control
---

> **Automatische vertaling**: Dit is een geautomatiseerde Nederlandse vertaling van [de Engelse versie]({{< ref "index.md" >}}).

# Missiecontrole voor coderingagenten: een geïntegreerde ervaring in VS Code

Een enkele coderingassistent is gemakkelijk te begrijpen. Meerdere agenten die op verschillende plaatsen werken niet.

Één agent draait lokaal in VS Code. Een ander werkt aan een GitHub-issue in de cloud. Een CLI-agent leeft in de terminal. Een externe coderingagent kan een ander sessiemodel en andere limieten hebben. Zonder een gedeeld overzicht besteden ontwikkelaars meer tijd aan het volgen van werk dan aan het superviseren ervan.

De geïntegreerde agentenervaring van VS Code pakt dit coördinatieprobleem aan met Agent Sessions: één plek om agenten te starten, hun status te zien, hun gesprekken te openen en in te grijpen wanneer het plan verandert.

Dit gaat minder om een ander agent toevoegen en meer om meerdere agenten beheersbaar te maken.

## Één weergave voor verschillende soorten werk

Het bronartikel beschrijft vier verschillende deelnemers: lokale GitHub Copilot, Copilot Coding Agent in de cloud, GitHub Copilot CLI en OpenAI Codex voor in aanmerking komende Copilot-abonnees.

Ze hebben verschillende sterke punten:

- Een lokale agent kan de huidige werkruimte inspecteren en snelle wijzigingen aanbrengen.
- Een cloud-coderingagent kan asynchroon aan een issue werken en een pull request openen.
- Een CLI-agent past in terminal-zware workflows en operationele opdrachten.
- Een ander platform kan een ander model of redeneerstijl bieden.

Agent Sessions geeft die taken een gezamenlijk thuis. U kunt zien wat er draait, wat het doet en waar u het gesprek kunt voortzetten.

Die zichtbaarheid is belangrijk omdat autonoom werk coördinatie niet verwijdert. Het maakt coördinatie een eerste-klassige engineeringtaak.

## Onderbrekingen zijn onderdeel van de workflow

De bron maakt een eenvoudige waarneming: "Het is gebruikelijk om een prompt te sturen en je te realiseren dat je iets belangrijks bent vergeten." Eerder was de keuze vaak wachten of annuleren. Met chat-editors kunt u een actieve sessie openen en informatie toevoegen terwijl de agent werkt.

Dit is meer van echte samenwerking. Vereisten veranderen. Een test onthult een aanname. Een reviewer merkt op dat een API achterwaarts compatibel moet blijven. De bruikbare agent is niet degene die nooit correctie nodig heeft; het is degene die correctie kan opnemen zonder de hele taak kwijt te raken.

Voor .NET-werk kan een onderbreking zo eenvoudig zijn als:

```text
Keep the existing public route unchanged. Add the new behavior behind the application service,
use the existing ProblemDetails convention, and add a test for the old response shape.
```

De instructie is kort omdat de repository al de grotere context bevat. De sessie is de plek om de richting aan te passen, niet om het hele systeem opnieuw uit te leggen.

## Aangepaste agenten veranderen teamgewoonten in rollen

VS Code introduceert ook gespecialiseerde agenten zoals Plan. In plaats van onmiddellijk te implementeren, stelt een planningsagent vragen over bereik, componenten, bibliotheken en beperkingen voordat een implementatiespecificatie wordt opgesteld.

Dit patroon is bruikbaar buiten een ingebouwde agent. Een team kan gerichte rollen definiëren:

- **Onderzoek** verzamelt bewijzen en schrijft een kort besluitkaart.
- **Review** controleert een wijziging tegen repository-conventies.
- **Testen** identificeert gemiste gevallen en stelt een testplan voor.
- **Architectuur** vergelijkt opties zonder bestanden te wijzigen.

Een kleine aangepaste agentdefinitie kan er als volgt uitzien:

```yaml
type: agent
name: plan
description: "Refines vague requests into clear implementation specs"
prompt: |
  Ask about scope, constraints, existing patterns, and edge cases.
  Produce a concise specification before any implementation begins.
```

Het nuttige onderdeel is niet de YAML. Het is de expliciete scheiding van verantwoordelijkheden. Een planningsagent mag niet stilletjes productiegoed bewerken. Een review-agent mag niet het ontwerp herschrijven dat het zou moeten evalueren.

## Subagenten verminderen contextbotsingen

Lange conversaties verzamelen onrelated context. Subagenten bieden een geïsoleerde werkruimte voor een begrensd onderzoekstaak, dan geven ze het resultaat terug aan de hoofdsessie.

Dit is een goed geschikt voor vragen als:

```text
Analyze the API project and recommend an authentication strategy.
Return trade-offs and a decision record. Do not edit files.
```

De hoofdagent blijft gericht op implementatie terwijl de onderzoeksagent een enger vraag aanpakt. Hetzelfde principe is van toepassing op teams: duidelijke delegatie levert betere resultaten op dan het starten van verschillende agenten met overlappende autoriteit.

## De voorbehoud: meer agenten betekenen meer coördinatie

Agent Sessions kan activiteit tonen, maar het kan geen conflicterende eigendom oplossen. Twee agenten die hetzelfde gebied bewerken, kunnen nog steeds een merge-probleem creëren. Een cloudagent en een lokale agent kunnen incompatibele aannames doen. Een aangepaste agent kan een aanbeveling produceren die een ander agent negeert.

Stel grenzen in:

1. Één agent is eigenaar van implementatie voor een gegeven tak.
2. Onderzoeksagenten retourneren artefacten, niet ontraced bewerkingen.
3. Pull requests blijven de review-grens.
4. Agentennamen en prompts stellen vast wat zij mogen veranderen.
5. Sessieuitvoer wordt behouden wanneer deze een belangrijk besluit verklaart.

## Mijn inzicht

De multi-agent toekomst is geen wachtrij van chatvensters. Het is een klein team met rollen, handoffs en verantwoording.

Agent Sessions is waardevol omdat het erkent dat deze realiteit. Het geeft ontwikkelaars een bedieningspaneel voor werk dat al in de editor, terminal en cloud plaatsvindt. De volgende productiviteitswinst zal minder voortkomen uit het hebben van meer agenten en meer uit het leesbaar maken van hun grenzen.

Voor een .NET-team zou ik beginnen met één planningsagent en één implementatieagent. Gebruik de planningsuitvoer als de issue- of pull request-specificatie en laat de implementatieagent binnen die grens werken. Meet herwerkingen voordat u meer rollen toevoegt.

De beste missiecontrole is nog steeds degene die eigendom duidelijk maakt.
