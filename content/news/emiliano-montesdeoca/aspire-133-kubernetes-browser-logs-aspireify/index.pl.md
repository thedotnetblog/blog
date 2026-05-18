---
title: "Aspire 13.3: Obsługa Kubernetes, logi przeglądarki i umiejętność Aspireify"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "Pięć tygodni po 13.2, Aspire 13.3 przynosi 45 nowych funkcji, w tym wdrożenie AKS pierwszej klasy, umiejętność onboardingu wspomaganą przez AI, przechwytywanie logów przeglądarki i ustrukturyzowane wyniki poleceń."
tags:
  - Aspire
  - .NET
  - Azure
  - AKS
  - Kubernetes
  - AI
---

Pięć tygodni to niedługo dla wydania, ale Aspire 13.3 tak nie wygląda. Główne elementy są istotne: wdrożenie Kubernetes i AKS pierwszej klasy za pomocą Helm, umiejętność onboardingu wspomagana przez agenta o nazwie Aspireify, przechwytywanie logów przeglądarki bezpośrednio w panelu oraz ustrukturyzowane wyniki poleceń. Dodatkowo 45 nowych funkcji, 134 ulepszeń i 93 poprawki błędów.

Przejdźmy do najważniejszych punktów.

## Aspireify: Onboarding wspomagany przez agenta

Dodanie Aspire do istniejącego projektu brzmi prosto — wstaw AppHost, gotowe. W praktyce wymaga dużo badań: które porty są ważne, które zmienne środowiskowe są prawdziwymi zależnościami, które usługi Docker Compose należy mapować na integracje Aspire.

Nowa **umiejętność Aspireify** daje Twojemu agentowi kodowania poprowadzony przepływ pracy właśnie do tego celu. Gdy `aspire init` tworzy szkieletowy AppHost, umiejętność Aspireify pomaga agentowi zbadać repozytorium, zrozumieć jak już działa i połączyć AppHost tak, aby pasował do aplikacji — nie odwrotnie.

Domyślna postawa to "minimalizować zmiany w Twoim kodzie." Jeśli Twoja aplikacja już odczytuje `DATABASE_URL`, agent mapuje to za pomocą `WithEnvironment()` zamiast prosić Cię o przepisanie konfiguracji. Jeśli port jest zakodowany na stałe, umiejętność mówi agentowi kiedy go zachować.

To jest właśnie ten rodzaj narzędzi AI, który naprawdę oszczędza czas zamiast generować więcej pracy do przejrzenia.

## Wdrożenie Kubernetes i AKS pierwszej klasy

To było na liście życzeń od jakiegoś czasu. Aspire 13.3 dostarcza **obsługę wdrożenia Kubernetes i AKS pierwszej klasy za pomocą Helm**. Teraz możesz wybrać AKS jako cel wdrożenia bezpośrednio z narzędzi Aspire.

Dla zespołów, które już uruchamiają produkcyjne obciążenia na AKS, to zamyka znaczącą lukę. Twój model aplikacji Aspire ma teraz przejrzystą ścieżkę od lokalnego tworzenia do Kubernetes bez ręcznego pisania wykresów Helm.

## Logi przeglądarki w panelu

To jedna z tych funkcji, które wyglądają na małe, dopóki nie debugujesz problemu z frontendem.

Nowe API `WithBrowserLogs()` dołącza śledzony zasób przeglądarki do dowolnego zasobu obsługującego endpointy. Aspire uruchamia Chromium za pomocą prywatnego potoku CDP i strumieniuje logi konsoli, żądania sieciowe i błędy bezpośrednio do strumienia logów zasobu:

```csharp
var frontend = builder.AddViteApp("frontend", "../frontend")
    .WithHttpEndpoint(port: 3000)
    .WithBrowserLogs();
```

TypeScript AppHost obsługuje to samo:

```typescript
const frontend = await builder.addViteApp("frontend", "../frontend")
    .withHttpEndpoint({ port: 3000 })
    .withBrowserLogs();
```

Błędy konsoli, nieudane żądania sieciowe, wyjątki po stronie klienta — wszystko widoczne w tym samym panelu, gdzie już obserwujesz ślady i metryki. Koniec z przełączaniem zakładek do DevTools przeglądarki dla podstawowych rzeczy.

## Ustrukturyzowane wyniki poleceń

Polecenia zasobów otrzymały znaczącą aktualizację. Do tej pory polecenia zwracały sukces/niepowodzenie. Teraz zwracają ustrukturyzowane wyniki: tekst, JSON lub Markdown przepływający przez model, interfejs panelu, CLI i narzędzia MCP.

Panel łączy to wszystko z nowym centrum powiadomień w nagłówku. Wyniki poleceń pojawiają się jako powiadomienia z znacznikiem czasu z renderowaniem Markdown i akcją "Wyświetl odpowiedź".

To sprawia, że polecenia zasobów są naprawdę składalne. Integracja może teraz udostępniać polecenie, które zwraca znaczące dane wyjściowe — takie jak URL tunelu — zamiast po prostu zmieniać stan gdzieś.

## Podsumowanie

Aspire 13.3 jest wart aktualizacji choćby dla obsługi Kubernetes. Logi przeglądarki i ustrukturyzowane wyniki poleceń wyglądają jak rodzaj ulepszeń jakości życia, które szybko się kumulują w codziennym przepływie pracy programistycznej.

Pełne informacje o wydaniu: [What's New in Aspire 13.3](https://devblogs.microsoft.com/aspire/whats-new-aspire-13-3/)
