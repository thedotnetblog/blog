---
title: "Agent Skills en Visual Studio: Enseña a Copilot Cómo Trabaja Tu Equipo"
date: 2026-06-05
author: "Emiliano Montesdeoca"
description: "Visual Studio ahora soporta Agent Skills — conjuntos de instrucciones reutilizables que enseñan a Copilot los flujos de trabajo específicos, estándares de código y convenciones de tu equipo. Defínelos una vez, aplícalos automáticamente."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Agents
  - Developer Tools
---

Una de las frustraciones persistentes con los asistentes de codificación de IA: conocen bien la programación general pero no conocen las convenciones específicas de *tu* equipo, tus APIs internas o tus patrones preferidos. En cada sesión, vuelves a explicar el contexto. Agent Skills en Visual Studio está diseñado para solucionar esto.

## Qué Son los Agent Skills

Conjuntos de instrucciones reutilizables — definidos en archivos `SKILL.md` — que enseñan a los agentes de Copilot cómo manejar tareas específicas. Define un skill para "cómo ejecutar nuestro pipeline de build", "cómo generar boilerplate para nuestra capa de servicio" o "nuestra lista de verificación de revisión de código". El agente aplica el skill automáticamente cuando es relevante.

Esto no es un concepto nuevo (`.github/copilot-instructions.md` existe desde hace un tiempo), pero la integración de Visual Studio los convierte en objetos de primera clase con una interfaz de descubrimiento.

## Creación de Skills en Visual Studio

El flujo de interfaz integrado: haz clic en el ícono de herramientas en Copilot Chat, abre el panel de skills, haz clic en `+`. Eliges el alcance global (personal) o de solución, seleccionas un nombre y Visual Studio genera una plantilla. El modo Agente de Copilot puede entonces ayudarte a completar la plantilla — usa el agente para escribir el skill para el agente.

Actualmente en el canal Insiders, próximamente en la versión Release.

También puedes crear skills manualmente:

```
.github/
  skills/
    github-issues/
      SKILL.md
      templates/
        bug-report.md
    code-review/
      SKILL.md
      checklist.md
```

## Ubicaciones de Descubrimiento

Los skills se descubren automáticamente desde rutas estándar:

**A nivel de solución (compartido via repo):** `.github/skills/`, `.claude/skills/`, `.agents/skills/`

**Global/personal (tu perfil de usuario, disponible en todas partes):** `~/.copilot/skills/`, `~/.agents/skills/`

El soporte multi-ubicación significa que la misma convención funciona con GitHub Copilot, Claude Code y otros frameworks de agentes — define tus skills una vez, úsalos en todas partes.

## El Formato

Los skills siguen el formato [agentskills.io/specification](https://agentskills.io/specification) — una especificación basada en Markdown que es tanto legible por humanos como analizable por máquinas. Puedes incluir scripts, plantillas y ejemplos junto al `SKILL.md`.

## Valor Práctico

El poder real no está en las características individuales — está en la combinación de skills compartidos por el equipo (via `.github/skills/`) y skills personales (via `~/.agents/skills/`). Los skills del equipo codifican cómo hace las cosas tu organización. Los skills personales codifican cómo trabajas tú específicamente. El agente obtiene ambos contextos automáticamente.

Para las organizaciones que ya usan Copilot intensivamente, este es un paso significativo hacia hacer que la herramienta sea realmente consciente de las convenciones específicas de tu base de código en lugar de dar consejos genéricos.

Post original: [Agent Skills in Visual Studio: Teach Copilot How Your Team Works](https://devblogs.microsoft.com/visualstudio/agent-skills-in-visual-studio/)
