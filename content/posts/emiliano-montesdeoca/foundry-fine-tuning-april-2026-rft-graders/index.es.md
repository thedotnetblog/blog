---
title: "El RFT de Foundry ahora es más barato e inteligente — Esto es lo que cambió"
date: 2026-04-18
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry lanzó tres actualizaciones de RFT este mes: entrenamiento global para o4-mini, nuevos evaluadores de modelo GPT-4.1 y una guía de mejores prácticas que te ahorrará horas de depuración."
tags:
  - ai
  - azure
  - foundry
  - fine-tuning
  - machine-learning
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "foundry-fine-tuning-april-2026-rft-graders" >}}).*

Si estás desarrollando aplicaciones .NET que dependen de modelos fine-tuneados, las actualizaciones de Foundry de este mes merecen tu atención. El Reinforcement Fine-Tuning ahora es más accesible y significativamente más barato.

Los detalles completos están en el [anuncio oficial](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-finetune-april-2026/), pero aquí va el resumen práctico.

## Entrenamiento Global para o4-mini

o4-mini es el modelo preferido para cargas de trabajo pesadas en razonamiento y agentes. La gran noticia: ahora puedes lanzar trabajos de fine-tuning desde más de 13 regiones de Azure con tarifas de entrenamiento por token más bajas en comparación con el entrenamiento Standard. Misma infraestructura, misma calidad, mayor alcance.

Si tu equipo está distribuido geográficamente, esto importa. Ya no estás limitado a un puñado de regiones para entrenar.

Aquí está la llamada a la API REST para iniciar un trabajo de entrenamiento global:

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

Ese flag `trainingType: globalstandard` es la diferencia clave.

## Nuevos Evaluadores de Modelo: Familia GPT-4.1

Los evaluadores definen la señal de recompensa contra la cual tu modelo optimiza. Hasta ahora, los evaluadores basados en modelo estaban limitados a un conjunto más pequeño de modelos. Ahora tienes tres nuevas opciones: GPT-4.1, GPT-4.1-mini y GPT-4.1-nano.

¿Cuándo deberías usar evaluadores de modelo en lugar de determinísticos? Cuando la salida de tu tarea es abierta, cuando necesitas puntuación parcial en múltiples dimensiones, o cuando estás construyendo flujos de trabajo con agentes donde la corrección de las llamadas a herramientas depende del contexto semántico.

La cuestión es que la estrategia de niveles es práctica:

- **GPT-4.1-nano** para iteraciones iniciales. Bajo costo, ciclos de retroalimentación rápidos.
- **GPT-4.1-mini** una vez que tu rúbrica de evaluación sea estable y necesites mayor fidelidad.
- **GPT-4.1** para evaluación en producción o rúbricas complejas donde cada decisión de puntuación cuenta.

Incluso puedes mezclar tipos de evaluadores en un solo trabajo de RFT. Usa string-match para la dimensión de "respuesta correcta" y un evaluador de modelo para evaluar la calidad del razonamiento. Esa flexibilidad es honestamente lo que lo hace útil para cargas de trabajo reales.

## El Problema del Formato de Datos de RFT

Esto confunde a mucha gente. El formato de datos de RFT es diferente al de SFT. El último mensaje en cada fila debe tener rol User o Developer — no Assistant. La respuesta esperada va en una clave de nivel superior como `reference_answer` que el evaluador referencia directamente.

Si has estado haciendo supervised fine-tuning y quieres cambiar a RFT, necesitas reestructurar tus datos de entrenamiento. No te saltes este paso o tus trabajos fallarán silenciosamente.

## Por Qué Esto Importa para Desarrolladores .NET

Si estás llamando modelos fine-tuneados desde tus aplicaciones .NET a través del SDK de Azure OpenAI, un entrenamiento más barato significa que puedes iterar de forma más agresiva. Las opciones de evaluadores de modelo significan que puedes hacer fine-tuning para tareas con matices — no solo escenarios de coincidencia exacta. Y la guía de mejores prácticas en [GitHub](https://github.com/microsoft-foundry/fine-tuning/blob/main/Demos/Agentic_RFT_PrivatePreview/RFT_Best_Practice.md) te ahorrará tiempo real de depuración.

Empieza pequeño. De diez a cien muestras. Evaluador simple. Valida el ciclo. Luego escala.
