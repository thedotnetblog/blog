---
title: "El Patró Handoff: Quan Un Agent No És Suficient"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "El patró d'orquestració Handoff de Microsoft Agent Framework permet als agents decidir qui gestiona el pròxim torn — sense perdre el context de la conversa ni trencar les regles de topologia."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

En algun moment, cada sistema multi-agent supera un router simple. El primer signe sol ser quan un agent especialista ha de fer una pregunta de seguiment, o s'adona a meitat d'un torn que un altre agent hauria de continuar. Un pipeline fix falla allà. Un router d'un sol pas falla allà.

Exactament és el problema per al qual el patró d'orquestració Handoff a Microsoft Agent Framework està dissenyat.

## Com Funciona Handoff

El desenvolupador declara un graf: aquí hi ha els agents, aquí hi ha les arestes entre ells. El framework fa la resta — sintetitza una eina handoff per aresta de sortida i la injecta a cada agent. Quan un agent decideix cedir el control, crida l'eina. El framework aplica la topologia.

Tres coses fan que això sigui diferent de simplement fer que els agents es cridin entre si:

1. **Una transcripció compartida** — l'agent receptor veu l'historial complet de la conversa. Sense tornar a començar des de zero.
2. **Aplicació de topologia** — un agent només pot fer handoff a destins declarats. Els errors de routing es detecten durant l'autoria, no a producció.
3. **Terminació natural** — quan l'agent actiu acaba el seu torn sense cridar una eina handoff, el flux de treball cedeix a l'usuari. Sense polling, sense condicions de sortida explícites.

## Un Exemple Mínim

A .NET, construir un flux de treball handoff té aquest aspecte:

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triage pot enviar a qualsevol especialista. Tots dos especialistes poden enviar de tornada a triage. El graf és compatible amb l'acíclic però admet arestes posteriors quan les necessites ("necessito més informació" → tornar a la recerca).

## Quan Utilitzar Handoff (i Quan No)

Handoff és una bona opció quan:

- **La propietat pot canviar a meitat de la conversa** — un agent pot adonar-se que és l'especialista equivocat
- **Les arestes posteriors importen** — potser cal revisitar un pas anterior sense reiniciar
- **Les decisions de routing són matisat** — la decisió de fer handoff és contextual i és millor que la prengui el model que predicats tipats

*No* és l'elecció correcta quan:

- El teu pipeline és fix i seqüencial — fes servir el flux de treball `Sequential` per a això
- Cada pas és independent — els agents que comparteixen una transcripció quan només un la necessitava és simplement soroll
- Necessites garanties estrictes de processament — el no-determinisme del routing impulsat pel model no és el que vols

## Arestes Posteriors i Human-in-the-Loop

Una de les formes més interessants que Handoff permet són les arestes posteriors reals. Un agent pot decidir "no tinc prou informació" i enrutar de tornada a un pas de recerca — no amb un bucle codificat, sinó perquè el model decideix que és la decisió correcta.

Les interaccions human-in-the-loop també es composen de manera natural. Quan un especialista necessita l'input de l'usuari, el flux de treball cedeix a l'usuari a través del bucle de torns per defecte, recull la resposta i reprèn amb context complet. L'agent mai ha perdut la conversa.

## Conclusió

Handoff és un d'aquells patrons que sembla simple però permet molt un cop interioritzat: routing descentralitzat, context compartit, topologia aplicada, terminació natural. És el proper pas correcte quan els teus agents comencen a dir "en realitat, algú altre hauria de gestionar això."

Llegeix el recorregut complet a la publicació original: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
