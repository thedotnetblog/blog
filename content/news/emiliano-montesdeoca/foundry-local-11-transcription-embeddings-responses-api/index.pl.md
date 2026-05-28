---
title: "Foundry Local 1.1: Transkrypcja w Czasie Rzeczywistym, Embeddings i Responses API"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1 dodaje transkrypcję na żywo z mikrofonu, embeddings tekstu i obsługę Responses API — wszystko działające lokalnie bez zależności od chmury, bez opóźnień sieciowych, bez opłat za token."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 udowodnił koncepcję: uruchamianie modeli AI lokalnie na Windows, macOS (Apple Silicon) i Linux x64 z przyjaznym dla deweloperów SDK. Wersja 1.1 dodaje trzy możliwości pokrywające wiele rzeczywistych przypadków użycia produkcyjnego.

## Transkrypcja Audio na Żywo

Najważniejsza nowa funkcja: strumieniowe przetwarzanie mowy na tekst w czasie rzeczywistym bezpośrednio z mikrofonu. Napisy, interfejsy głosowe, transkrypcja spotkań, narzędzia dostępności — wszystko działające lokalnie bez jakiejkolwiek zależności od chmury.

API jest oparte na sesjach i przesyła strumieniowo wyniki w miarę ich napływania, z markerami `is_final` do odróżniania tekstu tymczasowego od sfinalizowanego. Dostępne dla wszystkich powiązań językowych: JavaScript, C#, Python i Rust.

Załaduj model mowy strumieniowej z katalogu, utwórz sesję z ustawieniami audio (częstotliwość próbkowania, kanały, język), uruchom ją, wysyłaj surowe fragmenty audio PCM i konsumuj asynchroniczny strumień wyników. Post zawiera pełne przykłady w Python i C#.

## Embeddings Tekstu

Wyszukiwanie semantyczne, pipeline RAG, klastrowanie, dopasowywanie podobieństwa — to wszystko wymaga embeddings. Foundry Local 1.1 dodaje obsługę modeli embedding, aby generować wektory lokalnie z tego samego SDK bez wysyłania danych do endpointu w chmurze.

Dla aplikacji, w których ważna jest rezydencja danych lub przetwarzane są wrażliwe treści, lokalne generowanie embeddingów jest znaczącą możliwością.

## Responses API

Foundry Local obsługuje teraz [Responses API](https://platform.openai.com/docs/api-reference/responses) — ustrukturyzowany interfejs zaprojektowany do interakcji agentowych. Dodaje to:

- **Wywoływanie narzędzi** — pozwól lokalnie działającym modelom wywoływać zdefiniowane przez ciebie narzędzia
- **Multimodalny wejście wizja-język** — przekazuj obraz + tekst do modeli zdolnych do wizji
- Zgodny ze standardowym kształtem API, więc istniejący agenci kierowani na Responses API OpenAI działają z lokalnymi modelami

## Ulepszenia Rozmiaru Pakietu

Dwie zmiany zmniejszają rozmiar pakietu JavaScript:
- Warstwa FFI `koffi` została zastąpiona niestandardowym addonem C Node-API
- Dostawca wykonania WebGPU jest dostarczany jako oddzielna wtyczka, więc aplikacje niewymagające akceleracji GPU nie ponoszą kosztów rozmiaru

SDK C# teraz celuje w niższe wersje frameworka dla szerszej kompatybilności .NET.

## Dlaczego To Ważne

Trzy możliwości razem — transkrypcja, embeddings, wywoływanie narzędzi — pokrywają podstawowe składniki wielu aplikacji AI. Uruchamianie ich lokalnie oznacza:
- Nie wymaga internetu
- Brak opłat za token
- Żadne dane nie opuszczają maszyny
- Stałe opóźnienie niezależnie od warunków sieciowych

Foundry Local to właściwy wybór dla scenariuszy edge, obciążeń wrażliwych na prywatność, aplikacji offline lub wszystkiego, gdzie chcesz uniknąć zależności od chmury podczas tworzenia.

Oryginalny wpis: [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
