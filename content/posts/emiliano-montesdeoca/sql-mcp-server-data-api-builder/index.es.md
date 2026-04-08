---
title: "SQL MCP Server — La forma correcta de darle acceso a bases de datos a los agentes de IA"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "SQL MCP Server de Data API builder da a los agentes de IA acceso seguro y determinista a bases de datos sin exponer esquemas ni depender de NL2SQL. RBAC, caché, soporte multi-base de datos — todo incluido."
tags:
  - azure-sql
  - mcp
  - data-api-builder
  - ai
  - azure
  - databases
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "sql-mcp-server-data-api-builder.md" >}}).*

Seamos honestos: la mayoría de los servidores MCP de bases de datos disponibles hoy son aterradores. Toman una consulta en lenguaje natural, generan SQL al vuelo y lo ejecutan contra tus datos de producción. ¿Qué podría salir mal? (Todo. Todo podría salir mal.)

El equipo de Azure SQL acaba de [presentar SQL MCP Server](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/), y toma un enfoque fundamentalmente diferente. Construido como una característica de Data API builder (DAB) 2.0, da a los agentes de IA acceso estructurado y determinista a operaciones de base de datos — sin NL2SQL, sin exponer tu esquema, y con RBAC completo en cada paso.

## ¿Por qué no NL2SQL?

Esta es la decisión de diseño más interesante. Los modelos no son deterministas, y las consultas complejas son las más propensas a producir errores sutiles. Las consultas exactas que los usuarios esperan que la IA genere son también las que necesitan más escrutinio cuando se producen de forma no determinista.

En su lugar, SQL MCP Server usa un enfoque **NL2DAB**. El agente trabaja con la capa de abstracción de entidades de Data API builder y su constructor de consultas integrado para producir T-SQL preciso y bien formado de manera determinista. Mismo resultado para el usuario, pero sin el riesgo de JOINs alucinados o exposición accidental de datos.

## Siete herramientas, no setecientas

SQL MCP Server expone exactamente siete herramientas DML, sin importar el tamaño de la base de datos:

- `describe_entities` — descubrir entidades y operaciones disponibles
- `create_record` — insertar filas
- `read_records` — consultar tablas y vistas
- `update_record` — modificar filas
- `delete_record` — eliminar filas
- `execute_entity` — ejecutar procedimientos almacenados
- `aggregate_records` — consultas de agregación

Esto es inteligente porque las ventanas de contexto son el espacio de pensamiento del agente. Inundarlas con cientos de definiciones de herramientas deja menos espacio para el razonamiento. Siete herramientas fijas mantienen al agente enfocado en *pensar* en lugar de *navegar*.

Cada herramienta puede habilitarse o deshabilitarse individualmente:

```json
"runtime": {
  "mcp": {
    "enabled": true,
    "path": "/mcp",
    "dml-tools": {
      "describe-entities": true,
      "create-record": true,
      "read-records": true,
      "update-record": true,
      "delete-record": true,
      "execute-entity": true,
      "aggregate-records": true
    }
  }
}
```

## Empezando en tres comandos

```bash
dab init \
  --database-type mssql \
  --connection-string "@env('sql_connection_string')"

dab add Customers \
  --source dbo.Customers \
  --permissions "anonymous:*"

dab start
```

Eso es un SQL MCP Server funcionando y exponiendo tu tabla Customers. La capa de abstracción de entidades significa que puedes crear alias para nombres y columnas, limitar campos por rol, y controlar exactamente lo que ven los agentes — sin exponer detalles internos del esquema.

## La historia de seguridad es sólida

Aquí es donde la madurez de Data API builder da frutos:

- **RBAC en cada capa** — cada entidad define qué roles pueden leer, crear, actualizar o eliminar, y qué campos son visibles
- **Integración con Azure Key Vault** — cadenas de conexión y secretos gestionados de forma segura
- **Microsoft Entra + OAuth personalizado** — autenticación de nivel producción
- **Content Security Policy** — los agentes interactúan a través de un contrato controlado, no SQL crudo

La abstracción del esquema es particularmente importante. Los nombres internos de tus tablas y columnas nunca se exponen al agente. Defines entidades, alias y descripciones que tienen sentido para la interacción con IA — no tu diagrama ERD de la base de datos.

## Multi-base de datos y multi-protocolo

SQL MCP Server soporta Microsoft SQL, PostgreSQL, Azure Cosmos DB y MySQL. Y como es una característica de DAB, obtienes endpoints REST, GraphQL y MCP simultáneamente desde la misma configuración. Mismas definiciones de entidades, mismas reglas RBAC, misma seguridad — en los tres protocolos.

La auto-configuración en DAB 2.0 puede incluso inspeccionar tu base de datos y construir la configuración dinámicamente, si te resulta cómodo menos abstracción para prototipado rápido.

## Mi opinión

Así es como debería funcionar el acceso empresarial a bases de datos para agentes de IA. No "hey LLM, escríbeme algo de SQL y YOLO contra producción." En su lugar: una capa de entidades bien definida, generación determinista de consultas, RBAC en cada paso, caché, monitoreo y telemetría. Es aburrido de la mejor manera posible.

Para desarrolladores .NET, la historia de integración es limpia — DAB es una herramienta .NET, el MCP Server se ejecuta como contenedor, y funciona con Azure SQL, que la mayoría ya estamos usando. Si estás construyendo agentes de IA que necesitan acceso a datos, empieza aquí.

## Para cerrar

SQL MCP Server es gratuito, de código abierto y se ejecuta en cualquier lugar. Es el enfoque prescriptivo de Microsoft para dar acceso seguro a bases de datos a los agentes de IA. Consulta el [post completo](https://devblogs.microsoft.com/azure-sql/introducing-sql-mcp-server/) y la [documentación](https://aka.ms/sql/mcp) para empezar.
