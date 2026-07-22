---
title: "Les Extensions MCP d'Agent Governance Toolkit Fan el Camí Segur Molt Més Fàcil a .NET"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "Les noves extensions MCP d'Agent Governance Toolkit per a .NET porten l'aplicació de polítiques, l'escaneig d'inici i la sanitització de respostes directament al flux del constructor del servidor MCP. Aquest és exactament el tipus d'historial secure-by-default que vull veure."
tags:
  - .NET
  - MCP
  - AI
  - Security
  - Agent Governance Toolkit
---

Un dels problemes més grans en les eines d'agents ara mateix és que el camí feliç sol ser el camí insegur.

Pots tenir un servidor MCP funcionant. Pots exposar eines ràpidament. Pots fer que la demo funcioni.

Després arriben les preguntes incòmodes just després:

* qui pot cridar què?
* què passa si les metadades d'una eina són malicioses o enganyoses?
* què passa si una sortida insegura torna directament al model?
* quant d'això és política i quant és només convenció?

Per això importen les noves **Extensions MCP d'Agent Governance Toolkit per a .NET**.

No resolen tots els problemes de seguretat de l'ecosistema d'agents, però fan una cosa molt important: fan que el flux del constructor .NET per defecte sigui molt més fàcil d'endurir.

## La frase més important de l'anunci

El post font diu que el paquet afegeix "**govern amb una sola crida**" a `IMcpServerBuilder`.

Aquesta és la frase exacta en què em centraria.

Perquè la majoria d'equips no fallen a l'hora de construir govern d'agents per manca de consciència. Fracassen perquè el camí segur és més feina, més cablejat, més codi personalitzat i més oportunitats d'ajornar la neteja per a més tard.

I "més tard" és on li encanta viure al risc.

## Per què això és una bona història per a .NET

El que m'agrada aquí és com encaixa el paquet de manera natural al model constructor existent.

En lloc de forçar els equips a:

* un sidecar
* un proxy separat
* una arquitectura de wrapper personalitzada
* o un SDK alternatiu estrany

el paquet amplia el flux constructor oficial de C# MCP directament.

Això importa molt.

Si la seguretat requereix acrobàcies arquitectòniques, l'adopció cau immediatament. Si la seguretat sembla una part normal de la configuració del servidor, l'adopció es torna molt més realista.

## El model d'amenaça ja no és teòric

Una cosa que crec que els equips no haurien de subestimar és la rapidesa amb què el risc relacionat amb MCP es torna real en sistemes de producció.

L'article font planteja preguntes com:

* "**Cada eina registrada hauria de ser cridable per qualsevol agent?**"
* "**Què passa si una descripció d'eina inclou instruccions d'injecció de prompt?**"

Aquestes són exactament les preguntes correctes.

Perquè quan les eines es converteixen en la superfície d'execució per als agents, el sistema ja no només genera text. Està prenent decisions que poden tenir conseqüències de seguretat, fiabilitat i govern.

Això canvia el llistó.

## Què fa bé el paquet

L'elecció de disseny més forta de l'extensió és que agrupa múltiples capes de seguretat en un flux coherent:

* escaneig d'inici per a definicions d'eines insegures
* aplicació de polítiques en execució
* govern conscient de la identitat
* sanitització de respostes abans que el contingut torni al client o al model
* ganxos d'auditoria i mètriques

Aquesta és la forma correcta.

No un "mode seguretat" gegant. Un conjunt de controls específics que cobreixen diferents punts de fallada al cicle de vida.

### L'escaneig d'inici importa més del que molts equips creuen

M'agrada especialment que les metadades d'eines insegures puguin fer fallar l'inici per defecte.

Aquesta és una opinió forta, i crec que és la correcta.

Com més aviat puguis bloquejar una definició d'eina enverinada o sospitosa, millor. Esperar fins al runtime ja és massa tard per a tota una classe de problemes.

### La sanitització de respostes també és una capa molt pràctica

Un altre punt infravalorat de l'anunci és l'enfocament en la sanitització de sortides.

Molts equips pensen en l'entrada perillosa.

Pocs pensen prou en la sortida perillosa que torna d'una eina i es lliura directament a un bucle d'agent.

Aquest és un lloc fàcil per cremar-se.

## Què encara vigilaria amb atenció

Tot i que m'agrada molt aquest paquet, encara aniria amb compte amb una cosa: les eines de govern només funcionen si els equips realment defineixen i mantenen polítiques significatives.

L'extensió facilita connectar el mecanisme. Això és genial.

Però els equips encara necessiten fer la feina organitzativa més difícil de decidir:

* quines eines estan permeses
* quins agents o identitats poden cridar-les
* què significa realment "denegar per defecte" al seu entorn
* com es gestionen els falsos positius i les excepcions

Així que tractaria aquest paquet com una capa d'aplicació forta, no un reemplaçament del judici arquitectònic.

## La meva opinió

Aquest és un dels anuncis d'**agents segurs per defecte** a .NET més clars que he vist en un temps.

No perquè prometi màgia, sinó perquè agafa una categoria de treball de seguretat que els equips probablement implementarien de manera inconsistent i li dóna una llar més neta i natural a la canonada del constructor.

Aquest és exactament el tipus de paquet que vull en aquest ecosistema.

No acaba la conversa més àmplia sobre govern. Fa una cosa més pràctica: fa que sigui molt més difícil pretendre que el govern hauria de ser la tasca de neteja d'un altre més tard.

I això és un progrés real.

Publicació original: [Announcing Agent Governance Toolkit MCP Extensions for .NET](https://devblogs.microsoft.com/dotnet/announcing-agent-governance-toolkit-mcp-extensions-for-dotnet/)