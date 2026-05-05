---
title: "C# 15 में Union Types आ गए — और वे बिल्कुल वैसे ही हैं जैसा हम माँग रहे थे"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 में union keyword पेश किया गया है — compiler-enforced discriminated unions जिसमें exhaustive pattern matching है। यहाँ देखें ये कैसे दिखते हैं, क्यों मायने रखते हैं, और आज इन्हें कैसे आज़माएँ।"
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "csharp-15-union-types-exhaustive-matching" >}}).*

यही वह feature है जिसका मैं इंतज़ार कर रहा था। C# 15 में `union` keyword पेश किया गया है — उचित discriminated unions जिनमें compiler-enforced exhaustive pattern matching है। अगर आपने कभी F# के discriminated unions या Rust के enums से ईर्ष्या की है, तो आप जानते हैं कि यह क्यों मायने रखता है।

Bill Wagner ने .NET blog पर [इसका विस्तृत विश्लेषण](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/) publish किया है, और सच में? Design clean, practical, और बिल्कुल C# style का है। आइए मैं आपको बताता हूँ कि यहाँ वास्तव में क्या है और यह पहली नज़र में जितना लगता है उससे बड़ी बात क्यों है।

## Union Types किस समस्या को हल करते हैं

C# 15 से पहले, किसी method से "कई possible types में से एक" return करना हमेशा एक compromise था:

- **`object`** — कोई constraints नहीं, कोई compiler help नहीं, हर जगह defensive casting
- **Marker interfaces** — बेहतर, लेकिन कोई भी उन्हें implement कर सकता है। Compiler कभी set को complete नहीं मान सकता
- **Abstract base classes** — वही समस्या, साथ ही types को एक common ancestor की ज़रूरत है

इनमें से कोई भी आपको वह नहीं देता जो आप वास्तव में चाहते हैं: types का एक closed set जहाँ compiler guarantee करता है कि आपने हर case handle किया है। Union types यही करते हैं।

## Syntax खूबसूरती से सरल है

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

एक line। `Pet` एक `Cat`, एक `Dog`, या एक `Bird` hold कर सकता है। Implicit conversions automatically generate होती हैं:

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

और यहाँ जादू है — compiler exhaustive matching enforce करता है:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

`_` discard की ज़रूरत नहीं। Compiler जानता है कि यह switch हर possible case cover करता है। अगर आप बाद में union में चौथा type जोड़ते हैं, तो हर switch expression जो उसे handle नहीं करती warning produce करती है। Missing cases build time पर पकड़ी जाती हैं, runtime पर नहीं।

## यह व्यावहारिक रूप से कहाँ काम आता है

`Pet` का उदाहरण प्यारा है, लेकिन real code में unions वास्तव में कहाँ चमकते हैं यह देखें।

### API responses जो अलग-अलग shapes return करती हैं

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

अब हर consumer को success, error, और validation failure handle करने पर मजबूर किया जाता है। "मैं error case check करना भूल गया" bugs नहीं।

### Single value या collection

`OneOrMore<T>` pattern दिखाता है कि unions में helper methods के साथ एक body कैसे हो सकती है:

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

Callers जो भी form सुविधाजनक हो वह pass करते हैं:

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### असंबंधित types को Compose करना

यह traditional hierarchies पर killer feature है। आप ऐसे types को union कर सकते हैं जिनमें कुछ भी common नहीं है — `string` और `Exception`, `int` और `IEnumerable<T>`। कोई common ancestor ज़रूरी नहीं।

## मौजूदा Libraries के लिए Custom Unions

यहाँ एक smart design choice है: कोई भी class या struct जिसमें `[Union]` attribute हो, उसे union type के रूप में पहचाना जाता है, जब तक वह basic pattern follow करे (case types के लिए public constructors और एक `Value` property)। OneOf जैसी libraries जो पहले से union-like types provide करती हैं, वे अपनी internals rewrite किए बिना compiler support में opt in कर सकती हैं।

Value types के साथ performance-sensitive scenarios के लिए, libraries `HasValue` और `TryGetValue` methods के साथ एक non-boxing access pattern implement कर सकती हैं।

## बड़ी तस्वीर

Union types C# में आने वाली एक broader exhaustiveness story का हिस्सा हैं:

- **Union types** — types के closed set पर exhaustive matching (अभी preview में available)
- **Closed hierarchies** — `closed` modifier defining assembly के बाहर derived classes को रोकता है (proposed)
- **Closed enums** — declared members के अलावा values बनाने से रोकता है (proposed)

साथ में, ये तीन features C# को किसी भी mainstream language में सबसे comprehensive type-safe pattern matching systems में से एक देंगे।

## आज ही आज़माएँ

Union types .NET 11 Preview 2 में available हैं:

1. [.NET 11 Preview SDK](https://dotnet.microsoft.com/download/dotnet) install करें
2. अपने project में `net11.0` target करें
3. `<LangVersion>preview</LangVersion>` set करें

एक caveat: Preview 2 में, आपको अपने project में `UnionAttribute` और `IUnion` declare करने होंगे क्योंकि वे अभी runtime में नहीं हैं। Docs repo से [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs) लें, या यह add करें:

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

## निष्कर्ष

Union types उन features में से हैं जो आपको सोचने पर मजबूर करते हैं कि इनके बिना हम कैसे काम करते थे। Compiler-enforced exhaustive matching, clean syntax, generic support, और मौजूदा pattern matching के साथ integration — यह सब कुछ है जो हम माँग रहे थे, C# के style में।

.NET 11 Preview 2 में इन्हें आज़माएँ, चीज़ें तोड़ें, और [GitHub पर अपना feedback share करें](https://github.com/dotnet/csharplang/discussions/9663)। यह preview है, और C# team सक्रिय रूप से सुन रही है। आपके edge cases और design feedback final release को आकार देंगे।

पूर्ण language reference के लिए, [union types docs](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) और [feature specification](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions) देखें।
