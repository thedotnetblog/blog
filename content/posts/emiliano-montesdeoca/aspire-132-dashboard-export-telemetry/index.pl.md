---
title: "Dashboard Aspire 13.2 Właśnie Dostał Telemetry API — i To Zmienia Wszystko"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 dostarcza mądrzejszy eksport telemetrii, programowalny API dla śladów i logów oraz ulepszenia wizualizacji GenAI. Oto dlaczego ma to znaczenie dla twojego przepływu debugowania."
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "aspire-132-dashboard-export-telemetry" >}}).*

Jeśli budujesz rozproszone aplikacje z .NET Aspire, wiesz już, że dashboard jest najlepszą częścią całego doświadczenia. Aspire 13.2 znacznie go poprawił.

## Eksportowanie telemetrii jak normalna osoba

Aspire 13.2 dodaje odpowiedni dialog **Zarządzaj logami i telemetrią**, gdzie możesz:
- Wyczyścić całą telemetrię
- Wyeksportować wybraną telemetrię do pliku ZIP w standardowym formacie OTLP/JSON
- Zaimportować ten ZIP do dowolnego dashboardu Aspire później

Ta ostatnia część to kluczowa funkcja. Reprodukujesz błąd, eksportujesz telemetrię, dołączasz do elementu pracy, a twój kolega może zaimportować go do własnego dashboardu.

## Telemetry API to prawdziwy przełom

Dashboard udostępnia teraz HTTP API pod `/api/telemetry`:
- `GET /api/telemetry/resources` — lista zasobów z telemetrią
- `GET /api/telemetry/spans` — zapytania o spany z filtrami
- `GET /api/telemetry/logs` — zapytania o logi z filtrami
- `GET /api/telemetry/traces` — lista śladów

To zasila nowe polecenia CLI `aspire agent mcp` i `aspire otel`.

## Telemetria GenAI staje się praktyczna

VS Code Copilot chat i Copilot CLI obsługują konfigurowanie `OTEL_EXPORTER_OTLP_ENDPOINT` — wskaż je na dashboard Aspire i możesz obserwować, jak twoje agenty AI myślą w czasie rzeczywistym.

## Podsumowanie

Aspire 13.2 zamienia dashboard z "ładnego UI do debugowania" w "programowalną platformę obserwowalności". Sprawdź [aspire.dev](https://aspire.dev).
