---
title: "MCP Uygulamaları Fluent API Kazandı — .NET'te Üç Adımda Zengin AI Araç Arayüzleri Oluşturun"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Azure Functions'daki MCP Apps için yeni fluent yapılandırma API'si, herhangi bir .NET MCP aracını yalnızca birkaç satır kodla görünümler, izinler ve CSP politikaları olan tam bir uygulamaya dönüştürmenizi sağlar."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "mcp-fluent-api-azure-functions-dotnet" >}}).*

MCP araçları, AI agent'larına yetenekler kazandırmak için harika. Peki ya aracınızın kullanıcıya bir şey göstermesi gerekiyorsa — bir dashboard, bir form, etkileşimli bir görselleştirme? MCP Apps tam bu noktada devreye giriyor ve çok daha kolay hale geldi.

Azure SDK ekibinden Lilian Kasem, .NET Azure Functions'daki MCP Apps için [yeni fluent yapılandırma API'sini tanıttı](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) ve bu, neden başından beri bu kadar basit olmadığını düşündüren türden bir geliştirici deneyimi iyileştirmesi.

## MCP Apps Nedir?

MCP Apps, araçların kendi UI görünümlerini, statik varlıklarını ve güvenlik kontrollerini taşımasına izin vererek Model Context Protocol'ü genişletir. MCP aracınız yalnızca metin döndürmek yerine tam HTML deneyimleri render edebilir — etkileşimli dashboard'lar, veri görselleştirmeleri, yapılandırma formları — bunların hepsi AI agent'ları tarafından çağrılabilir ve MCP istemcileri tarafından kullanıcılara sunulur.

Sorun şuydu: tüm bunları manuel olarak bağlamak MCP spesifikasyonunu yakından bilmeyi gerektiriyordu: `ui://` URI'leri, özel mime türleri, araçlar ve kaynaklar arasında metadata koordinasyonu. Zor değil, ama zahmetli.

## Üç Adımda Fluent API

**Adım 1: Fonksiyonunuzu tanımlayın.** Standart bir Azure Functions MCP aracı:

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Adım 2: Bir MCP App'e yükseltin.** Program başlatmanızda:

```csharp
builder.ConfigureMcpTool("HelloApp")
    .AsMcpApp(app => app
        .WithView("assets/hello-app.html")
        .WithTitle("Hello App")
        .WithPermissions(McpAppPermissions.ClipboardWrite | McpAppPermissions.ClipboardRead)
        .WithCsp(csp =>
        {
            csp.AllowBaseUri("https://www.microsoft.com")
               .ConnectTo("https://www.microsoft.com");
        }));
```

**Adım 3: HTML görünümünüzü ekleyin.** İhtiyacınız olan herhangi bir UI ile `assets/hello-app.html` dosyasını oluşturun.

Hepsi bu kadar. Fluent API tüm MCP spesifikasyon altyapısını halleder — sentetik kaynak fonksiyonu oluşturma, doğru mime türünü ayarlama, aracınızı görünümüne bağlayan metadata'yı ekleme.

## API Yüzeyi İyi Tasarlanmış

Gerçekten beğendiğim birkaç şey:

**Görünüm kaynakları esnektir.** HTML'i diskteki dosyalardan sunabilir veya kendi kendine yetişen dağıtımlar için kaynakları doğrudan assembly'nize gömebilirsiniz:

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**CSP kompozisyona uygundur.** Uygulamanızın ihtiyaç duyduğu kaynakları açıkça beyaz listeye alırsınız, en az ayrıcalık ilkelerini izleyerek. `WithCsp`'yi birden fazla kez çağırın ve kaynaklar birikir:

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**Görünürlük kontrolü.** Bir aracı yalnızca LLM'ye görünür, yalnızca host UI'a görünür veya her ikisine de görünür yapabilirsiniz. Yalnızca UI render eden ve model tarafından çağrılmaması gereken bir araç mı istiyorsunuz? Kolay:

```csharp
.WithVisibility(McpVisibility.App) // Yalnızca UI, modelden gizli
```

## Başlarken

Preview paketini ekleyin:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

Zaten Azure Functions ile MCP araçları oluşturuyorsanız, bu yalnızca bir paket güncellemesi. Konsepte yeniyseniz [MCP Apps hızlı başlangıç kılavuzu](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp) başlamak için en iyi yer.

## Son Söz

MCP Apps, AI araçlama alanındaki daha heyecan verici gelişmelerden biri — yalnızca *işler yapan* değil, kullanıcılara *şeyler gösterebilen* araçlar. Fluent API protokol karmaşıklığını ortadan kaldırır ve önemli olan şeye odaklanmanızı sağlar: aracınızın mantığı ve UI'ı.

Tam API referansı ve örnekler için [tam yazıyı](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) okuyun.
