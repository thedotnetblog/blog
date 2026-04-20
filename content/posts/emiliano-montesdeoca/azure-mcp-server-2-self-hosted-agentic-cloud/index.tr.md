---
title: "Azure MCP Server 2.0 Yayınlandı — Self-Hosted Agentic Bulut Otomasyonu Artık Burada"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0, self-hosted uzak dağıtımlar, 57 Azure servisi genelinde 276 araç ve kurumsal düzeyde güvenlikle kararlı sürüme ulaştı — agentic iş akışları geliştiren .NET geliştiricileri için önemli olan her şey burada."
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud" >}}).*

Son zamanlarda MCP ve Azure ile bir şeyler geliştirdiyseniz, yerel deneyimin gayet iyi çalıştığını muhtemelen zaten biliyorsunuzdur. Bir MCP server bağlayın, AI agent'ınızın Azure kaynaklarıyla konuşmasına izin verin, devam edin. Ama bu kurulumu bir ekip genelinde paylaşmanız gerektiğinde? İşte orada işler karmaşıklaşıyordu.

Artık değil. Azure MCP Server [2.0 kararlı sürüme ulaştı](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) ve başlık özelliği tam olarak kurumsal ekiplerin istediği şey: **self-hosted uzak MCP server desteği**.

## Azure MCP Server nedir?

Kısa bir hatırlatma. Azure MCP Server, [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) spesifikasyonunu uygular ve Azure yeteneklerini AI agent'larının çağırabileceği yapılandırılmış, keşfedilebilir araçlar olarak sunar. Agent'ınız ile Azure arasında standartlaştırılmış bir köprü olarak düşünebilirsiniz — sağlama, dağıtım, izleme, tanılama, hepsi tek tutarlı bir arayüz üzerinden.

Rakamlar kendisi konuşuyor: **57 Azure servisi genelinde 276 MCP aracı**. Bu ciddi bir kapsam.

## Büyük haber: self-hosted uzak dağıtımlar

Şöyle ki. MCP'yi kendi makinenizde yerel olarak çalıştırmak geliştirme ve deneyler için sorun değil. Ama gerçek bir ekip senaryosunda şunlara ihtiyacınız var:

- Geliştiriciler ve dahili agent sistemleri için paylaşımlı erişim
- Merkezi yapılandırma (tenant bağlamı, abonelik varsayılanları, telemetri)
- Kurumsal ağ ve politika sınırları
- CI/CD pipeline'larına entegrasyon

Azure MCP Server 2.0 tüm bunları ele alıyor. HTTP tabanlı taşıma, uygun kimlik doğrulama ve tutarlı yönetişimle merkezi olarak yönetilen bir dahili servis olarak dağıtabilirsiniz.

Kimlik doğrulama için iki sağlam seçenek var:

1. **Managed Identity** — [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry) ile birlikte çalışırken
2. **On-Behalf-Of (OBO) akışı** — Azure API'lerini oturum açmış kullanıcının bağlamını kullanarak çağıran OpenID Connect delegasyonu

Bu OBO akışı, .NET geliştiricileri olarak bizim için özellikle ilginç. Agentic iş akışlarınızın aşırı ayrıcalıklı bir servis hesabı yerine kullanıcının gerçek izinleriyle çalışabileceği anlamına geliyor. En az ayrıcalık ilkesi, doğrudan yerleşik.

## Güvenlik güçlendirmesi

Bu yalnızca bir özellik sürümü değil — aynı zamanda bir güvenlik sürümü. 2.0 sürümü şunları ekliyor:

- Daha güçlü endpoint doğrulaması
- Sorgu odaklı araçlarda injection kalıplarına karşı koruma
- Geliştirme ortamları için daha sıkı izolasyon kontrolleri

MCP'yi paylaşımlı bir servis olarak sunacaksanız, bu güvenceler önemli. Çok önemli.

## Nerede kullanabilirsiniz?

İstemci uyumluluk hikayesi geniş. Azure MCP Server 2.0 şunlarla çalışıyor:

- **IDE'ler**: VS Code, Visual Studio, IntelliJ, Eclipse, Cursor
- **CLI agent'ları**: GitHub Copilot CLI, Claude Code
- **Bağımsız**: basit kurulumlar için yerel server
- **Self-hosted uzak**: 2.0'ın yeni yıldızı

Ayrıca düzenlenmiş dağıtımlar için kritik olan Azure US Government ve 21Vianet tarafından işletilen Azure için sovereign bulut desteği de var.

## Bu .NET geliştiricileri için neden önemli

.NET ile agentic uygulamalar geliştiriyorsanız — ister Semantic Kernel, ister Microsoft Agent Framework, ister kendi orkestrasyon çözümünüz — Azure MCP Server 2.0, agent'larınızın Azure altyapısıyla etkileşime geçmesi için üretime hazır bir yol sunuyor. Özel REST wrapper'ları yok. Servise özgü entegrasyon kalıpları yok. Sadece MCP.

Birkaç gün önce yayınlanan [MCP Apps için fluent API](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) ile birleşince .NET MCP ekosistemi hızla olgunlaşıyor.

## Başlarken

Kendi yolunuzu seçin:

- **[GitHub Repo](https://aka.ms/azmcp)** — kaynak kodu, dokümantasyon, her şey
- **[Docker Image](https://aka.ms/azmcp/download/docker)** — container'lı dağıtım
- **[VS Code Extension](https://aka.ms/azmcp/download/vscode)** — IDE entegrasyonu
- **[Self-hosting rehberi](https://aka.ms/azmcp/self-host)** — 2.0'ın öne çıkan özelliği

## Sonuç

Azure MCP Server 2.0, demoda gösterişli görünmeyen ama pratikte her şeyi değiştiren altyapı yükseltmesi türünden. Uygun kimlik doğrulama, güvenlik güçlendirmesi ve sovereign bulut desteğiyle self-hosted uzak MCP, gerçek ekiplerin Azure üzerinde gerçek agentic iş akışları oluşturması için hazır olduğu anlamına geliyor. "Kurumsal kullanıma hazır" sinyalini bekliyordunuz — işte bu.
