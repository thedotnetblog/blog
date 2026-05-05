---
title: "C# 15 Gets Union Types — and They're Exactly What We've Been Asking For"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 introduces the union keyword — compiler-enforced discriminated unions with exhaustive pattern matching. Here's what they look like, why they matter, and how to try them today."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

This is the one I've been waiting for. C# 15 introduces the `union` keyword — proper discriminated unions with compiler-enforced exhaustive pattern matching. If you've ever envied F#'s discriminated unions or Rust's enums, you know exactly why this matters.

Bill Wagner [published the deep dive](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/) on the .NET blog, and honestly? The design is clean, practical, and very C#. Let me walk you through what's actually here and why it's a bigger deal than it might seem at first glance.

## The problem unions solve

Before C# 15, returning "one of several possible types" from a method was always a compromise:

- **`object`** — no constraints, no compiler help, defensive casting everywhere
- **Marker interfaces** — better, but anyone can implement them. The compiler can never consider the set complete
- **Abstract base classes** — same issue, plus the types need a common ancestor

None of these give you what you actually want: a closed set of types where the compiler guarantees you've handled every case. That's what union types do.

## The syntax is beautifully simple

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

One line. `Pet` can hold a `Cat`, a `Dog`, or a `Bird`. Implicit conversions are generated automatically:

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

And here's the magic — the compiler enforces exhaustive matching:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

No discard `_` needed. The compiler knows this switch covers every possible case. If you later add a fourth type to the union, every switch expression that doesn't handle it produces a warning. Missing cases caught at build time, not at runtime.

## Where this gets practical

The `Pet` example is cute, but here's where unions actually shine in real code.

### API responses that return different shapes

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Now every consumer is forced to handle success, error, and validation failure. No more "I forgot to check the error case" bugs.

### Single value or collection

The `OneOrMore<T>` pattern shows how unions can have a body with helper methods:

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

Callers pass whichever form is convenient:

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### Composing unrelated types

This is the killer feature over traditional hierarchies. You can union types that have nothing in common — `string` and `Exception`, `int` and `IEnumerable<T>`. No common ancestor needed.

## Custom unions for existing libraries

Here's a smart design choice: any class or struct with a `[Union]` attribute is recognized as a union type, as long as it follows the basic pattern (public constructors for case types and a `Value` property). Libraries like OneOf that already provide union-like types can opt into compiler support without rewriting their internals.

For performance-sensitive scenarios with value types, libraries can implement a non-boxing access pattern with `HasValue` and `TryGetValue` methods.

## The bigger picture

Union types are part of a broader exhaustiveness story coming to C#:

- **Union types** — exhaustive matching over a closed set of types (available now in preview)
- **Closed hierarchies** — `closed` modifier prevents derived classes outside the defining assembly (proposed)
- **Closed enums** — prevents creation of values other than declared members (proposed)

Together, these three features will give C# one of the most comprehensive type-safe pattern matching systems in any mainstream language.

## Try it today

Union types are available in .NET 11 Preview 2:

1. Install the [.NET 11 Preview SDK](https://dotnet.microsoft.com/download/dotnet)
2. Target `net11.0` in your project
3. Set `<LangVersion>preview</LangVersion>`

One caveat: in Preview 2, you'll need to declare `UnionAttribute` and `IUnion` in your project since they're not in the runtime yet. Grab [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs) from the docs repo, or add this:

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

## Wrapping up

Union types are one of those features that make you wonder how we got by without them. Compiler-enforced exhaustive matching, clean syntax, generic support, and integration with existing pattern matching — it's everything we've been asking for, done the C# way.

Try them in .NET 11 Preview 2, break things, and [share your feedback on GitHub](https://github.com/dotnet/csharplang/discussions/9663). This is preview, and the C# team is actively listening. Your edge cases and design feedback will shape the final release.

For the full language reference, check out the [union types docs](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) and the [feature specification](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions).
