---
title: "L'actualització de març de Visual Studio us permet crear agents de pilot personalitzats, i l'eina find_symbol és una gran cosa"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "L'actualització de març de 2026 de Visual Studio inclou agents Copilot personalitzats, habilitats d'agent reutilitzables, una eina find_symbol conscient de l'idioma i perfils basats en Copilot des de Test Explorer. Aquí teniu el que importa."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

Visual Studio acaba de rebre la seva actualització Copilot més important fins ara. Mark Downie [va anunciar el llançament de març](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/), i el títol és agents personalitzats, però sincerament, l'eina `find_symbol` soterrada més avall podria ser la característica que canviï més el vostre flux de treball.

Permeteu-me desglossar el que hi ha realment aquí.

## Agents de Copilot personalitzats al vostre dipòsit

Voleu que Copilot segueixi els estàndards de codificació del vostre equip, executi el vostre pipeline de compilació o consulti els vostres documents interns? Ara pots construir exactament això.

Els agents personalitzats es defineixen com a fitxers `.agent.md` que deixeu anar a `.github/agents/` al vostre repositori. Cada agent té accés complet a la consciència de l'espai de treball, la comprensió del codi, les eines, el model preferit i les connexions MCP a serveis externs. Apareixen al selector d'agents al costat dels agents integrats.

Aquest és el mateix patró que VS Code ha donat suport, i és fantàstic veure que Visual Studio es posa al dia. Per als equips que ja han creat agents per a VS Code, els vostres fitxers `.agent.md` haurien de funcionar en ambdós IDE (tot i que els noms d'eines poden variar, així que proveu-los).

El repositori [awesome-copilot](https://github.com/github/awesome-copilot) té configuracions d'agents contribuïts per la comunitat que podeu utilitzar com a punts de partida.

## Habilitats d'agent: paquets d'instruccions reutilitzables

Les habilitats es recullen automàticament de `.github/skills/` al vostre repositori o `~/.copilot/skills/` al vostre perfil. Cada habilitat és un fitxer `SKILL.md` seguint l'[especificació d'habilitats de l'agent](https://agentskills.io/specification).

Penseu en les habilitats com a experiència modular que podeu combinar i combinar. És possible que tingueu una habilitat per a les convencions de l'API, una altra per als vostres patrons de prova i una altra per al vostre flux de treball de desplegament. Quan s'activa una habilitat, apareix al xat perquè sàpigues que s'està aplicant.

Si heu estat utilitzant habilitats a VS Code, ara funcionen de la mateixa manera a Visual Studio.

## find_symbol: navegació conscient de l'idioma per als agents

Aquí és on les coses es posen realment interessants. La nova eina `find_symbol` ofereix al mode d'agent de Copilot una navegació real de símbols basada en el servei d'idiomes. En lloc de cercar el vostre codi com a text, l'agent pot:

- Trobeu totes les referències a un símbol al vostre projecte
- Informació de tipus d'accés, declaracions i metadades d'abast
- Navegueu pels llocs de trucades amb coneixement complet de l'idioma

Què significa això a la pràctica: quan demaneu a Copilot que refactori un mètode o actualitzeu una signatura de paràmetres en llocs de trucada, realment pot veure l'estructura del vostre codi. No més situacions "l'agent va canviar el mètode però va perdre tres llocs de trucades".

Els llenguatges admesos inclouen C#, C++, Razor, TypeScript i qualsevol cosa amb una extensió LSP compatible. Per als desenvolupadors de.NET, aquesta és una millora massiva: les bases de codi C# amb jerarquies i interfícies de tipus profundes es beneficien enormement de la navegació conscient dels símbols.

## Proves de perfil amb Copilot

Ara hi ha una ordre **Perfil amb Copilot** al menú contextual de l'Explorador de proves. Seleccioneu una prova, feu clic al perfil i l'agent de perfils l'executa automàticament i analitza el rendiment, combinant l'ús de la CPU i les dades d'instrumentació per oferir informació útil.

No més configurar manualment sessions de perfilador, executar la prova, exportar resultats i intentar llegir un gràfic de flama. L'agent fa l'anàlisi i us diu què és lent i per què. Actualment només.NET, cosa que té sentit donada la profunda integració de diagnòstic.NET de Visual Studio.

## Consells de rendiment durant la depuració en directe

L'optimització del rendiment ara es produeix mentre depureu, no després. A mesura que passeu pel codi, Visual Studio mostra el temps d'execució i els senyals de rendiment en línia. Veus una línia lenta? Feu clic al Consell de rendiment i demaneu a Copilot suggeriments d'optimització allà mateix.

L'agent de perfils captura automàticament les dades del temps d'execució (temps transcorregut, ús de la CPU, comportament de la memòria) i Copilot les utilitza per identificar els punts calents. Això manté el treball de rendiment com a part del vostre flux de depuració en lloc d'una tasca separada que continueu posposant.

## Corregiu les vulnerabilitats de NuGet des de l'Explorador de solucions

Quan es detecta una vulnerabilitat en un paquet NuGet, ara veuràs una notificació amb un enllaç **Corregir amb GitHub Copilot** directament a l'Explorador de solucions. Feu clic i Copilot analitza la vulnerabilitat, recomana les actualitzacions de paquets adequades i les implementa.

Per als equips que lluiten per mantenir les dependències actualitzades (que és bàsicament per a tothom), això elimina la fricció de "Sé que hi ha una vulnerabilitat, però esbrinar la ruta d'actualització correcta és un projecte en si mateix".

## Tancant

Els agents personalitzats i les habilitats són el titular, però `find_symbol` és l'èxit dormint: canvia fonamentalment la precisió que pot ser Copilot quan es refactoritza el codi.NET. Combinada amb la integració de perfils en directe i les correccions de vulnerabilitats, aquesta actualització fa que les funcions d'IA de Visual Studio se sentin realment pràctiques en lloc de preparar-se per a la demostració.

Baixeu [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/) per provar-ho tot.
