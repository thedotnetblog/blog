---
title: "MAESTRO, Defense-in-Depth y Por Qué SQL Server Ahora Es un Límite de Seguridad para la IA"
date: 2026-06-04
author: "Emiliano Montesdeoca"
description: "La IA agéntica introduce amenazas para las que los modelos STRIDE tradicionales no fueron diseñados. Así es como Microsoft SQL se mapea al framework MAESTRO para proporcionar un límite de ejecución gobernado."
tags:
  - Azure SQL
  - AI
  - Security
  - Agentic AI
  - SQL Server 2025
---

Los modelos de amenazas de seguridad se construyen sobre suposiciones sobre quién o qué está haciendo las solicitudes. STRIDE asume actores humanos que interactúan con sistemas a través de interfaces definidas. Los agentes de IA no funcionan de esa manera.

## STRIDE No Fue Diseñado para Agentes de IA

Los sistemas agénticos operan de forma autónoma, encadenan herramientas a través de llamadas a APIs, toman decisiones sobre qué datos recuperar y qué acciones ejecutar, y pueden recibir instrucciones de múltiples fuentes — prompts del usuario, resultados de herramientas, datos recuperados. El modelo de amenaza STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) no captura adecuadamente vectores de ataque específicos de agentes como la inyección de prompts, el envenenamiento de contexto o el abuso de herramientas.

La Cloud Security Alliance publicó el framework MAESTRO específicamente para el riesgo de agentes de IA.

## El Framework MAESTRO

MAESTRO organiza el riesgo de IA agéntica en siete capas:

1. **Foundation Models** — los LLMs subyacentes y sus vulnerabilidades de entrenamiento
2. **Data Operations** — recuperación, almacenamiento y manipulación de datos
3. **Agent Frameworks** — el middleware de orquestación y coordinación de agentes
4. **Deployment & Infrastructure** — donde se ejecutan los agentes y cómo se configuran
5. **Evaluation & Observability** — monitoreo del comportamiento de los agentes en el tiempo
6. **Security & Compliance** — controles de acceso, auditoría y cumplimiento normativo
7. **Agent Ecosystem** — cómo los agentes interactúan entre sí y con herramientas externas

Cada capa tiene vectores de ataque específicos que las controles de seguridad tradicionales no abordan directamente.

## Microsoft SQL Como Límite de Ejecución Gobernado

SQL Server 2025 se mapea a las capas de MAESTRO de formas concretas:

**Capa de Operaciones de Datos**: `AI_GENERATE_EMBEDDINGS` integrado en T-SQL mantiene las operaciones de vectores dentro del límite gobernado de la base de datos. Los datos no necesitan salir al servicio del modelo para el procesamiento de embeddings.

**Capas de Seguridad y Compliance**: La seguridad a nivel de fila (RLS) y el enmascaramiento dinámico de datos (DDM) se aplican independientemente de cómo llegó la solicitud — sea de un usuario humano o un agente de IA. El agente no puede eludir controles que son impuestos por la base de datos misma.

**Capa de Agent Frameworks**: Los procedimientos almacenados sirven como límites de herramientas. En lugar de dar a los agentes acceso SQL arbitrario, defines las operaciones permitidas como procedimientos y los expones como herramientas de agente. Las consultas parametrizadas previenen la inyección a nivel de ejecución.

**Capa de Evaluation & Observability**: El registro de auditoría y Query Store capturan lo que cada agente ejecutó realmente — no solo lo que se le pidió que hiciera. Esta trazabilidad es crítica para investigaciones de incidentes en sistemas agénticos donde la atribución es compleja.

## Defense-in-Depth para IA Agéntica

El principio se mantiene igual que en la seguridad tradicional: ningún control único es suficiente. Lo que cambia es qué controles importan más para los agentes:

**Reducir el radio de impacto**: los límites de herramientas de procedimientos almacenados significan que un agente comprometido solo puede ejecutar operaciones predefinidas. No puede pivotar a consultas arbitrarias.

**Observabilidad**: debes ser capaz de responder "¿qué hizo exactamente este agente?" después de un incidente. Los sistemas de IA agéntica sin trazabilidad a nivel de base de datos tienen puntos ciegos que la registración de aplicaciones no cubre.

**Ejecución restringida**: la parametrización, RLS y DDM son activos de seguridad independientemente de si el llamador es humano. No los debilites para acomodar agentes.

**Responsabilidad**: el registro de auditoría de SQL Server crea un registro de quién (qué agente, usando qué credenciales) ejecutó qué en qué momento. Esto importa cuando los sistemas agénticos toman acciones con consecuencias reales en el mundo.

SQL Server 2025 no fue construido para resolver el riesgo agéntico en abstracto — fue construido para ser una base de datos relacional. Pero la gobernanza que hace a una base de datos empresarial confiable resulta ser exactamente lo que hace que un límite de ejecución de agentes sea seguro.

Post original: [Microsoft SQL Security Across the MAESTRO Stack](https://devblogs.microsoft.com/azure-sql/microsoft-sql-security-across-the-maestro-stack-building-secure-agentic-ai-with-defense-in-depth/)
