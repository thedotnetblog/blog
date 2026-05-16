---
title: "Eliminando el Trabajo Tedioso de la Migración con Agentic Platform Engineering"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape recorre la migración de un despliegue real de AWS Terraform a Azure Bicep — extrayendo la intención del despliegue y remapeando la arquitectura en lugar de hacer una conversión sintáctica 1:1."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — un recorrido de Git-Ape (herramienta git de ingeniería de plataformas agéntica) que migra un repositorio Terraform real de AWS a Azure, centrándose en la extracción de intención en lugar de una conversión línea por línea.

## La entrada: contoso-migration

La fuente es un proyecto Terraform real (`contoso-migration`) que despliega una aplicación Next.js en AWS — EC2 para cómputo, ALB para balanceo de carga, S3 para artefactos y claves IAM para identidad. Costo: ~34 $/mes. El objetivo no es reproducir la misma infraestructura en Azure; es descubrir qué intenta hacer realmente el despliegue y reconstruirlo con servicios nativos de Azure.

## Paso 1: Validación y autenticación

Git-Ape comienza validando todas las herramientas CLI requeridas — `az`, `aws`, `gh`, `jq`, `git` — y confirmando las sesiones de autenticación activas antes de tocar nada. Sin ejecuciones parciales.

## Paso 2: Extracción de intención

El agente lee todo el repositorio fuente a través de la API de GitHub y extrae la intención de despliegue: tiempo de ejecución (Node.js), tipo de cómputo, patrón de ingress, manejo de artefactos, modelo de identidad, red y monitoreo. Este es el paso clave — está construyendo un modelo semántico de lo que hace el despliegue, no qué palabras clave de Terraform utiliza.

## Paso 3: Mapeo de servicios

Los servicios de AWS se mapean a equivalentes de Azure:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → Balanceo de carga integrado de App Service
- Roles/claves IAM → Managed Identity
- Terraform → Bicep + GitHub Actions

## Paso 4: Agente crítico

Antes de generar la salida, se ejecuta un agente crítico que detecta dos problemas bloqueantes:

1. **Anti-patrón de build al inicio** — el Terraform original ejecutaba `npm install && npm run build` en EC2 al arrancar. Solución: construir en CI, desplegar un artefacto listo.
2. **Blob Storage innecesario** — S3 se usaba para la preparación de artefactos que podría eliminarse con CI/CD adecuado. El agente crítico lo eliminó por completo.

## Paso 5: Salida generada

El resultado son ~80 líneas de Bicep en lugar de las 200+ líneas originales de Terraform. El agente creó un nuevo repositorio GitHub con `infra/main.bicep` y `.github/workflows/deploy.yml` y eliminó todos los archivos específicos de AWS.

## Comparación de postura de seguridad

La migración también produjo una mejora significativa de seguridad:

| AWS original | Salida Azure |
|---|---|
| Solo HTTP | Solo HTTPS, TLS 1.2 |
| SSH abierto a 0.0.0.0/0 | Sin exposición SSH |
| Claves de acceso IAM | OIDC + Managed Identity |
| Sin monitoreo | Application Insights |

Costo: ~13 $/mes vs los 34 $/mes originales.

## Qué lo diferencia de un convertidor de sintaxis

El paso del agente crítico es lo que separa esto de una traducción mecánica. Detectó patrones que habrían funcionado en AWS pero serían incorrectos en Azure — y los corrigió en lugar de replicarlos. La salida no es "AWS en sintaxis de Azure"; es un despliegue nativo de Azure que logra el mismo objetivo de manera más limpia.

Consulta el [recorrido completo](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) para ver la traza completa del agente y los archivos generados.
