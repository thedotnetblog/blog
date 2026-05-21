---
title: "Przestań Atakować Zmagającą się Zależność: Wzorce Retry dla Azure Functions + Service Bus"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "Wzorce exponential backoff i circuit breaker są teraz obsługiwane natywnie dla Azure Functions wyzwalanych przez Service Bus — oto jak działają i dlaczego potrzebujesz obu."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

Oto jak odwracalna awaria staje się przestojem w aplikacji Functions: zależność zaczyna dawać timeout, każda instancja Functions natychmiast i bezterminowo ponawia próby, zależność jest bombardowana setkami równoczesnych nieudanych żądań, i to, co zaczęło się jako przejściowy problem, staje się ogólnosystemowym zdarzeniem przeciwciśnienia.

Pewnie znasz tę historię. Azure Functions szybko skaluje się — o to w tym wszystkim chodzi. Ale "szybkie skalowanie" i "natychmiastowe ponawianie" razem mogą dramatycznie pogorszyć awarie.

Dwa wzorce pomagają. Exponential backoff i circuit breaker. Oba są teraz obsługiwane natywnie dla Azure Functions wyzwalanych przez Service Bus.

## Dwa Wzorce, Różne Role

Te wzorce są komplementarne, nie alternatywne:

**Exponential backoff** odpowiada: *kiedy powinienem spróbować ponownie?*
Zwiększa opóźnienie między próbami, aby zależność miała czas na odzyskanie. Na poziomie wiadomości, regulując tempo retry.

**Circuit breaker** odpowiada: *czy powinienem w ogóle teraz wywoływać tę zależność?*
Zatrzymuje powtarzające się wywołania do niezdrowej zależności po osiągnięciu progu awarii, a następnie ostrożnie sonduje po okresie ochłodzenia. Na poziomie systemu, zapobiegając burzom retry.

Chcesz obu. Backoff obsługuje tempo ponownych prób na wiadomość. Circuit breaker obsługuje zagregowane decyzje zdrowotne.

## Dlaczego Jest To Szczególnie Ważne dla Service Bus

Kolejka absorbuje ruch seryjny, co jest dobre. Ale bez kontroli kolejka może rosnąć, podczas gdy workerzy nadal marnują zasoby obliczeniowe na wywołania, które nie powiedzie się. Toksyczne wiadomości pozostają aktywne dłużej niż powinny. Gorące partycje lub ograniczona pojemność downstream tworzą kaskadowe problemy.

Bezpieczniejszy projekt:

1. Wykryć przejściową awarię
2. Opóźnić następną próbę z exponential backoff
3. Zatrzymać wywołania do zależności po osiągnięciu progu awarii (obwód otwarty)
4. Ostrożnie wznowić po okresie ochłodzenia (sonda obwodu)
5. Przenieść nieodwracalną pracę do dead-letter lub ścieżki kwarantanny

## Jak Wygląda Natywne Wsparcie

Nowe wsparcie integruje się z istniejącym modelem hosta Azure Functions — bez dodatkowych bibliotek, bez niestandardowych implementacji. Konfiguracja trafia do Twojego `host.json`:

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

Konfiguracja circuit breakera ustawia próg awarii i interwał resetowania, aby niezdrowe zależności nie były bombardowane podczas odzyskiwania.

## Obsługiwane Języki

To nie tylko dla .NET. Funkcja obejmuje dotnet, JavaScript, TypeScript i Python — pełny zestaw języków obsługiwanych przez wyzwalacz Service Bus w Azure Functions.

## Podsumowanie

Wzorce retry nie są ekscytujące do konfigurowania do pierwszego razu, gdy awaria downstream powoduje, że Twoje Functions pogłębiają problem zamiast degradować się łagodnie. Konfigurowanie ich proaktywnie jest tanie. Dostosowywanie ich podczas incydentu takie nie jest.

Oryginalny post: [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
