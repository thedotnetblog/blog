---
title: ".NET 11 por fin arregla la API de Procesos"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process recibe su mayor actualización en años. RunAndCaptureTextAsync, KillOnParentExit, APIs SafeProcessHandle y control total sobre la redirección de handles estándar — sin más boilerplate de deadlock."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

Todo desarrollador .NET que alguna vez ha necesitado lanzar un proceso y capturar su salida ha escrito alguna variación del mismo boilerplate peligroso: lectura async de stdout, lectura async de stderr, `WaitForExitAsync`, sin olvidar drenar ambos streams o producirás un deadlock. Es una trampa conocida que lleva años ahí.

.NET 11 finalmente lo arregla correctamente.

## RunAndCaptureTextAsync

La adición principal: un único método estático que inicia un proceso, captura stdout y stderr, y espera la salida sin producir deadlock.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

Una sola llamada. Sin drenaje manual de streams. Sin un `WaitForExit` colocado cuidadosamente. Si simplemente necesitas ejecutar algo y obtener su salida, esta es la API que quieres.

También existe `Process.RunAsync` para el caso en que quieras esperar la salida sin capturar el output.

## KillOnParentExit

Un problema común con los procesos lanzados: si el padre falla o es terminado, los procesos hijo siguen ejecutándose como huérfanos. `KillOnParentExit` te permite declarar en el momento de iniciar el proceso que el proceso hijo debe terminar cuando el proceso padre salga.

Esta es una funcionalidad que ha existido de formas específicas de plataforma (job objects en Windows, prctl en Linux), pero requería p/invoke o bibliotecas de terceros para usarla desde .NET. Ahora es una propiedad de primera clase en `ProcessStartInfo`.

## APIs Basadas en SafeProcessHandle

La nueva superficie de API ligera está construida sobre `SafeProcessHandle` en lugar de la clase `Process` completa. La clase `Process` completa lleva mucho estado y es difícil de recortar — la ruta de `SafeProcessHandle` es más amigable con el trimmer para aplicaciones que necesitan minimizar el tamaño de salida (WASM, AOT nativo).

## Control Total Sobre la Herencia de Handles

La actualización también añade control detallado sobre qué handles hereda un proceso hijo y cómo se redirigen los handles estándar. Anteriormente podías redirigir stdin/stdout/stderr, pero no podías especificar exactamente qué handles heredar a nivel de SO. Las nuevas APIs exponen ese control.

## Por Qué Importa

La clase `Process` se usa en tooling, sistemas de build, ejecutores de pruebas y cualquier aplicación que invoca otros ejecutables. La superficie de API anterior databa de .NET Framework y estaba mostrando su edad. No es un cambio que rompe compatibilidad — las APIs antiguas siguen funcionando — pero el nuevo código debería preferir la nueva superficie.

Para aplicaciones recortadas o escenarios de compilación AOT, la ruta de `SafeProcessHandle` es especialmente bienvenida. La antigua clase `Process` arrastraba mucho código pesado en reflexión que complicaba el recorte.

Post original: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
