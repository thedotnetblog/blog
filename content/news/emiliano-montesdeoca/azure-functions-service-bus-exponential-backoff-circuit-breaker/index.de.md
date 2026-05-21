---
title: "Hör auf, eine kämpfende Abhängigkeit zu bombardieren: Retry-Muster für Azure Functions + Service Bus"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "Exponential Backoff und Circuit-Breaker-Muster werden jetzt nativ für Service Bus-ausgelöste Azure Functions unterstützt — hier erfahren Sie, wie sie funktionieren und warum Sie beide brauchen."
tags:
  - Azure Functions
  - Service Bus
  - Resilience
  - .NET
  - Azure SDK
  - Serverless
---

So wird ein behebbarer Fehler zu einem Ausfall in einer Functions-Anwendung: Eine Abhängigkeit beginnt zu timeoutn, jede Functions-Instanz wiederholt sofort und unbegrenzt, die Abhängigkeit wird mit Hunderten gleichzeitiger fehlgeschlagener Anfragen bombardiert, und was als vorübergehender Hickup begann, wird zu einem systemweiten Gegendruck-Ereignis.

Sie kennen diese Geschichte wahrscheinlich. Azure Functions skaliert schnell — das ist der ganze Sinn. Aber "schnell skalieren" und "sofort wiederholen" zusammen können Fehler dramatisch verschlimmern.

Zwei Muster helfen. Exponential Backoff und Circuit Breaker. Beide werden jetzt nativ für Service Bus-ausgelöste Azure Functions unterstützt.

## Zwei Muster, Verschiedene Rollen

Diese Muster ergänzen sich, sind keine Alternativen:

**Exponential Backoff** beantwortet: *Wann soll ich es erneut versuchen?*
Es erhöht die Verzögerung zwischen Wiederholungsversuchen, damit eine Abhängigkeit Zeit hat, sich zu erholen. Auf Nachrichtenebene, Taktung des Retry-Timings.

**Circuit Breaker** beantwortet: *Soll ich diese Abhängigkeit gerade überhaupt aufrufen?*
Er stoppt wiederholte Aufrufe an eine ungesunde Abhängigkeit, nachdem ein Fehlerschwellenwert erreicht wurde, und testet dann vorsichtig nach einer Abkühlungsperiode. Auf Systemebene, Verhinderung von Retry-Stürmen.

Sie wollen beide. Backoff kümmert sich um das Retry-Timing pro Nachricht. Circuit Breaker kümmert sich um aggregierte Gesundheitsentscheidungen.

## Warum Das Besonders für Service Bus Wichtig Ist

Die Warteschlange absorbiert Burst-Traffic, was gut ist. Aber ohne Kontrollen kann die Warteschlange wachsen, während Worker weiterhin Rechenleistung für Aufrufe verschwenden, die fehlschlagen werden. Poison Messages bleiben länger aktiv als sie sollten. Heiße Partitionen oder begrenzte Downstream-Kapazität erzeugen Kaskadenprobleme.

Das sicherere Design:

1. Vorübergehenden Fehler erkennen
2. Den nächsten Versuch mit Exponential Backoff verzögern
3. Aufrufe an die Abhängigkeit stoppen, wenn ein Fehlerschwellenwert erreicht wird (Schaltkreis offen)
4. Nach einer Abkühlungsperiode vorsichtig fortfahren (Schaltkreis-Sonde)
5. Nicht wiederherstellbare Arbeit in Dead-Letter oder einen Quarantänepfad verschieben

## Wie die Native Unterstützung Aussieht

Die neue Unterstützung integriert sich mit dem bestehenden Azure Functions-Host-Modell — keine zusätzlichen Bibliotheken, keine benutzerdefinierten Implementierungen. Die Konfiguration geht in Ihre `host.json`:

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

Die Circuit-Breaker-Konfiguration legt den Fehlerschwellenwert und das Reset-Intervall fest, damit ungesunde Abhängigkeiten während der Wiederherstellung nicht bombardiert werden.

## Abgedeckte Sprachen

Das ist nicht nur für .NET. Das Feature deckt dotnet, JavaScript, TypeScript und Python ab — den vollständigen Satz der vom Service Bus-Trigger in Azure Functions unterstützten Sprachen.

## Fazit

Retry-Muster sind nicht aufregend zu konfigurieren, bis zum ersten Mal ein Downstream-Ausfall dazu führt, dass Ihre Functions das Problem verschlimmern, anstatt angemessen zu degradieren. Diese proaktiv einzurichten ist günstig. Sie während eines Incidents nachzurüsten nicht.

Originalbeitrag: [Exponential backoff and circuit breaker for Service Bus-triggered Azure Functions](https://devblogs.microsoft.com/azure-sdk/exponential-backoff-circuit-breaker-azure-functions/)
