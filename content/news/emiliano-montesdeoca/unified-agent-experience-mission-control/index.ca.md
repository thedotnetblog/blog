---
title: "Control de Missió per a Agents de Programació: Una Experiència Unificada a VS Code"
description: "VS Code reuneix agents de programació locals, en la nuvola, CLI i de tercers en Sessons d'Agents perquè els desenvolupadors puguin fer un seguiment, interrompre i coordinar el treball autònom."
date: 2026-08-07
author: Emiliano Montesdeoca
tags: [agents, orchestration, multi-agent, VS Code, automation, Codex]
slug: unified-agent-experience-mission-control
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

# Control de Missió per a Agents de Programació: Una Experiència Unificada a VS Code

Un únic assistent de programació és fàcil de comprendre. Diversos agents treballant en llocs diferents no ho són.

Un agent s'executa localment a VS Code. Un altre treballa en una qüestió de GitHub a la nuvola. Un agent CLI viu a la terminal. Un agent de programació de tercers pot tenir un model de sessió diferent i límits diferents. Sense una vista compartida, els desenvolupadors dediquen més temps a fer un seguiment del treball que a supervisar-lo.

L'experiència unificada d'agents de VS Code aborda aquest problema de coordinació amb les Sessons d'Agents: un lloc per llançar agents, veure l'estat, obrir les seves converses i intervenir quan el pla canvia.

Això és menys sobre afegir un altre agent i més sobre fer que múltiples agents siguin manejables.

## Una Vista per a Diferents Tipus de Treball

L'article font descriu quatre participants distints: GitHub Copilot local, Copilot Coding Agent a la nuvola, GitHub Copilot CLI i OpenAI Codex per a subscriptors de Copilot elegibles.

Tenen fortaleses diferents:

- Un agent local pot inspeccionar l'espai de treball actual i fer canvis ràpids.
- Un agent de programació en la nuvola pot treballar de forma asincrònica en una qüestió i obrir una sol·licitud d'extracció.
- Un agent CLI s'ajusta als fluxos de treball amb terminal pesada i comandaments operacionals.
- Un altre proveïdor pot oferir un model diferent o un estil de raonament.

Les Sessons d'Agents proporcionen una llar comuna per a aquestes tasques. Podeu veure què s'està executant, què està fent i on continuar la conversa.

Aquesta visibilitat és important perquè el treball autònom no elimina la coordinació. Fa que la coordinació sigui una tasca d'enginyeria de primera classe.

## Les Interrupcions Són Part del Flux de Treball

La font fa una observació senzilla: «És comú enviar una indicació i adonar-se que has oblidat quelcom important». Anteriorment, l'opció era sovint d'esperar o cancel·lar. Amb editors de xat, podeu obrir una sessió activa i afegir informació mentre l'agent està treballant.

Això és més proper a la col·laboració real. Els requisits canvien. Una prova revela una suposició. Un revisor nota que una API ha de mantenir la compatibilitat amb versions anteriors. L'agent útil no és aquell que mai necessita correccions; és aquell que pot absorbir correccions sense perdre tota la tasca.

Per al treball .NET, una interrupció pot ser tan senzilla com:

```text
Keep the existing public route unchanged. Add the new behavior behind the application service,
use the existing ProblemDetails convention, and add a test for the old response shape.
```

La instrucció és breu perquè el repositori ja porta el context més gran. La sessió és el lloc per corregir la direcció, no per reafirmar tot el sistema.

## Els Agents Personalitzats Transformen els Hàbits del Equip en Rols

VS Code també introdueix agents especialitzats com Plan. En lloc d'implementar immediatament, un agent de planificació fa preguntes sobre abast, components, biblioteques i restriccions abans de produir una especificació d'implementació.

Aquest patró és útil més enllà d'un agent integrat. Un equip pot definir rols enfocats:

- **Investigació** recopila evidència i escriu un registre de decisions curt.
- **Revisió** comprova un canvi contra les convencions del repositori.
- **Prova** identifica casos perduts i proposa un pla de prova.
- **Arquitectura** compara opcions sense modificar fitxers.

Una definició de agent personalitzat petit podria tenir aquest aspecte:

```yaml
type: agent
name: plan
description: "Refines vague requests into clear implementation specs"
prompt: |
  Ask about scope, constraints, existing patterns, and edge cases.
  Produce a concise specification before any implementation begins.
```

La part útil no és el YAML. Es tracta de la separació explícita de responsabilitats. Un agent de planificació no hauria de silenciosament editar codi de producció. Un agent de revisió no hauria de reescriure el disseny que se suposava que havia d'avaluar.

## Els Subagents Redueixen les Col·lisions de Context

Les converses llargues acumulen context no relacionat. Els subagents proporcionen un espai de treball aïllat per a una tasca de recerca limitada i després retornen el resultat a la sessió principal.

Això és un bon ajust per a preguntes com:

```text
Analyze the API project and recommend an authentication strategy.
Return trade-offs and a decision record. Do not edit files.
```

L'agent principal se centra en la implementació mentre que l'agent de recerca gestiona una pregunta més estreta. El mateix principi s'aplica als equips: la delegació clara produeix millors resultats que llançar diversos agents amb autoritat superposada.

## L'Advertència: Més Agents Signifiquen Més Coordinació

Les Sessions d'Agents poden mostrar activitat, però no pot resoldre conflictes de propietat. Dos agents editant la mateixa àrea poden crear un problema de fusió. Un agent en la nuvola i un agent local poden fer suposicions incompatibles. Un agent personalitzat pot produir una recomanació que un altre agent ignora.

Establir límits:

1. Un agent és propietari de la implementació d'una branca donada.
2. Els agents de recerca retornen artefactes, no edicions no rastrejades.
3. Les sol·licituds d'extracció romanen el límit de revisió.
4. Els noms dels agents i les indicacions indiquen què poden canviar.
5. La sortida de la sessió es manté quan explica una decisió important.

## La Meva Opinió

El futur multiagent no és una cua de finestres de xat. És un petit equip amb rols, traspàs i responsabilitat.

Les Sessons d'Agents són valuoses perquè reconeixen aquesta realitat. Proporciona als desenvolupadors una superfície de control per al treball que ja està passant en l'editor, la terminal i la nuvola. El proper guany de productivitat provindran menys de tenir més agents i més de fer que els seus límits siguin llegibles.

Per a un equip .NET, començaria amb un agent de planificació i un agent d'implementació. Utilitzeu la sortida de planificació com a especificació de problema o sol·licitud d'extracció, i permetre que l'agent d'implementació treballi dins d'aquest límit. Mesureu el treball reanomenat abans d'afegir més rols.

El millor control de missió és aquell que fa que la propietat sigui obvia.
