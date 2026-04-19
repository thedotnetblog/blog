---
title: "El servidor Azure DevOps MCP arriba a Microsoft Foundry: què significa això per als vostres agents d'IA"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "El servidor Azure DevOps MCP ja està disponible a Microsoft Foundry. Connecteu els vostres agents d'IA directament als fluxos de treball de DevOps (elements de treball, repositoris, canalitzacions) amb uns quants clics."
tags:
  - azure
  - devops
  - ai
  - mcp
  - foundry
---

MCP (Model Context Protocol) ha tingut un moment. Si heu estat seguint l'ecosistema d'agents d'IA, probablement heu notat que els servidors MCP apareixen a tot arreu, donant als agents la possibilitat d'interaccionar amb eines i serveis externs mitjançant un protocol estandarditzat.

Ara el [Servidor MCP d'Azure DevOps està disponible a Microsoft Foundry](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/), i aquesta és una d'aquestes integracions que et fa pensar en les possibilitats pràctiques.

## Què està passant realment aquí

Microsoft ja va llançar l'Azure DevOps MCP Server com a [vista prèvia pública](https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview), això és el propi servidor MCP. La novetat és la integració de Foundry. Ara podeu afegir l'Azure DevOps MCP Server als vostres agents de Foundry directament des del catàleg d'eines.

Per a aquells que encara no estiguin familiaritzats amb Foundry: és la plataforma unificada de Microsoft per crear i gestionar aplicacions i agents basats en IA a escala. Accés al model, orquestració, avaluació, desplegament, tot en un sol lloc.

## Configurant-lo

La configuració és sorprenentment senzilla:

1. Al vostre agent de Foundry, aneu a **Afegeix eines** > **Catàleg**
2. Cerqueu "Azure DevOps"
3. Seleccioneu el servidor Azure DevOps MCP (visualització prèvia) i feu clic a **Crea**
4. Introduïu el nom de la vostra organització i connecteu-vos

Això és tot. El vostre agent ara té accés a les eines d'Azure DevOps.

## Controlar a què pot accedir el vostre agent

Aquesta és la part que agraeixo: no us enganxeu amb un enfocament de tot o res. Podeu especificar quines eines estan disponibles per al vostre agent. Per tant, si només voleu que llegeixi elements de treball però no toqui les canalitzacions, podeu configurar-ho. Principi de privilegis mínims, aplicat als vostres agents d'IA.

Això és important per als escenaris empresarials en què no voleu que un agent activi accidentalment una canalització de desplegament perquè algú li va demanar que "ajudés amb el llançament".

## Per què això és interessant per als equips.NET

Penseu en què permet això a la pràctica:

- **Ajudants de planificació de sprint**: agents que poden extreure elements de treball, analitzar dades de velocitat i suggerir capacitat de sprint
- **Bots de revisió de codi**: agents que entenen el vostre context de relacions públiques perquè poden llegir els vostres repositoris i els elements de treball enllaçats.
- **Resposta a incidents**: agents que poden crear elements de treball, consultar implementacions recents i correlacionar errors amb canvis recents
- **Incorporació de desenvolupadors** — "En què he de treballar?" obté una resposta real recolzada per dades reals del projecte

Per als equips.NET que ja utilitzen Azure DevOps per als seus pipelines CI/CD i la gestió de projectes, tenir un agent d'IA que pugui interactuar directament amb aquests sistemes és un pas important cap a una automatització útil (no només chatbot com a servei).

## La imatge MCP més gran

Això forma part d'una tendència més àmplia: els servidors MCP s'estan convertint en la manera estàndard en què els agents d'IA interactuen amb el món exterior. Els veiem per a GitHub, Azure DevOps, bases de dades, API SaaS, i Foundry s'està convertint en el centre on s'uneixen totes aquestes connexions.

Si esteu creant agents a l'ecosistema.NET, val la pena prestar atenció a MCP. El protocol està estandarditzat, les eines estan madurant i la integració de Foundry el fa accessible sense haver de connectar manualment les connexions del servidor.

## Tancant

El servidor Azure DevOps MCP a Foundry està en vista prèvia, així que espereu que evolucioni. Però el flux de treball bàsic és sòlid: connecteu-vos, configureu l'accés a les eines i deixeu que els vostres agents treballin amb les vostres dades de DevOps. Si ja sou a l'ecosistema de Foundry, això és a uns quants clics. Prova-ho i mira quins fluxos de treball pots crear.

Consulteu l'[anunci complet](https://devblogs.microsoft.com/devops/remote-mcp-server-preview-in-microsoft-foundry/) per a la configuració pas a pas i més detalls.
