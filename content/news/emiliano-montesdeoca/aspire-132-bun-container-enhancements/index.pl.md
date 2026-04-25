---
title: "Aspire 13.2 dodaje Bun, lepsze kontenery i mniej tarcia przy debugowaniu"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 dodaje pełnoprawne wsparcie dla Bun w aplikacjach Vite, poprawia niezawodność Yarn i wprowadza ulepszenia kontenerów, które sprawiają, że lokalne środowisko zachowuje się bardziej uczciwie. Oto, co naprawdę się zmieniło i dlaczego ma to znaczenie."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

Jeśli budujesz w Aspire backendy .NET z frontendami JavaScript, to 13.2 jest takim wydaniem, które po cichu poprawia Ci dzień. Bez efektownych nowych paradygmatów. Po prostu solidne usprawnienia rzeczy, które były tylko trochę irytujące.

Spójrzmy, co faktycznie trafiło do wydania.

## Bun jest teraz pełnoprawny

Najważniejsza nowość: wsparcie Bun dla aplikacji Vite w Aspire. Jedno płynne wywołanie i gotowe.

```typescript
// TypeScript AppHost
const builder = await createBuilder();

await builder
  .addViteApp("frontend", "./frontend")
  .withBun();

await builder.build().run();
```

Jeśli Twój zespół już używa Bun — a pewnie używa, biorąc pod uwagę znacznie szybsze instalacje i start — Aspire nie zmusza Cię już do walki pod prąd. Wcześniej Aspire zakładał npm i trzeba było to obejść. Teraz `.withBun()` jest opcją pierwszej kategorii obok `.withYarn()` i domyślnego zachowania npm.

Dlaczego to ważne? Bo szybkość narzędzi JavaScript bezpośrednio wpływa na Twój inner dev loop. Jeśli frontend potrzebuje 30 sekund na instalację zależności za każdym razem, gdy stawiasz nowe środowisko, to zaczyna się to kumulować. Bun mocno to skraca.

Odpowiedniki AppHost w C# są opisane na [aspire.dev](https://aspire.dev/integrations/frameworks/javascript/#use-bun), jeśli wolisz pisać w C# — te same wzorce nadal obowiązują.

## Yarn stał się bardziej niezawodny

Bun zgarnia nagłówki, ale użytkownicy Yarn dostają coś być może jeszcze ważniejszego: mniej tajemniczych awarii. Aspire 13.2 poprawia niezawodność `withYarn()` wraz z `addViteApp()`.

Takie poprawki nie brzmią ekscytująco, dopóki nie spędzisz 20 minut na szukaniu, dlaczego frontend oparty na Yarn nie chce się uruchomić. Można uznać temat za załatwiony.

## Publikowanie kontenerów, które naprawdę da się ogarnąć

Dwie poprawki związane z kontenerami, które warto znać:

### Jawna polityka pull

Publikowanie przez Docker Compose obsługuje teraz `PullPolicy`, w tym opcję `Never`:

```typescript
import { createBuilder, ImagePullPolicy } from './.modules/aspire.js';

const builder = await createBuilder();
await builder.addDockerComposeEnvironment("compose");

const worker = await builder.addContainer("worker", "myorg/worker:latest")
  .withImagePullPolicy(ImagePullPolicy.Never);

await builder.build().run();
```

To jest ten workflow, który mówi: „użyj obrazu, który już zbudowałem, i zostaw rejestr w spokoju”. Bardzo przydatne, gdy lokalnie iterujesz nad obrazami budowanymi i publikowanymi ręcznie albo gdy CI produkuje obraz i chcesz, żeby Compose użył dokładnie tego obrazu, bez ukradkowego pobierania zdalnego.

### Wolumeny PostgreSQL 18+ znów działają

PostgreSQL 18 zmienił wewnętrzny układ katalogu danych. To po cichu zepsuło mapowanie wolumenów w Aspire — wolumen danych był tworzony, ale trwałość danych nie działała prawidłowo. 13.2 to naprawia.

```typescript
const postgres = await builder.addPostgres("postgres")
  .withDataVolume({ isReadOnly: false });
```

Jeśli uruchamiasz PostgreSQL 18 lub nowszy z wolumenem danych, zaktualizuj do Aspire 13.2 i nie wracaj do tego tematu.

## Usprawnienia debugowania, które realnie ułatwiają życie

Kilka rzeczy, które sprawiają, że krokowe przechodzenie przez sesję AppHost jest mniej frustrujące:

- **`DebuggerDisplayAttribute` dla typów core** — `DistributedApplication`, zasoby i wyrażenia endpointów pokazują teraz przydatne wartości w debugerze zamiast zmuszać do przekopywania się przez drzewka obiektów
- **Lepsze komunikaty błędów `WaitFor`** — gdy zasoby nie startują, kontekst błędu jest teraz naprawdę pomocny
- **`BeforeResourceStartedEvent` odpala się we właściwym momencie** — tylko wtedy, gdy zasób faktycznie zaczyna się uruchamiać, a nie przy niezwiązanych zmianach stanu
- **`launchSettings.json` jest bardziej odporny** — mniejsze ryzyko, że uszkodzona konfiguracja zepsuje start środowiska deweloperskiego

Żadna z tych zmian nie jest samodzielnie przełomowa, ale razem usuwają tarcie z doświadczenia debugowania. Jeśli kiedykolwiek musiałeś zejść trzy poziomy w dół do obiektu zasobu Aspire, żeby sprawdzić, jakiego endpointu używa, to samo ulepszenie debugger display jest warte aktualizacji.

## Podsumowanie

Aspire 13.2 to wydanie skupione na jakości. Wsparcie Bun jest nagłówkiem, ale to ulepszenia kontenerów i debugowania sprawią, że codzienna praca będzie płynniejsza. Warto zaktualizować — szczególnie jeśli używasz PostgreSQL 18 z wolumenami danych.

Szczegóły znajdziesz w [oryginalnym wpisie Davida Pine'a](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/) oraz w [dokumentacji nowości Aspire 13.2](https://aspire.dev/whats-new/aspire-13-2/).