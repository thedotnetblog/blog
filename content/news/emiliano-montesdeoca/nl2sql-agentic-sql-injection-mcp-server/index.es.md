---
title: "NL2SQL Es la Inyección SQL de la Era Agéntica"
date: 2026-06-03
author: "Emiliano Montesdeoca"
description: "Antes de dejar que un agente consulte tu base de datos con lenguaje natural, lee esto. NL2SQL parece simple hasta que analizas la completitud del esquema, el indeterminismo y lo que SQL MCP Server realmente resuelve."
tags:
  - Azure SQL
  - AI
  - Agents
  - MCP
  - SQL MCP Server
  - Security
---

Hay una versión del argumento de NL2SQL que suena perfecta: los usuarios hacen preguntas en lenguaje natural, los agentes generan SQL, los datos regresan. Menos pantallas, menos consultas, menos código. Simple.

Luego lo piensas cinco minutos más.

## Los Problemas de los que Nadie Habla en la Demo

**Los esquemas no fueron diseñados para explicar las cosas.** Nombres de tablas crípticos, nombres de columnas inconsistentes, relaciones técnicamente válidas pero semánticamente inválidas sin predicados adicionales — esto es normal en bases de datos empresariales. No son errores, son simplemente la historia acumulada de cambios de negocio. Pero cuando le pides a un modelo que infiera intención de un esquema que no fue diseñado para comunicar intención, el modelo lo intentará de todas formas. No se rendirá. Generará su mejor consulta posible y devolverá resultados con confianza.

**Los modelos no son deterministas.** Haz la misma pregunta sobre la misma base de datos dos veces y podrías obtener SQL diferente. El modelo está calculando probabilidades, y variaciones ligeras en el contexto generan salidas diferentes. No puedes probar tu camino hacia una garantía de que el agente siempre genera la consulta correcta.

**La revisión del usuario no escala.** "Solo revisa cada consulta antes de la ejecución" suena seguro. Pero asume que los usuarios son expertos tanto en el modelo de datos como en SQL — exactamente las personas que no necesitaban la interfaz de lenguaje natural. También introduce sobrecarga cognitiva y una nueva clase de sesgo de confirmación, donde los usuarios abrumados por la complejidad de la consulta aprueban consultas inválidas en lugar de investigarlas.

**Y luego está la inyección.** En el desarrollo SQL tradicional, la parametrización resolvió la inyección porque la entrada del usuario llenaba parámetros, no la estructura SQL. Con NL2SQL, el modelo genera el SQL en sí. El prompt, el contexto del esquema, el historial de conversación y los datos recuperados influyen en lo que se ejecuta. Si alguien elabora un prompt que cambia lo que el modelo genera, eso es inyección — no a nivel de parámetro, sino a nivel de generación de consultas. Y a diferencia de eliminar una tabla (obvio, recuperable), la inyección NL2SQL produce consultas que devuelven resultados incorrectos sin ningún error visible. Las decisiones de negocio se toman sobre datos incorrectos.

## Lo que SQL MCP Server Realmente Resuelve

Aquí es donde el artículo hace su punto práctico más útil. En lugar de dar a un agente acceso arbitrario al esquema y esperar lo mejor, SQL MCP Server expone una **superficie API curada** construida sobre [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/overview).

La diferencia importa: el agente no genera SQL. Llama a endpoints con nombre que devuelven formas de resultado predefinidas. El SQL se escribe una vez, por un desarrollador, y es determinista. El no-determinismo del agente se limita a elegir *qué* endpoint llamar, no a construir consultas arbitrarias.

Esto es análogo a lo que la parametrización hizo para la inyección SQL en el modelo de aplicación tradicional — eliminas la capacidad de construir consultas arbitrarias a partir de entrada no confiable.

## La Pregunta Correcta

El artículo no dice "nunca uses NL2SQL." Dice: sé deliberado sobre *dónde* lo aplicas y *qué* expones. Para análisis exploratorio en un entorno controlado, con un esquema limitado y acceso de solo lectura, NL2SQL podría estar bien. Para sistemas de producción donde las decisiones de negocio dependen de los resultados, una capa API curada es significativamente más segura.

Honestidad: algunos problemas se resuelven genuinamente mejor con consultas estructuradas detrás de endpoints con nombre que con lenguaje natural a SQL. SQL MCP Server te da esa opción sin abandonar completamente la interfaz agéntica.

Publicación original: [Considering NL2SQL? Should your database really be the prompt? How can SQL MCP Server help?](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-nl2sql/)
