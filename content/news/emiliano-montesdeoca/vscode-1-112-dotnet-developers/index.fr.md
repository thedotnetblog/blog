---
title: "VS Code 1.112 : Ce qui devrait vraiment intéresser les développeurs .NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 vient de sortir avec des améliorations d'agents, un débogueur de navigateur intégré, le sandboxing MCP et le support monorepo. Voici ce qui compte vraiment si vous développez avec .NET."
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

VS Code 1.112 vient d'atterrir, et honnêtement ? Celui-ci frappe différemment si vous passez vos journées dans le monde .NET. Il y a beaucoup dans les [notes de version officielles](https://code.visualstudio.com/updates/v1_112), mais laissez-moi vous épargner du défilement et me concentrer sur ce qui nous importe vraiment.

## Copilot CLI est devenu bien plus utile

Le grand thème de cette version est l'**autonomie de l'agent** — donner à Copilot plus de liberté pour faire son travail sans que vous surveilliez chaque étape.

### Direction et file d'attente de messages

Vous connaissez ce moment où Copilot CLI est à mi-chemin d'une tâche et vous réalisez que vous avez oublié de mentionner quelque chose ? Avant, vous deviez attendre. Maintenant vous pouvez envoyer des messages pendant qu'une requête est encore en cours — soit pour diriger la réponse actuelle, soit pour mettre en file d'attente des instructions de suivi.

C'est énorme pour ces tâches de scaffolding `dotnet` plus longues où vous regardez Copilot configurer un projet et pensez "oh attends, j'ai aussi besoin de MassTransit là-dedans."

### Niveaux de permissions

C'est celui qui m'excite le plus. Les sessions Copilot CLI supportent maintenant trois niveaux de permissions :

- **Permissions par défaut** — le flux habituel où les outils demandent confirmation avant d'exécuter
- **Contourner les approbations** — auto-approuve tout et réessaie en cas d'erreur
- **Autopilote** — entièrement autonome : approuve les outils, répond à ses propres questions et continue jusqu'à ce que la tâche soit terminée

Si vous faites quelque chose comme créer une nouvelle API ASP.NET Core avec Entity Framework, des migrations et un setup Docker — le mode Autopilote signifie que vous décrivez ce que vous voulez et allez chercher un café. Il se débrouillera.

Vous pouvez activer l'Autopilote avec le paramètre `chat.autopilot.enabled`.

### Prévisualiser les changements avant délégation

Quand vous déléguez une tâche à Copilot CLI, il crée un worktree. Avant, si vous aviez des changements non commités, vous deviez vérifier le Contrôle de Source pour voir ce qui serait affecté. Maintenant la vue Chat affiche les changements en attente juste là avant que vous décidiez de les copier, déplacer ou ignorer.

Petit détail, mais ça vous évite ce moment "attends, qu'est-ce que j'avais en staging ?"

## Déboguez les apps web sans quitter VS Code

Le navigateur intégré supporte maintenant le **débogage complet**. Vous pouvez placer des breakpoints, parcourir le code pas à pas et inspecter les variables — le tout dans VS Code. Plus besoin de basculer vers Edge DevTools.

Il y a un nouveau type de débogage `editor-browser`, et si vous avez déjà des configurations de lancement `msedge` ou `chrome`, migrer est aussi simple que changer le champ `type` dans votre `launch.json` :

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

Pour les développeurs Blazor, c'est un game changer. Vous exécutez déjà `dotnet watch` dans le terminal — maintenant votre débogage reste dans la même fenêtre aussi.

Le navigateur a aussi obtenu des niveaux de zoom indépendants (enfin), des menus contextuels avec clic droit appropriés, et le zoom est mémorisé par site web.

## Sandboxing des serveurs MCP

Ceci importe plus que vous ne le pensez. Si vous utilisez des serveurs MCP — peut-être que vous en avez configuré un personnalisé pour vos ressources Azure ou vos requêtes de base de données — ils fonctionnaient avec les mêmes permissions que votre processus VS Code. Ça signifie un accès total à votre système de fichiers, réseau, tout.

Maintenant vous pouvez les sandboxer. Dans votre `mcp.json` :

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

Quand un serveur sandboxé a besoin d'accéder à quelque chose qu'il n'a pas, VS Code vous demande d'accorder la permission. Bien mieux que l'approche "espérons que personne ne fait rien de bizarre".

> **Note :** Le sandboxing est disponible sur macOS et Linux pour l'instant. Le support Windows arrive — les scénarios distants comme WSL fonctionnent cependant.

## Découverte des personnalisations en monorepo

Si vous travaillez dans un monorepo (et soyons honnêtes, beaucoup de solutions .NET d'entreprise finissent par en être un), ça résout un vrai point douloureux.

Avant, si vous ouvriez un sous-dossier de votre repo, VS Code ne trouvait pas votre `copilot-instructions.md`, `AGENTS.md` ou vos skills personnalisés situés à la racine du dépôt. Maintenant avec le paramètre `chat.useCustomizationsInParentRepositories`, il remonte jusqu'à la racine `.git` et découvre tout.

Ça signifie que votre équipe peut partager des instructions d'agent, des fichiers de prompt et des outils personnalisés entre tous les projets dans un monorepo sans que tout le monde ait à ouvrir le dossier racine.

## /troubleshoot pour le débogage d'agents

Vous avez déjà configuré des instructions personnalisées ou des skills et vous vous êtes demandé pourquoi ils ne sont pas détectés ? Le nouveau skill `/troubleshoot` lit les logs de débogage de l'agent et vous dit ce qui s'est passé — quels outils ont été utilisés ou ignorés, pourquoi les instructions n'ont pas chargé, et ce qui cause des réponses lentes.

Activez-le avec :

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

Puis tapez simplement `/troubleshoot why is my custom skill not loading?` dans le chat.

Vous pouvez aussi exporter et importer ces logs de débogage maintenant, ce qui est super pour les partager avec votre équipe quand quelque chose ne fonctionne pas comme prévu.

## Support des fichiers image et binaires

Les agents peuvent maintenant lire les fichiers image depuis le disque et les fichiers binaires nativement. Les fichiers binaires sont présentés au format hexdump, et les sorties image (comme les captures d'écran du navigateur intégré) s'affichent dans une vue carrousel.

Pour les développeurs .NET, pensez : collez une capture d'écran d'un bug UI dans le chat et laissez l'agent comprendre ce qui ne va pas, ou faites-lui analyser la sortie du rendu d'un composant Blazor.

## Références de symboles automatiques

Petite amélioration de qualité de vie : quand vous copiez un nom de symbole (une classe, méthode, etc.) et le collez dans le chat, VS Code le convertit maintenant automatiquement en une référence `#sym:Name`. Ça donne à l'agent le contexte complet sur ce symbole sans que vous ayez à l'ajouter manuellement.

Si vous voulez du texte brut à la place, utilisez `Ctrl+Shift+V`.

## Les plugins peuvent maintenant être activés/désactivés

Avant, désactiver un serveur MCP ou un plugin signifiait le désinstaller. Maintenant vous pouvez les activer et désactiver — globalement et par workspace. Clic droit dans la vue Extensions ou la vue Personnalisations et c'est fait.

Les plugins de npm et pypi peuvent aussi se mettre à jour automatiquement maintenant, bien qu'ils demanderont une approbation d'abord puisque les mises à jour signifient exécuter du nouveau code sur votre machine.

## Pour conclure

VS Code 1.112 pousse clairement fort sur l'expérience agent — plus d'autonomie, meilleur débogage, sécurité plus serrée. Pour les développeurs .NET, le débogage du navigateur intégré et les améliorations de Copilot CLI sont les fonctionnalités phares.

Si vous n'avez pas encore essayé de lancer une session Copilot CLI complète en mode Autopilote pour un projet .NET, cette version est un bon moment pour commencer. N'oubliez pas de configurer vos permissions et laissez mijoter.

[Télécharger VS Code 1.112](https://code.visualstudio.com/updates/v1_112) ou mettre à jour depuis VS Code via **Aide > Vérifier les mises à jour**.
