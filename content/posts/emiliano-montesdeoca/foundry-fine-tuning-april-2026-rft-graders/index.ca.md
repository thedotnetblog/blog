---
title: "L'RFT de Foundry s'ha tornat més barat i intel·ligent: això és el que ha canviat"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry va enviar tres actualitzacions de RFT aquest mes: formació global per a o4-mini, nous gradadors de models GPT-4.1 i una guia de bones pràctiques que us estalviarà hores de depuració."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

Si esteu creant aplicacions.NET que es basen en models afinats, val la pena prestar atenció a les actualitzacions de Foundry d'aquest mes. L'afinació del reforç acaba de ser més accessible i molt més barata.

Els detalls complets es troben a l'[anunci oficial](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/), però aquí teniu el desglossament pràctic.

## Formació global per a o4-mini

o4-mini és el model de referència per a càrregues de treball pesades i de raonament. La gran notícia: ara podeu llançar treballs d'ajustament de més de 13 regions Azure amb taxes d'entrenament per testimoni més baixes en comparació amb la formació estàndard. Mateixa infraestructura, mateixa qualitat, abast més ampli.

Si el vostre equip està repartit per geografies, això és important. Ja no estàs fixat a un grapat de regions per entrenar.

Aquí teniu la crida a l'API REST per iniciar una feina de formació global:

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

Aquesta bandera `trainingType: globalstandard` és la diferència clau.

## Nou model de classificadors: família GPT-4.1

Els qualificadors defineixen el senyal de recompensa amb el qual optimitza el vostre model. Fins ara, els qualificadors basats en models es limitaven a un conjunt més petit de models. Ara teniu tres opcions noves: GPT-4.1, GPT-4.1-mini i GPT-4.1-nano.

Quan hauríeu d'aconseguir els qualificadors model en lloc dels deterministes? Quan la sortida de la vostra tasca és oberta, quan necessiteu una puntuació de crèdit parcial en diverses dimensions o quan esteu creant fluxos de treball agents on la correcció de la trucada d'eines depèn del context semàntic.

Aquesta és la qüestió: l'estratègia de classificació és pràctica:

- **GPT-4.1-nano** per a les iteracions inicials. Bucles de retroalimentació ràpids i de baix cost.
- **GPT-4.1-mini** un cop la rúbrica de qualificació sigui estable i necessiteu una fidelitat més alta.
- **GPT-4.1** per a la qualificació de la producció o rúbriques complexes on cada decisió de puntuació compta.

Fins i tot podeu barrejar tipus de classificador en un sol treball RFT. Utilitzeu string-match per a la dimensió "resposta correcta" i un model de qualificació per avaluar la qualitat del raonament. Aquesta flexibilitat és sincerament el que fa que sigui útil per a càrregues de treball reals.

## El format de dades de RFT es troba

Això fa ensorrar la gent. El format de dades RFT és diferent de SFT. L'últim missatge de cada fila ha de ser una funció d'usuari o de desenvolupador, no d'assistent. La resposta esperada va en una clau de nivell superior com `reference_answer` que el qualificador fa referència directament.

Si heu estat fent un ajustament supervisat i voleu canviar a RFT, heu de reestructurar les vostres dades d'entrenament. No us salteu aquest pas o els vostres treballs fallaran en silenci.

## Per què això és important per als desenvolupadors de.NET

Si truqueu a models ajustats des de les vostres aplicacions.NET mitjançant l'SDK d'Azure OpenAI, una formació més barata significa que podeu repetir de manera més agressiva. Les opcions de classificació del model us permeten ajustar amb precisió les tasques matisades, no només escenaris de concordança exacta. I la guia de bones pràctiques a [GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) us estalviarà temps real de depuració.

Comença petit. De deu a cent mostres. Avaluador simple. Valida el bucle. Després escala.
