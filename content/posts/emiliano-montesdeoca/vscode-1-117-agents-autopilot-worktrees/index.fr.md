---
title: "VS Code 1.117 : Les Agents Obtiennent Leurs Propres Branches Git et Je Suis Totalement Pour"
date: 2026-04-19
author: "Emiliano Montesdeoca"
description: "VS Code 1.117 apporte l'isolation par worktree pour les sessions d'agents, le mode Autopilot persistant et le support des sous-agents. Le workflow de codage agentique devient vraiment concret."
tags:
  - vscode
  - developer-tools
  - ai
  - github-copilot
  - agents
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "vscode-1-117-agents-autopilot-worktrees" >}}).*

La frontière entre « assistant IA » et « coéquipier IA » continue de s'amincir. VS Code 1.117 vient de sortir et les [notes de version complètes](https://code.visualstudio.com/updates/v1_117) sont bien remplies, mais l'histoire est claire : les agents deviennent des citoyens de première classe dans votre workflow de développement.

Voici ce qui compte vraiment.

## Le mode Autopilot se souvient enfin de votre préférence

Avant, il fallait réactiver Autopilot à chaque nouvelle session. Agaçant. Maintenant votre mode de permissions persiste d'une session à l'autre, et vous pouvez configurer la valeur par défaut.

L'Agent Host supporte trois configurations de session :

- **Default** — les outils demandent confirmation avant de s'exécuter
- **Bypass** — approuve tout automatiquement
- **Autopilot** — totalement autonome, répond à ses propres questions et continue

Si vous construisez un nouveau projet .NET avec des migrations, Docker et de la CI — réglez-le sur Autopilot une fois et oubliez-le. Cette préférence reste.

## Worktree et isolation git pour les sessions d'agents

C'est le gros morceau. Les sessions d'agents supportent maintenant l'isolation complète par worktree et git. Cela signifie que quand un agent travaille sur une tâche, il obtient sa propre branche et son propre répertoire de travail. Votre branche principale reste intacte.

Encore mieux — Copilot CLI génère des noms de branche significatifs pour ces sessions worktree. Fini le `agent-session-abc123`. Vous obtenez quelque chose qui décrit réellement ce que l'agent fait.

Pour les développeurs .NET qui gèrent plusieurs branches de fonctionnalités ou corrigent des bugs pendant qu'une longue tâche de scaffolding tourne, c'est un vrai changement. Vous pouvez avoir un agent qui construit vos contrôleurs d'API dans un worktree pendant que vous déboguez un problème dans la couche de services dans un autre. Pas de conflits. Pas de stashing. Pas de bazar.

## Sous-agents et équipes d'agents

L'Agent Host Protocol supporte maintenant les sous-agents. Un agent peut lancer d'autres agents pour gérer des parties d'une tâche. Pensez-y comme de la délégation — votre agent principal coordonne, et des agents spécialisés s'occupent des morceaux.

C'est encore tôt, mais le potentiel pour les workflows .NET est évident. Imaginez un agent qui gère vos migrations EF Core pendant qu'un autre configure vos tests d'intégration. On n'y est pas encore complètement, mais le fait que le support du protocole arrive maintenant signifie que l'outillage suivra rapidement.

## La sortie terminal automatiquement incluse quand les agents envoient de l'input

Petit mais significatif. Quand un agent envoie de l'input au terminal, la sortie du terminal est maintenant automatiquement incluse dans le contexte. Avant, l'agent devait faire un tour supplémentaire juste pour lire ce qui s'était passé.

Si vous avez déjà vu un agent exécuter `dotnet build`, échouer, puis faire un aller-retour supplémentaire juste pour voir l'erreur — cette friction a disparu. Il voit la sortie immédiatement et réagit.

## L'application Agents sur macOS se met à jour automatiquement

L'application autonome Agents sur macOS se met maintenant à jour automatiquement. Plus besoin de télécharger manuellement les nouvelles versions. Elle reste simplement à jour.

## Les petites choses qui valent la peine d'être connues

- Les **survols package.json** affichent maintenant la version installée et la dernière disponible. Utile si vous gérez des outils npm aux côtés de vos projets .NET.
- Les **images dans les commentaires JSDoc** s'affichent correctement dans les survols et les complétions.
- Les **sessions Copilot CLI** indiquent maintenant si elles ont été créées par VS Code ou en externe — pratique quand vous sautez entre les terminaux.
- **Copilot CLI, Claude Code et Gemini CLI** sont reconnus comme types de shell. L'éditeur sait ce que vous exécutez.

## Ce qu'il faut retenir

VS Code 1.117 n'est pas un déversement de fonctionnalités tape-à-l'œil. C'est de l'infrastructure. Isolation par worktree, permissions persistantes, protocoles de sous-agents — ce sont les briques pour un workflow où les agents gèrent des tâches réelles et parallèles sans marcher sur votre code.

Si vous développez avec .NET et que vous ne vous êtes pas encore lancé dans le workflow agentique, honnêtement, c'est le moment de commencer.
