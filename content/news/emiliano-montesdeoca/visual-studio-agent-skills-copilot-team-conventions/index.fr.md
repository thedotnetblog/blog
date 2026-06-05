---
title: "Agent Skills dans Visual Studio : Apprenez à Copilot Comment Votre Équipe Travaille Vraiment"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio prend désormais en charge les Agent Skills — des ensembles d'instructions réutilisables qui apprennent à Copilot les workflows, standards de code et conventions spécifiques de votre équipe. Définissez une fois, appliquez automatiquement."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

L'une des frustrations persistantes avec les assistants de codage IA : ils connaissent bien la programmation générale mais ne connaissent pas les conventions spécifiques de *votre* équipe, vos API internes ou vos patterns préférés. À chaque session, vous réexpliquez le contexte. Agent Skills dans Visual Studio est conçu pour résoudre ce problème.

## Ce que Sont les Agent Skills

Des ensembles d'instructions réutilisables — définis dans des fichiers `SKILL.md` — qui apprennent aux agents Copilot comment gérer des tâches spécifiques. Définissez un skill pour "comment exécuter notre pipeline de build", "comment générer du boilerplate pour notre couche de service" ou "notre checklist de révision de code". L'agent applique le skill automatiquement quand c'est pertinent.

Ce n'est pas un concept nouveau (`.github/copilot-instructions.md` existe depuis un moment), mais l'intégration de Visual Studio en fait des objets de première classe avec une interface de découverte.

## Création de Skills dans Visual Studio

Le flux d'interface intégré : cliquez sur l'icône d'outils dans Copilot Chat, ouvrez le panneau des skills, cliquez sur `+`. Vous choisissez la portée globale (personnelle) ou au niveau de la solution, choisissez un nom et Visual Studio génère un modèle. Le mode Agent de Copilot peut ensuite vous aider à remplir le modèle — utilisez l'agent pour écrire le skill pour l'agent.

Actuellement dans le canal Insiders, à venir bientôt en Release.

Vous pouvez également créer des skills manuellement :

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## Emplacements de Découverte

Les skills sont auto-découverts depuis des chemins standard :

**Au niveau de la solution (partagé via le dépôt) :** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**Global/personnel (votre profil utilisateur, disponible partout) :** `~/.copilot/skills/`, `~/.agents/skills/`

Le support multi-emplacement signifie que la même convention fonctionne avec GitHub Copilot, Claude Code et d'autres frameworks d'agents — définissez vos skills une fois, utilisez-les partout.

## Le Format

Les skills suivent le format [agentskills.io/specification](https://agentskills.io/specification) — une spécification basée sur Markdown à la fois lisible par les humains et analysable par les machines. Vous pouvez inclure des scripts, des modèles et des exemples aux côtés du `SKILL.md`.

## Valeur Pratique

La vraie puissance n'est pas dans les fonctionnalités individuelles — c'est dans la combinaison des skills partagés par l'équipe (via `.github/skills/`) et des skills personnels (via `~/.agents/skills/`). Les skills d'équipe encodent comment votre organisation fait les choses. Les skills personnels encodent comment vous travaillez spécifiquement. L'agent obtient les deux contextes automatiquement.

Pour les organisations qui utilisent déjà intensément Copilot, c'est une étape significative vers rendre l'outil réellement conscient des conventions spécifiques de votre base de code plutôt que de donner des conseils génériques.

Post original : [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
