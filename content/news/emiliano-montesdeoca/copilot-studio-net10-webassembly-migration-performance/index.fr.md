---
title: "Comment Copilot Studio a Migré vers .NET 10 WebAssembly et Gagné 20% de Vitesse"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "Les améliorations de .NET 10 WASM ne concernent pas seulement les nouveaux projets. Voici ce que Copilot Studio a mesuré après la mise à niveau depuis .NET 8 : fingerprinting automatique, WasmStripILAfterAOT par défaut et de vrais chiffres de performances d'exécution."
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

L'équipe Copilot Studio a fait quelque chose que tous les développeurs Blazor WASM voulaient savoir : ils ont réellement mis à niveau une application de production de .NET 8 vers .NET 10 et mesuré les résultats. La publication partage des chiffres spécifiques, ce qui est rare et vraiment utile.

## La Migration Était Ennuyeuse (C'est Positif)

Mettre à jour le framework cible, actualiser les références de paquets, corriger les changements cassants. C'est tout. La build .NET 10 tourne maintenant en production. La migration elle-même n'était pas la partie intéressante — les changements dans .NET 10 le sont.

## Fingerprinting Automatique des Ressources

Auparavant, distribuer une application WASM impliquait d'écrire des scripts personnalisés pour renommer les ressources publiées avec des hachages SHA256 pour l'invalidation du cache. Copilot Studio avait un script PowerShell faisant exactement cela — renommer les fichiers, injecter des attributs `integrity` dans le chargeur JavaScript, gérer tout manuellement.

Dans .NET 10, tout cela est intégré. Les ressources publiées sont automatiquement empreintées, importées directement depuis `dotnet.js` et validées avec intégrité sans intervention manuelle. L'équipe a supprimé le script de renommage.

Petit changement en portée, réduction significative de la complexité.

## WasmStripILAfterAOT Est Maintenant Activé par Défaut

Dans .NET 8, supprimer le IL des assemblages compilés AOT était opt-in. Dans .NET 10 c'est le comportement par défaut. Après la compilation AOT, le bytecode IL original est supprimé de la sortie — il n'est pas nécessaire au moment de l'exécution, et le garder gonflait la taille du paquet inutilement.

Copilot Studio utilise une optimisation spécifique : il distribue à la fois un moteur JIT (démarrage rapide) et un moteur AOT (performances maximales en régime permanent), les chargeant en parallèle et passant de JIT à AOT une fois qu'il est prêt. Il déduplique également les fichiers identiques entre les deux moteurs.

Le nouveau comportement de suppression d'IL signifie que les assemblages AOT ne correspondent plus bit pour bit à leurs homologues JIT, donc moins de fichiers sont dédupliqués :
- .NET 8 : 59 fichiers partagés
- .NET 10 : 22 fichiers partagés

Résultat net : taille du paquet approximativement 15% plus grande pour le moteur AOT. Le téléchargement AOT est ~6% plus lent sur LAN rapide, ~17% plus lent en 4G. Mais tout se passe en arrière-plan après que l'application est déjà interactive.

## Les Chiffres de Performance

Voici la partie qui compte :

- **~20% plus rapide** sur le premier appel (chemin froid)
- **~5% plus rapide** sur les appels suivants (chemin chaud)

Les améliorations sont les plus visibles dans les "grands bots" — des agents larges et complexes où le code compilé AOT domine. Pour des flux de travail plus simples, le gain est moindre.

## Si Vous Êtes Encore sur .NET 8

L'histoire de migration est genuinement simple : mettez à jour `<TargetFramework>`, actualisez les références de paquets, supprimez les scripts de fingerprinting personnalisés, et vous bénéficierez automatiquement de `WasmStripILAfterAOT`. Si vous compilez en AOT, attendez-vous à des gains de performances similaires.

Une note de la publication : si vous chargez le runtime .NET WASM dans un `WebWorker`, définissez `dotnetSidecar = true` lors de l'initialisation.

Post original : [Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
