---
title: "Microsoft Foundry Juny 2026: De Llançaments de Funcions a una Plataforma d'Agents Governada"
date: 2026-07-18
author: Emiliano Montesdeoca
description: "Les actualitzacions de Foundry de juny senyalitzen una transició de plataforma: distribució, eines, memòria, observabilitat i optimització convergeixen en un stack d'operacions d'agents preparat per a empreses."
tags:
  - Microsoft Foundry
  - Agents
  - Toolboxes
  - Observability
  - AI Platform
  - Enterprise AI
---

L'onada de Foundry de juny de 2026 no és només un altre resum mensual. Marca una transició de maduresa de "construir agents guais" a "operar agents com a sistemes empresarials governats." Aquesta distinció importa més que qualsevol funció individual.

Font original: https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/

Tres actualitzacions defineixen el canvi. Primer, la publicació d'agents a Microsoft 365 Copilot i Teams va arribar a GA, cosa que mou la distribució de projectes d'integració personalitzats a un carril de desplegament opinió. Segon, Toolboxes va guanyar controls de descobriment i execució més sòlids, incloent cerca d'eines i routines. Tercer, l'observabilitat més l'optimització es van convertir en un bucle tancat deliberat, no una idea tardana.

La meva opinió: aquest és el patró més important del llançament. Traçat, avaluació, optimització i desplegament controlat formen el model operatiu mínim viable per a sistemes no deterministes. Si només teniu una d'aquestes peces, teniu telemetria o ajust, no govern.

Claude GA dins de Foundry també és estratègic, però no principalment per la qualitat del model. El valor més gran és la integració empresarial: autenticació Entra, RBAC, continuitat de facturació i alineació de polítiques. Els equips que es mouen d'endpoints de model directes a Foundry haurien d'emmarcar-ho com a consolidació operativa, no només com a canvi de proveïdor.

Els agents autopilot són prometedors, però les organitzacions haurien d'apropar-s'hi amb eleccions d'arquitectura sobries. La col·laboració en espai compartit a Teams pot desbloquejar productivitat, però augmenta la complexitat d'identitat, permisos i responsabilitat ràpidament. Comenceu amb àmbits limitats i punts de control d'aprovació estrictes abans d'un desplegament ampli.

Recomanacions pràctiques:

Si ja esteu en pilot, prioritzeu la instrumentació abans de l'expansió de capacitats. Connecteu el traçat GenAI primer. Després establir conjunts d'avaluadors lligats a resultats de negoci, no a mètriques genèriques de model. Només després d'això hauríeu d'executar bucles d'optimitzador i fluxos de promoció.

Per a agents amb moltes eines, activeu la cerca d'eines aviat per reduir el soroll de context i el risc de selecció d'eina incorrecta a mesura que els catàlegs creixen. Per a agents amb memòria, definiu TTL i política de retenció per endavant. La memòria sense controls de cicle de vida es converteix en deute de compliment.

La conclusió més opinió que puc extreure és aquesta: Foundry ara tracta menys de "quin model escullo?" i més de "puc executar el comportament d'agent com un cicle de vida gestionat?" Els equips que responguin bé la segona pregunta s'adaptaran fàcilment al canvi de models. Els equips obsessionats amb els rànquings de models seguiran reconstruint stacks fràgils cada trimestre.

El llançament de juny fa una cosa clara. Foundry s'està convertint en una plataforma d'operacions per a sistemes d'IA, no només un kit d'eines de desenvolupament. Aquest és un producte més difícil de construir, i molt més valuós d'adoptar.