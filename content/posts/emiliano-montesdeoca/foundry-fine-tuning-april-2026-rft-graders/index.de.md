---
title: "Foundrys RFT ist jetzt günstiger und intelligenter — Das hat sich geändert"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry hat diesen Monat drei RFT-Updates veröffentlicht: globales Training für o4-mini, neue GPT-4.1 Model-Grader und einen Best-Practices-Leitfaden, der euch Stunden beim Debugging spart."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

Wenn ihr .NET-Apps entwickelt, die auf fine-getunte Modelle angewiesen sind, solltet ihr die Foundry-Updates dieses Monats im Auge behalten. Reinforcement Fine-Tuning ist jetzt zugänglicher und deutlich günstiger geworden.

Die vollständigen Details findet ihr in der [offiziellen Ankündigung](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/), aber hier ist die praktische Zusammenfassung.

## Globales Training für o4-mini

o4-mini ist das Go-to-Modell für reasoning-intensive und agentenbasierte Workloads. Die große Neuigkeit: Ihr könnt jetzt Fine-Tuning-Jobs aus über 13 Azure-Regionen starten, mit niedrigeren Pro-Token-Trainingskosten im Vergleich zum Standard-Training. Gleiche Infrastruktur, gleiche Qualität, größere Reichweite.

Wenn euer Team über verschiedene Regionen verteilt ist, ist das relevant. Ihr seid nicht mehr auf eine Handvoll Regionen zum Trainieren beschränkt.

Hier ist der REST-API-Aufruf, um einen globalen Trainingsjob zu starten:

```bash
curl -X POST "https://<your-resource>.openai.azure.com/openai/fine_tuning/jobs?api-version=2025-04-01-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: $AZURE_OPENAI_API_KEY" \
  -d '{
    "model": "o4-mini",
    "training_file": "<your-training-file-id>",
    "method": {
      "type": "reinforcement",
      "reinforcement": {
        "grader": {
          "type": "string_check",
          "name": "answer-check",
          "input": "{{sample.output_text}}",
          "reference": "{{item.reference_answer}}",
          "operation": "eq"
        }
      }
    },
    "hyperparameters": {
      "n_epochs": 2,
      "compute_multiplier": 1.0
    },
    "trainingType": "globalstandard"
  }'
```

Dieses `trainingType: globalstandard`-Flag ist der entscheidende Unterschied.

## Neue Model-Grader: GPT-4.1-Familie

Grader definieren das Belohnungssignal, gegen das euer Modell optimiert. Bisher waren modellbasierte Grader auf eine kleinere Auswahl von Modellen beschränkt. Jetzt habt ihr drei neue Optionen: GPT-4.1, GPT-4.1-mini und GPT-4.1-nano.

Wann solltet ihr Model-Grader statt deterministischer Grader verwenden? Wenn eure Aufgabenausgabe offen ist, wenn ihr partielle Bewertung über mehrere Dimensionen braucht, oder wenn ihr agentenbasierte Workflows baut, bei denen die Korrektheit von Tool-Aufrufen vom semantischen Kontext abhängt.

Die Sache ist — die Tier-Strategie ist praktisch:

- **GPT-4.1-nano** für erste Iterationen. Niedrige Kosten, schnelle Feedback-Schleifen.
- **GPT-4.1-mini** sobald eure Bewertungsrubrik stabil ist und ihr höhere Genauigkeit braucht.
- **GPT-4.1** für Produktionsbewertung oder komplexe Rubriken, bei denen jede Bewertungsentscheidung zählt.

Ihr könnt sogar Grader-Typen in einem einzigen RFT-Job mischen. Verwendet String-Match für die "richtige Antwort"-Dimension und einen Model-Grader zur Bewertung der Reasoning-Qualität. Diese Flexibilität ist ehrlich gesagt das, was es für echte Workloads nützlich macht.

## Die Stolperfalle beim RFT-Datenformat

Hierüber stolpern viele. Das RFT-Datenformat unterscheidet sich von SFT. Die letzte Nachricht in jeder Zeile muss eine User- oder Developer-Rolle haben — nicht Assistant. Die erwartete Antwort kommt in einen Top-Level-Schlüssel wie `reference_answer`, auf den der Grader direkt verweist.

Wenn ihr bisher Supervised Fine-Tuning gemacht habt und auf RFT umsteigen wollt, müsst ihr eure Trainingsdaten umstrukturieren. Überspringt diesen Schritt nicht, sonst schlagen eure Jobs stillschweigend fehl.

## Warum das für .NET-Entwickler wichtig ist

Wenn ihr fine-getunte Modelle aus euren .NET-Apps über das Azure OpenAI SDK aufruft, bedeutet günstigeres Training, dass ihr aggressiver iterieren könnt. Die Model-Grader-Optionen bedeuten, dass ihr für nuancierte Aufgaben fine-tunen könnt — nicht nur für Exact-Match-Szenarien. Und der Best-Practices-Leitfaden auf [GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) wird euch echte Debugging-Zeit sparen.

Fangt klein an. Zehn bis hundert Samples. Einfacher Grader. Validiert den Loop. Dann skaliert.
