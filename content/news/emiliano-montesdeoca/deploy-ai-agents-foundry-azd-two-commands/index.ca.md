---
title: "De l'ordinador portàtil a la producció: desplegament d'agents d'IA a Microsoft Foundry amb dues ordres"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "L'Azure Developer CLI ara té ordres \"azd ai agent\" que porten el vostre agent d'IA des del desenvolupador local a un punt final de Foundry en directe en qüestió de minuts. Aquí teniu el flux de treball complet."
tags:
  - azure
  - ai
  - foundry
  - developer-tools
  - azd
---

Coneixeu aquesta bretxa entre "funciona a la meva màquina" i "està desplegat i atén el trànsit"? Per als agents d'IA, aquesta bretxa ha estat dolorosament àmplia. Heu de subministrar recursos, desplegar models, connectar la identitat, configurar la supervisió, i això és abans que ningú pugui trucar al vostre agent.

L'Azure Developer CLI acaba de convertir-ho en un [assumpte de dos comandaments](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/).

## El nou flux de treball `azd ai agent`

Permeteu-me explicar com és realment això. Teniu un projecte d'agent d'IA, diguem-ne un agent de consergeria d'hotel. Funciona localment. Voleu que funcioni a Microsoft Foundry.

```bash
azd ai agent init
azd up
```

Això és tot. Dues ordres. `azd ai agent init` arma la infraestructura com a codi al vostre dipòsit i `azd up` proveeix tot a Azure i publica el vostre agent. Obteniu un enllaç directe al vostre agent al portal de Foundry.

## Què passa sota el capó

L'ordre `init` genera plantilles de bíceps reals i inspeccionables al vostre repositori:

- Un **Recurs de Foundry** (contenidor de primer nivell)
- Un **Projecte de Foundry** (on viu el vostre agent)
- **Configuració del model de desplegament** (GPT-4o, etc.)
- **Identitat gestionada** amb assignacions de rol RBAC adequades
- `azure.yaml` per al mapa de serveis
- `agent.yaml` amb metadades de l'agent i variables d'entorn

Aquí teniu la part clau: sou el propietari de tot això. Està versionat Bicep al teu repositori. Podeu inspeccionar-lo, personalitzar-lo i confirmar-lo juntament amb el vostre codi d'agent. Sense capses negres màgiques.

## El bucle intern del desenvolupament

El que m'agrada molt és la història del desenvolupament local. Quan esteu iterant la lògica de l'agent, no voleu tornar a desplegar cada vegada que canvieu una sol·licitud:

```bash
azd ai agent run
```

Això inicia el vostre agent localment. Vinculeu-lo amb `azd ai agent invoke` per enviar sol·licituds de prova i teniu un bucle de comentaris ajustat. Edita el codi, reinicia, invoca, repeteix.

L'ordre `invoke` també és intel·ligent pel que fa a l'encaminament: quan s'executa un agent local, l'orienta automàticament. Quan no ho és, arriba al punt final remot.

## Monitorització en temps real

Aquesta és la característica que em va vendre. Un cop desplegat el vostre agent:

```bash
azd ai agent monitor --follow
```

Cada sol·licitud i resposta que flueix pel vostre agent es transmet al vostre terminal en temps real. Per depurar problemes de producció, això és inestimable. Sense investigar l'analítica de registres, sense esperar que les mètriques s'agreguin; veuràs què està passant ara mateix.

## El conjunt d'ordres complet

Aquí teniu la referència ràpida:

|Comandament|Què fa|
|---------|-------------|
|`azd ai agent init`|Armar un projecte d'agent de Foundry amb IaC|
|`azd up`|Proveïu els recursos d'Azure i implementeu l'agent|
|`azd ai agent invoke`|Envieu sol·licituds a l'agent local o remot|
|`azd ai agent run`|Executeu l'agent localment per al desenvolupament|
|`azd ai agent monitor`|Transmet els registres en temps real de l'agent publicat|
|`azd ai agent show`|Comproveu l'estat i l'estat de l'agent|
|`azd down`|Netegeu tots els recursos d'Azure|

## Per què això és important per als desenvolupadors de.NET

Tot i que la mostra de l'anunci està basada en Python, la història de la infraestructura és independent del llenguatge. El vostre agent.NET obté la mateixa bastida Bíceps, la mateixa configuració d'identitat gestionada, la mateixa canalització de monitorització. I si ja esteu utilitzant `azd` per a les vostres aplicacions.NET Aspire o implementacions d'Azure, això s'adapta perfectament al vostre flux de treball existent.

La bretxa de desplegament dels agents d'IA ha estat un dels punts de fricció més grans de l'ecosistema. Passar d'un prototip de treball a un punt final de producció amb una identitat, una xarxa i un seguiment adequats no hauria de requerir una setmana de treball DevOps. Ara requereix dues ordres i uns minuts.

## Tancant

`azd ai agent` ja està disponible. Si heu postergat la implementació dels vostres agents d'IA perquè la configuració de la infraestructura us semblava massa feina, proveu-ho. Fes una ullada a la [tutorial completa](https://devblogs.microsoft.com/azure-sdk/azd-ai-agent-end-to-end/) per veure el pas a pas complet, inclosa la integració de l'aplicació de xat frontal.
