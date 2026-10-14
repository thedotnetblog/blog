---
title: "Deep Agents + Cosmos DB Pokazują Praktyczny Wzorzec Pracy na Żywych Danych Operacyjnych"
date: 2026-06-22
author: "Emiliano Montesdeoca"
description: "Przykład Deep Agents z Azure Cosmos DB jest interesujący, ponieważ pokazuje agenta pracującego bezpośrednio na danych operacyjnych, planującego w wielu krokach, weryfikującego zapisy i pozostającego ugruntowanego w tym samym magazynie, którego biznes już używa."
tags:
  - Azure Cosmos DB
  - AI
  - Agents
  - Azure
  - Architecture
---

Lubię przykłady agentów, które pozostają blisko prawdziwych przepływów operacyjnych.

Ten nowy przykład **Deep Agents + Azure Cosmos DB** robi dokładnie to.

Zamiast wymyślać oderwany świat demo, umieszcza agenta na kolejce zgłoszeń wsparcia przechowywanej w Cosmos DB i każe mu robić rzeczy, które faktycznie interesują zespoły:

- triage pracy
- wykrywanie wzorców
- aktualizowanie rekordów
- weryfikowanie wyników

To znacznie bardziej użyteczny kształt systemu agentowego.

## Prawdziwa wartość to nie „AI rozmawia z bazą danych"

Widzieliśmy już tę historię.

To, co czyni ten przykład lepszym, to dyscyplina operacyjna wokół niego:

- agent używa konkretnych narzędzi
- zapisy przechodzą przez kontrolowaną ścieżkę
- weryfikacja odczyt-po-zapisie jest częścią przepływu
- partycjonowanie i koszt zapytań są brane pod uwagę
- system działa na danych operacyjnych w stylu live, a nie na bocznym cache'u udającym rzeczywistość

Ta kombinacja czyni wzorzec interesującym.

## Dlaczego Cosmos DB dobrze tu pasuje

Cosmos DB dobrze pasuje do tego rodzaju obciążenia, ponieważ dane są już dynamiczne, w kształcie dokumentu i operacyjne.

Agent może:

- czytać zgłoszenia bezpośrednio
- uruchamiać zapytania w całej kolejce, gdy potrzeba
- łatkować konkretne elementy
- utrzymywać stan i historię blisko samych danych

W scenariuszach agentowych jest to często bardziej użyteczne niż przepychanie wszystkiego przez osobną warstwę analityczną.

## Moje zdanie

Najważniejszym wnioskiem jest to, że systemy agentowe stają się znacznie bardziej przekonujące, gdy operują na tych samych danych i tych samych przepływach pracy, na których biznes już polega.

To właśnie ten przykład robi dobrze.

Traktuje agenta jako uczestnika operacyjnego z jasnymi granicami narzędzi, a nie jako odłączony interfejs czatu udający pomoc.

To wzorzec wart studiowania.

Oryginalny wpis: [How to Use Deep Agents with Azure Cosmos DB – Plan, act, and verify against operational data](https://devblogs.microsoft.com/cosmosdb/deep-agents-to-plan-act-verify-against-operational-data/)