---
title: "C# 15 ganha Union Types — e são exatamente o que estávamos pedindo"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 introduz a palavra-chave union — uniões discriminadas com pattern matching exaustivo imposto pelo compilador. Veja como são, por que importam e como experimentar hoje."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "csharp-15-union-types-exhaustive-matching.md" >}}).*

Essa é a que eu estava esperando. C# 15 introduz a palavra-chave `union` — uniões discriminadas de verdade com pattern matching exaustivo imposto pelo compilador. Se você já invejou as uniões discriminadas do F# ou os enums do Rust, sabe exatamente por que isso importa.

Bill Wagner [publicou a análise detalhada](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/) no blog do .NET, e sinceramente? O design é limpo, prático e muito C#. Deixa eu te mostrar o que realmente tem aqui e por que é mais importante do que parece à primeira vista.

## O problema que as uniões resolvem

Antes do C# 15, retornar "um dentre vários tipos possíveis" de um método era sempre um compromisso:

- **`object`** — sem restrições, sem ajuda do compilador, casting defensivo por toda parte
- **Interfaces marcadoras** — melhor, mas qualquer um pode implementá-las. O compilador nunca pode considerar o conjunto completo
- **Classes base abstratas** — mesmo problema, além dos tipos precisarem de um ancestral comum

Nenhuma dessas opções te dá o que você realmente quer: um conjunto fechado de tipos onde o compilador garante que você tratou todos os casos. É isso que os tipos union fazem.

## A sintaxe é lindamente simples

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

Uma linha. `Pet` pode conter um `Cat`, um `Dog` ou um `Bird`. Conversões implícitas são geradas automaticamente:

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

E aqui está a mágica — o compilador impõe o matching exaustivo:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

Sem necessidade de discard `_`. O compilador sabe que esse switch cobre todos os casos possíveis. Se você depois adicionar um quarto tipo à union, cada expressão switch que não o trata produz um aviso. Casos faltantes detectados no tempo de compilação, não em tempo de execução.

## Onde isso se torna prático

O exemplo do `Pet` é bonitinho, mas é aqui que as uniões realmente brilham em código real.

### Respostas de API que retornam formas diferentes

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Agora todo consumidor é obrigado a tratar sucesso, erro e falha de validação. Chega de bugs de "esqueci de verificar o caso de erro".

### Valor único ou coleção

O padrão `OneOrMore<T>` mostra como as uniões podem ter um corpo com métodos auxiliares:

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

Os chamadores passam a forma que for mais conveniente:

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### Compor tipos não relacionados

Essa é a funcionalidade matadora em relação às hierarquias tradicionais. Você pode unir tipos que não têm nada em comum — `string` e `Exception`, `int` e `IEnumerable<T>`. Sem necessidade de ancestral comum.

## Uniões personalizadas para bibliotecas existentes

Aqui vai uma decisão de design inteligente: qualquer classe ou struct com um atributo `[Union]` é reconhecida como um tipo union, desde que siga o padrão básico (construtores públicos para os tipos de caso e uma propriedade `Value`). Bibliotecas como OneOf que já fornecem tipos similares a uniões podem optar pelo suporte do compilador sem reescrever seus internos.

Para cenários sensíveis a performance com tipos de valor, bibliotecas podem implementar um padrão de acesso sem boxing com os métodos `HasValue` e `TryGetValue`.

## O panorama geral

Os tipos union fazem parte de uma história mais ampla de exaustividade chegando ao C#:

- **Tipos union** — matching exaustivo sobre um conjunto fechado de tipos (disponível agora em preview)
- **Hierarquias fechadas** — o modificador `closed` impede classes derivadas fora do assembly de definição (proposto)
- **Enums fechados** — impede a criação de valores além dos membros declarados (proposto)

Juntas, essas três funcionalidades darão ao C# um dos sistemas de pattern matching type-safe mais completos em qualquer linguagem mainstream.

## Experimente hoje

Os tipos union estão disponíveis no .NET 11 Preview 2:

1. Instale o [SDK .NET 11 Preview](https://dotnet.microsoft.com/download/dotnet)
2. Aponte para `net11.0` no seu projeto
3. Configure `<LangVersion>preview</LangVersion>`

Um detalhe: no Preview 2, você vai precisar declarar `UnionAttribute` e `IUnion` no seu projeto já que eles ainda não estão no runtime. Pegue o [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs) do repo de docs, ou adicione isso:

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

## Fechando

Os tipos union são uma daquelas funcionalidades que fazem você se perguntar como sobrevivemos sem elas. Pattern matching exaustivo imposto pelo compilador, sintaxe limpa, suporte a generics e integração com o pattern matching existente — é tudo que pedimos, feito do jeito C#.

Experimente no .NET 11 Preview 2, quebre coisas e [compartilhe seu feedback no GitHub](https://github.com/dotnet/csharplang/discussions/9663). Isso é preview, e o time de C# está ouvindo ativamente. Seus edge cases e feedback de design vão moldar a versão final.

Para a referência completa da linguagem, confira a [documentação de tipos union](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) e a [especificação da funcionalidade](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions).
