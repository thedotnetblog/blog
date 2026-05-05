---
title: "C# 15 trae los tipos unión — y son exactamente lo que estábamos pidiendo"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 introduce la palabra clave union — uniones discriminadas con coincidencia de patrones exhaustiva impuesta por el compilador. Así se ven, por qué importan y cómo probarlas hoy."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "csharp-15-union-types-exhaustive-matching.md" >}}).*

Esta es la que estuve esperando. C# 15 introduce la palabra clave `union` — uniones discriminadas con coincidencia de patrones exhaustiva impuesta por el compilador. Si alguna vez envidiaste las uniones discriminadas de F# o los enums de Rust, sabés exactamente por qué esto importa.

Bill Wagner [publicó el análisis a fondo](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/) en el blog de .NET, y sinceramente? El diseño es limpio, práctico y muy C#. Déjame mostrarte qué hay realmente y por qué es más importante de lo que parece a primera vista.

## El problema que resuelven las uniones

Antes de C# 15, devolver "uno de varios tipos posibles" desde un método siempre era un compromiso:

- **`object`** — sin restricciones, sin ayuda del compilador, casting defensivo por todos lados
- **Interfaces marcadoras** — mejor, pero cualquiera puede implementarlas. El compilador nunca puede considerar el conjunto completo
- **Clases base abstractas** — mismo problema, además los tipos necesitan un ancestro común

Ninguna de estas opciones te da lo que realmente querés: un conjunto cerrado de tipos donde el compilador garantiza que manejaste todos los casos. Eso es lo que hacen los tipos unión.

## La sintaxis es hermosamente simple

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

Una línea. `Pet` puede contener un `Cat`, un `Dog` o un `Bird`. Las conversiones implícitas se generan automáticamente:

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

Y acá está la magia — el compilador impone la coincidencia exhaustiva:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

No se necesita descarte `_`. El compilador sabe que este switch cubre todos los casos posibles. Si después agregás un cuarto tipo a la unión, cada expresión switch que no lo maneje produce una advertencia. Casos faltantes detectados en tiempo de compilación, no en tiempo de ejecución.

## Donde esto se vuelve práctico

El ejemplo de `Pet` es simpático, pero acá es donde las uniones realmente brillan en código real.

### Respuestas de API que devuelven diferentes formas

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Ahora cada consumidor está obligado a manejar éxito, error y fallo de validación. No más bugs de "me olvidé de chequear el caso de error".

### Valor único o colección

El patrón `OneOrMore<T>` muestra cómo las uniones pueden tener un cuerpo con métodos auxiliares:

```csharp
public union OneOrMore<T>(T, IEnumerable<T>)
{
    public IEnumerable<T> AsEnumerable() => Value switch
    {
        T single => [single],
        IEnumerable<T> multiple => multiple,
        null => []
    };
}
```

Los consumidores pasan la forma que les resulte conveniente:

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### Componer tipos no relacionados

Esta es la funcionalidad definitiva sobre las jerarquías tradicionales. Podés unir tipos que no tienen nada en común — `string` y `Exception`, `int` e `IEnumerable<T>`. No se necesita un ancestro común.

## Uniones personalizadas para bibliotecas existentes

Acá hay una decisión de diseño inteligente: cualquier clase o struct con un atributo `[Union]` es reconocida como tipo unión, siempre que siga el patrón básico (constructores públicos para los tipos de caso y una propiedad `Value`). Bibliotecas como OneOf que ya proveen tipos similares a uniones pueden optar por el soporte del compilador sin reescribir sus internos.

Para escenarios sensibles al rendimiento con tipos de valor, las bibliotecas pueden implementar un patrón de acceso sin boxing con los métodos `HasValue` y `TryGetValue`.

## El panorama general

Los tipos unión son parte de una historia más amplia de exhaustividad que viene a C#:

- **Tipos unión** — coincidencia exhaustiva sobre un conjunto cerrado de tipos (disponible ahora en preview)
- **Jerarquías cerradas** — el modificador `closed` previene clases derivadas fuera del assembly que las define (propuesto)
- **Enums cerrados** — previene la creación de valores distintos a los miembros declarados (propuesto)

Juntas, estas tres funcionalidades le darán a C# uno de los sistemas de coincidencia de patrones con seguridad de tipos más completos en cualquier lenguaje mainstream.

## Probalo hoy

Los tipos unión están disponibles en .NET 11 Preview 2:

1. Instalá el [SDK de .NET 11 Preview](https://dotnet.microsoft.com/download/dotnet)
2. Apuntá a `net11.0` en tu proyecto
3. Configurá `<LangVersion>preview</LangVersion>`

Una aclaración: en Preview 2, vas a necesitar declarar `UnionAttribute` e `IUnion` en tu proyecto ya que todavía no están en el runtime. Agarrá [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs) del repo de docs, o agregá esto:

```csharp
namespace System.Runtime.CompilerServices
{
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Struct,
        AllowMultiple = false)]
    public sealed class UnionAttribute : Attribute;

    public interface IUnion
    {
        object? Value { get; }
    }
}
```

## Para cerrar

Los tipos unión son una de esas funcionalidades que te hacen preguntarte cómo sobrevivimos sin ellas. Coincidencia exhaustiva impuesta por el compilador, sintaxis limpia, soporte genérico e integración con el pattern matching existente — es todo lo que pedimos, hecho a la manera de C#.

Probalos en .NET 11 Preview 2, rompé cosas y [compartí tu feedback en GitHub](https://github.com/dotnet/csharplang/discussions/9663). Esto es preview, y el equipo de C# está escuchando activamente. Tus casos extremos y feedback de diseño van a dar forma a la versión final.

Para la referencia completa del lenguaje, consultá la [documentación de tipos unión](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) y la [especificación de la funcionalidad](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions).
