---
title: "VS Code 1.128 fa una aposta clara: la finestra d'agents s'està convertint en el nou espai de treball"
date: 2026-07-25
author: Emiliano Montesdeoca
description: "VS Code 1.128 transforma els fluxos d'agents de novetat a ergonomia diària amb sessions de xat múltiple, suport vision en GA i controls més profunds d'host/sessió."
tags:
  - VS Code
  - AI Agents
  - Copilot
  - Developer Experience
  - Multimodal
  - Productivity
---

Visual Studio Code 1.128 és una versió rellevant no per una funció estrella, sinó perquè diversos canvis s'alineen en una direcció única: el desenvolupament agent-first dins l'editor s'està tornant estructurat, paral·lel i operativament manejable.

Font original: https://code.visualstudio.com/updates/v1_128

El més destacat és un comportament multi-xat més ric en sessions host d'agents, incloent xats entre iguals, forks i torns concurrents sota una mateixa sessió pare. Això és exactament el que els desenvolupadors amb experiència necessiten quan exploren implementacions alternatives o divideixen tasques entre diferents vies de verificació. Reflecteix la feina d'enginyeria real, que rarament és lineal.

La meva opinió: aquesta és la primera versió de VS Code on la finestra d'agents se sent menys com un panell de xat i més com una superfície d'orquestració de l'espai de treball.

Els xats ràpids sense un espai de treball seleccionat també importen més del que semblen. Redueixen la fricció per a preguntes conceptuals o arquitectòniques, mantenint alhora les sessions lligades al projecte ben diferenciades. Aquesta separació pot reduir el desordre i preservar la integritat del context per a fluxos que modifiquen codi.

Copilot Vision arribant a GA és un altre punt d'inflexió. Un cop les imatges i PDFs siguin entrades normals al xat, les tasques amb molta documentació i interfície gràfica es tornen significativament més fluides. Els equips haurien de pensar ara en el context multimodal com una capacitat per defecte, no com un extra avançat.

També hi ha implicacions pràctiques de plataforma. El suport BYOK en escenaris host d'agents, els paràmetres de mostra configurables del model i els per defecte de models d'utilitat indiquen una maduresa creixent per a la governança de models empresarials. Les organitzacions amb requisits estrictes de proveïdor ara poden donar forma al comportament amb un control més fi, en lloc de configuracions genèriques.

Recomanacions per als equips que adoptin la 1.128:

Definiu convencions per a la ramificació i nomenclatura de xats en sessions multi-xat perquè l'exploració paral·lela no es converteixi en soroll conversacional. Animeu els desenvolupadors a mantenir un xat per a la implementació i un altre per a tests o anàlisi de fallades. Utilitzeu els xats ràpids de manera intencionada per a preguntes no relacionades amb el repositori.

Si executeu endpoints BYOK, establiu perfils base de temperatura/top_p per classe de càrrega de treball i documenteu les excepcions. Decidiu també si els fluxos d'utilitat haurien d'executar-se en models proporcionats per Copilot o BYOK per evitar buits de comportament silenciosos accidentals.

Finalment, considereu les dreceres a nivell de SO de manera estratègica. Poder activar comandaments de VS Code a nivell de sistema pot millorar el flux per a usuaris avançats, però una proliferació de dreceres sense gestió pot perjudicar la coherència entre equips.

VS Code 1.128 no afegeix simplement funcions. Ajusta la mecànica de la col·laboració amb agents en els bucles reals de desenvolupament. Els editors que guanyin en el proper cicle seran aquells que tractin les interaccions amb agents com a primitives de flux de treball de primera classe, no com a experiments laterals. Aquesta versió mostra que VS Code entén aquesta cursa.