---
title: "La història d'observabilitat a ROI de Foundry és el que necessiten les plataformes d'agents serioses"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: "L'últim anunci de Foundry sobre observabilitat importa perquè connecta traça, avaluació, optimització i ROI en un únic bucle operatiu per a agents d'IA."
tags:
  - Microsoft Foundry
  - AI
  - Agents
  - Observability
  - Evaluations
---

*Aquesta publicació s'ha traduït automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Si els agents d'IA han de viure en producció, l'observabilitat no pot quedar-se en logs i traces.

Per això la nova història de Foundry d'observabilitat a ROI sembla important.

El missatge real no és "hem afegit més panells".

El missatge real és que les plataformes d'agents serioses necessiten un bucle operatiu continu:

- traçar què ha passat
- avaluar si ha estat bo
- optimitzar el que necessita feina
- connectar el resultat amb el valor de negoci

Aquesta és una història molt més sòlida que el bla bla habitual de plataforma.

## La frase clau de l'article original ho diu tot

L'article original comença amb una línia a la qual crec que tot equip que construeixi agents hauria de prestar atenció:

> "Llançar un agent d'IA és la part fàcil. Mantenir-lo precís, segur i responsable en producció és on els equips es queden encallats."

Això és exactament cert.

Ja hem passat la fase en què la pregunta principal era "puc fer que un agent faci una cosa interessant?"

La pregunta més difícil i més valuosa és:

**puc operar la cosa un cop comença a interactuar amb usuaris reals, eines reals i costos reals?**

Aquí és on Foundry intenta empènyer la conversa.

## Per què això importa més que una altra demo d'agent

Molts anuncis d'agents d'IA encara se centren en la creació: construeix l'agent, connecta les eines, enruta les tasques, publica la interfície.

Tot això està bé.

Però les qüestions operatives són el punt en què la majoria de sistemes seriosos acaben sent sostenibles o experiments cars:

- què està fent realment l'agent en producció?
- ha fet la cosa correcta?
- empitjora amb el temps?
- és massa car per al valor que crea?
- quins canvis de configuració han millorat de debò la qualitat?

Per això crec que l'anunci de Foundry és més important que un resum de funcionalitats típic. Intenta definir un bucle d'Agent DevOps, no només una història de creació d'agents.

## El bucle de quatre parts és el producte real aquí

L'article organitza bàsicament la plataforma al voltant de quatre capacitats:

- Trace
- Evaluate
- Monitor
- Optimize

Aquesta és la forma correcta.

De fet, diria que qualsevol plataforma que vulgui ser presa seriosament per a càrregues de treball d'agents en producció acabarà necessitant les quatre.

Traçar sol no és suficient.

Avaluar sol no és suficient.

Optimitzar sense proves és només endevinar.

I parlar de ROI sense telemetria normalment és teatre.

## L'angle d'interoperabilitat és especialment intel·ligent

Una de les decisions més encertades de l'anunci és que Foundry no fa veure que tots els agents es construiran en un sol framework.

L'article original parla explícitament d'estendre el tracing i les avaluacions a través de:

- LangChain
- LangGraph
- OpenAI SDK
- Microsoft Agent Framework
- frameworks personalitzats via OpenTelemetry

Això és important.

Perquè el lock-in de plataforma és una de les maneres més ràpides de fer que una història d'operacions que en teoria era útil acabi sent menys atractiva.

Si els equips poden conservar les seves opcions de framework i, alhora, obtenir telemetria i superfícies d'avaluació de nivell producció, la fricció baixa molt.

## L'avaluació amb rúbriques pot acabar important més del que la gent espera

La part d'avaluació amb rúbriques també val la pena destacar-la.

Crec que aquesta és una de les incorporacions més pràctiques de tot el post.

Per què? Perquè el que és "bo" depèn del context.

L'article diu que l'avaluació amb rúbriques genera "criteris d'avaluació sensibles al context a partir del comportament previst del teu agent". Aquesta és exactament la direcció que necessiten aquests sistemes.

La puntuació de qualitat genèrica és útil.

Però al final els equips necessiten puntuar els agents segons els seus propis estàndards:

- to
- finalització de tasques
- adhesió a polítiques
- expectatives de latència
- límits de cost
- regles de negoci específiques del domini

Aquí és on l'avaluació comença a ser operativament significativa en lloc de només acadèmicament interessant.

## El ROI és la part més incòmoda, i per això importa

També penso que la part de ROI de l'anunci és important precisament perquè és incòmoda.

L'article fa la pregunta directament:

> "aquest agent val el que costa?"

Aquesta pregunta s'esquiva molt en les converses d'IA.

Però és la pregunta correcta.

Si la plataforma realment pot connectar cost, finalització de tasques, temps estalviat i traces de producció en un sol lloc, això dona a l'enginyeria i al lideratge un llenguatge compartit molt millor.

I sincerament, aquest llenguatge compartit és molt necessari.

## La meva opinió

Aquest és un dels millors anuncis a nivell de plataforma del lot perquè se centra a operar agents, no només a construir-los.

I aquí és on de debò comença la part difícil.

Les plataformes d'IA més fortes dels pròxims anys no seran només les que tinguin accés a més models o més demos. Seran les que ajudin els equips a traçar el comportament, avaluar resultats, optimitzar amb seguretat i justificar el cost amb proves.

Aquesta història de Foundry intenta avançar exactament en aquesta direcció.

Per això val la pena prendre-la seriosament.

Publicació original: [Build 2026: From observability to ROI for AI agents on any framework](https://devblogs.microsoft.com/foundry/build-2026-from-observability-to-roi-for-ai-agents-on-any-framework/)