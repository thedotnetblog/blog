---
title: "Endpoints Privés, VNets, NSGs — Aspire Gère le Réseau Maintenant"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "Le nouveau support réseau d'entreprise Azure pour Aspire vous permet de modéliser les VNets, les endpoints privés, les passerelles NAT, les NSG et les périmètres de sécurité réseau directement dans votre AppHost, sans dérive d'infrastructure."
tags:
  - Aspire
  - Azure
  - Networking
  - Security
  - .NET
---

J'ai vu ce scénario trop de fois. L'application est terminée. La démo est excellente. Puis la liste de contrôle de sécurité arrive : sortir le stockage d'internet public, s'exécuter dans un VNet, fournir des IPs sortantes pour la liste d'autorisation du partenaire, prouver que seuls les bons sous-réseaux parlent aux bons services.

À ce stade, le modèle d'application et le modèle d'infrastructure commencent à diverger de manières douloureuses à maintenir.

Le nouveau support réseau d'entreprise Azure pour Aspire répond directement à cela. Vous décrivez la forme du réseau à côté des ressources qui l'utilisent, dans votre AppHost.

## Les Blocs de Construction

Voici à quoi sert chaque concept réseau Azure, résumé :

| Fonctionnalité | Utilisez-le quand | Pourquoi c'est important |
|---------|------------|----------------|
| Réseau virtuel | Vous avez besoin d'un espace d'adressage privé | La limite réseau pour les sous-réseaux, les endpoints privés et le routage |
| Sous-réseau | Vous devez séparer les charges de travail dans le VNet | Chaque partie du système obtient sa propre plage d'adresses et surface de politique |
| Sous-réseau délégué | Un service de plateforme (comme ACA) doit gérer un sous-réseau | Permet au service de placer une infrastructure gérée dans votre VNet en toute sécurité |
| Passerelle NAT | Vous avez besoin d'IPs publiques sortantes prévisibles | Adresse stable pour les listes d'autorisation et l'audit |
| Endpoint privé | Vous voulez une ressource PaaS accessible privément | Place une IP privée pour ce service dans votre VNet, supprime l'exposition publique |
| NSG | Vous avez besoin de règles de trafic au niveau du sous-réseau | Autoriser/refuser explicitement pour le trafic entrant et sortant par sous-réseau |

## Le Décrire dans votre AppHost

Le changement clé ici est que vous modélisez le réseau *aux côtés* des ressources qui l'utilisent, pas dans un fichier Bicep séparé qui dérive du modèle d'application avec le temps.

Depuis l'AppHost, vous pouvez :

- Créer des VNets et des sous-réseaux avec `AddVirtualNetwork()` et `AddSubnet()`
- Attacher une passerelle NAT aux sous-réseaux pour des IPs sortantes stables
- Créer des endpoints privés pour le stockage, Key Vault, SQL et d'autres services PaaS
- Définir des NSG avec des règles de sécurité entrantes et sortantes
- Configurer des Périmètres de Sécurité Réseau pour des politiques inter-ressources

Le résultat est que lorsque vous exécutez `azd up`, l'infrastructure correspond à ce que le modèle d'application dit qu'il a besoin. Pas ce que dit un modèle maintenu manuellement.

## Pourquoi C'est Important pour les Applications Réelles

Quelques choses qui deviennent significativement plus faciles une fois que le réseau est modélisé dans Aspire :

**Endpoints privés pour Key Vault et stockage** — vous décrivez `WithPrivateEndpoint()` sur ces ressources, et Aspire gère la configuration des zones DNS et l'attachement des endpoints. L'application ne change jamais.

**IPs sortantes cohérentes** — ajoutez une passerelle NAT au sous-réseau concerné et chaque requête sortante de votre application passe par une IP connue et stable. Les partenaires peuvent l'autoriser. Les auditeurs peuvent la tracer.

**Règles NSG depuis le code** — au lieu de cliquer dans le portail ou de maintenir un extrait Bicep, vos règles de sécurité vivent dans l'AppHost aux côtés des ressources qu'elles protègent.

C'est le type d'intégration qui ne rend pas les démos excitantes mais rend les systèmes de production maintenables.

## Conclusion

La sécurité réseau apparaissant tard dans le cycle de vie du projet est un problème résolu si vous la modélisez aux côtés de l'application dès le début. Le support réseau d'entreprise d'Aspire rend cela possible sans nécessiter une piste d'infrastructure séparée.

Détails complets dans l'article original : [Securing Azure apps with Aspire enterprise networking](https://devblogs.microsoft.com/aspire/aspire-azure-enterprise-networking/)
