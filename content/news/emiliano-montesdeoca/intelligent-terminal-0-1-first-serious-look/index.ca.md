---
title: "Intelligent Terminal 0.1 és un primer intent seriós d’una shell nativa per a IA"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "Intelligent Terminal 0.1 introdueix una agent pane nativa, assistència conscient dels errors, tasques en segon pla i fluxos d’agent activats des de la command palette. Encara és experimental, però la direcció és molt prometedora."
tags:
  - Terminal
  - AI
  - GitHub Copilot
  - Developer Tools
  - Windows Terminal
---

> *Aquest article ha estat traduït automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Crec que la terminal és un dels llocs més naturals perquè el desenvolupament assistit per IA esdevingui realment útil.

Per això **Intelligent Terminal 0.1** sembla un anunci seriós, fins i tot en la seva forma experimental.

La part interessant no és només "xatejar dins de la terminal". És la integració nativa de:

- una agent pane
- detecció d’errors
- gestió de sessions
- tasques en segon pla
- accions d’agent activades des de la command palette

Això ja comença a semblar una experiència shell real, no pas un afegit enganxat al costat.

## L’article original entén el punt de dolor real

Una de les millors parts del post original és que no comença amb una ambició abstracta d’IA.

Comença amb una experiència de desenvolupador molt normal:

> "**Alguna vegada has introduït una ordre de PowerShell, t’ha donat un error, l’has copiat, has obert el navegador, l’has enganxat i has saltat per diversos fòrums per arreglar-ho?**"

La pregunta funciona perquè és dolorosament familiar.

La terminal és plena d’aquestes petites interrupcions.

Així que, si la IA ha d’estar en algun lloc, és al costat d’aquestes interrupcions.

## Per què això sembla més sòlid que la majoria de demos d’IA per a terminal

El que fa que això sigui interessant no és només que hi hagi un agent.

És que l’experiència de terminal es replanteja al voltant de com treballen realment els desenvolupadors:

- una superfície d’agent persistent
- context procedent de la sortida del shell
- ajuda ràpida quan apareixen errors
- creació de tasques en segon pla
- reprendre sessions
- la command palette com a punt d’entrada

Això està molt més a prop d’un workflow usable que no pas un chatbot flotant connectat a una finestra shell.

## La agent pane és el producte de veritat aquí

Si hagués de triar la part més important del disseny, probablement seria la agent pane.

Per què? Perquè crea un terme mig entre dos modes incòmodes:

- abandonar completament la terminal
- o intentar encabir tota la interacció dins de text shell en línia

És una bona decisió de disseny.

Respecta la terminal com a superfície de treball i, alhora, dona a l’agent prou espai per ser més que un simple autocomplete.

## La detecció d’errors és on el valor comença a fer-se evident

La detecció automàtica d’errors també és exactament el tipus de funcionalitat que té sentit aquí.

La terminal ja té el context.
L’error ja ha passat.
I el desenvolupador ja està dins del flux.

Això fa que el shell sigui un dels millors llocs per a:

- diagnosi immediata
- suggeriments de correcció
- iteració ràpida
- raonament de seguiment sense sortir de l’entorn actual

No és màgia. Simplement és col·locar el workflow al lloc adequat.

## La meva opinió

Encara és aviat, però és una de les direccions d’IA per a terminal més convincents que he vist fins ara.

No perquè prometi màgia.
Sinó perquè es manté a prop de com ja treballen els desenvolupadors dins del shell.

I si continua evolucionant en aquesta direcció, crec que podria convertir-se en una de les experiències de desenvolupament nadiues per IA més interessants del portfolio d’eines de Microsoft.

Article original: [Announcing Intelligent Terminal 0.1](https://devblogs.microsoft.com/commandline/announcing-intelligent-terminal-version-0-1/)
