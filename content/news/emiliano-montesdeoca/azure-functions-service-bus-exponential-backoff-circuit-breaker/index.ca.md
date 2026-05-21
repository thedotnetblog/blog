---
title: "Deixa de Martillar una Dependència en Dificultats: Patrons de Reintent per a Azure Functions + Service Bus"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "La retirada exponencial i els patrons de circuit breaker ara estan suportats de manera nativa per a Azure Functions activades per Service Bus — aquí tens com funcionen i per què vols tots dos."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

Aquí tens com una fallada recuperable es converteix en una interrupció en una aplicació de Functions: una dependència comença a donar timeout, cada instància de Function reintenta immediatament i indefinidament, la dependència rep centenars de sol·licituds fallides concurrents, i el que va començar com un problema transitori es converteix en un event de contrapressió a tot el sistema.

Probablement coneixes aquesta història. Azure Functions escala ràpidament — aquest és tot el punt. Però "escalar ràpidament" i "reintentar immediatament" junts poden empitjorar dramàticament les fallades.

Dos patrons ajuden. Retirada exponencial i circuit breaker. Tots dos ara estan suportats de manera nativa per a Azure Functions activades per Service Bus.

## Dos Patrons, Rols Diferents

Aquests patrons són complementaris, no alternatives:

**La retirada exponencial** respon: *quan hauria de tornar a intentar-ho?*
Augmenta el retard entre reintentos perquè una dependència tingui temps de recuperar-se. A nivell de missatge, marcant el ritme del temporitzador de reintent.

**El circuit breaker** respon: *hauria de cridar aquesta dependència ara mateix?*
Atura les cridades repetides a una dependència poc saludable després d'assolir un llindar de fallades, i després sonda curosament després d'un període de refredament. A nivell de sistema, prevenint tempestes de reintentos.

Vols tots dos. La retirada gestiona el ritme de reintent per missatge. El circuit breaker gestiona les decisions de salut agregades.

## Per Què Importa Especialment per a Service Bus

La cua absorbeix el tràfic en ràfegues, cosa que és bona. Però sense controls, la cua pot créixer mentre els workers continuen malbaratant còmput en cridades que fallaran. Els missatges enverinats romanen actius més temps del que haurien. Les particions calentes o la capacitat aigüestaixa agüestaires creen problemes en cascada.

El disseny més segur:

1. Detectar la fallada transitòria
2. Retardar el proper intent amb retirada exponencial
3. Aturar les cridades a la dependència quan s'assoleix un llindar de fallades (circuit obert)
4. Reprendre curosament després d'un període de refredament (sonda de circuit)
5. Moure el treball irrecuperable a dead-letter o a una ruta de quarantena

## Com és el Suport Natiu

El nou suport s'integra amb el model d'host existent d'Azure Functions — sense llibreries addicionals, sense implementacions personalitzades. La configuració va al teu `host.json`:

```json
{
  "extensions": {
    "serviceBus": {
      "messageHandlerOptions": {
        "maxRetryCount": 5,
        "retryPolicy": {
          "mode": "exponentialBackoff",
          "minBackoff": "00:00:02",
          "maxBackoff": "00:05:00",
          "maxRetryCount": 5
        }
      }
    }
  }
}
```

La configuració del circuit breaker estableix el llindar de fallades i l'interval de restabliment perquè les dependències poc saludables no siguin assetjades durant la recuperació.

## Llenguatges Coberts

Això no és només per a .NET. La funcionalitat cobreix dotnet, JavaScript, TypeScript i Python — el conjunt complet de llenguatges suportats pel trigger de Service Bus a Azure Functions.

## Conclusió

Els patrons de reintent no són emocionants de configurar fins la primera vegada que una interrupció aigüestaixa de downstream fa que les teves Functions empitjorin el problema en lloc de degradar-se gràcilment. Configurar-los de manera proactiva és barat. Implementar-los durant un incident no ho és.

Post original: [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
