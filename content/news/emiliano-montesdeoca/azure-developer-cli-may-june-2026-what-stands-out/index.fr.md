---
title: "Azure Developer CLI devient de plus en plus un meilleur outil d'inner loop"
date: 2026-06-28
author: "Emiliano Montesdeoca"
description: "Les versions de mai et juin 2026 d'Azure Developer CLI ajoutent beaucoup, mais la plus grande valeur est la façon dont elles améliorent la boucle quotidienne : meilleure gestion des outils, provisioning plus sûr, meilleur support des extensions et workflows d'exécution plus pratiques."
tags:
  - Azure Developer CLI
  - azd
  - Azure
  - Developer Tools
  - .NET
---

*Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Les grands récapitulatifs CLI peuvent être éprouvants à lire parce qu'ils mélangent de grosses améliorations de workflow et de petits correctifs dans un même mur de texte.

Alors voici ma version courte : les dernières mises à jour d'**Azure Developer CLI** comptent parce que `azd` continue de devenir un **meilleur outil d'inner loop**, pas seulement un habillage de déploiement.

C'est ça, le vrai changement.

## La gestion des outils devient une partie du produit, pas une tâche annexe

L'une de mes nouveautés préférées est la nouvelle commande `azd tool`.

Tout ce qui réduit la friction d'installation mérite qu'on s'y arrête, surtout dans les projets où un environnement fonctionnel dépend d'un mélange de SDK, de CLI, de Docker, de Bicep et d'extensions.

Si l'outil peut désormais aider à découvrir, installer, vérifier et mettre à jour ces dépendances directement, cela enlève beaucoup des modes de panne agaçants qui frappent souvent d'abord les nouveaux arrivants.

C'est de la vraie valeur.

## `azd exec` semble aussi plus important qu'il n'y paraît

À première vue, `azd exec` peut ressembler à une petite fonctionnalité de confort.

Je ne pense pas que ce soit le cas.

Exécuter des commandes avec tout le contexte de l'environnement `azd`, y compris la résolution des secrets, est exactement le type de capacité qui rend l'automatisation locale et le scripting beaucoup plus propres.

Cela réduit le besoin de scripts de glue supplémentaires et aide à garder une exécution cohérente d'un environnement à l'autre.

C'est un gain très concret.

## Le provisioning plus sûr et le meilleur comportement d'annulation sont des améliorations sous-estimées

La version inclut aussi des changements autour des dépendances de provisioning, de la gestion de l'annulation et du comportement de déploiement, des choses qui peuvent ne pas paraître glamour mais sont très bienvenues.

Les invites d'annulation interactives, une meilleure modélisation des dépendances et un état de déploiement plus clair sont exactement le genre d'améliorations qui donnent à un CLI un air fiable quand vous travaillez avec de vraies ressources Azure.

Et la confiance est un sujet majeur pour ce genre d'outils.

## Mon avis

Plus `azd` s'améliore en configuration, scripting, sécurité de déploiement et support des extensions, plus il ressemble à quelque chose que vous pouvez garder dans votre boucle quotidienne plutôt que de ne toucher qu'au moment du déploiement.

C'est la bonne direction.

Pour les équipes qui construisent des applications cloud-native ou pilotées par l'IA sur Azure, cela rend le CLI plus utile là où cela compte le plus : pendant le développement réel.

Article original : [Azure Developer CLI (azd) – May and June 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/)