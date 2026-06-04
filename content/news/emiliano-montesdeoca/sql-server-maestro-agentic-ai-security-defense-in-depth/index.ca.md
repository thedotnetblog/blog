---
title: "MAESTRO, Defensa en Profunditat i per Què SQL Server és Ara una Frontera de Seguretat per a la IA"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "La IA agèntica introdueix amenaces per a les quals els models STRIDE tradicionals no van ser dissenyats. Aquí s'explica com Microsoft SQL s'alinea amb el marc MAESTRO per proporcionar un límit d'execució governat."
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

Els models d'amenaça de seguretat es construeixen sobre supòsits sobre qui o què fa les sol·licituds. STRIDE assumeix actors humans que interactuen amb sistemes a través d'interfícies definides. Els agents d'IA no funcionen d'aquesta manera.

## STRIDE No Va Ser Dissenyat per a Agents d'IA

Els sistemes agèntics operen de manera autònoma, encadenen eines a través de crides a l'API, prenen decisions sobre quines dades recuperar i quines accions executar, i poden rebre instruccions de múltiples fonts — instruccions d'usuari, resultats d'eines, dades recuperades. El model d'amenaça STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) no captura adequadament els vectors d'atac específics d'agents com la injecció de prompts, l'enverinament de context o l'abús d'eines.

La Cloud Security Alliance va publicar el marc MAESTRO específicament per al risc dels agents d'IA.

## El Marc MAESTRO

MAESTRO organitza el risc de la IA agèntica en set capes:

1. **Foundation Models** — els LLM subjacents i les seves vulnerabilitats d'entrenament
2. **Data Operations** — recuperació, emmagatzematge i manipulació de dades
3. **Agent Frameworks** — el programari intermediari d'orquestració i coordinació d'agents
4. **Deployment & Infrastructure** — on s'executen els agents i com es configuren
5. **Evaluation & Observability** — supervisió del comportament dels agents al llarg del temps
6. **Security & Compliance** — controls d'accés, auditoria i compliment normatiu
7. **Agent Ecosystem** — com els agents interactuen entre ells i amb eines externes

Cada capa té vectors d'atac específics que els controls de seguretat tradicionals no aborden directament.

## Microsoft SQL com a Límit d'Execució Governat

SQL Server 2025 s'alinea amb les capes MAESTRO de maneres concretes:

**Capa Data Operations**: `AI_GENERATE_EMBEDDINGS` integrat a T-SQL manté les operacions vectorials dins del límit governat de la base de dades. Les dades no han de sortir al servei del model per al processament d'embeddings.

**Capes Security & Compliance**: La seguretat a nivell de fila (RLS) i l'emmascarament dinàmic de dades (DDM) s'apliquen independentment de com hagi arribat la sol·licitud — d'un usuari humà o d'un agent d'IA. L'agent no pot eludir els controls que aplica la pròpia base de dades.

**Capa Agent Frameworks**: Els procediments emmagatzemats funcionen com a límits d'eines. En lloc de donar als agents accés SQL arbitrari, es defineixen les operacions permeses com a procediments i s'exposen com a eines d'agents. Les consultes parametritzades prevenen la injecció a nivell d'execució.

**Capa Evaluation & Observability**: El registre d'auditoria i el Query Store captura el que cada agent ha executat realment — no només el que se li ha demanat que fes. Aquesta traçabilitat és crucial per a les investigacions d'incidents en sistemes agèntics on l'atribució és complexa.

## Defensa en Profunditat per a la IA Agèntica

El principi és el mateix que en la seguretat tradicional: cap control individual és suficient. El que canvia és quins controls compten més per als agents:

**Reduir el radi d'explosió**: el límit d'eines a través de procediments emmagatzemats significa que un agent compromès només pot executar operacions predefinides. No pot pivotar cap a consultes arbitràries.

**Observabilitat**: heu de poder respondre "què va fer exactament aquest agent?" després d'un incident. Els sistemes d'IA agèntica sense traçabilitat a nivell de base de dades tenen punts cecs que el registre d'aplicacions no cobreix.

**Execució restringida**: la parametrització, RLS i DDM són actius de seguretat independentment de si el que crida és humà o no. No els debiliteu per acomodar els agents.

**Responsabilitat**: el registre d'auditoria de SQL Server crea un registre de qui (quin agent, usant quines credencials) va executar què en quin moment. Això importa quan els sistemes agèntics prenen accions amb conseqüències reals al món.

SQL Server 2025 no va ser construït per resoldre el risc agèntic de manera abstracta — va ser construït per ser una base de dades relacional. Però la governança que fa que una base de dades empresarial sigui de confiança resulta ser exactament el que fa que un límit d'execució d'agents sigui segur.

Post original: [Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
