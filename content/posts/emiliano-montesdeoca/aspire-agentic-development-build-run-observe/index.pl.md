---
title: ".NET Aspire 13.2 Chce Być Najlepszym Przyjacielem Twojego Agenta AI"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 stawia wszystko na agentic development — ustrukturyzowane wyjście CLI, izolowane uruchomienia, środowiska samoleczące i pełne dane OpenTelemetry, żeby agenci AI mogli faktycznie budować, uruchamiać i obserwować twoje aplikacje."
tags:
  - aspire
  - dotnet
  - ai
  - cli
  - telemetry
  - developer-tools
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "aspire-agentic-development-build-run-observe" >}}).*

Znasz ten moment, kiedy twój agent kodowania AI pisze świetny kod, ekscytujesz się, a potem wszystko się sypie, kiedy próbuje to *uruchomić*? Konflikty portów, phantom processes, złe zmienne środowiskowe — nagle agent spala tokeny na rozwiązywanie problemów ze startem zamiast budować funkcje.

Zespół Aspire opublikował [bardzo przemyślany post](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) dokładnie o tym problemie, a ich odpowiedź jest przekonująca: Aspire 13.2 jest zaprojektowany nie tylko dla ludzi, ale dla agentów AI.

## Aspire jako infrastruktura agentów

Oto co Aspire 13.2 wnosi do stołu agentic development:

**Cały stos w typowanym kodzie.** AppHost definiuje pełną topologię — w kompilowanym TypeScript lub C#:

```typescript
import { createBuilder } from './.modules/aspire.js';

const builder = await createBuilder();

const postgres = await builder.addPostgres("pg").addDatabase("catalog");
const cache = await builder.addRedis("cache");

const api = await builder
  .addNodeApp("api", "./api", "src/index.ts")
  .withHttpEndpoint({ env: "PORT" })
  .withReference(postgres)
  .withReference(cache);

await builder
  .addViteApp("frontend", "./frontend")
  .withReference(api)
  .waitFor(api);

await builder.build().run();
```

**Jedno polecenie do wszystkiego.** Zamiast żonglowania `docker compose up`, `npm run dev` i skryptami startowymi bazy danych — wszystko to po prostu `aspire start`.

**Izolowany tryb dla równoległych agentów.** Z `--isolated`, każde uruchomienie Aspire dostaje własne losowe porty i oddzielne sekrety użytkownika.

**Oczy agenta przez telemetrię.** CLI Aspire eksponuje pełne dane OpenTelemetry podczas developmentu — ślady, metryki, ustrukturyzowane logi.

## Analogia do kul w kręglach

Zespół Aspire używa świetnej analogii: pomyśl o Aspire jak o odbojnikach toru do kręgli dla agentów AI. Jeśli agent nie jest doskonały (a nie będzie), odbojniki nie pozwolą mu rzucać na rynsztok.

## Podsumowanie

Aspire 13.2 to nie tylko framework dla aplikacji rozproszonych — staje się niezbędną infrastrukturą agentów. Przeczytaj [pełny post](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) od zespołu Aspire.
