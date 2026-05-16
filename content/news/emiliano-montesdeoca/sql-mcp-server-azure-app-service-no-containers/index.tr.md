---
title: "SQL MCP Server Azure App Service'te — Konteyner Gerekmez"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "SQL MCP Server artık Docker veya Kubernetes olmadan Azure App Service'te çalışabiliyor. SQL veritabanlarıyla iletişim kuran AI ajanları geliştiren .NET geliştiricileri için ne anlama geldiğini ele alıyoruz."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*Bu yazı otomatik olarak çevrilmiştir. Orijinal sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

Dürüst olmak gerekirse: bir öğreticide "konteyner gerektirir" ifadesini her gördüğümde içimden bir ah çıkıyor. Konteynerler harika — ta ki ekibinizin bir konteyner stratejisi olmayana kadar, ve basit görünen bir özellik aniden kimsenin planlamadığı beklenmedik orkestrasyon karmaşıklığına takılıp kalıyor.

İşte bu yüzden bu dikkatimi çekti. SQL MCP Server artık Azure App Service'te çalışabiliyor — Docker yok, Kubernetes yok, yalnızca SQL veritabanınızı MCP, REST ve GraphQL üzerinden açığa çıkaran aynı Data API Builder (DAB) yapılandırma dosyasıyla.

## SQL MCP Server Nedir?

Henüz tanışmadıysanız hızlı bir giriş. SQL MCP Server, AI ajanınız ile SQL veritabanı arasına konumlanır. Ajana veritabanına doğrudan erişim vermek yerine (berbat bir fikir), tablolarınızı ve görünümlerinizi tanımlı izinlere sahip varlıklar olarak bir soyutlama katmanıyla açığa çıkarır.

[Data API Builder](https://learn.microsoft.com/tr-tr/azure/data-api-builder/) üzerine inşa edilmiştir; bu da tek bir yapılandırma dosyasının MCP *ve* REST *ve* GraphQL'i aynı anda yönettiği anlamına gelir. Ajanınız MCP uç noktasıyla konuşur. Geleneksel uygulamanız REST veya GraphQL ile konuşur. Aynı yapılandırma, aynı çalışma zamanı, farklı yüzeyler.

Bu gerçekten kullanışlı — iki ayrı API katmanını sürdürmenize gerek yok.

## Konteyner Sorunu (ve Çözümü)

SQL MCP Server'ın orijinal dağıtım modeli konteyner kullanıyordu. Pek çok ekip için iyi çalışıyor — ama hepsi için değil. Birçok .NET ekibi Azure App Service veya sanal makinelerde standartlaşmış. Yalnızca bir SQL uç noktasını açığa çıkarmak için konteyner çalışma zamanı gerektirmek, kimsenin istemediği bir sürtünme yaratıyor.

Yeni kılavuz konteyneri tamamen atlama yöntemini gösteriyor. Her şey `dab start` komutuyla çalışıyor ve App Service üzerinde standart bir .NET 8 web süreci olarak barındırılıyor.

```bash
# Data API Builder'ı yükleyin
dotnet tool install microsoft.dataapibuilder --prerelease -g

# Yapılandırmayı başlatın
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# Bir varlık ekleyin
dab add products --source dbo.products --permissions "authenticated:*"

# App Service kimlik doğrulama sağlayıcısını yapılandırın
dab configure --runtime.host.authentication.provider AppService

# Sunucuyu başlatın
dab start
```

Bu noktada `/mcp`'de MCP'niz var, aynı süreçten REST ve GraphQL var — ve hiçbir şey bir konteynerde çalışmıyor.

## Paylaşılan API Anahtarı Olmadan Kimlik Doğrulama

En çok değer verdiğim kısım bu. App Service'e dağıtırken Microsoft Entra ID'yi kimlik doğrulama sağlayıcısı olarak yapılandırıyorsunuz. Yapılandırma dosyalarında paylaşılan sır yok, döndürülecek API anahtarı yok.

Bağlantı dizesi App Service ortam değişkenlerinde tutuluyor (`dab-config.json`'da değil) ve MCP uç noktası platform kimlik doğrulamasıyla korunuyor. Azure iş yükleriniz Entra ID ile zaten uyumluysa bu doğal bir şekilde entegre oluyor.

Yerel geliştirme için `Simulator` moduna ve STDIO aktarımına geçin. Dağıtımdan önce `AppService` moduna geri dönün. Temiz ve açık.

## App Service'e Dağıtım

```bash
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

Ardından ekibinizin halihazırda kullandığı kod dağıtım yöntemini kullanarak DAB projenizi dağıtın. Önemli nokta: bu bir **kod** dağıtımıdır, konteyner dağıtımı değil.

## .NET Geliştiricileri İçin Neden Önemli

.NET'te AI ajanları geliştiriyorsanız, er ya da geç ajanınızın bir veritabanıyla iletişim kurması gerekecek. SQL MCP Server, ham bağlantı dizelerini açığa çıkarmadan bunu yapmanın yapılandırılmış bir yolunu sunuyor.

Tam kılavuzu [orijinal blog yazısında](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) ve [GitHub örnek deposunda](https://github.com/Azure-Samples/SQL-MCP-NoContainer) inceleyin.

## Sonuç

App Service'teki SQL MCP Server, konteyner stratejisi olmaksızın ajanlara yapılandırılmış SQL veri erişimi sağlamak isteyen .NET ekipleri için pratik bir seçenek. Deneyin — ajanlarınız temiz API yüzeyini takdir edecek.
