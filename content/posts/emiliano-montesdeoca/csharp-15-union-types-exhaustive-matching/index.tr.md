---
title: "C# 15 Union Türlerini Alıyor — ve Bunlar Tam İstediğimiz Şey"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15, union anahtar sözcüğünü tanıtıyor — derleyici tarafından zorunlu kılınan kapsamlı desen eşleştirmeli discriminated union'lar. Nasıl göründükleri, neden önemli oldukları ve bugün nasıl deneyebileceğiniz burada."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "csharp-15-union-types-exhaustive-matching" >}}).*

Bunu bekliyordum. C# 15, `union` anahtar sözcüğünü tanıtıyor — derleyici tarafından zorunlu kılınan kapsamlı desen eşleştirmeli gerçek discriminated union'lar. F#'ın discriminated union'larını ya da Rust'ın enum'larını hiç kıskandıysanız, bunun neden önemli olduğunu tam olarak biliyorsunuzdur.

Bill Wagner, .NET bloğunda [konunun derinlemesine incelemesini yayımladı](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/) ve dürüst olmak gerekirse? Tasarım temiz, pratik ve son derece C# ruhuyla örtüşüyor. Gerçekte ne olduğunu ve neden ilk bakışta göründüğünden daha büyük bir mesele olduğunu size anlatayım.

## Union türlerinin çözdüğü sorun

C# 15 öncesinde, bir metottan "birkaç olası türden biri" döndürmek her zaman bir uzlaşıydı:

- **`object`** — kısıtlama yok, derleyici yardımı yok, her yerde savunmacı casting
- **İşaretçi arayüzler** — daha iyi, ama herkes bunları uygulayabilir. Derleyici kümenin tamamlanmış olduğunu asla kabul edemez
- **Soyut taban sınıflar** — aynı sorun, üstelik türlerin ortak bir atası olması gerekiyor

Bunların hiçbiri gerçekte istediğinizi vermiyor: derleyicinin her durumu ele aldığınızı garanti ettiği kapalı bir tür kümesi. Union türlerinin yaptığı tam olarak bu.

## Sözdizimi güzelce basit

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

Tek satır. `Pet`, bir `Cat`, bir `Dog` veya bir `Bird` tutabilir. Örtülü dönüşümler otomatik olarak oluşturulur:

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

Ve işte sihir — derleyici kapsamlı eşleştirmeyi zorunlu kılıyor:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

`_` atma ifadesi gerekmiyor. Derleyici bu switch'in olası her durumu kapsadığını biliyor. Daha sonra union'a dördüncü bir tür eklerseniz, bunu ele almayan her switch ifadesi bir uyarı üretiyor. Eksik durumlar çalışma zamanında değil, derleme zamanında yakalanıyor.

## Bu pratikte ne anlama geliyor

`Pet` örneği şirin, ama işte union'ların gerçek kodda asıl parladığı yer burası.

### Farklı şekiller döndüren API yanıtları

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Artık her tüketici başarı, hata ve doğrulama başarısızlığını ele almak zorunda. "Hata durumunu kontrol etmeyi unuttum" hataları artık yok.

### Tek değer veya koleksiyon

`OneOrMore<T>` deseni, union'ların yardımcı metotlarla nasıl bir gövdeye sahip olabileceğini gösteriyor:

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

Çağıranlar hangi form uygunsa onu kullanıyor:

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### İlgisiz türleri birleştirme

Bu, geleneksel hiyerarşiler üzerindeki öldürücü özelliktir. Ortak atası olmayan türleri — `string` ve `Exception`, `int` ve `IEnumerable<T>` — union'layabilirsiniz.

## Mevcut kütüphaneler için özel union'lar

İşte akıllı bir tasarım seçimi: `[Union]` özniteliğine sahip herhangi bir sınıf veya struct, temel deseni izlediği sürece (durum türleri için public constructor'lar ve bir `Value` özelliği) bir union türü olarak tanınır. OneOf gibi union benzeri türler zaten sağlayan kütüphaneler, iç yapılarını yeniden yazmadan derleyici desteğini benimseyebilir.

Değer türleriyle performans açısından kritik senaryolar için kütüphaneler, `HasValue` ve `TryGetValue` metotlarıyla boxing yapmayan erişim deseni uygulayabilir.

## Büyük resim

Union türleri, C#'a gelen daha kapsamlı bir bütünlük hikayesinin parçası:

- **Union türleri** — kapalı bir tür kümesi üzerinde kapsamlı eşleştirme (şu an önizlemede mevcut)
- **Kapalı hiyerarşiler** — `closed` değiştiricisi, tanımlayan derleme dışında türetilmiş sınıfları engelliyor (önerildi)
- **Kapalı enum'lar** — bildirilmiş üyeler dışında değer oluşturulmasını engelliyor (önerildi)

Bu üç özellik birlikte, C#'a herhangi bir ana akım dilde en kapsamlı tür güvenli desen eşleştirme sistemlerinden birini kazandıracak.

## Bugün deneyin

Union türleri .NET 11 Preview 2'de mevcut:

1. [.NET 11 Preview SDK](https://dotnet.microsoft.com/download/dotnet)'yi yükleyin
2. Projenizde `net11.0` hedefleyin
3. `<LangVersion>preview</LangVersion>` ayarlayın

Bir uyarı: Preview 2'de, henüz çalışma zamanında bulunmadıkları için `UnionAttribute` ve `IUnion`'ı projenizde bildirmeniz gerekecek. Docs reposundan [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs) dosyasını alın veya şunu ekleyin:

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

## Sonuç

Union türleri, nasıl bu olmadan idare ettiğimizi merak ettiren özelliklerden biri. Derleyici tarafından zorunlu kılınan kapsamlı eşleştirme, temiz sözdizimi, generic desteği ve mevcut desen eşleştirmeyle entegrasyon — C# yolunda yapılmış, istediğimiz her şey bu.

.NET 11 Preview 2'de deneyin, şeyleri kırın ve [GitHub'da geri bildiriminizi paylaşın](https://github.com/dotnet/csharplang/discussions/9663). Bu önizleme aşamasında ve C# ekibi aktif olarak dinliyor. Uç durumlarınız ve tasarım geri bildiriminiz nihai sürümü şekillendirecek.

Tam dil referansı için [union türleri belgelerine](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) ve [özellik spesifikasyonuna](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions) bakın.
