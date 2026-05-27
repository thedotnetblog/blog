---
title: "La part difícil del desenvolupament d'IA ja no és l'accés. És fer servir bé el model correcte"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "La nova guia de Foundry fa un argument molt sòlid: la selecció del model, el control de costos, l'avaluació i la gestió del cicle de vida són ara els veritables diferenciadors dels sistemes d'IA en producció."
tags:
  - Microsoft Foundry
  - AI
  - Models
  - Cost Optimization
  - Evaluations
---

> *Aquesta publicació s'ha traduït automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Ja hem superat l'etapa en què simplement tenir accés a un model potent era suficient.

Això és el que aquesta nova **guia de Foundry per gestionar models, cost i qualitat** encerta.

El veritable repte ara és operatiu:

- triar el model adequat per a cada càrrega de treball
- validar-lo amb les teves pròpies dades
- gestionar la latència i la despesa
- governar les actualitzacions i el risc de regressió

Això és el que els equips seriosos han d'aprendre a fer bé.

## L'article original defineix bé el problema

Una frase de la publicació original captura molt bé aquest canvi:

> "**La part més difícil de construir sistemes d'IA avui ja no és accedir a un model capaç. És saber com triar, validar, optimitzar i operar el model correcte durant tot el cicle de vida d'una aplicació real.**"

Aquesta és exactament la diagnosi correcta.

Massa equips encara pensen que la selecció del model és la decisió principal.

No ho és.

L'operació del model és el problema més gran:

- quin model rep cada càrrega de treball?
- com es verifica la qualitat?
- quin nivell de cost és acceptable?
- què passa quan apareix un model nou o un de vell es degrada?
- com proves un canvi sense trencar fluxos de treball reals?

Això és la feina d'enginyeria real ara.

## Per què aquesta peça de Foundry és útil

M'agrada aquest article perquè parla dels sistemes d'IA com realment els han de pensar els enginyers de plataforma amb experiència.

No com "tria el model més intel·ligent i segueix".

Sinó com sistemes que viuen sota compensacions:

- capacitat
- latència
- cost
- seguretat
- governança
- pressió de les actualitzacions

Això és molt més útil que l'optimisme basat només en benchmarks.

## El canvi més important és pensar primer en els criteris

La publicació original recomana definir els criteris d'èxit abans d'obrir el catàleg de models.

Penso que aquest és un dels hàbits més importants que poden adoptar els equips.

Si obres primer el catàleg, t'ancores en la reputació.

Si defineixes primer els criteris, t'ancores en la realitat de la càrrega de treball.

És un procés més sa.

Perquè el model que guanya en un benchmark no és automàticament el que guanya en:

- les teves promptes
- el teu pressupost de latència
- els teus límits de cost
- els teus requisits de governança

Aquesta distinció és on comença l'enginyeria d'IA madura.

## La història multillenguatge s'està convertint en un avantatge real

Una altra cosa que m'agrada és el plantejament explícitament agnòstic respecte al model.

L'article presenta Foundry no com una destinació d'un sol model, sinó com una superfície operativa sobre:

- models de Microsoft
- models de socis
- models de codi obert
- variants postentrenades
- estratègies d'enrutament i optimització

Això importa perquè la flexibilitat del model ja no és un luxe. És part de la gestió del risc.

Si la qualitat canvia, els preus es mouen o la quota es restringeix, els equips necessiten opcions.

## El control de costos no és una preocupació secundària

L'article també té raó en presentar el cost com una qüestió arquitectònica.

Això no és un problema de "ja ho optimitzarem més endavant".

Si envies cada tasca al model més pesat per defecte, això pot funcionar molt bé en una demo i col·lapsar sota l'economia de producció.

Per això crec que les seccions sobre:

- enrutament
- batching
- caching
- provisioned throughput
- gestió de quota

són més importants del que molta gent podria pensar.

Els equips que tracten la disciplina del cost com a part del disseny del sistema aguantaran molt millor que els que la tracten com una feina de neteja posterior.

## La meva opinió

Aquesta és una peça útil de Foundry perquè parla dels sistemes d'IA tal com els han d'operar realment els enginyers experimentats.

No com a demos.
No com a prototips d'una sola vegada.
I no com a turisme de classificacions.

Sinó com a sistemes operatius per a càrregues de treball, restriccions, compensacions i canvi constant.

Aquest és el nivell de conversa cap al qual cal continuar movent-se.

I si estàs construint sistemes d'IA en producció, aquest és exactament el tipus de mentalitat que vull que els equips adoptin aviat.

Publicació original: [A Developer’s Guide to Managing Models, Cost and Quality in Microsoft Foundry](https://devblogs.microsoft.com/foundry/build-2026-foundry-models/)