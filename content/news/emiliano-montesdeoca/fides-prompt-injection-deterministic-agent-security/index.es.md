---
title: "FIDES es el tipo de historia de seguridad de agentes determinista que quiero ver más a menudo"
date: 2026-06-10
author: "Emiliano Montesdeoca"
description: "Las nuevas capacidades de FIDES en Agent Framework importan porque mueven la defensa contra prompt injection lejos de las heurísticas y hacia una política aplicable basada en contenido etiquetado y comprobaciones de middleware."
tags:
  - Agent Framework
  - AI
  - Security
  - Prompt Injection
  - Middleware
---

> *Esta publicación se ha traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

Las defensas contra prompt injection a menudo parecen apoyarse sobre terreno inestable.

Añades un system prompt más fuerte. Añades un filtro. Pones unas cuantas listas de अनुमति. Y esperas que la siguiente entrada extraña no rompa las suposiciones.

Por eso **FIDES** es interesante.

La parte fuerte de la historia es que mueve la seguridad hacia algo más determinista:

- etiquetas sobre el contenido
- propagación de las etiquetas a través del flujo de trabajo
- aplicación mediante middleware antes de que se ejecuten herramientas privilegiadas
- límites de política claros sobre lo que el contexto no confiable puede influir

## El artículo original es directo en el buen sentido

Empieza diciendo que prompt injection es "**el riesgo número 1 en el OWASP LLM Top 10**".

Bien.

Me gusta ese tipo de franqueza aquí, porque demasiados equipos siguen tratando la seguridad de agentes como si fuera una preocupación futura en lugar de un problema actual de diseño de runtime.

Y el artículo sigue con un contraste práctico muy claro: la mayoría de las defensas actuales son heurísticas, mientras que FIDES intenta llevar el sistema hacia la política y la aplicación.

Ese es exactamente el cambio correcto.

## Qué lo hace más convincente que otro whitepaper de seguridad

Muchos textos sobre seguridad de IA se quedan en lo abstracto.

Este artículo hace algo mejor. Recorre un ejemplo muy concreto: un agente de triage de issues de GitHub, un cuerpo de issue malicioso, una lectura de archivo privilegiada y un intento de filtrar un comentario público.

Eso es útil porque aterriza toda la discusión en un flujo de trabajo real.

Y una vez que ves ese escenario, el valor de los controles deterministas se vuelve mucho más fácil de entender.

## La idea clave no es "haz que el modelo sea más listo"

Lo más importante aquí es que FIDES no le pide al modelo que se vuelva mágicamente mejor detectando ataques.

Está cambiando el contrato del runtime.

Eso significa:

- se etiquetan los contenidos
- las etiquetas se propagan
- las herramientas declaran qué aceptan
- el middleware bloquea los caminos inseguros antes de la ejecución

Ese es un enfoque mucho más sano.

Porque, una vez que el agente puede llamar a herramientas con consecuencias reales, la seguridad no puede depender solo de si el modelo tuvo un buen día.

## Mi opinión

Esta es exactamente la clase de dirección en seguridad de agentes que quiero ver más a menudo.

No "confía en que el modelo ignore las instrucciones malas", sino "construye la valla de política dentro del runtime".

Ese es un modelo mucho más sano.

Y si los frameworks de agentes quieren ser tomados en serio en producción, necesitarán más historias como esta.

Publicación original: [Stop prompt injection from hijacking your agent, new security capabilities now released within Agent Framework](https://devblogs.microsoft.com/agent-framework/fides/)