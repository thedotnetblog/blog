---
title: "Créer des Agents, C'est la Partie Facile — Les Exécuter en Toute Sécurité, C'est la Partie Difficile"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework et Agent Governance Toolkit s'associent pour appliquer les politiques d'exécution, gouverner les appels d'outils et fournir des journaux d'audit chaînés par Merkle — sans toucher aux prompts de l'agent."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

Il existe un modèle dans le développement d'agents IA que j'ai commencé à appeler le « regret de démo ». L'agent fonctionne très bien dans les démos. Ensuite, quelqu'un demande : que se passe-t-il s'il appelle le mauvais outil ? Et s'il accède à des données auxquelles il ne devrait pas ? Qui a audité ça ?

Microsoft Agent Framework vous soutient pour la construction et l'orchestration. Agent Governance Toolkit (AGT) couvre la partie après — gouvernance, application des politiques et auditabilité à l'exécution.

## Ce Que Chaque Projet Fait Vraiment

**Microsoft Agent Framework (MAF)** vous offre le modèle de programmation : workflows multi-agents, interopérabilité du protocole A2A, hooks de middleware, mémoire et hébergement géré via Foundry Agent Service. Il gère la sécurité du contenu au niveau de l'entrée/sortie du modèle.

**Agent Governance Toolkit (AGT)** se connecte à ce même pipeline de middleware pour gouverner les *actions*. Chaque appel d'outil, accès aux ressources et message inter-agents est évalué par rapport à la politique avant l'exécution. Surcharge inférieure à la milliseconde. Pas de sidecars, pas de proxies, pas de prompts modifiés.

```
Action Agent --> Vérification Politique --> Autoriser / Refuser --> Journal Audit    (< 0.1 ms)
```

Des couches différentes, une couverture complète, un pipeline.

## S'intégrer, C'est Juste Ajouter un Middleware

En Python, AGT s'ajoute au même paramètre `middleware` que vous utiliseriez pour la journalisation ou les filtres de contenu :

```python
agent = Agent(
    client=OpenAIChatClient(model="gpt-5.3"),
    name="Contoso Loan Officer",
    instructions="You are a governed loan assistant.",
    tools=[check_credit_score, get_loan_rates, approve_small_loan],
    middleware=[
        AuditTrailMiddleware(audit_log=audit_log, agent_did="loan-agent"),
        GovernancePolicyMiddleware(evaluator=evaluator, audit_log=audit_log),
        CapabilityGuardMiddleware(allowed_tools=["check_credit_score", "get_loan_rates"]),
        RogueDetectionMiddleware(detector=detector, agent_id="loan-agent"),
    ],
)
```

En .NET, même modèle via `.Use()` :

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Même agent, même orchestration, mêmes outils. AGT ajoute des capacités de gouvernance sans toucher à la logique de l'agent.

## Ce Que Vous Obtenez

- **GovernancePolicyMiddleware** — évalue chaque action par rapport aux règles de politique déclaratives
- **CapabilityGuardMiddleware** — liste blanche des outils qu'un agent est autorisé à appeler (l'outil `approve_small_loan` n'est pas dans la liste autorisée ci-dessus — délibérément)
- **RogueDetectionMiddleware** — détecte les modèles de comportement anormaux à l'exécution
- **AuditTrailMiddleware** — journal d'audit chaîné par Merkle pour que chaque action soit cryptographiquement inviolable

Ce dernier point compte pour la conformité. Une chaîne Merkle signifie que si quelqu'un modifie le journal, la chaîne se rompt. L'audit est la preuve.

## Cinq Scénarios Industriels

Le dépôt AGT comprend cinq scénarios complets de bout en bout : services financiers (agent de crédit), santé (données patient), juridique (examen de contrat), gouvernement (services aux citoyens) et fabrication (contrôle qualité). Chacun associe de vrais agents MAF avec un vrai middleware de gouvernance AGT.

Ce ne sont pas des démos jouets. Ce sont le type de scénarios où vous auriez vraiment besoin d'une gouvernance en production.

## Conclusion

Si vous construisez des agents qui touchent des données réelles, prennent des décisions avec des conséquences, ou s'exécutent sans surveillance en production — la gouvernance n'est pas optionnelle. La combinaison MAF + AGT vous donne la pile complète : construisez-le avec Agent Framework, gouvernez-le avec AGT.

Les deux projets sont open source. L'article original contient des liens vers les exemples de code complets.

Publication originale : [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
