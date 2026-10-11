---
title: "Deep Agents + Cosmos DB Mostren un Patró Pràctic per Treballar amb Dades Operatives en Viu"
date: 2026-06-22
author: "Emiliano Montesdeoca"
description: "La mostra de Deep Agents amb Azure Cosmos DB és interessant perquè mostra un agent treballant directament sobre dades operatives, planificant en múltiples passos, verificant escriptures i mantenint-se ancorat al mateix emmagatzematge que el negoci ja utilitza."
tags:
  - Azure Cosmos DB
  - AI
  - Agents
  - Azure
  - Architecture
---

M'agraden les mostres d'agents que es mantenen a prop dels fluxos de treball operatius reals.

Aquest nou exemple de **Deep Agents + Azure Cosmos DB** fa exactament això.

En lloc d'inventar un món de demo desconnectat, posa l'agent sobre una cua de tiquets de suport emmagatzemada a Cosmos DB i li demana que faci coses que als equips realment els importen:

- triatge de treball
- detecció de patrons
- actualització de registres
- verificació de resultats

Aquesta és una forma molt més útil per a un sistema d'agents.

## El valor real no és "IA parla amb la base de dades"

Ja hem vist aquesta història.

El que fa que aquesta mostra sigui millor és la disciplina operativa al seu voltant:

- l'agent utilitza eines específiques
- les escriptures passen per un camí controlat
- la verificació de lectura-després-d'escriptura és part del flux
- la partició i el cost de les consultes es consideren
- el sistema treballa amb dades operatives en viu, no amb una cau secundària que pretén ser realitat

Aquesta combinació és el que fa que el patró sigui interessant.

## Per què Cosmos DB encaixa bé aquí

Cosmos DB és un bon ajust per a aquest tipus de càrrega de treball perquè les dades ja són dinàmiques, en forma de document i operatives.

L'agent pot:

- llegir tiquets directament
- executar consultes a tota la cua quan sigui necessari
- modificar elements específics
- mantenir l'estat i l'historial a prop de les mateixes dades

Per a escenaris d'agents, això sovint és més útil que forçar-ho tot a través d'una capa analítica separada primer.

## La meva opinió

La conclusió més important aquí és que els sistemes d'agents es tornen molt més convincents quan operen sobre les mateixes dades i els mateixos fluxos de treball que el negoci ja utilitza.

Això és el que aquesta mostra fa bé.

Tracta l'agent com un participant operatiu amb límits d'eines clars, no com una interfície de xat desconnectada que pretén ajudar.

Aquest és un patró que val la pena estudiar.

Article original: [How to Use Deep Agents with Azure Cosmos DB – Plan, act, and verify against operational data](https://devblogs.microsoft.com/cosmosdb/deep-agents-to-plan-act-verify-against-operational-data/)