---
title: "Mise à jour d'avril de Visual Studio 2026 : agent cloud, agents personnalisés et agent débogueur"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "La mise à jour d'avril de Visual Studio 2026 (18.5) apporte l'intégration d'agent cloud, des agents personnalisés au niveau utilisateur, les outils C++ en GA et un Agent Débogueur qui valide les corrections contre le comportement réel à l'exécution."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

[La mise à jour d'avril de Visual Studio 2026 (18.5)](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) inclut l'intégration d'agent cloud, des agents personnalisés au niveau utilisateur, les outils C++ passant en GA, et un nouvel Agent Débogueur.

## Agent cloud : déléguer le travail à une session Copilot distante

Depuis le sélecteur d'agents dans la fenêtre Chat, sélectionner **Cloud** permet de confier une tâche à un agent de codage Copilot distant. Vous décrivez le travail, l'agent crée un issue GitHub dans votre dépôt, puis ouvre une PR quand il a terminé. Vous recevez une notification avec "View PR" / "Open in browser" — tout fonctionne pendant que vous continuez à coder, ou même avec l'IDE fermé.

## Les agents personnalisés vous accompagnent maintenant partout

Les agents personnalisés au niveau utilisateur stockés dans `%USERPROFILE%/.github/agents/` ne sont plus limités à un dépôt — ils vous suivent d'un projet à l'autre. Le chemin de stockage est configurable sous Tools > Options > GitHub > Copilot > Chat. Le bouton `+` dans le sélecteur d'agents permet de créer directement de nouveaux agents. Ils obtiennent les mêmes capacités que les agents liés à un dépôt : conscience de l'espace de travail, outils, sélection de modèle et connexions MCP.

Agents intégrés : Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## Les outils d'édition de code C++ passent en GA

Deux outils — `get_symbol_call_hierarchy` et `get_symbol_class_hierarchy` — sont maintenant activés par défaut. Ils donnent à Copilot une navigation consciente du langage dans les bases de code C++, couvrant les hiérarchies d'héritage et les chaînes d'appel de fonctions. Activez via l'icône Tools dans Copilot Chat. Fonctionne mieux avec les modèles d'appel d'outils.

## Agent Débogueur : corrections validées contre le comportement réel à l'exécution

Démarrez depuis un issue GitHub ou Azure DevOps (ou une description en langage naturel), passez en mode Debugger, et l'agent :

1. Crée un reproducteur minimal
2. Génère des hypothèses de défaillance
3. Instrumente l'application avec des tracepoints et des breakpoints conditionnels
4. Lance une vraie session de débogage
5. Analyse la télémétrie en direct
6. Suggère un correctif précis

Vous restez dans la boucle tout au long du processus — c'est interactif, pas entièrement autonome.

## Correction de priorité IntelliSense

VS supprime désormais les complétions Copilot pendant que la liste IntelliSense est active. Une seule suggestion à la fois. C'était un point de friction fréquent et c'est maintenant activé par défaut.

Notes de version complètes et téléchargement sur [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/).
