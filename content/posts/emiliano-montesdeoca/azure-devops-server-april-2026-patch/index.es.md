---
title: "Azure DevOps Server Parche Abril 2026 — Corrección en Completado de PRs y Actualizaciones de Seguridad"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server recibe el Parche 3 con una corrección para fallos en el completado de PRs, validación mejorada en cierre de sesión y restauración de conexiones PAT con GitHub Enterprise Server."
tags:
  - azure-devops
  - devops
  - patches
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "azure-devops-server-april-2026-patch.md" >}}).*

Aviso rápido para equipos que ejecutan Azure DevOps Server en sus propios servidores: Microsoft lanzó el [Parche 3 de abril 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) con tres correcciones específicas.

## Qué se corrigió

- **Fallos en el completado de pull requests** — una excepción de referencia nula durante el auto-completado de work items podía hacer que los merges de PRs fallaran. Si te topaste con errores aleatorios al completar PRs, esta es probablemente la causa
- **Validación en la redirección de cierre de sesión** — se mejoró la validación durante el cierre de sesión para prevenir posibles redirecciones maliciosas. Esta es una corrección de seguridad que vale la pena aplicar pronto
- **Conexiones PAT con GitHub Enterprise Server** — la creación de conexiones con Personal Access Token hacia GitHub Enterprise Server estaba rota, ahora se restauró

## Cómo actualizar

Descarga el [Parche 3](https://aka.ms/devopsserverpatch3) y ejecuta el instalador. Para verificar que el parche se aplicó:

```bash
<patch-installer>.exe CheckInstall
```

Si estás ejecutando Azure DevOps Server en tus propias instalaciones, Microsoft recomienda encarecidamente mantenerse en el último parche tanto por seguridad como por fiabilidad. Consulta las [notas de la versión](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026) para todos los detalles.
