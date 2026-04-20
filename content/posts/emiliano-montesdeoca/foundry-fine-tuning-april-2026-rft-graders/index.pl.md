---
title: "RFT Foundry Stał Się Tańszy i Mądrzejszy — Oto Co Się Zmieniło"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry wysłał w tym miesiącu trzy aktualizacje RFT: globalne szkolenie dla o4-mini, nowe oceniające modele GPT-4.1 i przewodnik po najlepszych praktykach."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

Jeśli tworzysz aplikacje .NET opierające się na dostrojonych modelach, aktualizacje Foundry z tego miesiąca są warte uwagi.

Pełne szczegóły są w [oficjalnym ogłoszeniu](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/).

## Globalne szkolenie dla o4-mini

o4-mini to model do intensywnego rozumowania i obciążeń agentycznych. Możesz teraz uruchamiać zadania dostrajania z 13+ regionów Azure z niższymi stawkami trenowania.

```bash
"trainingType": "globalstandard"
```

## Nowe oceniające modele: rodzina GPT-4.1

Trzy nowe opcje: GPT-4.1, GPT-4.1-mini i GPT-4.1-nano.

Strategia poziomowania:
- **GPT-4.1-nano** do wstępnych iteracji. Niski koszt, szybka pętla informacji zwrotnych.
- **GPT-4.1-mini** gdy rubrum oceniania jest stabilne.
- **GPT-4.1** do produkcyjnego oceniania.

## Pułapka formatu danych RFT

Format danych RFT różni się od SFT. Ostatnia wiadomość w każdym wierszu musi mieć rolę User lub Developer — nie Assistant.

## Dlaczego to ważne dla programistów .NET

Tańsze szkolenie oznacza, że możesz bardziej agresywnie iterować. Przewodnik po najlepszych praktykach na [GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) zaoszczędzi ci czasu debugowania.
