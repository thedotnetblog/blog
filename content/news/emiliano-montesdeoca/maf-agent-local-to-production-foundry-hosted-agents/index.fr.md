---
title: "Votre Agent MAF Local Vient d'Obtenir une Maison en Production"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents donne à votre agent Microsoft Agent Framework une identité, un scaling, une persistance de session et une observabilité sans configuration supplémentaire. Voici à quoi cela ressemble en pratique."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

Faire fonctionner un agent localement est la partie amusante. La partie délicate est tout ce qui vient après : le déployer sans perdre la tête, gérer les sessions, configurer l'identité, câbler l'observabilité. Cela signifie généralement beaucoup d'infrastructure personnalisée.

Foundry Hosted Agents vient de supprimer la majeure partie de cette infrastructure pour les utilisateurs de Microsoft Agent Framework (MAF).

## Ce que Foundry Hosted Agents Fait Vraiment

Lorsque vous déployez un agent MAF dans Foundry Hosted Agents, la plateforme gère une liste étonnamment longue de choses que vous auriez autrement à construire vous-même :

- **Mise à l'échelle à zéro** — votre agent ne coûte rien en idle et redémarre automatiquement
- **Sandboxes isolés par VM par session** — chaque session utilisateur obtient son propre sandbox avec persistance du système de fichiers qui survit aux événements de réduction d'échelle
- **Entra ID intégré** — chaque agent obtient sa propre identité pour appeler les modèles Foundry, Toolbox et les services Azure sans secrets dans l'image
- **Déploiements versionnés** — chaque déploiement est un instantané immuable, avec support de déploiement blue/green et canary
- **Observabilité sans configuration** — `APPLICATIONINSIGHTS_CONNECTION_STRING` est injecté au runtime pour que les traces OpenTelemetry de MAF s'écoulent automatiquement dans App Insights

Ce dernier point est vraiment appréciable. Pas de câblage supplémentaire, pas de configuration additionnelle. Les traces apparaissent simplement.

## La Différence de Code Est Minime

C'est ce que j'apprécie le plus dans cette intégration. Vous ne réécrivez pas votre agent. Vous l'encapsulez simplement :

**En .NET :**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**En Python :**

```python
server = ResponsesHostServer(agent)
server.run()
```

C'est tout. La même logique que vous avez testée localement est ce qui s'exécute en production. La plateforme l'encapsule dans l'infrastructure de gestion de sessions, d'identité et de scaling.

## Deux Protocoles, Un Agent

Les Hosted Agents supportent deux styles d'endpoints :

- **Responses** (`/responses`) — compatible OpenAI, gère l'historique des conversations et le streaming. Bon défaut pour les agents de type chat.
- **Invocations** (`/invocations`) — vous définissez le schéma requête/réponse. Bon pour les workflows non conversationnels.

Si vous construisez quelque chose qui ressemble à une conversation, commencez avec Responses. Si vous construisez un agent de type API qui prend une entrée structurée et retourne une sortie structurée, Invocations vous donne la flexibilité.

## Le Flux de Déploiement avec `azd`

Lorsque vous exécutez `azd up` avec un agent MAF :

1. Crée optionnellement un projet Foundry et déploie un modèle
2. Empaquette votre code et pousse une image vers Azure Container Registry
3. Provisionne du calcul depuis l'image ACR
4. Attribue un Entra ID dédié à l'agent
5. Expose un endpoint stable (`https://{project_endpoint}/agents/{agent_name}`)
6. Gère tout le reste à partir de ce point

Les sessions persistent jusqu'à 30 jours. Le calcul inactif est déprovisionné après 15 minutes et restauré transparemment sur la prochaine requête. Du point de vue de l'agent, rien n'a changé.

## Conclusion

La distance entre "fonctionnant localement" et "s'exécutant en production" a toujours été longue et douloureuse pour les agents IA. Foundry Hosted Agents + MAF réduit considérablement cet écart. Si vous avez déjà un agent local construit avec Agent Framework, cela vaut la peine d'essayer aujourd'hui.

L'équipe annonce que GA arrive bientôt — c'est actuellement en preview. Consultez les [docs d'intégration MAF Hosted Agent](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) et les [exemples .NET](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) pour démarrer.

Article original : [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
