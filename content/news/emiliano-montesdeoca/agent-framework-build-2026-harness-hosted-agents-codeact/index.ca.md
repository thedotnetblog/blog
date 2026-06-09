---
title: "Agent Harness, Hosted Agents i CodeAct: aquesta és l'actualització d'Agent Framework en què em fixaria"
date: 2026-06-08
author: "Emiliano Montesdeoca"
description: "L'anunci d'Agent Framework a Build 2026 va carregat de contingut, però els fils més importants són el model de harness, els agents allotjats a Foundry i CodeAct per reduir la sobrecàrrega d'orquestració."
tags:
  - Agent Framework
  - AI
  - Agents
  - Microsoft Foundry
  - CodeAct
---

L'anunci gran d'Agent Framework a Build abasta moltes coses, però tres idees em destaquen de seguida:

- **que el harness esdevingui una peça de runtime més central**
- **que els agents allotjats a Foundry ofereixin un camí clar cap a producció**
- **que CodeAct redueixi la sobrecàrrega d'orquestració de diversos passos**

Aquestes són les parts a les quals em fixaria.

## El harness s'està convertint en el veritable centre de gravetat

La publicació original descriu el harness com la capa on el raonament del model es troba amb l'execució real.

Aquesta és la descripció correcta, i també la raó per la qual crec que aquesta part importa més que molts punts de funcions concrets.

En el moment que un agent necessita:

- accés a fitxers
- execució de shell
- modes de planificació
- tasques pendents
- memòria de sessió
- fluxos d'aprovació

ja no estàs parlant només d'un prompt amb un model.

Estàs parlant de comportament en temps d'execució.

És aquí on els frameworks es tornen útils de debò o bé queden en simples joguines.

I Microsoft Agent Framework clarament intenta ser més útil exactament en aquesta capa.

## Els agents allotjats són on la història del local a producció es fa real

També crec que la part dels agents allotjats és una de les més importants estratègicament de l'anunci.

La publicació original diu explícitament que és la manera més fàcil de donar a aquell agent una llar en producció.

Aquesta frase importa perquè la majoria de frameworks d'agents encara són molt més forts en l'experimentació local que no pas en el desplegament operatiu.

Si els agents allotjats de Foundry fan molt més fàcil passar del desenvolupament local a:

- escalabilitat
- observabilitat
- identitat gestionada
- gestió de sessions
- versionat

llavors s'està tapant una de les bretxes més grans de l'ecosistema d'agents actual.

Això és una millora significativa.

## CodeAct és la idea tècnica més emocionant d'aquesta actualització

Si hagués de triar el concepte tècnic més interessant de la publicació, probablement triaria CodeAct.

El problema que intenta resoldre és molt real: massa fluxos d'agents de diversos passos són cars perquè el bucle d'orquestració mateix consumeix massa torns de model.

Així que, quan la publicació mostra un resultat com aquest:

- 52.4% més ràpid
- 63.9% menys de tokens

em crida l'atenció immediatament.

És clar que són xifres de benchmark lligades a una càrrega de treball representativa, no pas una llei universal. Però la idea de fons continua sent molt convincent.

Si el model pot comprimir una cadena de trucades a eines en una forma d'execució més eficient, l'economia dels sistemes d'agents pot canviar força.

## Què crec que els desenvolupadors haurien d'extreure realment d'aquesta actualització

La lliçó important no és quantes funcions han sortit.

La lliçó és que el framework s'està enfortint en els llocs que les aplicacions reals necessiten més:

- runtime
- camí de desplegament
- eficiència d'execució
- patrons operatius incorporats

Aquest és el tipus de senyal de maduresa que m'importa molt més que una altra llista superficial de funcions d'IA.

## La meva lectura

Aquesta actualització importa perquè no només afegeix més superfície.

Està reforçant la història de runtime i desplegament al voltant dels agents d'una manera que hauria d'importar per a aplicacions reals, especialment per a equips que volen passar d'experiments locals a sistemes que puguin executar i mantenir de debò.

És aquí on el framework es torna més atractiu.

I si seguís aquest llançament de prop, aquestes tres àrees serien sens dubte on pararia més atenció.

Publicació original: [Microsoft Agent Framework at BUILD 2026: Agent Harness, Hosted Agents, CodeAct, and more]({{< ref "index.md" >}})
