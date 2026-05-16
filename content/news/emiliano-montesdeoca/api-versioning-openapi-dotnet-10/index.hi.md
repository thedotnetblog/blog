---
title: ".NET 10 में API Versioning को OpenAPI के साथ मिलाना"
date: 2026-05-07
author: "Emiliano Montesdeoca"
description: "Asp.Versioning v10 पहला संस्करण है जो .NET 10 और Microsoft.AspNetCore.OpenApi दोनों को आधिकारिक रूप से सपोर्ट करता है, और प्रत्येक API संस्करण के लिए अलग OpenAPI दस्तावेज़ तैयार करता है।"
tags:
  - .NET
  - API Design
  - OpenAPI
  - .NET 10
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

[.NET 10 में API Versioning को OpenAPI के साथ मिलाना](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/) — Microsoft MVP सैंडर तेन ब्रिंके का गेस्ट पोस्ट — नए `Asp.Versioning` v10 पैकेज को समझाता है, जो .NET 10 और बिल्ट-इन `Microsoft.AspNetCore.OpenApi` लाइब्रेरी के लिए विशेष रूप से बनाया गया पहला संस्करण है।

## Asp.Versioning v10: नए OpenAPI स्टैक के लिए बनाया गया

पिछला `Asp.Versioning` v8.x अभी भी implicit roll-forward के ज़रिए .NET 10 पर काम करता है, लेकिन v10 पहला संस्करण है जो विशेष रूप से `Microsoft.AspNetCore.OpenApi` के लिए डिज़ाइन किया गया है। मुख्य सेटअप `AddApiVersioning` को `AddApiExplorer` के साथ चेन करना है, साथ ही हर उस version के लिए अलग `AddOpenApi` कॉल जिसे आप expose करना चाहते हैं:

```csharp
builder.Services.AddApiVersioning(options => {
    options.DefaultApiVersion = new ApiVersion(1, 0);
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.ReportApiVersions = true;
})
.AddApiExplorer(options => {
    options.GroupNameFormat = "'v'VVV";
    options.SubstituteApiVersionInUrl = true;
});

builder.Services.AddOpenApi("v1");
builder.Services.AddOpenApi("v2");
```

इससे `/openapi/v1.json` और `/openapi/v2.json` पर अलग-अलग दस्तावेज़ बनते हैं।

## Versioning रणनीतियाँ: URL Path, Query String, Header, Media Type

पैकेज चार रणनीतियों को सपोर्ट करता है। URL Path versioning (`/api/v1/resource`) public APIs के लिए सबसे आम है। Query string (`?version=1.0`) और custom header (`X-API-Version`) internal services में लोकप्रिय हैं। `Accept` header के ज़रिए media type versioning वह है जो GitHub अपनी REST API के लिए उपयोग करता है।

## Minimal APIs और Controllers दोनों के लिए सपोर्ट

Minimal APIs के लिए, एक version set बनाएं और हर route को एक specific version पर map करें:

```csharp
var versionSet = app.NewApiVersionSet()
    .HasApiVersion(new ApiVersion(1, 0))
    .HasApiVersion(new ApiVersion(2, 0))
    .Build();

app.MapGet("/users", GetUsersV1).WithApiVersionSet(versionSet).MapToApiVersion(1);
app.MapGet("/users", GetUsersV2).WithApiVersionSet(versionSet).MapToApiVersion(2);
```

Controllers के लिए, class और action level पर `[ApiVersion("1.0")]` और `[MapToApiVersion("1.0")]` attributes लगाए जाते हैं।

## SwaggerUI और Scalar बिना अतिरिक्त सेटअप के काम करते हैं

`Swashbuckle.AspNetCore.SwaggerUI` और `Scalar.AspNetCore` दोनों आसानी से integrate होते हैं — बस per-version document URLs की ओर point करें और बिना extra plumbing के version-aware UI मिलती है।

## Code Examples .NET 10 के File-Based Apps का उपयोग करते हैं

आर्टिकल के उदाहरण C# 14 / .NET 10 की नई file-based app feature का उपयोग करते हैं: एक `.cs` फ़ाइल को `dotnet <filename>.cs` से चलाएं, कोई project file नहीं चाहिए। इससे snippets self-contained हैं और locally try करना आसान है।

## निष्कर्ष

यदि आप .NET 10 use कर रहे हैं और third-party middleware जोड़े बिना clean, versioned OpenAPI contracts चाहते हैं, तो `Asp.Versioning` v10 ही आधिकारिक रास्ता है।

पूरा आर्टिकल पढ़ें: [.NET 10 में API Versioning को OpenAPI के साथ मिलाना](https://devblogs.microsoft.com/dotnet/api-versioning-in-dotnet-10-applications/)
