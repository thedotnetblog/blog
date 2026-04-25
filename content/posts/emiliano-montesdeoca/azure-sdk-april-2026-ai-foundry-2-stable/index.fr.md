---
title: "Azure SDK Avril 2026 : AI Foundry 2.0 et Ce Que les Développeurs .NET Doivent Savoir"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "La version Azure SDK d'avril 2026 livre Azure.AI.Projects 2.0.0 stable avec des changements cassants importants, des correctifs de sécurité critiques pour Cosmos DB et de nouvelles bibliothèques de Provisioning pour .NET."
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici](https://thedotnetblog.com/posts/emiliano-montesdeoca/azure-sdk-april-2026-ai-foundry-2-stable/).*

Les versions mensuelles du SDK sont souvent faciles à ignorer. Celle-ci a quelques points à retenir — surtout si vous construisez avec AI Foundry, Cosmos DB en Java, ou faites du provisionnement d'infrastructure depuis du code .NET.

## Azure.AI.Projects 2.0.0 — Changements Cassants Qui Font Sens

Le paquet NuGet `Azure.AI.Projects` atteint la version stable 2.0.0: séparations de namespaces, types renommés, et convention `Is*` cohérente pour les booléens.

## Cosmos DB Java : Correctif de Sécurité Critique (RCE)

La version 4.79.0 inclut un correctif critique pour une **vulnérabilité d'exécution de code à distance (CWE-502)**. Mise à jour immédiate requise.

## Nouvelles Bibliothèques de Provisioning pour .NET

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

## Conclusion

Le point fort pour les développeurs .NET ce mois-ci : `Azure.AI.Projects 2.0.0` est stable. Post original : [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).
