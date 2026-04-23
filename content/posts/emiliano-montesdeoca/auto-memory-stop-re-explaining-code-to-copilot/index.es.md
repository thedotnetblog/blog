---
title: "¿68 Minutos al Día Re-Explicando Código a Copilot? Hay una Solución"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "El 'context rot' es real — tu agente de IA se pierde después de 30 turnos y pagas el impuesto de la compactación cada hora. auto-memory le da a GitHub Copilot CLI una memoria quirúrgica sin quemar miles de tokens."
tags:
  - "GitHub Copilot"
  - "Developer Productivity"
  - "MCP"
  - "AI Foundry"
  - "AI Apps"
  - "Agentic DevOps"
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí](https://thedotnetblog.com/posts/emiliano-montesdeoca/auto-memory-stop-re-explaining-code-to-copilot/).*

¿Conoces ese momento en que tu sesión de Copilot llega al `/compact` y el agente olvida completamente lo que estabas haciendo? Pasas los siguientes cinco minutos re-explicando la estructura de archivos, el test fallido, los tres enfoques que ya intentaste. Y luego vuelve a pasar. Y otra vez.

Desi Villanueva lo midió: **68 minutos al día** — solo en re-orientación. No escribiendo código. No revisando PRs. Solo poniéndole al día a la IA en cosas que ya sabía.

Resulta que hay una razón concreta por la que esto pasa, y una solución concreta.

## La Mentira de la Ventana de Contexto

Tu agente viene con un número grande en la caja. 200K tokens. Suena masivo. En la práctica es un techo, no una garantía.

Aquí está la matemática real:

- 200K de contexto total
- Menos ~65K para herramientas MCP cargadas al inicio (~33%)
- Menos ~10K para archivos de instrucciones como `AGENTS.md` o `copilot-instructions.md`

Eso te deja aproximadamente **125K antes de escribir una sola palabra**. Y empeora — los LLMs no se degradan de forma gradual al llenarse el contexto. Tienen un tope al llegar al 60% de capacidad. El modelo empieza a perder cosas mencionadas hace 30 turnos, contradice respuestas anteriores, alucina nombres de archivos que declaró con confianza hace 10 minutos. La industria llama a esto el problema del "lost in the middle".

Límite efectivo: **45K tokens** antes de que la calidad se degrade. Eso son tal vez 20-30 turnos de conversación activa antes de que el agente empiece a derivar. Por eso estás usando `/compact` cada 45 minutos — no porque hayas llenado 200K tokens, sino porque el modelo ya está "podrido" a los 120K.

## El Impuesto de la Compactación

Cada `/compact` te cuesta el estado de flujo. Llevas 30 minutos en una sesión de depuración. El agente conoce la estructura de archivos, el test fallido, la hipótesis. Luego llega la advertencia.

- Ignorarla → el agente se vuelve progresivamente más tonto, alucina el estado anterior
- Ejecutar `/compact` → el agente tiene un resumen de 2 párrafos de una investigación de 30 minutos

De cualquier manera pierdes. De cualquier manera estás narrando tu propio proyecto como si fuera un empleado nuevo en su primer día.

La parte cruel: **la memoria ya existe**. Copilot CLI escribe cada sesión en una base de datos SQLite local en `~/.copilot/session-store.db` — cada archivo tocado, cada turno, cada checkpoint. Todo está en el disco. El agente simplemente no puede leerlo.

## auto-memory: Una Capa de Recall, No un Sistema de Memoria

Esa es la idea central detrás de [auto-memory](https://github.com/dezgit2025/auto-memory): no construyas un nuevo sistema de memoria — construye una capa de consulta de solo lectura sobre el que ya existe.

```bash
pip install auto-memory
```

~1.900 líneas de Python. Cero dependencias. Se instala en 30 segundos.

En lugar de inundar el contexto con resultados de grep, le das al agente acceso quirúrgico a lo que realmente importa:

| Operación | Tokens | Qué obtienes |
|-----------|--------|--------------|
| `grep -r "auth" src/` | ~5.000–10.000 | 500 resultados, la mayoría irrelevantes |
| `find . -name "*.py"` | ~2.000 | Todos los archivos Python, sin contexto |
| Re-orientación del agente | ~2.000 | Tú explicando lo que ya debería saber |
| **`auto-memory files --json --limit 10`** | **~50** | **Los 10 archivos que tocaste ayer** |

Una mejora de 200x. El agente se salta la excavación arqueológica y va directo a lo que importa.

## ¿Por Qué Importa Esto para Desarrolladores .NET?

Si usas GitHub Copilot CLI para trabajo con .NET — scaffolding de servicios, depuración de queries EF Core, iterando en componentes Blazor — el problema del context rot golpea igual de fuerte. Soluciones complejas con múltiples proyectos y librerías compartidas son exactamente el tipo de código donde el agente pierde el hilo más rápido.

## Resumiendo

El context rot es una restricción arquitectónica real, no un bug que se parchará. auto-memory lo soluciona dándole a tu agente un mecanismo de recall barato y preciso en lugar de re-exploración costosa y ruidosa. Si haces desarrollo serio asistido por IA con GitHub Copilot CLI, vale la pena el install de 30 segundos.

Échale un vistazo: [auto-memory en GitHub](https://github.com/dezgit2025/auto-memory). Post original de Desi Villanueva: [I Wasted 68 Minutes a Day Re-Explaining My Code](https://devblogs.microsoft.com/all-things-azure/i-wasted-68-minutes-a-day-re-explaining-my-code-then-i-built-auto-memory/).
