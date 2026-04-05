---
title: "C# 15 引入联合类型 — 正是我们一直在期待的"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 引入了 union 关键字 — 编译器强制的可区分联合类型，支持穷举模式匹配。来看看它们长什么样、为什么重要，以及如何今天就试用。"
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "csharp-15-union-types-exhaustive-matching.md" >}})。*

这就是我一直在等的那个功能。C# 15 引入了 `union` 关键字 — 真正的可区分联合类型，带有编译器强制的穷举模式匹配。如果你曾经羡慕过 F# 的可区分联合或 Rust 的 enum，你就明白这为什么重要了。

Bill Wagner 在 .NET 博客上[发布了深度解析](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/)，说实话？设计干净、实用，非常 C#。让我带你看看实际有什么，以及为什么它比乍看之下更重要。

## 联合类型解决的问题

在 C# 15 之前，从方法返回"多个可能类型之一"总是一种妥协：

- **`object`** — 没有约束，没有编译器帮助，到处都是防御性类型转换
- **标记接口** — 好一些，但任何人都可以实现它们。编译器永远无法认为集合是完整的
- **抽象基类** — 同样的问题，而且类型需要共同的祖先

这些都无法给你真正想要的东西：一个封闭的类型集合，编译器保证你已经处理了每种情况。这就是联合类型的作用。

## 语法优雅简洁

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

一行代码。`Pet` 可以包含一个 `Cat`、一个 `Dog` 或一个 `Bird`。隐式转换会自动生成：

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

魔法来了 — 编译器强制穷举匹配：

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

不需要丢弃模式 `_`。编译器知道这个 switch 覆盖了所有可能的情况。如果你之后向联合添加第四个类型，每个没有处理它的 switch 表达式都会产生警告。缺失的情况在编译时被捕获，而不是在运行时。

## 真正实用的地方

`Pet` 的例子很可爱，但这里才是联合类型在真实代码中真正发光的地方。

### 返回不同形状的 API 响应

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

现在每个消费者都被强制处理成功、错误和验证失败。再也不会有"忘记检查错误情况"的 bug 了。

### 单值或集合

`OneOrMore<T>` 模式展示了联合如何拥有带有辅助方法的主体：

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

调用者传递最方便的形式：

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### 组合不相关的类型

这是相对于传统继承层次结构的杀手级功能。你可以联合没有任何共同点的类型 — `string` 和 `Exception`、`int` 和 `IEnumerable<T>`。不需要共同祖先。

## 为现有库创建自定义联合

这是一个聪明的设计选择：任何带有 `[Union]` 属性的类或结构体都会被识别为联合类型，只要它遵循基本模式（case 类型的公共构造函数和 `Value` 属性）。像 OneOf 这样已经提供类似联合功能的库可以选择加入编译器支持，而无需重写其内部实现。

对于使用值类型的性能敏感场景，库可以通过 `HasValue` 和 `TryGetValue` 方法实现无装箱的访问模式。

## 更大的图景

联合类型是 C# 即将到来的更广泛穷举性故事的一部分：

- **联合类型** — 对封闭类型集合的穷举匹配（现已在预览版中可用）
- **密封层次结构** — `closed` 修饰符阻止在定义程序集之外派生类（已提议）
- **密封枚举** — 阻止创建声明成员之外的值（已提议）

这三个功能结合在一起，将使 C# 拥有所有主流语言中最全面的类型安全模式匹配系统之一。

## 今天就试试

联合类型在 .NET 11 Preview 2 中可用：

1. 安装 [.NET 11 Preview SDK](https://dotnet.microsoft.com/download/dotnet)
2. 在项目中目标设为 `net11.0`
3. 设置 `<LangVersion>preview</LangVersion>`

一个注意事项：在 Preview 2 中，你需要在项目中声明 `UnionAttribute` 和 `IUnion`，因为它们还没有包含在运行时中。从 docs 仓库获取 [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs)，或添加以下代码：

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

## 总结

联合类型是那种让你不禁感叹"以前没有它们我们是怎么过来的"的功能。编译器强制的穷举匹配、简洁的语法、泛型支持，以及与现有模式匹配的集成 — 这是我们一直要求的一切，以 C# 的方式实现。

在 .NET 11 Preview 2 中试用它们，尽情折腾，并[在 GitHub 上分享你的反馈](https://github.com/dotnet/csharplang/discussions/9663)。这是预览版，C# 团队正在积极倾听。你的边界情况和设计反馈将塑造最终版本。

完整的语言参考请查看[联合类型文档](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union)和[功能规范](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions)。
