---
title: "Manteniment de.NET d'abril de 2026: pegats de seguretat que hauríeu d'aplicar avui"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "La versió de servei d'abril de 2026 aplega 6 CVE a.NET 10,.NET 9,.NET 8 i.NET Framework, incloses dues vulnerabilitats d'execució de codi remota."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

Les [actualitzacions de servei d'abril de 2026](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) per a.NET i.NET Framework ja estan fora, i aquesta inclou solucions de seguretat que voldreu aplicar aviat. Sis CVE pegats, incloses dues vulnerabilitats d'execució de codi remota (RCE).

## Què està pegat

Aquí teniu el resum ràpid:

|CVE|Tipus|Afecta|
|-----|------|---------|
|CVE-2026-26171|Bypass de les funcions de seguretat|.NET 10, 9, 8 +.NET Framework|
|CVE-2026-32178|**Execució de codi remota**|.NET 10, 9, 8 +.NET Framework|
|CVE-2026-33116|**Execució de codi remota**|.NET 10, 9 i 8|
|CVE-2026-32203|Denegació de servei|.NET 10, 9, 8 +.NET Framework|
|CVE-2026-23666|Denegació de servei|.NET Framework 3.0–4.8.1|
|CVE-2026-32226|Denegació de servei|.NET Framework 2.0–4.8.1|

Els dos CVE RCE (CVE-2026-32178 i CVE-2026-33116) afecten la gamma més àmplia de versions.NET i haurien de ser la prioritat.

## Versions actualitzades

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

Tots estan disponibles a través dels canals habituals: [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0), imatges de contenidors a MCR i gestors de paquets de Linux.

## Què fer

Actualitzeu els vostres projectes i pipelines CI/CD a les últimes versions de pedaços. Si utilitzeu contenidors, traieu les imatges més recents. Si esteu a.NET Framework, consulteu les [Notes de la versió de.NET Framework](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes) per trobar els pedaços corresponents.

Per a aquells que executen.NET 10 en producció (és la versió actual), 10.0.6 és una actualització obligatòria. El mateix per a.NET 9.0.15 i.NET 8.0.26 si esteu en aquestes pistes LTS. Dues vulnerabilitats RCE no són una cosa que posposeu.
