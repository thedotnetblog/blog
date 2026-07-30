---
title: "El Veritable Guany en UX d'Agents és l'Autonomia Segura, no l'Autonomia Màxima"
date: 2026-07-11
author: "Emiliano Montesdeoca"
description: "L'accés a fitxers, les aprovacions i el disseny de memòria són la tríada pràctica per a un comportament fiable dels agents en producció."
tags:
  - microsoft-agent-framework
  - ai-agents
  - approvals
  - security
  - dotnet
  - python
---

Font original: [Agent Harness: Working with your data, safely](https://devblogs.microsoft.com/agent-framework/agent-harness-working-with-your-data-safely/)

Aquest és un dels articles d'enginyeria d'agents més útils d'aquest any perquè rebutja el parany comú de l'autonomia centrada en demos. En lloc d'això, se centra en com els agents haurien d'operar amb dades reals d'usuaris i conseqüències reals.

Els tres blocs de construcció destacats aquí són exactament els correctes.

L'accés a fitxers dóna als agents un fonament útil en dades propietat de l'usuari.

L'aprovació controlada evita l'execució silenciosa d'accions amb conseqüències.

La memòria duradora evita interaccions repetitives sense sacrificar el control.

La majoria d'equips sobredimensionen la varietat d'eines i subinverteixen en la semàntica de permisos. Això és al revés. Un agent amb deu eines i límits d'aprovació febles és menys valuós que un agent amb tres eines i punts de control previsibles.

El millor patró pràctic d'aquest article és l'estratègia d'aprovació per capes:

* Requereix sempre aprovació per a eines d'alt impacte, com operacions de trading o destructives.
* Autoaprova les lectures de baix risc per preservar el flux.
* Utilitza aprovacions permanents amb abast per a accions repetitives de confiança dins d'una sessió.

Això crea un gradient de risc saludable. Els usuaris no són interromputs per lectures inofensives, però continuen al cercle quan les conseqüències es tornen cares o irreversibles.

També m'agrada la divisió explícita entre memòria de fitxers i memòria de Foundry. Els equips haurien de deixar de forçar un model de memòria únic per resoldre tots els problemes. Els artefactes de fitxer explícits i gruixuts són excel·lents per a l'estat visible per l'usuari, com informes i llistes de seguiment. L'extracció de memòria a nivell de fets és millor per a preferències i context conversacional. Barrejar ambdós dóna millors resultats que pretendre que qualsevol dels dos és suficient.

La meva opinió: el futur de la qualitat dels agents es mesurarà menys per prompts enginyoses i més per l'ergonomia de seguretat. Si les sol·licituds d'aprovació són sorolloses, els usuaris fan clic a cegues. Si els límits de memòria no són clars, els usuaris deixen de confiar en l'assistent. Si els accessos per defecte a dades són permissius, els equips de seguretat aturaran el projecte.

Per als equips de .NET i Python que adopten aquest patró, el moviment clau és tractar les crides de política i les regles d'aprovació com a lògica de negoci central, versionada i provada com qualsevol altre codi crític. No les deixis com a lambdas ad-hoc enterrades en exemples.

Els sistemes d'agents que guanyen confiança no són els que fan més. Són els que fan exactament el que els usuaris pretenien, ni més ni menys, amb punts d'interrupció clars quan el risc augmenta.

Aquesta és la diferència entre una demo impressionant i un programari al qual la gent està disposada a delegar feina real.