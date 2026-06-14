---
title: "FIDES és el tipus d'història de seguretat d'agents determinista que vull veure més sovint"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Les noves capacitats de FIDES a Agent Framework importen perquè allunyen la defensa contra el prompt injection de les heurístiques i la porten cap a una política aplicable basada en contingut etiquetat i comprovacions de middleware."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *Aquest article s'ha traduït automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Les defenses contra el prompt injection sovint semblen reposar sobre un terreny inestable.

Afeges un system prompt més fort. Hi afegeixes un filtre. Hi poses algunes llistes d'autorització. I esperes que l'entrada estranya següent no trenqui les suposicions.

Per això **FIDES** és interessant.

La part forta de la història és que trasllada la seguretat cap a alguna cosa més determinista:

- etiquetes sobre el contingut
- propagació de les etiquetes a través del flux de treball
- imposició via middleware abans que s'executin eines privilegiades
- límits de política clars sobre allò que el context no fiable pot influir

## L'article original és clar en el bon sentit

Comença dient que el prompt injection és "**el risc número 1 del OWASP LLM Top 10**".

Bé.

M'agrada aquest tipus de franquesa aquí, perquè massa equips encara tracten la seguretat dels agents com si fos una preocupació futura en lloc d'un problema de disseny de runtime present.

I l'article ho segueix amb un contrast pràctic fort: la majoria de defenses actuals són heurístiques, mentre que FIDES intenta portar el sistema cap a la política i la imposició.

Aquest és exactament el canvi correcte.

## Què el fa més convincent que un altre whitepaper de seguretat

Molts escrits sobre seguretat d'IA es queden en l'abstracció.

Aquest article fa una cosa millor. Passa per un exemple molt concret: un agent de triatge d'issues de GitHub, un cos d'issue maliciós, una lectura de fitxer privilegiada i un intent de filtrar un comentari públic.

Això és útil perquè arrossega tota la discussió a un flux de treball real.

I un cop veus aquest escenari, el valor dels controls deterministes és molt més fàcil d'entendre.

## La idea clau no és "fes el model més intel·ligent"

El més important aquí és que FIDES no demana al model que es torni màgicament millor detectant atacs.

Està canviant el contracte del runtime.

Això vol dir:

- es classifica el contingut
- les etiquetes es propaguen
- les eines declaren què accepten
- el middleware bloqueja els camins insegurs abans de l'execució

Aquest és un enfocament molt millor.

Perquè, un cop l'agent pot cridar eines amb conseqüències reals, la seguretat no pot dependre només de si el model ha tingut un bon dia.

## La meva opinió

Aquesta és exactament la mena de direcció en seguretat d'agents que vull veure més sovint.

No "confia en el model perquè ignori les instruccions dolentes", sinó "construeix la tanca de política dins del runtime".

Això és un model molt més sa.

I si els frameworks d'agents volen ser presos seriosament en producció, en necessitaran més històries com aquesta.

Article original: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)