---
title: "Foundry Local 1.1: Transcripción en Tiempo Real, Embeddings y la API de Respuestas"
date: 2026-05-28
author: "Emiliano Montesdeoca"
description: "Foundry Local 1.1 añade transcripción en vivo desde el micrófono, embeddings de texto y soporte para la API de Respuestas — todo ejecutándose localmente sin dependencia de la nube, sin latencia de red, sin coste por token."
tags:
  - Foundry
  - Local AI
  - AI
  - Azure
  - On-Device AI
---

Foundry Local 1.0 demostró el concepto: ejecutar modelos de IA localmente en Windows, macOS (Apple Silicon) y Linux x64 con un SDK amigable para desarrolladores. La versión 1.1 añade tres capacidades que cubren muchos casos de uso reales en producción.

## Transcripción de Audio en Vivo

La nueva característica más significativa: streaming de voz a texto en tiempo real directamente desde el micrófono. Subtítulos, interfaces de voz, transcripción de reuniones, herramientas de accesibilidad — todo ejecutándose localmente sin ninguna dependencia de la nube.

La API es basada en sesiones y transmite resultados a medida que llegan, con marcadores `is_final` para distinguir texto intermedio del finalizado. Disponible en todos los bindings de lenguajes: JavaScript, C#, Python y Rust.

Carga un modelo de voz en streaming del catálogo, crea una sesión con ajustes de audio (frecuencia de muestreo, canales, idioma), iníciala, envía fragmentos de audio PCM sin procesar y consume el stream asíncrono de resultados. El artículo tiene ejemplos completos en Python y C#.

## Embeddings de Texto

Búsqueda semántica, pipelines RAG, clustering, comparación de similitudes — todo esto requiere embeddings. Foundry Local 1.1 añade soporte para modelos de embeddings para que puedas generar vectores localmente desde el mismo SDK, sin enviar datos a un endpoint en la nube.

Para aplicaciones donde la residencia de datos importa o donde procesas contenido sensible, la generación local de embeddings es una capacidad significativa.

## API de Respuestas

Foundry Local ahora soporta la [API de Respuestas](https://platform.openai.com/docs/api-reference/responses) — la interfaz estructurada diseñada para interacciones agénticas. Esto añade:

- **Llamada a herramientas** — permite que los modelos que se ejecutan localmente invoquen herramientas que defines tú
- **Entrada multimodal visión-lenguaje** — pasa imagen + texto a modelos capaces de visión
- Compatible con la forma estándar de la API, por lo que los agentes existentes que apuntan a la API de Respuestas de OpenAI funcionan contra modelos locales

## Mejoras en el Tamaño del Paquete

Dos cambios reducen el tamaño del paquete de JavaScript:
- La capa FFI `koffi` ha sido reemplazada por un addon C de Node-API personalizado
- El proveedor de ejecución WebGPU se distribuye como un plugin separado, para que las aplicaciones que no necesitan aceleración por GPU no paguen el coste de tamaño

El SDK de C# ahora apunta a versiones de framework inferiores para mayor compatibilidad con .NET.

## Por Qué Esto Importa

Las tres capacidades juntas — transcripción, embeddings, llamada a herramientas — cubren los bloques de construcción fundamentales de muchas aplicaciones de IA. Ejecutarlos localmente significa:
- Sin internet requerido
- Sin costes por token
- Sin datos que salgan de la máquina
- Latencia consistente independientemente de las condiciones de red

Foundry Local es la elección correcta para escenarios en el borde, cargas de trabajo sensibles a la privacidad, aplicaciones sin conexión, o cualquier cosa donde quieras evitar la dependencia de la nube durante el desarrollo.

Post original: [Foundry Local 1.1: Live Transcription, Embeddings, and Responses API](https://devblogs.microsoft.com/foundry/foundry-local-v1-1/)
