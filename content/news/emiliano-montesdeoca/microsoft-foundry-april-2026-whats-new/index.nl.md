---
title: "Microsoft Foundry april 2026: Foundry Local GA, GPT-5.5, CodeAct met Hyperlight"
date: 2026-06-02
author: "Emiliano Montesdeoca"
description: "De Foundry-samenvatting van april is uitgebreid: Foundry Local bereikt GA, GPT-5.5 arriveert, Agent Framework krijgt OpenTelemetry-tracing, CodeAct draait Python in Hyperlight micro-VM's en het Agent Monitoring Dashboard landt."
tags:
  - Foundry
  - Azure
  - AI
  - Agent Framework
  - GPT-5.5
---

Een drukke maand voor Microsoft Foundry. Hier zijn de belangrijkste aankondigingen.

## Foundry Local algemeen beschikbaar

Foundry Local — Microsoft's cross-platform lokale AI-runtime — is overgegaan van preview naar GA op Windows, macOS (Apple Silicon) en Linux x64. Productieklare lokale modelinferentie met een ontwikkelaarsvriendelijke SDK. Versie 1.1 voegt ondersteuning toe voor transcriptie, embeddings en de Responses API.

## GPT-5.5

Het nieuwste model in de GPT-5-familie is nu beschikbaar in Foundry. Standaardquotum voor Tier 5- en Tier 6-abonnementen. Als u met eerdere GPT-5-varianten heeft gewerkt, is het de moeite waard dit te evalueren voor uw gebruiksscenario.

## Agent Framework-tracing in Foundry

Deze maand komen twee tracingfuncties als preview beschikbaar:

**Microsoft Agent Framework-tracing** — MAF-agents kunnen nu OpenTelemetry-traces exporteren naar Foundry. Debug agentgedrag, volg meertraps-uitvoeringen, leg latentie en fouten bloot bij tool-aanroepen. Dit vult een echte lacune: weten *wat de agent daadwerkelijk deed in productie*, niet alleen wat het teruggaf.

**Gehoste agenttracing** — Sessies, tool-aanroepen en uitvoerstappen van gehoste agents verschijnen ook in Foundry-traces. Hetzelfde observability-verhaal wordt uitgebreid naar de gehoste laag.

## CodeAct met Hyperlight (Alpha)

Dit is de technisch meest interessante toevoeging: Agent Framework kan nu Python-code uitvoeren binnen [Hyperlight](https://github.com/hyperlight-dev/hyperlight) micro-virtuele machines.

CodeAct is het patroon waarbij agents Python-code genereren en uitvoeren als tool. De voor de hand liggende zorg is beveiliging — u voert door het model gegenereerde code uit. Hyperlight's micro-VM's bieden isolatie op procesniveau met bijna native opstarttijden, waardoor sandbox-code-uitvoering praktisch wordt zonder de overhead van volledige containers of VM's.

Voor agentworkflows die code-uitvoering vereisen, is dit een aanzienlijke beveiligingsverbetering ten opzichte van het uitvoeren van code in het hostproces.

## Agent Monitoring Dashboard (Preview)

Een uniform operationeel dashboard dat tokengebruik, latentie, uitvoersuccespercentage en evaluatorscores in één weergave combineert. Het verschil met gewone observability-dashboards: het bevat evaluatieresultaten naast operationele metrics, zodat u "agent is trager geworden" kunt correleren met "evaluatorscores zijn gedaald" — of kunt bevestigen dat ze niets met elkaar te maken hebben.

## Aangepaste evaluatoren voor continue evaluatie (Preview)

U kunt nu uw eigen code- of prompt-gebaseerde evaluatoren in de continue evaluatiepijplijn brengen. Voorheen was continue evaluatie beperkt tot ingebouwde evaluatoren. Aangepaste evaluatoren stellen u in staat teamspecifieke kwaliteitsnormen toe te passen in de productiemonitoringlus.

## Agentinventaris in het Control Plane

De Operate-weergave in het Foundry Control Plane toont nu alle ondersteunde agents in uw abonnement: Foundry-agents, Azure SRE Agent, Logic Apps-agentlussen en geregistreerde aangepaste agents. Één weergave om te begrijpen wat waar is geïmplementeerd.

Origineel bericht: [What's new in Microsoft Foundry | April 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)
