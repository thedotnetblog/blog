---
title: "Memperbaiki Pemrosesan Batch Semua-atau-Tidak-Ada di Azure Service Bus"
date: 2026-05-10
author: "Emiliano Montesdeoca"
description: "Azure Functions kini mendukung penyelesaian per pesan untuk pemicu Service Bus, memungkinkan Anda menyelesaikan, mengabaikan, men-dead-letter, atau menangguhkan setiap pesan secara independen dalam satu batch."
tags:
  - .NET
  - Azure Service Bus
  - Messaging
  - Reliability
---

*Posting ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "index.md" >}}).*

[Penyelesaian per pesan untuk Azure Service Bus di Azure Functions](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/) memecahkan masalah kegagalan batch semua-atau-tidak-ada yang klasik: jika satu pesan dalam batch 50 gagal, semua 50 dikembalikan ke antrean.

## Masalah batch

Dalam model lama, Azure Functions memproses pesan dalam mode batch dengan hasil biner: seluruh batch berhasil atau seluruh batch gagal. Satu pesan yang salah format berarti semua 49 pesan yang sehat dikembalikan ke antrean, diproses ulang, dan diperiksa ulang idempotency-nya — membuang sumber daya komputasi, meningkatkan biaya, dan menciptakan loop percobaan ulang yang sulit diputus.

## Empat aksi penyelesaian per pesan

Penyelesaian per pesan memberikan empat aksi independen pada setiap pesan:

- **Selesaikan (Complete)** — hapus pesan dari antrean (pemrosesan berhasil)
- **Abaikan (Abandon)** — kembalikan untuk percobaan ulang, dengan opsi memodifikasi properti aplikasi (berguna untuk kesalahan sementara)
- **Dead-letter** — pindahkan ke antrean dead-letter (pesan beracun, tidak dapat dipulihkan)
- **Tangguhkan (Defer)** — simpan tetapi hanya dapat diambil berdasarkan nomor urut

Dalam batch 50, Anda sekarang dapat menyelesaikan 47, mengabaikan 2 dengan kesalahan sementara, dan men-dead-letter 1 pesan yang salah format — semuanya dalam satu pemanggilan fungsi.

## Contoh kode

**.NET (C#):**
```csharp
[Function("ProcessOrderBatch")]
public async Task Run(
    [ServiceBusTrigger("orders-queue", IsBatched = true)] ServiceBusReceivedMessage[] messages,
    ServiceBusMessageActions messageActions)
{
    foreach (var message in messages)
    {
        try {
            await messageActions.CompleteMessageAsync(message);
        } catch {
            await messageActions.DeadLetterMessageAsync(message);
        }
    }
}
```

**Node.js/TypeScript:**
```typescript
import '@azure/functions-extensions-servicebus';
export async function processOrderBatch(sbContext, context) {
    const { messages, actions } = sbContext;
    for (const message of messages) {
        try {
            await processOrder(messageBodyAsJson(message));
            await actions.complete(message);
        } catch {
            await actions.deadletter(message);
        }
    }
}
app.serviceBusQueue('processOrderBatch', {
    sdkBinding: true,
    autoCompleteMessages: false,
    cardinality: 'many',
    handler: processOrderBatch
});
```

**Python V2:**
```python
@app.service_bus_queue_trigger(auto_complete_messages=False, cardinality="many")
def process_order_batch(messages, message_actions):
    for message in messages:
        try:
            process_order(json.loads(message.body))
            message_actions.complete(message)
        except:
            message_actions.deadletter(message)
```

## Backoff eksponensial tanpa infrastruktur tambahan

Menggabungkan `abandon` dengan properti aplikasi yang dimodifikasi memungkinkan backoff eksponensial langsung di antrean — tanpa Durable Functions atau antrean tambahan. Simpan hitungan percobaan ulang di properti aplikasi pesan, baca saat pengiriman ulang, dan hitung penundaan Anda. Pola ini dulunya memerlukan orkestrasi yang signifikan; sekarang hanya beberapa baris di penangan percobaan ulang.

## Keuntungan efisiensi batch

Model pra-batch lama mengirimkan setiap pesan sebagai pemanggilan fungsi terpisah: 50 pesan berarti 50 koneksi, 50 cold start, 50 teardown. Model baru menangani semua 50 dalam satu pemanggilan, dan penyelesaian per pesan berarti Anda tidak mengorbankan efisiensi tersebut saat terjadi kesalahan.

Baca posting lengkap di [devblogs.microsoft.com](https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/).
