---
title: "FIDES est exactement le genre d'histoire de sécurité déterministe pour agents que je veux voir plus souvent"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Les nouvelles capacités FIDES dans Agent Framework sont importantes parce qu'elles déplacent la défense contre le prompt injection des heuristiques vers une politique applicable, fondée sur le contenu étiqueté et les vérifications de middleware."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

Les défenses contre le prompt injection donnent souvent l'impression de reposer sur un terrain fragile.

Vous ajoutez un system prompt plus fort. Vous ajoutez un filtre. Vous mettez quelques listes d'autorisation. Et vous espérez que la prochaine entrée étrange ne casse pas les hypothèses.

C'est pourquoi **FIDES** est intéressant.

Le point fort de l'histoire, c'est qu'il fait évoluer la sécurité vers quelque chose de plus déterministe :

- des étiquettes sur le contenu
- la propagation des étiquettes tout au long du workflow
- l'application via middleware avant l'exécution d'outils privilégiés
- des limites de politique claires sur ce que le contexte non fiable peut influencer

## L'article source est direct dans le bon sens

Il commence en disant que le prompt injection est "**le risque numéro 1 du OWASP LLM Top 10**".

Très bien.

J'aime ce genre de franchise ici, parce que trop d'équipes traitent encore la sécurité des agents comme une préoccupation future au lieu d'un problème actuel de conception runtime.

Et l'article enchaîne avec un contraste pratique fort : la plupart des défenses actuelles sont heuristiques, alors que FIDES essaie de faire passer le système vers la politique et l'application.

C'est exactement le bon changement.

## Ce qui le rend plus convaincant qu'un autre livre blanc de sécurité

Beaucoup d'écrits sur la sécurité de l'IA restent abstraits.

Cet article fait mieux. Il déroule un exemple très concret : un agent de triage d'issues GitHub, un corps d'issue malveillant, une lecture de fichier privilégiée et une tentative de fuite via un commentaire public.

C'est utile parce que cela ancre toute la discussion dans un workflow réel.

Et une fois qu'on voit ce scénario, la valeur des contrôles déterministes devient beaucoup plus facile à comprendre.

## L'idée clé n'est pas "rendre le modèle plus intelligent"

Le plus important ici, c'est que FIDES ne demande pas au modèle de devenir magiquement meilleur pour détecter les attaques.

Il modifie le contrat d'exécution.

Cela signifie :

- le contenu est étiqueté
- les étiquettes se propagent
- les outils déclarent ce qu'ils acceptent
- le middleware bloque les chemins non sûrs avant l'exécution

C'est une approche bien plus saine.

Parce qu'une fois que l'agent peut appeler des outils avec de vraies conséquences, la sécurité ne peut pas dépendre uniquement du fait que le modèle passe une bonne journée ou non.

## Mon avis

C'est exactement le type de direction en matière de sécurité des agents que je veux voir plus souvent.

Pas "faites confiance au modèle pour ignorer les mauvaises instructions", mais "construisez la barrière de politique dans le runtime".

C'est un modèle beaucoup plus sain.

Et si les frameworks d'agents veulent être pris au sérieux en production, il leur faudra davantage d'histoires comme celle-ci.

Article original : [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)