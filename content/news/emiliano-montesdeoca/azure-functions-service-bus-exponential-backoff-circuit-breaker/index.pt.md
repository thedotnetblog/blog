---
title: "Pare de Bombardear uma Dependência em Dificuldades: Padrões de Retry para Azure Functions + Service Bus"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "Os padrões de exponential backoff e circuit breaker agora são suportados nativamente para Azure Functions acionadas pelo Service Bus — veja como funcionam e por que você quer os dois."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

Veja como uma falha recuperável se torna uma interrupção em um aplicativo Functions: uma dependência começa a dar timeout, cada instância Functions tenta novamente imediatamente e indefinidamente, a dependência é bombardeada com centenas de requisições com falha concorrentes, e o que começou como um soluço transitório se torna um evento de contrapressão em todo o sistema.

Você provavelmente conhece essa história. Azure Functions escala rapidamente — esse é todo o ponto. Mas "escalar rapidamente" e "tentar novamente imediatamente" juntos podem piorar dramaticamente as falhas.

Dois padrões ajudam. Exponential backoff e circuit breaker. Ambos agora são suportados nativamente para Azure Functions acionadas pelo Service Bus.

## Dois Padrões, Papéis Diferentes

Esses padrões são complementares, não alternativos:

**O exponential backoff** responde a: *quando devo tentar novamente?*
Aumenta o atraso entre as tentativas para que uma dependência tenha tempo de se recuperar. No nível da mensagem, regulando o tempo de retry.

**O circuit breaker** responde a: *devo chamar essa dependência agora?*
Interrompe chamadas repetidas a uma dependência não saudável após atingir um limiar de falhas e, em seguida, sonda cuidadosamente após um período de resfriamento. No nível do sistema, prevenindo tempestades de retry.

Você quer os dois. O backoff gerencia o ritmo de retry por mensagem. O circuit breaker gerencia as decisões de saúde agregadas.

## Por Que Isso Importa Especialmente para Service Bus

A fila absorve o tráfego em rajadas, o que é bom. Mas sem controles, a fila pode crescer enquanto os workers continuam desperdiçando recursos de computação em chamadas que vão falhar. Mensagens envenenadas ficam ativas por mais tempo do que deveriam. Partições quentes ou capacidade downstream limitada criam problemas em cascata.

O design mais seguro:

1. Detectar a falha transitória
2. Atrasar a próxima tentativa com exponential backoff
3. Parar de chamar a dependência quando um limiar de falha é atingido (circuito aberto)
4. Retomar cuidadosamente após um período de resfriamento (sonda de circuito)
5. Mover o trabalho irrecuperável para dead-letter ou um caminho de quarentena

## Como É o Suporte Nativo

O novo suporte se integra com o modelo de host Azure Functions existente — sem bibliotecas extras, sem implementações personalizadas. A configuração vai no seu `host.json`:

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

A configuração do circuit breaker define o limiar de falha e o intervalo de reset para que dependências não saudáveis não sejam bombardeadas durante a recuperação.

## Linguagens Cobertas

Isso não é apenas para .NET. O recurso cobre dotnet, JavaScript, TypeScript e Python — o conjunto completo de linguagens suportadas pelo trigger Service Bus no Azure Functions.

## Conclusão

Os padrões de retry não são emocionantes de configurar até a primeira vez que uma interrupção downstream faz com que suas Functions piorem o problema em vez de degradar graciosamente. Configurá-los proativamente é barato. Adaptá-los durante um incidente não é.

Post original: [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
