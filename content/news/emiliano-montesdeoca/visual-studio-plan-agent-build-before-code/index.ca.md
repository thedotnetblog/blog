---
title: "El nou Plan agent de Visual Studio resol un problema molt real del flux de treball d'IA"
date: 2026-06-11
author: "Emiliano Montesdeoca"
description: "El nou Plan agent de Visual Studio importa perquè crea una etapa de planificació estructurada abans de la implementació, que és exactament el que sovint necessiten les funcions grans i les refactoritzacions."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI Agents
  - Planning
  - Developer Experience
---

> *Aquest article s'ha traduït automàticament. L'original és [aquí]({{< ref "visual-studio-plan-agent-build-before-code.md" >}}).* 

Un dels fluxos de treball més frustrants de programació amb IA és quan la implementació comença massa de pressa.

El codi fins i tot pot ser tècnicament correcte, però resol la versió equivocada del problema que tenies al cap.

Volies una refactorització. Va començar una reescriptura.
Volies una millora acotada. Va tocar mitja aplicació.
Volies parlar de les opcions. Va saltar directament als canvis de fitxer.

Per això el nou **Plan agent** de Visual Studio és una addició tan útil.

## Això resol un problema real de flux de treball, no només un problema estètic

La publicació original descriu una situació molt familiar: "**El codi no està malament... simplement no és el que volies.**"

Aquesta frase és perfecta.

Perquè el punt feble de molta feina assistida per IA no és si el model pot produir codi. És si el flux de treball crea prou espai per acordar la forma desitjada de la feina abans de començar la implementació.

Això és especialment important per a:

- funcions grans
- bases de codi desconegudes
- refactoritzacions no trivials
- canvis sensibles a l'arquitectura
- feina que necessita revisió de l'equip abans de començar a editar

En aquestes situacions, anar directament a implementar sovint és el moviment equivocat.

## Planificar no és sobrecàrrega quan la tasca és real

Crec que de vegades els equips subestimen quant temps perden quan comencen a implementar massa aviat.

Si l'agent:

- toca els fitxers equivocats
- tria l'enfocament equivocat
- passa per alt una restricció clau
- ignora un cas límit necessari

llavors el començament "ràpid" acaba sent un flux de treball més lent en conjunt.

Per això m'agrada aquesta funció.

Fa espai per a:

- preguntes de clarificació
- redacció del pla
- edició directa del pla
- compartir el pla abans que comencin els canvis de codi

Això no és burocràcia. Sovint és simplement bona enginyeria.

## El fitxer de pla en markdown és una tria intel·ligent

Un detall que m'agrada especialment és que cada pla es desa a `.copilot/plans/plan-{title}.md`.

Això fa que el pas de planificació sigui tangible.

Vol dir que el pla no queda atrapat dins d'un fil de conversa. Es converteix en una cosa que pots:

- revisar
- editar
- versionar mentalment
- discutir amb l'equip
- passar a la implementació de manera més deliberada

Això fa que la funció sembli molt més seriosa que un simple preàmbul temporal abans de generar codi.

## Aquí és on els fluxos d'IA comencen a respectar el procés de l'equip

Crec que aquest és un dels senyals més forts que aquestes eines estan madurant.

Els millors fluxos d'IA per a desenvolupadors no són els que eliminen tots els passos intermedis. Són els que milloren els passos intermedis adequats.

I la planificació és un d'aquests passos.

Si el pla és fort, implementar és més fàcil.
Si el pla és feble, la implementació es torna sorollosa.

Aquesta funció ho reconeix directament.

## La meva opinió

Això no és només una simplicitat d'IA.

És una millora del flux de treball.

I per a funcions reals i refactoritzacions reals, és exactament el tipus de millora que pot estalviar molt de churn innecessari, soroll de revisió i rework del tipus "això no és el que volia dir".

Crec que cada vegada més experiències d'agents acabaran necessitant una cosa així.

Visual Studio hi ha arribat abans d'una manera que se sent útil.

Publicació original: [Planifica abans de construir: presentem el Plan agent a Visual Studio](https://devblogs.microsoft.com/visualstudio/plan-before-you-build-introducing-the-plan-agent-in-visual-studio/)