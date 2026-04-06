---
title: "VS Code 1.115 — Notifications de Terminal en Arrière-plan, Mode Agent SSH et Plus"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 apporte les notifications de terminal en arrière-plan pour les agents, l'hébergement d'agents distants via SSH, le collage de fichiers dans les terminaux et le suivi des modifications avec reconnaissance de session. Voici ce qui compte pour les développeurs .NET."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "vscode-1-115-agent-improvements.md" >}}).*

VS Code 1.115 vient de [sortir](https://code.visualstudio.com/updates/v1_115), et bien que ce soit une version plus légère en termes de fonctionnalités phares, les améliorations liées aux agents sont vraiment utiles si vous travaillez quotidiennement avec des assistants de code IA.

Permettez-moi de souligner ce qui vaut vraiment la peine d'être connu.

## Les terminaux en arrière-plan communiquent avec les agents

C'est la fonctionnalité vedette. Les terminaux en arrière-plan notifient désormais automatiquement les agents lorsque les commandes se terminent, y compris le code de sortie et la sortie du terminal. Les invites de saisie dans les terminaux en arrière-plan sont également détectées et présentées à l'utilisateur.

Pourquoi est-ce important ? Si vous avez utilisé le mode agent de Copilot pour exécuter des commandes de build ou des suites de tests en arrière-plan, vous connaissez la frustration du "est-ce que c'est fini ?" — les terminaux en arrière-plan étaient essentiellement du fire-and-forget. Maintenant l'agent est notifié quand votre `dotnet build` ou `dotnet test` se termine, voit la sortie et peut réagir en conséquence. C'est un petit changement qui rend les workflows pilotés par les agents nettement plus fiables.

Il y a aussi un nouvel outil `send_to_terminal` qui permet aux agents d'envoyer des commandes aux terminaux en arrière-plan avec confirmation de l'utilisateur, corrigeant le problème où `run_in_terminal` avec un timeout déplaçait les terminaux en arrière-plan et les rendait en lecture seule.

## Hébergement d'agents distants via SSH

VS Code prend désormais en charge la connexion à des machines distantes via SSH, en installant automatiquement le CLI et en le démarrant en mode hôte d'agents. Cela signifie que vos sessions d'agents IA peuvent cibler directement des environnements distants — utile pour les développeurs .NET qui compilent et testent sur des serveurs Linux ou des VMs cloud.

## Suivi des modifications dans les sessions d'agents

Les modifications de fichiers effectuées pendant les sessions d'agents sont désormais suivies et restaurées, avec des diffs, annuler/rétablir et restauration d'état. Si un agent modifie votre code et que quelque chose tourne mal, vous pouvez voir exactement ce qui a changé et le reverter. La tranquillité d'esprit pour laisser les agents modifier votre codebase.

## Reconnaissance des onglets du navigateur et autres améliorations

Quelques ajouts supplémentaires de qualité de vie :

- **Suivi des onglets du navigateur** — le chat peut désormais suivre et lier les onglets du navigateur ouverts pendant une session, pour que les agents puissent référencer les pages web que vous consultez
- **Collage de fichiers dans le terminal** — collez des fichiers (y compris des images) dans le terminal avec Ctrl+V, glisser-déposer ou clic droit
- **Couverture de tests dans la minimap** — les indicateurs de couverture de tests s'affichent désormais dans la minimap pour un aperçu visuel rapide
- **Pinch-to-zoom sur Mac** — le navigateur intégré prend en charge les gestes de pinch-to-zoom
- **Droits Copilot dans les Sessions** — la barre d'état affiche les informations d'utilisation dans la vue Sessions
- **Favicon dans Aller au Fichier** — les pages web ouvertes affichent des favicons dans la liste de sélection rapide

## Pour conclure

VS Code 1.115 est une version incrémentale, mais les améliorations des agents — notifications de terminal en arrière-plan, hébergement d'agents SSH et suivi des modifications — contribuent à une expérience nettement plus fluide pour le développement assisté par IA. Si vous utilisez le mode agent de Copilot pour des projets .NET, ce sont le genre d'améliorations de qualité de vie qui réduisent les frictions au quotidien.

Consultez les [notes de version complètes](https://code.visualstudio.com/updates/v1_115) pour tous les détails.
