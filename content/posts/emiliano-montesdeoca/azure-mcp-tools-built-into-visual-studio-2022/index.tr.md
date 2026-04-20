---
title: "Azure MCP Araçları Artık Visual Studio 2022'ye Yerleşik — Uzantı Gerekmez"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Azure MCP araçları, Visual Studio 2022'deki Azure geliştirme iş yükünün bir parçası olarak geliyor. 45 Azure hizmetinde 230'dan fazla araç, yüklenecek sıfır uzantı."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-mcp-tools-built-into-visual-studio-2022" >}}).*

Azure MCP araçlarını ayrı uzantı aracılığıyla Visual Studio'da kullandıysanız, prosedürü biliyorsunuzdur — VSIX yükle, yeniden başlat, bozulmamasını umut et, sürüm uyumsuzluklarını yönet. Bu sürtünme gitti.

Yun Jung Choi, Azure MCP araçlarının artık Visual Studio 2022'deki Azure geliştirme iş yükünün bir parçası olarak doğrudan geldiğini [duyurdu](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/). Uzantı yok. VSIX yok.

## Nasıl etkinleştirilir

1. Visual Studio 2022 **17.14.30** veya üstüne güncelleyin
2. **Azure development** iş yükünün yüklü olduğundan emin olun
3. GitHub Copilot Chat'i açın
4. **Araç seç** düğmesine tıklayın (iki İngiliz anahtarı simgesi)
5. **Azure MCP Server**'ı etkinleştirin

## Notlar

Araçlar varsayılan olarak devre dışıdır — etkinleştirmeniz gerekir. Visual Studio'da yaşayan .NET geliştiricileri için bu, Azure portalına bağlam geçişi yapma nedenini azaltıyor.
