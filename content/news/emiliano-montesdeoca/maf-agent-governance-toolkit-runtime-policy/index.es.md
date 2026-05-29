---
title: "Construir Agentes Es la Parte Fácil — Ejecutarlos de Forma Segura Es la Parte Difícil"
date: 2026-05-29
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework y Agent Governance Toolkit se unen para aplicar políticas en tiempo de ejecución, gobernar las llamadas a herramientas y proporcionar registros de auditoría encadenados con Merkle — sin tocar los prompts del agente."
tags:
  - Agent Framework
  - AI
  - .NET
  - Security
  - Governance
  - A2A
---

Hay un patrón en el desarrollo de agentes de IA que he empezado a llamar "arrepentimiento de demo". El agente funciona genial en las demos. Luego alguien pregunta: ¿qué pasa si llama a la herramienta equivocada? ¿Y si accede a datos que no debería? ¿Quién auditó eso?

Microsoft Agent Framework te respalda para construir y orquestar. Agent Governance Toolkit (AGT) cubre la parte posterior — gobernanza, aplicación de políticas y auditabilidad en tiempo de ejecución.

## Qué Hace Realmente Cada Proyecto

**Microsoft Agent Framework (MAF)** te proporciona el modelo de programación: flujos de trabajo multi-agente, interoperabilidad del protocolo A2A, hooks de middleware, memoria y alojamiento administrado a través de Foundry Agent Service. Maneja la seguridad de contenido a nivel de entrada/salida del modelo.

**Agent Governance Toolkit (AGT)** se conecta a ese mismo pipeline de middleware para gobernar *acciones*. Cada llamada a herramienta, acceso a recursos y mensaje entre agentes se evalúa contra la política antes de la ejecución. Sobrecarga de submilisegundos. Sin sidecars, sin proxies, sin prompts modificados.

```
Acción del Agente --> Verificación de Política --> Permitir / Denegar --> Registro de Auditoría    (< 0.1 ms)
```

Capas diferentes, cobertura completa, un pipeline.

## Conectarse Es Solo Agregar Middleware

En Python, AGT se agrega al mismo parámetro `middleware` que usarías para registro o filtros de contenido:

```python
agent = Agent(
    client=OpenAIChatClient(model="gpt-5.3"),
    name="Contoso Loan Officer",
    instructions="You are a governed loan assistant.",
    tools=[check_credit_score, get_loan_rates, approve_small_loan],
    middleware=[
        AuditTrailMiddleware(audit_log=audit_log, agent_did="loan-agent"),
        GovernancePolicyMiddleware(evaluator=evaluator, audit_log=audit_log),
        CapabilityGuardMiddleware(allowed_tools=["check_credit_score", "get_loan_rates"]),
        RogueDetectionMiddleware(detector=detector, agent_id="loan-agent"),
    ],
)
```

En .NET, el mismo patrón a través de `.Use()`:

```csharp
var agent = builder.BuildAIAgent(model: "gpt-5.3")
    .Use(new GovernancePolicyMiddleware(evaluator))
    .Use(new CapabilityGuardMiddleware(allowedTools))
    .Use(new AuditTrailMiddleware(auditLog));
```

Mismo agente, misma orquestación, mismas herramientas. AGT agrega capacidades de gobernanza sin tocar la lógica del agente.

## Lo Que Obtienes

- **GovernancePolicyMiddleware** — evalúa cada acción contra reglas de política declarativas
- **CapabilityGuardMiddleware** — lista de permitidos qué herramientas tiene permiso de llamar un agente (la herramienta `approve_small_loan` no está en la lista de permitidos arriba — deliberadamente)
- **RogueDetectionMiddleware** — detecta patrones de comportamiento anómalo en tiempo de ejecución
- **AuditTrailMiddleware** — registro de auditoría encadenado con Merkle para que cada acción sea criptográficamente resistente a manipulaciones

Este último importa para el cumplimiento normativo. Una cadena Merkle significa que si alguien modifica el registro, la cadena se rompe. La auditoría es la evidencia.

## Cinco Escenarios de la Industria

El repositorio de AGT incluye cinco escenarios completos de extremo a extremo: servicios financieros (oficial de préstamos), atención médica (datos de pacientes), legal (revisión de contratos), gobierno (servicios al ciudadano) y manufactura (control de calidad). Cada uno combina agentes MAF reales con middleware de gobernanza AGT real.

Estas no son demos de juguete. Son el tipo de escenarios donde realmente necesitarías gobernanza en producción.

## Conclusión

Si estás construyendo agentes que tocan datos reales, toman decisiones con consecuencias, o se ejecutan sin supervisión en producción — la gobernanza no es opcional. La combinación de MAF + AGT te brinda el stack completo: constrúyelo con Agent Framework, govírnalo con AGT.

Ambos proyectos son de código abierto. El artículo original tiene enlaces a los ejemplos de código completos.

Publicación original: [Governance at the Speed of Agents: Microsoft Agent Framework and Agent Governance Toolkit, Better Together](https://devblogs.microsoft.com/agent-framework/governance-at-the-speed-of-agents-microsoft-agent-framework-and-agent-governance-toolkit-better-together/)
