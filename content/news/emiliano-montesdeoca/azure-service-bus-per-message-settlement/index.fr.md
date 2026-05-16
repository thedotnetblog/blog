---
title: "Résoudre le traitement par lots tout-ou-rien dans Azure Service Bus"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions prend désormais en charge le règlement par message pour les déclencheurs Service Bus, vous permettant de compléter, abandonner, mettre en dead-letter ou différer chaque message indépendamment dans un lot."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*Ce post a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "index.md" >}}).*

[Le règlement par message pour Azure Service Bus dans Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) résout le problème classique d'échec de lot tout-ou-rien : si un message sur 50 échoue, les 50 sont renvoyés dans la file d'attente.

## Le problème du lot

Dans l'ancien modèle, Azure Functions traitait les messages en mode lot avec un résultat binaire : soit tout le lot réussissait, soit tout le lot échouait. Un message malformé signifiait que les 49 messages sains retournaient dans la file, étaient retraités et leur idempotence revérifiée — gaspillant du calcul, augmentant les coûts et créant des boucles de réessai difficiles à quitter.

## Quatre actions de règlement par message

Le règlement par message vous offre quatre actions indépendantes sur chaque message :

- **Compléter (Complete)** — supprimer le message de la file (traitement réussi)
- **Abandonner (Abandon)** — le renvoyer pour réessai, en modifiant optionnellement les propriétés de l'application (utile pour les erreurs transitoires)
- **Dead-letter** — le déplacer vers la file de lettres mortes (message empoisonné, irrécupérable)
- **Différer (Defer)** — le conserver mais le rendre récupérable uniquement par numéro de séquence

Dans un lot de 50, vous pouvez maintenant compléter 47, abandonner 2 avec des erreurs transitoires et mettre en dead-letter 1 message malformé — tout dans une seule invocation de fonction.

## Exemples de code

**.NET (C#):**
```csharp
[Function("ProcessOrderBatch")]
public async Task Run(
    [ServiceBusTrigger("orders-queue", IsBatched = true)] ServiceBusReceivedMessage[] messages,
    ServiceBusMessageActions messageActions)
{
    foreach (var message in messages)
    {
        try {
            await messageActions.CompleteMessageAsync(message);
        } catch {
            await messageActions.DeadLetterMessageAsync(message);
        }
    }
}
```

**Node.js/TypeScript:**
```typescript
import '@azure/functions-extensions-servicebus';
export async function processOrderBatch(sbContext, context) {
    const { messages, actions } = sbContext;
    for (const message of messages) {
        try {
            await processOrder(messageBodyAsJson(message));
            await actions.complete(message);
        } catch {
            await actions.deadletter(message);
        }
    }
}
app.serviceBusQueue('processOrderBatch', {
    sdkBinding: true,
    autoCompleteMessages: false,
    cardinality: 'many',
    handler: processOrderBatch
});
```

**Python V2:**
```python
@app.service_bus_queue_trigger(auto_complete_messages=False, cardinality="many")
def process_order_batch(messages, message_actions):
    for message in messages:
        try:
            process_order(json.loads(message.body))
            message_actions.complete(message)
        except:
            message_actions.deadletter(message)
```

## Backoff exponentiel sans infrastructure supplémentaire

Combiner `abandon` avec des propriétés d'application modifiées permet d'implémenter un backoff exponentiel directement sur la file — sans Durable Functions ni files supplémentaires. Stockez un compteur de réessais dans les propriétés d'application du message, lisez-le à la nouvelle livraison et calculez votre délai. Ce schéma nécessitait auparavant une orchestration significative ; maintenant c'est quelques lignes dans le gestionnaire de réessais.

## Gains d'efficacité du lot

L'ancien modèle envoyait chaque message comme une invocation de fonction séparée : 50 messages signifiaient 50 connexions, 50 démarrages à froid, 50 démontages. Le nouveau modèle gère les 50 en une seule invocation, et le règlement par message signifie que vous ne sacrifiez pas cette efficacité quand des erreurs surviennent.

Lire l'article complet sur [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
