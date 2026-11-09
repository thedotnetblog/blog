---
title: "Fin de support .NET 8 et .NET 9 : traitez cela comme une échéance de livraison"
date: 2026-07-19
author: 'Emiliano Montesdeoca'
description: "Le 10 novembre 2026 n'est pas juste une date de support ; c'est le point où le risque de mise à niveau reporté devient explicite."
tags:
  - dotnet
  - net10
  - security
  - platform-lifecycle
  - engineering-leadership
---

Original source: [.NET 8 and .NET 9 will reach End of Support on November 10, 2026](https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support/)

Cette annonce est simple, et les équipes devraient répondre avec la même clarté : si vous prévoyez de continuer à livrer sur .NET 8 ou .NET 9 au-delà du 10 novembre 2026, vous prenez une décision intentionnelle d'exécuter un runtime non supporté.

Les applications continueront de fonctionner. Ce n'est pas le point. Le point, c'est que les mises à jour de sécurité et de maintenance s'arrêtent. Une fois que cela se produit, chaque vulnérabilité connue sans chemin de rétroportage devient votre responsabilité opérationnelle.

Mon avis tranché : les organisations traitent souvent les mises à niveau de framework comme une maintenance optionnelle, puis paient cette décision lors de fenêtres d'urgence, de constats d'audit et d'escalades précipitées auprès des fournisseurs. La planification de mise à niveau devrait être un élément de la feuille de route produit, pas une tâche secondaire.

Une posture de migration pratique pour les équipes .NET :

Fixez le reciblage vers .NET 10 comme un objectif daté, pas un élément de backlog ouvert.

Exécutez les tests de compatibilité et de régression en parallèle du travail de fonctionnalité maintenant, pas au T4.

Suivez la préparation des dépendances et de l'hébergement comme des chantiers séparés, car beaucoup d'échecs se produisent en dehors du fichier de projet.

Utilisez Upgrade Assistant et la documentation des changements cassants tôt pour anticiper les surprises.

Si vous possédez des bibliothèques partagées utilisées par plusieurs produits, publiez votre calendrier de support .NET 10 publiquement dans votre organisation. Les équipes en aval ont besoin de délai.

Le marquage des composants hors support par Visual Studio compte aussi opérationnellement. Il crée un signal clair que le nettoyage de la chaîne d'outils fait partie du maintien de la conformité. Les équipes qui ignorent cela dérivent habituellement vers des états de SDK mixtes et un comportement de build incohérent.

Un détail peu discuté est que .NET 8 et .NET 9 convergent vers la même date de fin. Cela comprime les fenêtres de mise à niveau pour les organisations qui ont échelonné l'adoption en espérant plus de marge. Si vous êtes passé à .NET 9 pour l'accès aux fonctionnalités, vous atterrissez quand même sur la même falaise de support.

Pour les responsables de plateforme, la matrice de décision est simple : migrer avant l'échéance, ou documenter et accepter le risque non supporté avec des contrôles compensatoires. Il n'y a pas de troisième option où rien ne change.

La bonne nouvelle, c'est que .NET 10 est une cible LTS jusqu'en novembre 2028, ce qui achète une marge de manœuvre stable une fois le déplacement terminé.

N'attendez pas le dernier Patch Tuesday pour commencer. Traitez ceci comme une échéance de livraison avec des implications de sécurité, parce que c'est exactement ce que c'est.
