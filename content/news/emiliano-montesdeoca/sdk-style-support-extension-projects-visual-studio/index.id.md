---
title: "Dukungan SDK-Style untuk Proyek Ekstensi di Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 menghadirkan format proyek SDK-style yang didukung resmi untuk ekstensi VSSDK, memangkas waktu build hingga 75% dan menyederhanakan file proyek menjadi ~20 baris."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

[Dukungan SDK-style untuk proyek ekstensi berbasis VSSDK](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) kini resmi hadir di Visual Studio 18.5 — proyek ekstensi VSIX klasik dapat meninggalkan format `.csproj` gaya MPF yang lama.

## Apa yang berubah dalam file proyek

Perubahan terbesar yang terlihat adalah betapa lebih kecilnya file proyek. Ekstensi VSSDK tipikal kini terlihat seperti ini:

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

`VSSDKBuildToolsAutoSetup=true` menerapkan default yang masuk akal: `CreateVsixContainer=true` dan `DeployExtension=false` yang lama. Satu properti ini menggantikan sebagian besar yang sebelumnya harus ditentukan secara eksplisit.

## Peningkatan waktu build

Fast Up-To-Date Check dan dukungan build inkremental disertakan. Untuk solusi besar dengan perubahan kecil, ini menghasilkan **pengurangan waktu build hingga 75%** — signifikan jika Anda mengerjakan ekstensi dalam solusi host yang besar.

## Proyek baru vs. yang sudah ada

Proyek ekstensi baru yang dibuat di 18.5 secara otomatis menggunakan SDK-style. Ekstensi gaya MPF yang sudah ada terus berfungsi — migrasi bersifat opsional. Satu hal yang perlu diperhatikan saat migrasi: tambahkan `<UseWpf>true</UseWpf>` jika ekstensi Anda menggunakan XAML. Anda juga perlu menandai ekstensi sebagai dapat di-deploy di file `.sln` atau `.slnx`.

Desainer vsixmanifest digantikan oleh editor XML sebagai default — klik kanan → Open With jika Anda ingin desainer lama.

## Jalur migrasi agentik

Agen Modernize di [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) dapat mengotomatiskan migrasi. Beberapa ekstensi nyata sudah dikonversi dengan cara ini: Smart Screen, Command Explorer, Postfix Templates, dan Whitespace Visualizer milik Mads Kristensen.

## Perlu dicatat

VisualStudio.Extensibility (framework ekstensibilitas yang lebih baru) sudah mendukung SDK-style. Pembaruan ini membawa keseimbangan dengan jalur VSSDK klasik. Satu-satunya persyaratan adalah workload pengembangan ekstensi Visual Studio.

Detail lengkap di [pos resmi](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
