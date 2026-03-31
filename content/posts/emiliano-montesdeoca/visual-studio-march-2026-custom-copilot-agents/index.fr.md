---
title: "La mise à jour de mars de Visual Studio permet de créer des agents Copilot personnalisés — et find_symbol est révolutionnaire"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "La mise à jour de mars 2026 de Visual Studio apporte des agents Copilot personnalisés, des skills réutilisables, l'outil find_symbol avec reconnaissance du langage, et le profiling avec Copilot depuis Test Explorer."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "visual-studio-march-2026-custom-copilot-agents.md" >}}).*

Visual Studio vient de recevoir sa mise à jour Copilot la plus significative. Mark Downie [a annoncé la version de mars](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/), et le titre principal concerne les agents personnalisés — mais honnêtement, l'outil `find_symbol` pourrait être la fonctionnalité qui change le plus votre workflow.

## Agents Copilot personnalisés dans votre repo

Envie que Copilot suive les standards de code de votre équipe ? Les agents personnalisés sont définis comme des fichiers `.agent.md` dans `.github/agents/`. Chaque agent a un accès complet au workspace, à la compréhension du code, aux outils, votre modèle préféré et aux connexions MCP.

## Agent skills : packs d'instructions réutilisables

Les skills sont chargés automatiquement depuis `.github/skills/` dans votre repo ou `~/.copilot/skills/` dans votre profil.

## find_symbol : navigation consciente du langage

Le nouvel outil `find_symbol` donne au mode agent de Copilot une navigation de symboles basée sur les services de langage. Au lieu de chercher du texte, l'agent peut trouver toutes les références d'un symbole et accéder aux informations de type et de portée.

Pour les développeurs .NET, c'est une amélioration massive — les bases de code C# avec des hiérarchies de types profondes en bénéficient énormément.

## Profiler des tests avec Copilot

Il y a un nouveau **Profile with Copilot** dans le menu contextuel du Test Explorer. Le Profiling Agent exécute le test et analyse automatiquement les performances.

## Perf tips pendant le débogage en direct

L'optimisation des performances se fait maintenant pendant le débogage. Visual Studio affiche le temps d'exécution inline. Ligne lente ? Cliquez sur le Perf Tip et demandez à Copilot des suggestions.

## Corriger les vulnérabilités NuGet depuis Solution Explorer

Un lien **Fix with GitHub Copilot** apparaît directement dans Solution Explorer quand une vulnérabilité est détectée.

## Pour conclure

Les agents personnalisés et les skills font le titre, mais `find_symbol` est la pépite cachée — il change fondamentalement la précision de Copilot lors du refactoring de code .NET. Téléchargez [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/) pour tout essayer.
