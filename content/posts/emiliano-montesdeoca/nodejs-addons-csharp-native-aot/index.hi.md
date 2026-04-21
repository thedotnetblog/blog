---
title: "Node.js के लिए C# में नेटिव ऐडऑन लिखना .NET Native AOT के साथ"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "C# Dev Kit टीम ने C++ Node.js ऐडऑन को .NET Native AOT से बदला — परिणाम क्लीनर, सुरक्षित है और केवल .NET SDK की जरूरत है।"
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *यह लेख स्वचालित रूप से अनुवादित किया गया है। मूल अंग्रेज़ी संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

यहाँ एक परिदृश्य है जो मुझे पसंद है: एक टीम जो .NET टूलिंग पर काम करती थी, उसके पास C++ में लिखे Native Node.js ऐडऑन थे जो `node-gyp` के माध्यम से कंपाइल होते थे। यह काम करता था। लेकिन इसके लिए हर डेवलपर की मशीन पर Python इंस्टॉल होना जरूरी था — Python का पुराना वर्जन, जो सिर्फ एक ऐसे पैकेज को बिल्ड करने के लिए था जिसे टीम का कोई भी सीधे नहीं छूता।

तो उन्होंने एक बहुत उचित सवाल पूछा: हमारे पास पहले से .NET SDK इंस्टॉल है, तो हम C++ क्यों लिख रहे हैं?

जवाब था Native AOT, और परिणाम वास्तव में सुंदर है। C# Dev Kit टीम के Drew Noakes ने बताया कि उन्होंने यह कैसे किया।

## बुनियादी विचार

Node.js नेटिव ऐडऑन एक शेयर्ड लाइब्रेरी है (Windows पर `.dll`, Linux पर `.so`, macOS पर `.dylib`) जिसे Node.js रनटाइम पर लोड कर सकता है। इंटरफेस को [N-API](https://nodejs.org/api/n-api.html) कहा जाता है — एक स्थिर, ABI-संगत C API। N-API को परवाह नहीं है कि लाइब्रेरी किस भाषा से बनी है, बस यह कि वह सही सिंबल एक्सपोर्ट करे।

.NET Native AOT ठीक यही कर सकता है। यह आपके C# कोड को आगे से नेटिव शेयर्ड लाइब्रेरी में कंपाइल करता है। यही पूरी चाल है।

## प्रोजेक्ट सेटअप

प्रोजेक्ट फाइल न्यूनतम है:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` SDK को `dotnet publish` पर शेयर्ड लाइब्रेरी बनाने के लिए कहता है।

## एंट्री पॉइंट एक्सपोर्ट करना

Node.js आपकी लाइब्रेरी से `napi_register_module_v1` एक्सपोर्ट करने की उम्मीद करता है। C# में, `[UnmanagedCallersOnly]` यही करता है:

```csharp
[UnmanagedCallersOnly(
    EntryPoint = "napi_register_module_v1",
    CallConvs = [typeof(CallConvCdecl)])]
public static nint Init(nint env, nint exports)
{
    Initialize();
    RegisterFunction(env, exports, "readStringValue"u8, &ReadStringValue);
    return exports;
}
```

`u8` सफ़िक्स UTF-8 स्ट्रिंग लिटरल के साथ `ReadOnlySpan<byte>` बनाता है, जो बिना किसी एन्कोडिंग आवंटन के सीधे N-API को पास होता है।

## TypeScript से कॉल करना

`dotnet publish` आपकी प्लेटफ़ॉर्म-विशिष्ट नेटिव लाइब्रेरी बनाता है। इसे `.node` में रीनेम करें और स्टैंडर्ड `require()` से उपयोग करें:

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk',
    'InstallLocation'
);
```

बस इतना। TypeScript से C# तक, बिना Python, बिना C++ के।

## निष्कर्ष

C# Dev Kit टीम ने Python/C++ ओवरहेड को क्लीन C# कोड से बदला। यह पैटर्न देखने के बाद जटिल नहीं है, और यह Native AOT का एक बेहतरीन उदाहरण है।

[.NET ब्लॉग पर मूल पोस्ट पढ़ें](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/)।
