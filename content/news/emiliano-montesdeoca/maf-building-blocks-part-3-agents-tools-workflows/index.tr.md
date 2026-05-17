---
title: "Microsoft Agent Framework Bölüm 3: Araçlardan İş Akışlarına — Yapı Taşları Yerine Oturdu"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: ".NET AI yapı taşları serisinin 3. bölümü Microsoft Agent Framework'ü ele alıyor — araçlara sahip tek agentlardan belleğe sahip çok agentlı iş akışlarına kadar. İşte gerçekten önemli olan."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*Bu yazı otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

.NET'teki Building Blocks for AI serisini takip ettiyseniz: Bölüm 1 bize `IChatClient`'ı (evrensel model arayüzü), Bölüm 2 ise `Microsoft.Extensions.VectorData`'yı (semantik arama ve RAG) verdi. Her ikisi de temel yapı taşları ve kendi başlarına kullanışlı. Ama her şeyin birbirine bağlanmaya başladığı yer burası.

Bölüm 3 [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) hakkında — dürüst olmak gerekirse, .NET'te görmek için sabırsızlandığım parça bu. 1.0 Nisan'da çıktı. API kararlı. Gerçek agentlar inşa etme zamanı geldi.

## Agent gerçekte nedir (chatbot'a karşı)

Koda dalmadan önce bu ayrımı netleştirelim. Chatbot girdi alır, modeli çağırır, çıktı döndürür. Basit döngü.

Agentın *özerkliği* vardır. Bir görev hakkında akıl yürütebilir, hangi araçları kullanacağına karar verebilir, onları çağırabilir, sonuçları değerlendirebilir ve sıradaki adıma karar verebilir — her senaryo için açık adım adım mantık yazmadan. Araçlar ve talimatlar verirsiniz, orkestrasyon kendiliğinden gerçekleşir.

Şöyle düşünün: `IChatClient` bir konuşma yapmak gibi. Agent, birine görev listesi devretmek gibi.

## 10 satırda ilk agentınız

```bash
dotnet add package Microsoft.Agents.AI
```

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri(endpoint),
    new DefaultAzureCredential())
    .GetChatClient(deploymentName)
    .AsAIAgent(
        instructions: "You are good at telling jokes.",
        name: "Joker");

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate."));
```

`.AsAIAgent()` uzantı yöntemi köprüdür. MEAI'dan `.AsIChatClient()` ile aynı desen — sağlayıcının SDK'sını kararlı bir soyutlamaya sarar. Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry veya yerel modellerle çalışır.

Akış da işe yarar:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## Agenta araçlar vermek

Burada agentlar süslü chatbot olmaktan çıkar. Araçlar, modelin kullanıcının istediklerine göre çağırmaya karar verebileceği fonksiyonlardır. Yönlendirme mantığına gerek yok — model kendisi çözüyor.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

İki şeye dikkat edin. Birincisi, `AIFunctionFactory` MEAI'dan — normal bir `IChatClient` ile kullanacağınız araç fabrikasıyla aynı. Sohbet senaryoları için araç tanımladıysanız, burada da çalışır.

İkincisi, `Description` öznitelikleri çok önemlidir. Modelin bir aracın ne yaptığını ve ne zaman kullanılacağını anlama biçimi budur. Bunlara insanlar için değil, yapay zekanız için belgeler gibi davranın.

## Oturumlar: Gerçekten hatırlayan konuşmalar

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Oturum olmadan her `RunAsync` çağrısı durumsuz. Oturumla, agent hangi şakadan bahsettiğinizi bilir. `AgentSession`, turlar arasında konuşma geçmişini korur.

Üretim durumsuz servisleri için oturumlar temiz bir şekilde serileştirilebilir:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... bir yerde saklayın ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

Agentınız sunucusuz veya yatay ölçeklenmiş ortamda çalışıyorsa bu kritiktir.

## AIContextProvider: Oturumlar arası kalıcı bellek

Oturumlar, konuşma geçmişini bir oturum *içinde* korur. Peki oturumlar arasında kullanıcı hakkında bir şeyler bilmek? `AIContextProvider` bunu ele alır.

İki kancası var:
- **`ProvideAIContextAsync`** — her etkileşimden *önce* çalışır, agenta bağlam enjekte eder
- **`StoreAIContextAsync`** — her etkileşimden *sonra* çalışır, öğrenmeye ve kalıcılaştırmaya olanak tanır

Desen zarif: birden fazla sağlayıcıyı yığın şeklinde kullanabilirsiniz — biri kullanıcı tercihleri için, biri son etkileşimler için, biri ilgili belgeler için VectorData deposunu sorgulayan. Sonuncusu tam olarak Bölüm 2'den RAG deseni, artık her agent çağrısında otomatik olarak çalışıyor.

## Çok agentlı iş akışları

Framework'ün adını hak ettiği yer burası. Yürütücülerin (agentlar, fonksiyonlar, her neyse) kenarlar üzerinden bağlandığı grafik tabanlı bir iş akışı sistemi içerir.

Yerel olarak desteklenen bazı desenler:

- **Sıralı**: Agent A'nın çıktısı Agent B'ye gider
- **Eşzamanlı (fan-out/fan-in)**: Paralel olarak birden fazla agenta gönderir, sonuçları toplar
- **Koşullu yönlendirme**: Çıktıya göre farklı agentlara iş yönlendirir
- **Yazar-eleştirmen döngüleri**: Bir agent yazar, diğeri değerlendirir, onaylanana kadar döngü
- **Alt iş akışları**: İş akışlarını hiyerarşik olarak oluşturur

Yazar-eleştirmen örneği:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Temiz, okunabilir ve koşul tabanlı yönlendirme, döngü mantığını kendiniz yazmanız gerekmediği anlamına gelir.

## Human-in-the-Loop

Her şey tamamen özerk çalışmamalı. Hassas operasyonlar için — veritabanı yazmaları, finansal işlemler, iletişim gönderme — agentın yürütmeden önce bir insanın onaylamasını istersiniz.

Framework, `FunctionApprovalRequestContent` ve `FunctionApprovalResponseContent` aracılığıyla bunun için yerleşik desteğe sahip. Agent araç çağrısını önerir, uygulama kodunuz bunu kullanıcıya sunar ve yanıt yürütmenin devam edip etmeyeceğini belirler.

Kurumsal ortamlarda agentlar hakkında düşünmenin doğru yolu bu: tam özerk değil, *muhafızlı özerklik*.

## Tam tablo

Bir adım geri çekilirseniz:

- **MEAI** herhangi bir modele evrensel arayüz sağlar
- **VectorData** semantik arama yoluyla agentlarınıza kuruluşunuzun bilgisine erişim verir
- **Agent Framework** her şeyi orkestre eder — dahili olarak `IChatClient` kullanır, bağlam sağlayıcılarıyla birleşir ve iş akışları üzerinden koordinasyon sağlar

Her parça diğerleriyle birleşecek şekilde tasarlanmış. [Jeremy Likness'ın orijinal gönderisi](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) ve tam örnekler için [Agent Framework GitHub deposuna](https://github.com/microsoft/agent-framework/tree/main/dotnet) bakın.

## Sonuç

Microsoft Agent Framework Bölüm 3 gönderisi yapı taşları serisindeki döngüyü kapatıyor. Araçları kullanan, şeyleri hatırlayan ve koordine eden gerçek AI agentları — sadece chatbot değil — oluşturmak isteyen .NET geliştiricileri için bu ilerlemenin yolu.

Kararlı 1.0 sürümü, bunu üretimde inşa edebileceğiniz anlamına gelir. .NET'te agent geliştirmeye atlamak için bekliyordunuz, doğru zaman şu an.
