---
title: "Escribir addons nativos de Node.js en C# con .NET Native AOT"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "El equipo de C# Dev Kit reemplazó addons de Node.js escritos en C++ con .NET Native AOT — el resultado es más limpio, más seguro y solo necesita el SDK de .NET."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *Este artículo fue traducido automáticamente. Para ver la versión original en inglés, [haz clic aquí]({{< ref "index.md" >}}).*

Este es un escenario que me encanta: un equipo que trabaja en herramientas .NET tenía addons nativos de Node.js escritos en C++ y compilados con `node-gyp`. Funcionaba. Pero requería instalar Python en la máquina de cada desarrollador — una versión antigua de Python, nada menos — solo para construir un paquete que nadie del equipo tocaría directamente.

Así que se hicieron una pregunta muy razonable: ya tenemos el SDK de .NET instalado, ¿por qué escribimos C++ en absoluto?

La respuesta fue Native AOT, y el resultado es genuinamente elegante. Drew Noakes del equipo de C# Dev Kit documentó cómo lo hicieron, y creo que vale la pena entenderlo aunque no estés construyendo extensiones de VS Code.

## La idea básica

Un addon nativo de Node.js es una biblioteca compartida (`.dll` en Windows, `.so` en Linux, `.dylib` en macOS) que Node.js puede cargar en tiempo de ejecución. La interfaz se llama [N-API](https://nodejs.org/api/n-api.html) — una API C estable y compatible con ABI. A N-API no le importa qué lenguaje produjo la biblioteca, solo que exporte los símbolos correctos.

.NET Native AOT puede producir exactamente eso. Compila tu código C# ahead-of-time en una biblioteca nativa compartida con puntos de entrada arbitrarios. Ese es todo el truco.

## Configuración del proyecto

El archivo de proyecto es mínimo:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` indica al SDK que produzca una biblioteca compartida al ejecutar `dotnet publish`. `AllowUnsafeBlocks` es necesario para el interop con N-API que usa punteros a funciones y buffers fijos.

## Exportar el punto de entrada

Node.js espera que tu biblioteca exporte `napi_register_module_v1`. En C#, `[UnmanagedCallersOnly]` hace exactamente eso:

```csharp
public static unsafe partial class RegistryAddon
{
    [UnmanagedCallersOnly(
        EntryPoint = "napi_register_module_v1",
        CallConvs = [typeof(CallConvCdecl)])]
    public static nint Init(nint env, nint exports)
    {
        Initialize();
        RegisterFunction(env, exports, "readStringValue"u8, &ReadStringValue);
        return exports;
    }
}
```

Algunas cosas que vale la pena señalar: `nint` es un entero de tamaño nativo — el equivalente gestionado de `intptr_t`. El sufijo `u8` produce un `ReadOnlySpan<byte>` con un literal de cadena UTF-8, pasado directamente a N-API sin ninguna asignación de codificación. Y `[UnmanagedCallersOnly]` exporta el método con el nombre de punto de entrada exacto que Node.js busca.

## Resolver N-API contra el proceso host

Las funciones de N-API las exporta `node.exe` en sí mismo, no una biblioteca separada. Así que en lugar de enlazar contra algo, las resuelves contra el proceso en ejecución al inicio:

```csharp
private static void Initialize()
{
    NativeLibrary.SetDllImportResolver(
        System.Reflection.Assembly.GetExecutingAssembly(),
        ResolveDllImport);

    static nint ResolveDllImport(
        string libraryName, Assembly assembly, DllImportSearchPath? searchPath)
    {
        if (libraryName is not "node") return 0;
        return NativeLibrary.GetMainProgramHandle();
    }
}
```

Con eso en su lugar, las declaraciones P/Invoke funcionan limpiamente, con `[LibraryImport]` y marshalling generado por código fuente.

## Una función exportada real

Aquí está el lector de registro que construyeron — la función completa, desde leer argumentos hasta devolver un resultado:

```csharp
[UnmanagedCallersOnly(CallConvs = [typeof(CallConvCdecl)])]
private static nint ReadStringValue(nint env, nint info)
{
    try
    {
        var keyPath = GetStringArg(env, info, 0);
        var valueName = GetStringArg(env, info, 1);

        if (keyPath is null || valueName is null)
        {
            ThrowError(env, "Expected two string arguments: keyPath, valueName");
            return 0;
        }

        using var key = Registry.CurrentUser.OpenSubKey(keyPath, writable: false);

        return key?.GetValue(valueName) is string value
            ? CreateString(env, value)
            : GetUndefined(env);
    }
    catch (Exception ex)
    {
        ThrowError(env, $"Registry read failed: {ex.Message}");
        return 0;
    }
}
```

Nota importante sobre el `try/catch`: una excepción no manejada en un método `[UnmanagedCallersOnly]` provoca el crash del proceso host. Siempre captura y reenvía a JavaScript mediante `ThrowError`.

## Llamándolo desde TypeScript

```typescript
interface RegistryAddon {
    readStringValue(keyPath: string, valueName: string): string | undefined;
}

const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;

const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk',
    'InstallLocation'
);
```

TypeScript → C#, sin Python, sin C++.

## Lo que ganaron

La victoria inmediata fue en la experiencia del contribuidor: ya no se necesita ninguna versión específica de Python, `yarn install` funciona solo con Node.js y el SDK de .NET. Los pipelines de CI también se simplificaron.

El rendimiento fue comparable a la implementación en C++. Native AOT produce código nativo optimizado, y para marshalling de cadenas y acceso al registro, la diferencia es insignificante.

## Por qué me parece interesante más allá de las extensiones VS Code

Cualquier entorno que pueda cargar una biblioteca nativa compartida — apps Electron, extensiones Python vía ctypes, Rust vía FFI, Node.js vía N-API — es ahora un posible host para código C#. Para desarrolladores .NET que tenían escenarios de interop en mente pero no querían aprender un sistema de compilación C++, este patrón vale la pena conocerlo.

## Conclusión

El equipo de C# Dev Kit reemplazó la sobrecarga de Python/C++ con código C# limpio que todo el equipo ya sabe escribir y depurar. Si quieres el recorrido completo con todos los helpers de marshalling de cadenas, consulta el [artículo original en el blog de .NET](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
