---
title: "dotnet new WinUI : Créer des apps Windows sans toucher à Visual Studio"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "Les modèles de projet WinUI fonctionnent maintenant avec dotnet new — apps vierges, modèles NavigationView et plus encore. Support VS Code, Visual Studio non requis, avec Fluent Design intégré par défaut."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

Le développement WinUI nécessitait auparavant Visual Studio. Cela est en train de changer : Microsoft a publié des modèles de projets et d'éléments open source pour WinUI qui fonctionnent avec `dotnet new`, intégrant le développement d'applications Windows dans le workflow standard de la CLI.

## Démarrer en trois commandes

```shell
# Installer les modèles
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# Créer une app NavigationView
dotnet new winui-navview -n MyApp

# L'exécuter
cd MyApp
dotnet run
```

Pas de Visual Studio, pas de configuration manuelle du projet. L'application s'exécute avec `dotnet run`.

## Ce qui est inclus

**Modèle vierge** (`dotnet new winui`) — un point de départ moderne avec une barre de titre Fluent déjà configurée, une icône d'app mise à jour avec un asset `.ico`, et des valeurs par défaut correctes pour le mode clair/sombre. Mieux que l'ancien modèle vierge qui vous laissait configurer les bases vous-même.

**Modèle NavigationView** (`dotnet new winui-navview`) — le modèle de navigation maître-détail, entièrement configuré avec un NavigationView, une barre de titre moderne et une structure de navigation multi-pages. Suit la silhouette standard des apps Windows pour les applications basées sur la navigation. Si vous construisez quelque chose avec une navigation latérale, commencez ici.

Les deux modèles suivent les [silhouettes d'apps Windows](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — des modèles Fluent Design modernes pour la mise en page, la navigation et la structure visuelle — dès le départ.

## Pourquoi c'est important pour les développeurs qui n'utilisent pas Visual Studio

Les développeurs WinUI utilisant VS Code, Rider ou les outils en ligne de commande ont été mal servis. Les modèles Visual Studio existants n'étaient pas utilisables en dehors de VS — il fallait recréer manuellement la structure du projet et configurer les bases.

Ces modèles sont open source (voir [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)), développés à partir des [retours de la communauté](https://github.com/microsoft/microsoft-ui-xaml/issues/10388), et disponibles maintenant. Le support Visual Studio est en cours — ces mêmes modèles fonctionneront également là-bas à terme.

Pour les équipes qui veulent automatiser la configuration de leurs projets WinUI, l'intégrer dans la CI, ou simplement utiliser un éditeur autre que Visual Studio, c'est une amélioration significative.

Post original : [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
