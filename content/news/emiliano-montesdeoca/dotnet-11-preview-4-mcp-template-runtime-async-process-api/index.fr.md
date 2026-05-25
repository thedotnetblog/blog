---
title: ".NET 11 Preview 4 : Modèle de Serveur MCP, Bibliothèques Runtime-Async, API Processus"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 est disponible. Les points forts : le modèle de serveur MCP dans le SDK, les bibliothèques runtime compilées avec runtime-async, dotnet watch pour mobile, et une importante expansion de l'API Processus."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 est disponible. Chaque version d'une preview majeure de .NET ajoute une longue liste d'éléments couvrant le runtime, le SDK, les bibliothèques, ASP.NET Core, MAUI, C# et Entity Framework. Plutôt que de répéter la liste complète, voici ce qui a retenu mon attention.

## Le Modèle de Serveur MCP Débarque dans le SDK .NET

L'élément le plus intéressant : un modèle de projet serveur MCP est maintenant inclus dans le SDK. Cela signifie que `dotnet new mcp-server` (ou quel que soit le nom final de la commande) fonctionne directement. Pour ceux qui développent des outils MCP en .NET, cela réduit considérablement la friction initiale. L'intégration MCP dans la chaîne d'outils de la plateforme indique la direction que prend l'écosystème.

## Bibliothèques Runtime Compilées avec Runtime-Async

Le runtime lui-même compile désormais ses bibliothèques standard en utilisant la fonctionnalité runtime-async. C'est un changement interne qui affecte les performances — les machines à états async dans le runtime deviennent plus efficaces. L'importance ici n'est pas dans les changements d'API visibles ; c'est que runtime-async est suffisamment mature pour être utilisé avec la BCL elle-même, ce qui est un signal fort sur la maturité de la fonctionnalité.

## Optimisations JIT et Intrinsèques Matériels

La Preview 4 continue le travail sur le JIT. Des améliorations des intrinsèques matériels et de la génération de code arrivent ici — les détails se trouvent dans les notes de version du runtime. Ces changements améliorent généralement le débit sur les boucles de calcul intensif sans modifier votre code.

## Expansion de l'API Processus

Une mise à jour majeure de `System.Diagnostics.Process` est fournie dans la Preview 4 :

- `Process.RunAndCaptureTextAsync` — démarrer un processus, capturer stdout/stderr, attendre la sortie, le tout en un seul appel sans risque de deadlock
- `KillOnParentExit` — couplage léger du cycle de vie entre processus parent et enfant
- APIs basées sur `SafeProcessHandle` plus compatibles avec le trimmer

Si vous avez déjà écrit du code répétitif pour capturer la sortie d'un processus sans provoquer de deadlocks (lecture async de stdout *et* stderr simultanément), `RunAndCaptureTextAsync` est l'API qui vous manquait.

## dotnet watch pour Android et iOS

`dotnet watch` prend maintenant en charge la sélection d'appareil pour les projets .NET MAUI Android et iOS. Une itération plus rapide sur mobile sans gérer manuellement les connexions d'appareils dans la boucle de build.

## APIs de Compression Basées sur Span

De nouvelles APIs d'encodeur/décodeur Deflate, ZLib et GZip basées sur span arrivent dans les bibliothèques. Moins d'allocations lors du traitement de données compressées — pertinent si vous faites du traitement de données à haut débit.

## Essayez-le

[Télécharger .NET 11 Preview 4](https://dotnet.microsoft.com/download/dotnet/11.0) — c'est une preview, pas prête pour la production, mais cela vaut la peine de la tester sur vos projets pour détecter les problèmes avant le cycle RC.

Post original : [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
