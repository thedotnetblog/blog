---
title: "VS Code 1.117: Els agents s'estan guanyant les seves pròpies branques Git i això m'encanta"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 incorpora aïllament de worktrees per a sessions d'agents, mode Autopilot persistent i suport per a subagents. El flux de treball de codificació agentica acaba de fer un salt seriós."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

La línia entre "assistència IA" i "company de feina IA" cada cop és més fina. VS Code 1.117 acaba d'arribar i les [notes completes de la versió](https://code.visualstudio.com/updates/v1_117) venen carregades, però el missatge és clar: els agents s'estan convertint en ciutadans de primera classe del teu flux de treball de desenvolupament.

Això és el que realment importa.

## El mode Autopilot finalment recorda la teva preferència

Abans, havies de reactivar Autopilot cada vegada que començaves una sessió nova. Molest. Ara el teu mode de permisos es manté entre sessions i pots configurar el valor per defecte.

L'Agent Host admet tres configuracions de sessió:

- **Per defecte** — les eines demanen confirmació abans d'executar-se
- **Bypass** — aprova automàticament tot
- **Autopilot** — totalment autònom, respon les seves pròpies preguntes i continua fins que la tasca s'acaba

Si estàs preparant un projecte .NET nou amb migracions, Docker i CI, configura-ho una vegada en mode Autopilot i oblida-t'en. Aquesta preferència es manté.

## Aïllament de worktree i Git per a sessions d'agents

Aquesta és la gran novetat. Les sessions d'agents ara admeten un aïllament complet de worktree i Git. Això vol dir que, quan un agent treballa en una tasca, obté la seva pròpia branca i el seu propi directori de treball. La teva branca principal queda intacta.

I encara millor: Copilot CLI genera noms de branca significatius per a aquestes sessions de worktree. Res de `agent-session-abc123`. Obtens alguna cosa que realment descriu el que l'agent està fent.

Per als desenvolupadors .NET que treballen amb diverses branques de funcionalitat o arreglen errors mentre corre una tasca llarga d'esqueletatge de projecte, això canvia les regles del joc. Pots tenir un agent construint els controladors de l'API en un worktree mentre tu depures un problema a la capa de serveis en un altre. Sense conflictes. Sense `stash`. Sense embolics.

## Subagents i equips d'agents

El protocol Agent Host ara admet subagents. Un agent pot engegar altres agents per encarregar-los parts d'una tasca. Pensa-ho com delegar: el teu agent principal coordina i els agents especialitzats fan les peces concretes.

Això encara és una funcionalitat inicial, però el potencial per als fluxos de treball .NET és evident. Imagina un agent gestionant les teves migracions d'EF Core mentre un altre prepara els tests d'integració. Encara no hi som del tot, però el suport al protocol que arriba ara farà que les eines segueixin ràpidament.

## La sortida del terminal s'inclou automàticament quan els agents envien entrada

Petita, però important. Quan un agent envia entrada al terminal, la sortida del terminal s'inclou automàticament al context. Abans, l'agent havia de fer un torn extra només per llegir què havia passat.

Si mai has vist un agent executar `dotnet build`, fallar i després fer una altra ronda només per llegir l'error, aquesta fricció desapareix. Ho veu de seguida i reacciona.

## L'app d'Agents s'actualitza sola a macOS

L'aplicació d'Agents independent per a macOS ara s'actualitza sola. Ja no cal descarregar noves versions manualment. Simplement es manté al dia.

## El que val la pena saber de la resta

- **Els hovers de package.json** ara mostren tant la versió instal·lada com la més recent. Útil si gestiones eines npm al costat dels teus projectes .NET.
- **Les imatges als comentaris JSDoc** es renderitzen correctament als hovers i a les completes.
- **Les sessions de Copilot CLI** ara indiquen si s'han creat des de VS Code o externament, cosa útil quan saltes entre terminals.
- **Copilot CLI, Claude Code i Gemini CLI** es reconeixen com a tipus de shell. L'editor sap què estàs executant.

## La conclusió

VS Code 1.117 no és un llançament ple de funcions espectaculars. És infraestructura. L'aïllament de worktrees, els permisos persistents i els protocols de subagents són els blocs de construcció d'un flux de treball on els agents gestionen tasques reals en paral·lel sense trepitjar-se el codi.

Si estàs construint amb .NET i encara no t'has llançat al flux de treball agentic, sincerament, ara és el moment de començar.
