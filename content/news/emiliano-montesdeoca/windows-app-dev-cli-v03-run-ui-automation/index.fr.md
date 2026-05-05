---
title: "Windows App Dev CLI v0.3 : F5 depuis le terminal et UI Automation pour les agents"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 apporte winapp run pour les lancements debug depuis le terminal, winapp ui pour l'automatisation UI, et un nouveau package NuGet qui fait fonctionner dotnet run avec les apps packagées."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

L'expérience F5 de Visual Studio est formidable. Mais devoir ouvrir VS uniquement pour lancer et déboguer une application Windows packagée, c'est trop — que ce soit dans un pipeline CI, un workflow automatisé, ou quand un agent IA effectue les tests.

Windows App Development CLI v0.3 vient d'être [publié](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) et répond directement à ce besoin avec deux fonctionnalités phares : `winapp run` et `winapp ui`.

## winapp run : F5 depuis n'importe où

`winapp run` prend un dossier d'application non packagée et un manifeste, et fait tout ce que VS fait au lancement debug : enregistre un package loose, lance l'application et préserve le `LocalState` entre les re-déploiements.

```bash
# Compiler l'app, puis la lancer comme app packagée
winapp run ./bin/Debug
```

Fonctionne pour WinUI, WPF, WinForms, Console, Avalonia et plus. Les modes sont conçus pour les développeurs et les workflows automatisés :

- **`--detach`** : Lance et rend immédiatement le contrôle au terminal. Idéal pour CI/automation.
- **`--unregister-on-exit`** : Nettoie le package enregistré à la fermeture de l'app.
- **`--debug-output`** : Capture les messages `OutputDebugString` et les exceptions en temps réel.

## Nouveau package NuGet : dotnet run pour les apps packagées

Pour les développeurs .NET, il y a un nouveau package NuGet : `Microsoft.Windows.SDK.BuildTools.WinApp`. Après installation, `dotnet run` gère tout l'inner loop : build, préparation du package loose-layout, enregistrement Windows et lancement — en une seule étape.

```bash
# Laisser winapp init tout configurer
winapp init
# Ou installer directement
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui : UI Automation depuis la ligne de commande

C'est la fonctionnalité qui ouvre les scénarios agentiques. `winapp ui` donne un accès UI Automation complet à toute application Windows en cours d'exécution — WPF, WinForms, Win32, Electron, WinUI3 — depuis le terminal.

Ce qu'on peut faire :

- Lister toutes les fenêtres de niveau supérieur
- Parcourir l'arborescence UI Automation complète d'une fenêtre
- Rechercher des éléments par nom, type ou ID d'automatisation
- Cliquer, invoquer et définir des valeurs
- Prendre des captures d'écran
- Attendre l'apparition d'éléments — idéal pour la synchronisation de tests

Combiner `winapp ui` avec `winapp run` donne un workflow complet build → lancement → vérification depuis le terminal. Un agent peut exécuter l'app, inspecter l'état de l'interface et valider le résultat.

## Autres nouveautés

- **`winapp unregister`** : Supprime un package sideloadé quand on a terminé.
- **`winapp manifest add-alias`** : Ajoute un alias pour lancer l'app par nom depuis le terminal.
- **Complétion automatique** : Un seul commande pour configurer la complétion PowerShell.

## Installation

```bash
winget install Microsoft.WinAppCli
# ou
npm install -g @microsoft/winappcli
```

La CLI est en preview publique. Le [dépôt GitHub](https://github.com/microsoft/WinAppCli) contient la documentation complète et l'[annonce originale](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) tous les détails.
