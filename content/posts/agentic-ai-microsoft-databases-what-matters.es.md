---
title: "SQL MCP Server, Copilot en SSMS y un Database Hub con agentes de IA: Lo que realmente importa de SQLCon 2026"
date: 2026-03-28
author: "Emiliano Montesdeoca"
description: "Microsoft soltó un montón de anuncios de bases de datos en SQLCon 2026. Esto es lo que realmente importa si estás construyendo apps con IA sobre Azure SQL."
tags:
  - azure
  - ai
  - sql
  - databases
  - mcp
---

Microsoft acaba de arrancar [SQLCon 2026 junto con FabCon en Atlanta](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/), y hay mucho que desempacar. El anuncio original cubre de todo, desde planes de ahorro hasta funciones de compliance empresarial. Yo me voy a saltar las diapositivas de precios enterprise y enfocarme en lo que importa si eres un desarrollador construyendo cosas con Azure SQL e IA.

## SQL MCP Server está en public preview

Este es el titular para mí. Azure SQL Database Hyperscale ahora tiene un **SQL MCP Server** en public preview que te permite conectar de forma segura tus datos SQL a agentes de IA y Copilots usando el [Model Context Protocol](https://modelcontextprotocol.io/).

Si has estado siguiendo la ola de MCP — y honestamente, es difícil no verla ahora mismo — esto es importante. En lugar de construir pipelines de datos personalizados para alimentar a tus agentes de IA con contexto de tu base de datos, tienes un protocolo estandarizado para exponer datos SQL directamente. Tus agentes pueden consultar, razonar y actuar sobre información de base de datos en tiempo real.

Para los que estamos construyendo agentes de IA con Semantic Kernel o el Microsoft Agent Framework, esto abre un camino de integración limpio. ¿Tu agente necesita verificar inventario? ¿Buscar un registro de cliente? ¿Validar un pedido? MCP le da una forma estructurada de hacerlo sin que tengas que escribir código a medida para cada escenario.

## GitHub Copilot en SSMS 22 ya está en GA

Si pasas algo de tiempo en SQL Server Management Studio — y seamos honestos, la mayoría todavía lo hacemos — GitHub Copilot ya está disponible de forma general en SSMS 22. La misma experiencia de Copilot que ya usas en VS Code y Visual Studio, pero para T-SQL.

El valor práctico es directo: asistencia por chat para escribir queries, refactorizar stored procedures, resolver problemas de rendimiento y manejar tareas de administración. Nada revolucionario en concepto, pero tenerlo ahí mismo en SSMS significa que no necesitas cambiar de contexto a otro editor solo para obtener ayuda de IA con tu trabajo de base de datos.

## Los índices vectoriales recibieron una mejora seria

Azure SQL Database ahora tiene índices vectoriales más rápidos y capaces con soporte completo de insert, update y delete. Eso significa que tus datos vectoriales se mantienen actualizados en tiempo real — sin necesidad de reindexar por lotes.

Esto es lo nuevo:
- **Cuantización** para tamaños de índice más pequeños sin perder demasiada precisión
- **Filtrado iterativo** para resultados más precisos
- **Integración más ajustada con el optimizador de queries** para rendimiento predecible

Si estás haciendo retrieval-augmented generation (RAG) con Azure SQL como tu almacén vectorial, estas mejoras son directamente útiles. Puedes mantener tus vectores junto con tus datos relacionales en la misma base de datos, lo que simplifica tu arquitectura significativamente comparado con ejecutar una base de datos vectorial separada.

Las mismas mejoras vectoriales también están disponibles en SQL database en Fabric, ya que ambos corren sobre el mismo motor SQL por debajo.

## Database Hub en Fabric: gestión agéntica

Este es más orientado al futuro, pero es interesante. Microsoft anunció el **Database Hub en Microsoft Fabric** (acceso anticipado), que te da una vista unificada de Azure SQL, Cosmos DB, PostgreSQL, MySQL y SQL Server vía Arc.

El ángulo interesante no es solo la vista unificada — es el enfoque agéntico para la gestión. Agentes de IA monitorean continuamente tu estate de bases de datos, te muestran qué cambió, explican por qué importa y sugieren qué hacer. Es un modelo human-in-the-loop donde el agente hace el trabajo pesado y tú tomas las decisiones.

Para equipos que gestionan más de un puñado de bases de datos, esto podría genuinamente reducir el ruido operacional. En lugar de saltar entre portales y revisar métricas manualmente, el agente te trae la señal.

## Qué significa esto para desarrolladores .NET

El hilo que conecta todos estos anuncios es claro: Microsoft está integrando agentes de IA en cada capa del stack de bases de datos. No como un truco, sino como una capa práctica de herramientas.

Si estás construyendo apps .NET respaldadas por Azure SQL, esto es lo que yo haría:

1. **Prueba el SQL MCP Server** si estás construyendo agentes de IA. Es la forma más limpia de darles acceso a base de datos sin plomería personalizada.
2. **Activa Copilot en SSMS** si no lo has hecho — ganancia de productividad gratis para el trabajo diario con SQL.
3. **Investiga los índices vectoriales** si estás haciendo RAG y actualmente tienes un almacén vectorial separado. Consolidar en Azure SQL significa un servicio menos que gestionar.

## Para cerrar

El anuncio completo tiene más — planes de ahorro, asistentes de migración, funciones de compliance — pero la historia para desarrolladores está en el MCP Server, las mejoras vectoriales y la capa de gestión agéntica. Estas son las piezas que cambian cómo construyes, no solo cómo presupuestas.

Revisa el [anuncio completo de Shireesh Thota](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) para la foto completa, y [regístrate para el acceso anticipado del Database Hub](https://aka.ms/database-hub) si quieres probar la nueva experiencia de gestión.
