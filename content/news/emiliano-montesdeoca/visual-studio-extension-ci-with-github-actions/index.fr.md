---
title: "Les équipes d'extensions Visual Studio devraient cesser de publier par habitude et commencer à publier par pipeline"
date: 2026-07-23
author: 'Emiliano Montesdeoca'
description: "Un flux GitHub Actions reproductible pour le versionnement et la publication VSIX est désormais suffisamment simple pour qu'il soit difficile de justifier des étapes de publication manuelles."
tags:
  - visual-studio
  - vsix
  - github-actions
  - ci-cd
  - developer-tooling
---

Source originale : [Automating your Visual Studio extension builds with GitHub Actions](https://devblogs.microsoft.com/visualstudio/automating-your-visual-studio-extension-builds-with-github-actions/)

Si vous maintenez des extensions Visual Studio et que vous effectuez encore manuellement une part significative de vos publications, voici votre signal pour moderniser vos pratiques.

Le workflow présenté dans cet article est délibérément pratique : définir le numéro de version, compiler, publier les artefacts de test dans une galerie, puis publier les binaires stables sur le Marketplace. Aucune lourde cérémonie plateforme, juste un comportement de publication déterministe.

Ce que j'apprécie le plus, c'est que le versionnement soit traité comme un état du pipeline, et non comme un élément de checklist pré-publication. Cette seule décision élimine un nombre surprenant d'erreurs : métadonnées discordantes, versions d'assembly obsolètes et notes de version incohérentes.

La séparation entre la publication en galerie et la publication sur le Marketplace est également mature sur le plan opérationnel. Les équipes ont besoin d'un endroit pour les builds de validation rapide qui n'ont pas la sémantique d'une version officielle. Tout pousser directement sur le Marketplace crée des frictions élevées et encourage des raccourcis risqués.

Un modèle de publication solide pour les équipes d'extensions est le suivant :

Sur les pull requests et les commits sur la branche principale, produisez des artefacts CI VSIX et publiez-les en galerie pour les testeurs.

Sur les releases taguées, publiez les packages signés et validés sur le Marketplace.

Limitez la gestion des tokens au minimum avec des secrets dédiés et des périmètres de privilèges minimaux.

Mon avis subjectif : les écosystèmes d'extensions accusent un retard par rapport aux écosystèmes d'applications en matière de discipline CI, car les petites équipes supposent que les workflows manuels sont gérables. Ils le sont jusqu'au jour où ils ne le sont plus. Un correctif expédié à la hâte, un package cassé, une mise à jour de manifeste oubliée, et la confiance s'effondre.

Ces actions réutilisables sont utiles car elles encapsulent une logique de publication répétée une seule fois et permettent aux équipes de se concentrer sur la qualité de l'extension plutôt que sur la mécanique d'empaquetage.

Un jugement d'ingénierie reste nécessaire. Vous devez conditionner la publication sur le Marketplace à des contrôles de qualité, et traiter les manifestes de publication comme des artefacts de release audités. Mais la complexité de base du pipeline est désormais suffisamment faible pour que les publications exclusivement manuelles relèvent surtout de la dette technique.

Si vous dirigez le développement d'extensions, standardisez ce processus dès maintenant sur l'ensemble de vos dépôts. Vous obtiendrez une meilleure traçabilité, un onboarding plus facile et moins de goulots d'étranglement liés à une seule personne.

Déploiement suggéré :

Commencez par la compilation et la publication en galerie pour une extension.

Introduisez le marquage de version après avoir validé vos conventions manifeste-source.

Ajoutez la publication sur le Marketplace seulement une fois que la gestion des secrets et les contrôles de publication sont en place.

Il ne s'agit pas de suivre la mode DevOps. Il s'agit de fiabilité pour les personnes qui installent vos outils et qui s'attendent à ce que les mises à jour fonctionnent.

Les écosystèmes d'extensions stables se construisent de la même manière que les applications stables : avec une automatisation fiable et répétable qui élimine les approximations humaines.