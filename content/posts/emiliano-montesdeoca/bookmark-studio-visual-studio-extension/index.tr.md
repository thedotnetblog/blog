---
title: "Bookmark Studio, Visual Studio Yer İşaretlerine Slot Tabanlı Gezinti ve Paylaşım Getiriyor"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Mads Kristensen'in yeni Bookmark Studio uzantısı, Visual Studio yer işaretlerine klavye odaklı slot gezintisi, bir yer işareti yöneticisi, renkler, etiketler ve dışa aktarma/paylaşma özellikleri ekliyor."
tags:
  - visual-studio
  - extensions
  - productivity
  - developer-tools
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "bookmark-studio-visual-studio-extension" >}}).*

Visual Studio'daki yer işaretleri her zaman... idare ederdi. Bir tane koyarsınız, bir sonrakine geçersiniz, hangisinin ne olduğunu unutursunuz. Çalışırlar, ama hiçbir zaman güçlü diyebileceğiniz bir özellik olmadılar.

Mads Kristensen, eğer yer işaretlerini düzenli kullanıyorsanız muhtemelen karşılaştığınız boşlukları tam olarak dolduran deneysel bir uzantı olan [Bookmark Studio'yu yayımladı](https://devblogs.microsoft.com/visualstudio/bookmark-studio-evolving-bookmarks-in-visual-studio/).

## Slot tabanlı gezinti

Temel yenilik şu: yer işaretleri artık 1–9 numaralı slotlara atanabilir ve doğrudan `Alt+Shift+1` ile `Alt+Shift+9` tuş kombinasyonlarıyla erişilebilir. Yeni yer işaretleri otomatik olarak bir sonraki boş slotu alır; dolayısıyla çoğu durumda herhangi bir yapılandırma gerektirmeden hızlı gezinti çalışır.

Bu basit görünüyor, ama yer işaretlerini "bir yerlerde bazı yer işaretlerim var" durumundan "Slot 3 API controller'ım, Slot 5 servis katmanı, Slot 7 test" haline getiriyor. Bu tür uzamsal bellek, odaklanılmış çalışma oturumlarında gezintiyi neredeyse anında yapıyor.

## Yer İşareti Yöneticisi

Yeni bir araç penceresi, tüm yer işaretlerinizi tek bir yerde ad, dosya, konum, renk veya slota göre filtreleme seçeneğiyle gösteriyor. Herhangi bir yer işaretine atlamak için çift tıklayabilir ya da klavyeyle gezinebilirsiniz.

Eğer hiç beş-altı yer işaretinden fazlasına sahip olup hangisinin ne olduğunu takip edemediğiniz olduysa, bu tek başına uzantıyı kurmaya değer.

## Etiketler, renkler ve klasörlerle organizasyon

Yer işaretlerine isteğe bağlı olarak etiket ve renk eklenebilir, klasörlere gruplandırılabilir. Bunların hiçbiri zorunlu değil — mevcut yer işareti iş akışınız çalışmaya devam eder. Ancak karmaşık bir sorunu hata ayıkladığınızda ya da tanıdık olmayan bir kod tabanını keşfettiğinizde, yer işaretlerinizi renklendirebilmek ve etiketleyebilmek yararlı bir bağlam katıyor.

Tüm meta veriler çözüm başına saklanır; dolayısıyla yer işareti organizasyonunuz oturumlar arasında kalıcı olur.

## Dışa aktarma ve paylaşma

Bilmeden istediğim özellik bu. Bookmark Studio, yer işaretlerini düz metin, Markdown veya CSV olarak dışa aktarmanıza izin veriyor. Yani şunları yapabilirsiniz:

- Pull request açıklamalarına yer işareti yollarını eklemek
- İnceleme izlerini takım arkadaşlarıyla paylaşmak
- Yer işareti kümelerini repolar veya dallar arasında taşımak

Yer işaretleri yalnızca kişisel bir gezinti aracı olmaktan çıkıp "işte bu kodun geçtiği yol" mesajını iletmenin bir yoluna dönüşüyor.

## Kod hareketini izleyen yer işaretleri

Bookmark Studio, yer işaretlerini bağlandıkları metne göre takip eder; böylece düzenleme yaparken yanlış satırlara kaymazlar. Hiç bir hata ayıklama oturumunda yer işaretleri koyup bir yeniden yapılandırmanın ardından hepsinin yanlış satırlara işaret ettiğini gördüyseniz — bu durumu düzeltiyor.

## Sonuç

Bookmark Studio hiçbir şeyi yeniden icat etmiyor. Yıllardır "yeterince iyi" olan bir özelliği alıp odaklanılmış geliştirme için gerçekten kullanışlı hale getiriyor. Slot gezintisi, Yer İşareti Yöneticisi ve dışa aktarma özellikleri öne çıkanlardır.

[Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.BookmarkStudio)'dan indirin ve deneyin.
