---
title: "Le Dashboard d'Aspire 13.2 a maintenant une API de télémétrie — et ça change tout"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 apporte un export de télémétrie plus intelligent, une API programmable pour les traces et logs, et des améliorations de visualisation GenAI. Voici pourquoi c'est important pour votre workflow de débogage."
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "aspire-132-dashboard-export-telemetry.md" >}}).*

Si vous développez des applications distribuées avec .NET Aspire, vous savez déjà que le dashboard est la meilleure chose de toute l'expérience. Toutes vos traces, logs et métriques au même endroit — pas de Jaeger externe, pas de configuration Seq, pas de moments « laissez-moi vérifier l'autre terminal ».

Aspire 13.2 vient de considérablement améliorer les choses. James Newton-King [a annoncé la mise à jour](https://devblogs.microsoft.com/aspire/aspire-dashboard-improvements-export-and-telemetry/), et honnêtement ? Les fonctionnalités d'export de télémétrie et l'API justifient à elles seules la mise à niveau.

## Exporter la télémétrie comme une personne normale

Voici le scénario qu'on a tous vécu : vous déboguez un problème distribué, vous le reproduisez enfin après vingt minutes de configuration, et maintenant vous devez partager ce qui s'est passé avec votre équipe. Avant ? Des captures d'écran. Du copier-coller d'identifiants de traces. Le bazar habituel.

Aspire 13.2 ajoute un dialogue **Gérer les logs et la télémétrie** où vous pouvez :

- Effacer toute la télémétrie (utile avant une tentative de reproduction)
- Exporter la télémétrie sélectionnée dans un fichier ZIP au format standard OTLP/JSON
- Ré-importer ce ZIP dans n'importe quel dashboard Aspire ultérieurement

Ce dernier point est la fonctionnalité phare. Vous reproduisez un bug, exportez la télémétrie, l'attachez à votre work item, et votre collègue peut l'importer dans son propre dashboard pour voir exactement ce que vous avez vu. Fini le « tu peux reproduire sur ta machine ? »

Les traces, spans et logs individuels ont aussi une option « Export JSON » dans leurs menus contextuels. Besoin de partager une trace spécifique ? Clic droit, copier le JSON, coller dans la description de votre PR. Terminé.

## L'API de télémétrie est le vrai changement majeur

C'est ce qui m'enthousiasme le plus. Le dashboard expose maintenant une API HTTP sous `/api/telemetry` pour interroger les données de télémétrie programmatiquement. Endpoints disponibles :

- `GET /api/telemetry/resources` — lister les ressources avec télémétrie
- `GET /api/telemetry/spans` — interroger les spans avec des filtres
- `GET /api/telemetry/logs` — interroger les logs avec des filtres
- `GET /api/telemetry/traces` — lister les traces
- `GET /api/telemetry/traces/{traceId}` — obtenir tous les spans d'une trace spécifique

Tout revient au format OTLP JSON. Cela alimente les nouvelles commandes CLI `aspire agent mcp` et `aspire otel`, mais l'implication réelle est plus grande : vous pouvez maintenant construire des outils, scripts et intégrations d'agents IA qui interrogent directement la télémétrie de votre app.

Imaginez un agent IA de codage qui peut voir vos traces distribuées réelles pendant le débogage. Ce n'est plus hypothétique — c'est ce que cette API permet.

## La télémétrie GenAI devient pratique

Si vous construisez des apps alimentées par l'IA avec Semantic Kernel ou Microsoft.Extensions.AI, vous apprécierez le visualiseur de télémétrie GenAI amélioré. Aspire 13.2 ajoute :

- Les descriptions d'outils IA rendues en Markdown
- Un bouton GenAI dédié sur la page des traces pour un accès rapide
- Une meilleure gestion des erreurs pour le JSON GenAI tronqué ou non standard
- Une navigation click-to-highlight entre les définitions d'outils

L'article mentionne que VS Code Copilot chat, Copilot CLI et OpenCode supportent tous la configuration d'un `OTEL_EXPORTER_OTLP_ENDPOINT`. Pointez-les vers le dashboard Aspire et vous pouvez littéralement regarder vos agents IA réfléchir en temps réel via la télémétrie. C'est une expérience de débogage que vous ne trouverez nulle part ailleurs.

## Pour conclure

Aspire 13.2 transforme le dashboard d'une « jolie UI de débogage » en « plateforme d'observabilité programmable ». Le workflow d'export/import seul fait gagner du temps réel en débogage distribué, et l'API de télémétrie ouvre la porte au diagnostic assisté par IA.

Si vous êtes déjà sur Aspire, mettez à jour. Sinon — c'est une bonne raison de découvrir [aspire.dev](https://aspire.dev).
