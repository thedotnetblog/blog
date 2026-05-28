---
title: "Foundry Local 1.1 : Transcription en Temps Réel, Embeddings et l'API de Réponses"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1 ajoute la transcription en direct depuis le microphone, les embeddings de texte et le support de l'API de Réponses — tout s'exécutant localement sans dépendance cloud, sans latence réseau, sans coût par token."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 a prouvé le concept : exécuter des modèles d'IA localement sur Windows, macOS (Apple Silicon) et Linux x64 avec un SDK adapté aux développeurs. La version 1.1 ajoute trois capacités qui couvrent de nombreux cas d'usage réels en production.

## Transcription Audio en Direct

La nouvelle fonctionnalité la plus significative : le streaming de parole en texte en temps réel directement depuis le microphone. Sous-titres, interfaces vocales, transcription de réunions, outils d'accessibilité — tout s'exécutant localement sans aucune dépendance cloud.

L'API est basée sur des sessions et transmet les résultats au fur et à mesure qu'ils arrivent, avec des marqueurs `is_final` pour distinguer le texte intermédiaire du texte finalisé. Disponible pour toutes les liaisons de langages : JavaScript, C#, Python et Rust.

Chargez un modèle de parole en streaming depuis le catalogue, créez une session avec les paramètres audio (fréquence d'échantillonnage, canaux, langue), lancez-la, poussez des blocs audio PCM bruts et consommez le flux asynchrone de résultats. Le post contient des exemples complets en Python et C#.

## Embeddings de Texte

Recherche sémantique, pipelines RAG, clustering, correspondance de similarité — tout cela nécessite des embeddings. Foundry Local 1.1 ajoute le support des modèles d'embedding pour générer des vecteurs localement depuis le même SDK, sans envoyer de données vers un endpoint cloud.

Pour les applications où la résidence des données est importante ou où vous traitez du contenu sensible, la génération locale d'embeddings est une capacité significative.

## API de Réponses

Foundry Local prend maintenant en charge l'[API de Réponses](https://platform.openai.com/docs/api-reference/responses) — l'interface structurée conçue pour les interactions agentiques. Cela ajoute :

- **Appel d'outils** — laissez les modèles s'exécutant localement invoquer des outils que vous définissez
- **Entrée multimodale vision-langage** — passez image + texte à des modèles capables de vision
- Compatible avec la forme d'API standard, donc les agents existants ciblant l'API de Réponses d'OpenAI fonctionnent contre des modèles locaux

## Améliorations de la Taille du Paquet

Deux changements réduisent la taille du paquet JavaScript :
- La couche FFI `koffi` a été remplacée par un addon C Node-API personnalisé
- Le fournisseur d'exécution WebGPU est livré comme plugin séparé, donc les applications qui n'ont pas besoin d'accélération GPU ne paient pas le coût de taille

Le SDK C# cible maintenant des versions de framework inférieures pour une compatibilité .NET plus large.

## Pourquoi C'est Important

Les trois capacités ensemble — transcription, embeddings, appel d'outils — couvrent les blocs de construction essentiels de nombreuses applications d'IA. Les exécuter localement signifie :
- Pas d'internet requis
- Pas de coûts par token
- Aucune donnée ne quitte la machine
- Latence constante quelles que soient les conditions réseau

Foundry Local est le bon choix pour les scénarios en périphérie, les charges de travail sensibles à la vie privée, les applications hors ligne, ou tout ce où vous voulez éviter la dépendance cloud pendant le développement.

Post original : [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
