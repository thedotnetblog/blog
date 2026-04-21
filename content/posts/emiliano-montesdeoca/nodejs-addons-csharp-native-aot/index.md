---
title: "Writing Node.js Native Addons in C# with .NET Native AOT"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "The C# Dev Kit team replaced C++ Node.js addons with .NET Native AOT — and the result is cleaner, safer, and only needs the .NET SDK."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

Here's a scenario I love: a team that works on .NET tooling had native Node.js addons written in C++ and compiled via `node-gyp`. It worked. But it required Python to be installed on every developer's machine — an old version of Python, mind you — just to build a package that nobody on the team would ever touch directly. 

So they asked a very reasonable question: we already have the .NET SDK installed, why are we writing C++ at all?

The answer was Native AOT, and the result is genuinely elegant. Drew Noakes from the C# Dev Kit team wrote up how they did it, and I think it's worth understanding even if you're not building VS Code extensions.

## The basic idea

A Node.js native addon is a shared library (`.dll` on Windows, `.so` on Linux, `.dylib` on macOS) that Node.js can load at runtime. The interface is called [N-API](https://nodejs.org/api/n-api.html) — a stable, ABI-compatible C API. N-API doesn't care what language produced the library, only that it exports the right symbols.

.NET Native AOT can produce exactly that. It compiles your C# code ahead-of-time into a native shared library with arbitrary entry points. That's the whole trick.

## The project setup

The project file is minimal:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` is what tells the SDK to produce a shared library on `dotnet publish`. `AllowUnsafeBlocks` is needed for the N-API interop with function pointers and fixed buffers.

## Exporting the entry point

Node.js expects your library to export `napi_register_module_v1`. In C#, `[UnmanagedCallersOnly]` does exactly that:

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

A few things worth calling out here. `nint` is a native-sized integer — the managed equivalent of `intptr_t`. The `u8` suffix produces a `ReadOnlySpan<byte>` with a UTF-8 string literal, passed directly to N-API without any encoding allocation. And `[UnmanagedCallersOnly]` exports the method with the exact entry point name Node.js is looking for.

## Resolving N-API against the host process

N-API functions are exported by `node.exe` itself, not a separate library. So instead of linking against something, you resolve them against the running process at startup:

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

With that in place, your P/Invoke declarations work cleanly:

```csharp
[LibraryImport("node", EntryPoint = "napi_create_string_utf8")]
internal static partial Status CreateStringUtf8(
    nint env, ReadOnlySpan<byte> str, nuint length, out nint result);
```

The source-generated `[LibraryImport]` handles the marshalling. `ReadOnlySpan<byte>` maps to `const char*`, function pointers pass through directly, and it's all trimming-compatible.

## What an actual exported function looks like

Here's the registry reader they built — the whole function, from reading arguments to returning a result:

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

Important note on the `try/catch`: an unhandled exception in an `[UnmanagedCallersOnly]` method crashes the host process. You always catch and forward to JavaScript via `ThrowError`.

## Calling it from TypeScript

`dotnet publish` produces your platform-specific native library. You rename it to `.node` (Node.js convention for native addons) and use it with a standard `require()`:

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

That's it. TypeScript into C#, no Python, no C++.

## What they gained

The immediate win was contributor experience: no specific Python version needed, `yarn install` works with just Node.js and the .NET SDK. CI pipelines got simpler too.

Performance was comparable to the C++ implementation. Native AOT produces optimized native code, and for string marshalling and registry access, the difference is negligible. The slightly larger memory footprint of the .NET runtime doesn't matter in a long-running VS Code extension process.

But the bit that caught my attention was this: they noted that with Native AOT producing shared libraries that load directly into the Node.js process, they could potentially host *more* .NET logic in-process, avoiding the serialization and process-management overhead of their current pipe-based approach. That's a longer-term exploration, but the foundation is now in place.

## Why I think this is interesting beyond VS Code extensions

We often talk about Native AOT in the context of serverless cold starts or embedded scenarios. This is a different angle: using Native AOT to bridge .NET into ecosystems that traditionally required C or C++. Any environment that can load a native shared library — Electron apps, Python extensions via ctypes, Rust via FFI, Node.js via N-API — is now a potential host for C# code.

For .NET developers who've been eyeing some interop scenario but didn't want to learn a C++ build system, this pattern is worth knowing. Write your logic in C#, expose it with `[UnmanagedCallersOnly]`, compile with `PublishAot`, and load it from wherever you need it.

## Wrapping up

The C# Dev Kit team replaced Python/C++ overhead with clean C# code that everyone on the team already knows how to write and debug. The approach is not complicated once you see it, and it's a great example of Native AOT solving a real problem that doesn't get talked about enough.

If you want the full walkthrough with all the string marshalling helpers, check the [original post on the .NET blog](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/). There's also [node-api-dotnet](https://github.com/microsoft/node-api-dotnet) if you need a higher-level framework for more complex scenarios.
