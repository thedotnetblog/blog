---
title: "Mission Control pour les agents de codage : une expérience unifiée dans VS Code"
description: "VS Code rassemble les agents de codage locaux, cloud, CLI et tiers dans Agent Sessions pour que les développeurs puissent suivre, interrompre et coordonner le travail autonome."
date: 2026-08-07
author: Emiliano Montesdeoca
tags: [agents, orchestration, multi-agent, VS Code, automation, Codex]
slug: unified-agent-experience-mission-control
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

# Mission Control pour les agents de codage : une expérience unifiée dans VS Code

Un seul assistant de codage est facile à comprendre. Plusieurs agents travaillant dans différents endroits ne le sont pas.

Un agent s'exécute localement dans VS Code. Un autre travaille sur une issue GitHub dans le cloud. Un agent CLI vit dans le terminal. Un agent de codage tiers peut avoir un modèle de session différent et des limites différentes. Sans une vue partagée, les développeurs passent plus de temps à suivre le travail qu'à le superviser.

L'expérience unifiée des agents de VS Code résout ce problème de coordination avec Agent Sessions : un seul endroit pour lancer des agents, voir leur statut, ouvrir leurs conversations et intervenir quand le plan change.

Il s'agit moins d'ajouter un autre agent que de rendre plusieurs agents gérables.

## Une vue pour différents types de travail

L'article source décrit quatre participants distincts : GitHub Copilot local, Copilot Coding Agent dans le cloud, GitHub Copilot CLI et OpenAI Codex pour les abonnés Copilot éligibles.

Ils ont des forces différentes :

- Un agent local peut inspecter l'espace de travail actuel et effectuer des modifications rapides.
- Un agent de codage cloud peut travailler de manière asynchrone sur une issue et ouvrir une pull request.
- Un agent CLI s'adapte aux flux de travail basés sur le terminal et aux commandes opérationnelles.
- Un autre fournisseur peut offrir un modèle différent ou un style de raisonnement différent.

Agent Sessions donne à ces tâches une maison commune. Vous pouvez voir ce qui s'exécute, ce qu'il fait et où reprendre la conversation.

Cette visibilité est importante car le travail autonome ne supprime pas la coordination. Il en fait une tâche d'ingénierie de première classe.

## Les interruptions font partie du flux de travail

La source fait une simple observation : « Il est courant d'envoyer une invite et de réaliser que vous avez oublié quelque chose d'important. » Auparavant, le choix était souvent d'attendre ou d'annuler. Avec les éditeurs de chat, vous pouvez ouvrir une session active et ajouter des informations pendant que l'agent travaille.

C'est plus proche de la véritable collaboration. Les exigences changent. Un test révèle une hypothèse. Un examinateur remarque qu'une API doit rester rétrocompatible. L'agent utile n'est pas celui qui n'a jamais besoin de correction ; c'est celui qui peut absorber la correction sans perdre toute la tâche.

Pour le travail .NET, une interruption pourrait être aussi simple que :

```text
Keep the existing public route unchanged. Add the new behavior behind the application service,
use the existing ProblemDetails convention, and add a test for the old response shape.
```

L'instruction est courte car le référentiel porte déjà le contexte plus large. La session est l'endroit pour corriger la direction, pas pour reformuler tout le système.

## Les agents personnalisés transforment les habitudes d'équipe en rôles

VS Code introduit également des agents spécialisés tels que Plan. Au lieu de mettre en œuvre immédiatement, un agent de planification pose des questions sur la portée, les composants, les bibliothèques et les contraintes avant de produire une spécification de mise en œuvre.

Ce modèle est utile au-delà d'un agent intégré. Une équipe peut définir des rôles focalisés :

- **Research** rassemble les preuves et rédige un court dossier de décision.
- **Review** vérifie une modification par rapport aux conventions du référentiel.
- **Testing** identifie les cas manquants et propose un plan de test.
- **Architecture** compare les options sans modifier les fichiers.

Une petite définition d'agent personnalisé pourrait ressembler à ceci :

```yaml
type: agent
name: plan
description: "Refines vague requests into clear implementation specs"
prompt: |
  Ask about scope, constraints, existing patterns, and edge cases.
  Produce a concise specification before any implementation begins.
```

La partie utile n'est pas le YAML. C'est la séparation explicite des responsabilités. Un agent de planification ne doit pas modifier silencieusement le code de production. Un agent d'examen ne doit pas réécrire la conception qu'il est supposé évaluer.

## Les sous-agents réduisent les collisions de contexte

Les longues conversations accumulent un contexte sans rapport. Les sous-agents fournissent un espace de travail isolé pour une tâche de recherche bornée, puis retournent le résultat à la session principale.

C'est un bon choix pour les questions telles que :

```text
Analyze the API project and recommend an authentication strategy.
Return trade-offs and a decision record. Do not edit files.
```

L'agent principal reste concentré sur la mise en œuvre tandis que l'agent de recherche gère une question plus étroite. Le même principe s'applique aux équipes : une délégation claire produit de meilleurs résultats que de lancer plusieurs agents avec une autorité chevauchante.

## La mise en garde : plus d'agents signifie plus de coordination

Agent Sessions peut afficher l'activité, mais ne peut pas résoudre les conflits de propriété. Deux agents modifiant la même zone peuvent toujours créer un problème de fusion. Un agent cloud et un agent local peuvent faire des hypothèses incompatibles. Un agent personnalisé peut produire une recommandation qu'un autre agent ignore.

Fixez des limites :

1. Un agent possède la mise en œuvre pour une branche donnée.
2. Les agents de recherche retournent des artefacts, pas des modifications non suivi.
3. Les pull requests restent la limite d'examen.
4. Les noms et invites des agents indiquent ce qu'ils peuvent modifier.
5. La sortie de session est conservée quand elle explique une décision importante.

## Mon avis

L'avenir multi-agents n'est pas une file de fenêtres de chat. C'est une petite équipe avec des rôles, des transferts et une responsabilité.

Agent Sessions est utile car elle reconnaît cette réalité. Elle donne aux développeurs une surface de contrôle pour le travail qui se produit déjà dans l'éditeur, le terminal et le cloud. Le prochain gain de productivité viendra moins de l'existence de plus d'agents et plus de la rendre leurs limites lisibles.

Pour une équipe .NET, je commencerais par un agent de planification et un agent de mise en œuvre. Utilisez la sortie de planification comme la spécification de l'issue ou de la pull request, puis laissez l'agent de mise en œuvre travailler à l'intérieur de cette limite. Mesurez le travail inutile avant d'ajouter plus de rôles.

Le meilleur mission control est toujours celui qui rend la propriété évidente.
