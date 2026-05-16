---
title: "Visual Studio में एक्सटेंशन प्रोजेक्ट्स के लिए SDK-Style सपोर्ट"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 VSSDK-आधारित एक्सटेंशन के लिए आधिकारिक रूप से समर्थित SDK-style प्रोजेक्ट फॉर्मेट लाता है, जिससे बिल्ड समय 75% तक कम होता है और प्रोजेक्ट फ़ाइलें ~20 लाइनों तक सिमट जाती हैं।"
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}}).*

[VSSDK-आधारित एक्सटेंशन प्रोजेक्ट्स के लिए SDK-Style सपोर्ट](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) अब Visual Studio 18.5 में आधिकारिक है — क्लासिक VSIX एक्सटेंशन प्रोजेक्ट्स पुराने MPF-Style `.csproj` फॉर्मेट को छोड़ सकते हैं।

## प्रोजेक्ट फ़ाइल में क्या बदलता है

सबसे बड़ा दृश्य परिवर्तन यह है कि प्रोजेक्ट फ़ाइल कितनी छोटी हो जाती है। एक विशिष्ट VSSDK एक्सटेंशन अब इस तरह दिखती है:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net472</TargetFramework>
    <VSSDKBuildToolsAutoSetup>true</VSSDKBuildToolsAutoSetup>
    <VsixDeployOnDebug>true</VsixDeployOnDebug>
    <GeneratePkgDefFile>true</GeneratePkgDefFile>
  </PropertyGroup>
  <ItemGroup><ProjectCapability Include="CreateVsixContainer" /></ItemGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.VisualStudio.SDK" Version="17.14.40265" ExcludeAssets="runtime" />
    <PackageReference Include="Microsoft.VSSDK.BuildTools" Version="18.5.38461" />
  </ItemGroup>
</Project>
```

`VSSDKBuildToolsAutoSetup=true` उचित डिफ़ॉल्ट लागू करता है: `CreateVsixContainer=true` और पुराना `DeployExtension=false`। यह एकल प्रॉपर्टी उस सब कुछ की जगह लेती है जो पहले स्पष्ट रूप से लिखनी पड़ती थी।

## बिल्ड समय में सुधार

Fast Up-To-Date Check और इंक्रीमेंटल बिल्ड सपोर्ट शामिल है। बड़े सॉल्यूशन में छोटे बदलावों के लिए यह **75% तक बिल्ड समय में कमी** का अनुवाद करता है — महत्वपूर्ण है यदि आप किसी बड़े होस्ट सॉल्यूशन के अंदर एक एक्सटेंशन पर काम कर रहे हैं।

## नए बनाम मौजूदा प्रोजेक्ट्स

18.5 में बनाए गए नए एक्सटेंशन प्रोजेक्ट स्वचालित रूप से SDK-style का उपयोग करते हैं। मौजूदा MPF-style एक्सटेंशन काम करती रहती हैं — माइग्रेशन वैकल्पिक है। माइग्रेशन के दौरान ध्यान रखें: `<UseWpf>true</UseWpf>` जोड़ें यदि आपकी एक्सटेंशन XAML का उपयोग करती है। आपको `.sln` या `.slnx` फ़ाइल में एक्सटेंशन को deployable के रूप में चिह्नित भी करना होगा।

vsixmanifest डिज़ाइनर को डिफ़ॉल्ट रूप से XML एडिटर से बदल दिया गया है — पुराना डिज़ाइनर चाहिए तो राइट-क्लिक → Open With।

## एजेंटिक माइग्रेशन पाथ

[vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) में Modernize एजेंट माइग्रेशन को स्वचालित कर सकता है। Mads Kristensen की Smart Screen, Command Explorer, Postfix Templates और Whitespace Visualizer सहित कई वास्तविक एक्सटेंशन पहले ही इस तरह से कनवर्ट हो चुकी हैं।

## ध्यान देने योग्य

VisualStudio.Extensibility (नया एक्सटेंसिबिलिटी फ्रेमवर्क) पहले से ही SDK-style को सपोर्ट करता था। यह अपडेट क्लासिक VSSDK पाथ के साथ समानता लाता है। एकमात्र आवश्यकता Visual Studio एक्सटेंशन डेवलपमेंट वर्कलोड है।

[आधिकारिक पोस्ट](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) में पूरी जानकारी।
