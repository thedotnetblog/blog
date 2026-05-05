---
title: "VS Code 1.116 — L'App Agents Obtient la Navigation Clavier et les Complétions de Contexte de Fichiers"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116 se concentre sur le polissage de l'app Agents — raccourcis clavier dédiés, améliorations d'accessibilité, complétions de contexte de fichiers et résolution de liens CSS @import."
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "vscode-1-116-agents-app-updates.md" >}}).*

VS Code 1.116 est la version d'avril 2026, et bien qu'elle soit plus légère que certaines mises à jour récentes, les changements sont ciblés et significatifs — surtout si vous utilisez l'app Agents au quotidien.

Voici ce qui a atterri, d'après les [notes de version officielles](https://code.visualstudio.com/updates/v1_116).

## Améliorations de l'app Agents

L'app Agents continue de mûrir avec un polissage de l'ergonomie qui fait une vraie différence dans les flux de travail quotidiens :

**Raccourcis clavier dédiés** — vous pouvez maintenant cibler la vue Changes, l'arborescence de fichiers dans Changes, et la vue des Personnalisations du Chat avec des commandes et raccourcis clavier dédiés. Si vous cliquiez partout dans l'app Agents pour naviguer, cela apporte des flux de travail entièrement pilotés au clavier.

**Dialogue d'aide à l'accessibilité** — appuyer sur `Alt+F1` dans la zone de saisie du chat ouvre maintenant un dialogue d'aide à l'accessibilité montrant les commandes et raccourcis disponibles. Les utilisateurs de lecteurs d'écran peuvent aussi contrôler la verbosité des annonces. Une bonne accessibilité profite à tout le monde.

**Complétions de contexte de fichiers** — tapez `#` dans le chat de l'app Agents pour déclencher les complétions de contexte de fichiers limitées à votre espace de travail actuel. C'est une de ces petites améliorations de qualité de vie qui accélèrent chaque interaction — plus besoin de taper des chemins de fichiers complets en référençant du code.

## Résolution des liens CSS `@import`

Agréable pour les développeurs frontend : VS Code résout maintenant les références CSS `@import` qui utilisent des chemins node_modules. Vous pouvez faire `Ctrl+clic` à travers des imports comme `@import "some-module/style.css"` en utilisant des bundlers. Petit mais élimine un point de friction dans les workflows CSS.

## Conclusion

VS Code 1.116 est une affaire de raffinement — rendre l'app Agents plus navigable, plus accessible et plus conviviale au clavier. Si vous passez beaucoup de temps dans l'app Agents (et je soupçonne que beaucoup d'entre nous le font), ces changements s'accumulent.

Consultez les [notes de version complètes](https://code.visualstudio.com/updates/v1_116) pour la liste exhaustive.
