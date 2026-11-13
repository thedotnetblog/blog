---
title: "NTLM disparaît de Git/libcurl : les équipes Azure DevOps Server ont besoin d'un vrai plan de migration"
date: 2026-07-20
author: Emiliano Montesdeoca
description: "La suppression de NTLM en septembre 2026 n'est pas un simple problème de compatibilité mineur ; c'est une échéance d'architecture d'identité pour les environnements Azure DevOps Server sur site."
tags:
  - Azure DevOps Server
  - Git
  - Security
  - Kerberos
  - Authentication
  - Enterprise IT
---

La suppression imminente de NTLM dans libcurl est de ces changements qui semblent techniques mais sont en réalité organisationnels. Si votre chemin Git via HTTPS vers Azure DevOps Server dépend encore de NTLM, votre problème n'est pas l'outillage, c'est une dette d'identité.

Original source: https://devblogs.microsoft.com/devops/upcoming-change-ntlm-removal-in-git-libcurl-impact-to-azure-devops-server-customers/

Microsoft a raison de pousser fort ici. NTLM a des faiblesses cryptographiques connues et ne devrait pas être une valeur par défaut d'entreprise moderne. La partie dangereuse, c'est que beaucoup d'environnements croient utiliser Kerberos alors qu'ils survivent en réalité grâce à un repli silencieux SPNEGO vers NTLM. Cette illusion disparaît en septembre 2026.

Mon avis : ne traitez pas cela comme un problème de « version de client ». Réactiver les indicateurs NTLM, épingler d'anciennes versions de Git, ou espérer que le repli reste disponible est une solution de contournement de courte durée avec un risque à long terme. Si votre stratégie de remédiation est de rétrograder et de retarder, vous augmentez activement la fragilité opérationnelle.

Une séquence de migration pratique devrait être directe et mesurable.

D'abord, vérifiez le comportement d'authentification actuel maintenant. Exécutez des vérifications basées sur des traces et une validation du cache de tickets dans de vrais contextes de développeurs et d'agents de build, y compris les chemins hors domaine et réseau distant. Ensuite, réparez Kerberos de bout en bout : SPN, alias DNS, paramètres d'équilibreur de charge, délégation, et joignabilité du contrôleur de domaine. Troisièmement, identifiez tôt les scénarios non joints au domaine ou en groupe de travail, et concevez une voie SSH là où Kerberos ne peut pas être rendu fiable.

Vous avez aussi besoin d'une clarté de propriété. Les équipes de sécurité devraient définir des bases de politique, mais l'ingénierie de plateforme doit posséder la préparation à l'implémentation. Cela ne peut pas être une tâche secondaire pour des administrateurs de dépôt individuels. Cela nécessite des changements coordonnés à travers IIS, AD, la bordure réseau, les agents CI, et les conseils aux postes de travail des développeurs.

Un risque subtil est l'automatisation. Les agents de build et les comptes de service s'exécutent fréquemment dans des contextes où les tickets Kerberos sont manquants ou invalides, même quand les utilisateurs humains vont bien. Si vous ne testez que les workflows interactifs des développeurs, vous manquerez les points de rupture les plus critiques.

L'avantage est réel. Passer proprement à Kerberos ou SSH évite non seulement la casse, mais réduit aussi la surface d'attaque et aligne les contrôles d'identité avec les attentes de conformité modernes. Les équipes qui commencent cette transition maintenant traiteront septembre comme un non-événement. Les équipes qui attendent déboguerons des échecs d'authentification sous pression de release.

Ce n'est pas un avertissement à archiver. C'est une échéance à exécuter.
