---
title: "Stop met het Bombarderen van een Worstelende Afhankelijkheid: Retry-patronen voor Azure Functions + Service Bus"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "Exponential backoff en circuit breaker-patronen worden nu native ondersteund voor Service Bus-getriggerde Azure Functions — hier is hoe ze werken en waarom je beide wilt."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

Zo wordt een herstelbare fout een storing in een Functions-app: een afhankelijkheid begint te timeoutten, elke Functions-instantie probeert het onmiddellijk en oneindig opnieuw, de afhankelijkheid wordt gebombardeerd met honderden gelijktijdige mislukte verzoeken, en wat begon als een tijdelijke storing wordt een systeembrede backpressure-gebeurtenis.

U kent dit verhaal waarschijnlijk. Azure Functions schaalt snel uit — dat is het hele punt. Maar "snel uitschalen" en "onmiddellijk opnieuw proberen" samen kunnen fouten dramatisch erger maken.

Twee patronen helpen. Exponential backoff en circuit breaker. Beide worden nu native ondersteund voor Service Bus-getriggerde Azure Functions.

## Twee Patronen, Verschillende Rollen

Deze patronen zijn complementair, geen alternatieven:

**Exponential backoff** beantwoordt: *wanneer moet ik het opnieuw proberen?*
Het vergroot de vertraging tussen nieuwe pogingen zodat een afhankelijkheid tijd heeft om te herstellen. Op berichtniveau, het tempo van retry-timing aanpassen.

**Circuit breaker** beantwoordt: *moet ik deze afhankelijkheid nu überhaupt aanroepen?*
Het stopt herhaalde aanroepen naar een ongezonde afhankelijkheid nadat een faaldrempel is bereikt, en sondeert dan voorzichtig na een afkoelperiode. Op systeemniveau, het voorkomen van retry-stormen.

U wilt beide. Backoff verwerkt de retry-pacing per bericht. Circuit breaker verwerkt geaggregeerde gezondheidsbeslissingen.

## Waarom Dit Bijzonder Belangrijk is voor Service Bus

De wachtrij absorbeert burstverkeer, wat goed is. Maar zonder controles kan de wachtrij groeien terwijl workers kostbare rekenkracht blijven verspillen aan oproepen die zullen mislukken. Poisonberichten blijven langer actief dan ze zouden moeten. Hete partities of beperkte downstreamcapaciteit veroorzaken cascadeproblemen.

Het veiligere ontwerp:

1. Tijdelijke fout detecteren
2. De volgende poging vertragen met exponential backoff
3. Stoppen met het aanroepen van de afhankelijkheid wanneer een faaldrempel is bereikt (circuit open)
4. Voorzichtig hervatten na een afkoelperiode (circuit sonde)
5. Niet-herstelbaar werk verplaatsen naar dead-letter of een quarantinepad

## Hoe de Native Ondersteuning Eruitziet

De nieuwe ondersteuning integreert met het bestaande Azure Functions-hostmodel — geen extra bibliotheken, geen aangepaste implementaties. De configuratie gaat in uw `host.json`:

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

De circuit breaker-configuratie stelt de faaldrempel en het reset-interval in zodat ongezonde afhankelijkheden niet worden gebombardeerd tijdens herstel.

## Talen Gedekt

Dit is niet alleen voor .NET. De functie dekt dotnet, JavaScript, TypeScript en Python — de volledige set van talen die worden ondersteund door de Service Bus-trigger in Azure Functions.

## Conclusie

Retry-patronen zijn niet opwindend om te configureren totdat de eerste keer een downstream-storing uw Functions het probleem laat verergeren in plaats van gracefully te degraderen. Ze proactief instellen is goedkoop. Ze tijdens een incident aanpassen is dat niet.

Originele post: [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
