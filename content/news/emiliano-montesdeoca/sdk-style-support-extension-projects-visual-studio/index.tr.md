---
title: "Visual Studio'da Uzantı Projeleri için SDK Tarzı Desteği"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5, VSSDK uzantı projeleri için resmi olarak desteklenen SDK tarzı proje biçimini ekliyor; derleme sürelerini %75'e kadar azaltıyor ve proje dosyalarını ~20 satıra indiriyor."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*Bu gönderi otomatik olarak çevrildi. Orijinal versiyon için [buraya tıklayın]({{< ref "index.md" >}}).*

[VSSDK uzantı projeleri için SDK tarzı desteği](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) artık Visual Studio 18.5'te resmi olarak kullanılabilir — klasik VSIX uzantı projeleri eski MPF tarzı `.csproj` biçiminden çıkabilir.

## Proje Dosyası Nasıl Değişiyor

En belirgin değişiklik proje dosyasının ne kadar küçüleceği. Tipik bir VSSDK uzantısı artık şöyle görünüyor:

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

`VSSDKBuildToolsAutoSetup=true` akıllı varsayılanları uygular: `CreateVsixContainer=true` ve eski `DeployExtension=false`. Bu tek özellik, eskiden açıkça belirtmek zorunda olduğunuz birçok şeyin yerini alıyor.

## Derleme Süresi İyileştirmesi

Fast Up-To-Date Check ve artımlı derleme desteği etkinleştiriliyor. Küçük değişiklikler içeren büyük çözümler için bu **%75'e kadar derleme süresi azalması** sağlıyor — büyük bir ana çözüm içinde bir uzantı üzerinde yineleme yapıyorsanız önemli.

## Yeni ve Mevcut Projeler

18.5'te oluşturulan yeni uzantı projeleri otomatik olarak SDK tarzını kullanıyor. Mevcut MPF tarzı uzantılar çalışmaya devam ediyor — geçiş isteğe bağlı. Geçiş için önemli bir not: uzantı XAML kullanıyorsa `<UseWpf>true</UseWpf>` ekleyin. Uzantıyı `.sln` veya `.slnx` dosyasında dağıtılabilir olarak da işaretlemeniz gerekiyor.

Vsixmanifest tasarımcısı varsayılan olarak XML düzenleyicisiyle değiştiriliyor — eski tasarımcı gerekiyorsa sağ tıklayın → Birlikte Aç.

## Ajanla Geçiş Yolu

[vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) içindeki Modernize ajanı geçişi otomatikleştirebilir. Birkaç gerçek dünya uzantısı bu şekilde zaten dönüştürüldü: Mads Kristensen'in Smart Screen, Command Explorer, Postfix Templates ve Whitespace Visualizer'ı dahil.

## Dikkat Edilecek Nokta

VisualStudio.Extensibility (daha yeni genişletilebilirlik çerçevesi) SDK tarzını zaten destekliyordu. Bu güncelleme klasik VSSDK yoluyla eşitlik sağlıyor. Tek gereksinim: Visual Studio uzantı geliştirme iş yükü.

Tüm ayrıntılar için [resmi gönderiye](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) bakın.
