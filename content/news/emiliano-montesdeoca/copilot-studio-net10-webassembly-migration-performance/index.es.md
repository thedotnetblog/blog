---
title: "Cómo Copilot Studio Migró a .NET 10 WebAssembly y Se Volvió un 20% Más Rápido"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "Las mejoras de .NET 10 WASM no son solo para proyectos nuevos. Aquí está lo que Copilot Studio midió después de actualizar desde .NET 8: fingerprinting automático, WasmStripILAfterAOT por defecto y números reales de rendimiento de ejecución."
tags:
  - .NET
  - .NET 10
  - WebAssembly
  - Blazor
  - Performance
---

El equipo de Copilot Studio hizo algo sobre lo que todos los desarrolladores Blazor WASM han sentido curiosidad: actualizaron una aplicación de producción de .NET 8 a .NET 10 y midieron los resultados. La publicación comparte números específicos, algo que es raro y genuinamente útil.

## La Actualización Fue Aburrida (Eso es Bueno)

Actualizar el framework de destino, actualizar las referencias de paquetes, corregir los cambios disruptivos. Eso es todo. La compilación de .NET 10 ahora está ejecutándose en producción. La migración en sí no fue la parte interesante — los cambios en .NET 10 sí lo son.

## Fingerprinting Automático de Activos

Anteriormente, distribuir una aplicación WASM significaba escribir scripts personalizados para renombrar los activos publicados con hashes SHA256 para la invalidación de caché. Copilot Studio tenía un script PowerShell haciendo exactamente esto — renombrar archivos, inyectar atributos `integrity` en el cargador JavaScript, gestionar todo manualmente.

En .NET 10, todo eso está integrado. Los activos publicados se marcan automáticamente con fingerprint, se importan directamente desde `dotnet.js` y se validan con integridad sin intervención manual. El equipo eliminó el script de renombrado.

Pequeño cambio en alcance, reducción significativa de complejidad.

## WasmStripILAfterAOT Ahora Está Activado por Defecto

En .NET 8, eliminar IL de los ensamblados compilados AOT era opt-in. En .NET 10 es el valor predeterminado. Después de la compilación AOT, el bytecode IL original se elimina de la salida — no se necesita en tiempo de ejecución, y mantenerlo inflaba el tamaño del paquete sin razón.

Copilot Studio usa una optimización específica: distribuye tanto un motor JIT (inicio rápido) como un motor AOT (rendimiento máximo en estado estable), cargando ambos en paralelo y transfiriendo de JIT a AOT una vez que está listo. También deduplica los archivos idénticos entre los dos motores.

El nuevo comportamiento de eliminación de IL significa que los ensamblados AOT ya no coinciden bit a bit con sus contrapartes JIT, por lo que menos archivos se deduplican:
- .NET 8: 59 archivos compartidos
- .NET 10: 22 archivos compartidos

Resultado neto: tamaño del paquete aproximadamente un 15% mayor para el motor AOT. La descarga AOT es ~6% más lenta en LAN rápida, ~17% más lenta en 4G. Pero todo sucede en segundo plano después de que la aplicación ya es interactiva.

## Los Números de Rendimiento

Esta es la parte que importa:

- **~20% más rápido** en la primera llamada (ruta fría)
- **~5% más rápido** en llamadas posteriores (ruta cálida)

Las mejoras son más visibles en "bots grandes" — agentes grandes y complejos donde domina el código compilado AOT. Para flujos de trabajo más simples la ganancia es menor.

## Si Todavía Estás en .NET 8

La historia de migración es genuinamente simple: actualiza `<TargetFramework>`, actualiza las referencias de paquetes, elimina cualquier script de fingerprinting personalizado, y automáticamente te beneficiarás de `WasmStripILAfterAOT`. Si estás compilando AOT, espera ganancias de rendimiento similares.

Una nota de la publicación: si cargas el runtime de .NET WASM dentro de un `WebWorker`, establece `dotnetSidecar = true` al inicializar.

Post original: [Copilot Studio gets faster with .NET 10 on WebAssembly](https://devblogs.microsoft.com/dotnet/copilot-studio-dotnet-10-migration/)
