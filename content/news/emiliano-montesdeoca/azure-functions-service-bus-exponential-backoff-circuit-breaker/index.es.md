---
title: "Deja de Martillar una Dependencia en Dificultades: Patrones de Reintento para Azure Functions + Service Bus"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "El retroceso exponencial y los patrones de circuit breaker ahora son compatibles de forma nativa para Azure Functions activadas por Service Bus — aquí se explica cómo funcionan y por qué quieres ambos."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

Aquí te explicamos cómo una falla recuperable se convierte en una interrupción en una aplicación de Functions: una dependencia comienza a dar timeout, cada instancia de Function reintenta inmediatamente e indefinidamente, la dependencia recibe cientos de solicitudes fallidas concurrentes, y lo que comenzó como un problema transitorio se convierte en un evento de contrapresión en todo el sistema.

Probablemente conoces esta historia. Azure Functions escala rápidamente — ese es todo el punto. Pero "escalar rápidamente" y "reintentar inmediatamente" juntos pueden empeorar dramáticamente las fallas.

Dos patrones ayudan. Retroceso exponencial y circuit breaker. Ambos ahora son compatibles de forma nativa para Azure Functions activadas por Service Bus.

## Dos Patrones, Roles Diferentes

Estos patrones son complementarios, no alternativas:

**El retroceso exponencial** responde: *¿cuándo debería intentarlo de nuevo?*
Aumenta el retraso entre reintentos para que una dependencia tenga tiempo de recuperarse. A nivel de mensaje, marcando el ritmo del temporizador de reintento.

**El circuit breaker** responde: *¿debería llamar a esta dependencia ahora mismo?*
Detiene las llamadas repetidas a una dependencia poco saludable después de alcanzar un umbral de fallas, y luego sondea cuidadosamente después de un período de enfriamiento. A nivel de sistema, previniendo tormentas de reintentos.

Quieres ambos. El retroceso maneja el ritmo de reintento por mensaje. El circuit breaker maneja las decisiones de salud agregadas.

## Por Qué Importa Especialmente para Service Bus

La cola absorbe el tráfico en ráfagas, lo que es bueno. Pero sin controles, la cola puede crecer mientras los workers continúan desperdiciando cómputo en llamadas que fallarán. Los mensajes envenenados permanecen activos más tiempo del que deberían. Las particiones calientes o la capacidad aguas abajo limitada crean problemas en cascada.

El diseño más seguro:

1. Detectar la falla transitoria
2. Retrasar el próximo intento con retroceso exponencial
3. Detener las llamadas a la dependencia cuando se alcanza un umbral de fallas (circuito abierto)
4. Reanudar cuidadosamente después de un período de enfriamiento (sonda de circuito)
5. Mover el trabajo irrecuperable a dead-letter o a una ruta de cuarentena

## Cómo se Ve el Soporte Nativo

El nuevo soporte se integra con el modelo de host existente de Azure Functions — sin bibliotecas adicionales, sin implementaciones personalizadas. La configuración va en tu `host.json`:

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

La configuración del circuit breaker establece el umbral de fallas y el intervalo de restablecimiento para que las dependencias poco saludables no sean acosadas durante la recuperación.

## Lenguajes Cubiertos

Esto no es solo para .NET. La funcionalidad cubre dotnet, JavaScript, TypeScript y Python — el conjunto completo de lenguajes compatibles con el trigger de Service Bus en Azure Functions.

## Conclusión

Los patrones de reintento no son emocionantes de configurar hasta la primera vez que una interrupción aguas abajo hace que tus Functions empeoren el problema en lugar de degradarse correctamente. Configurarlos de manera proactiva es barato. Implementarlos durante un incidente no lo es.

Post original: [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
