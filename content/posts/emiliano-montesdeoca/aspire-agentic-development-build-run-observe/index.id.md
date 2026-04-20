---
title: ".NET Aspire 13.2 Ingin Menjadi Sahabat Terbaik Agen AI Anda"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 all-in pada pengembangan agentik — output CLI terstruktur, eksekusi terisolasi, lingkungan yang menyembuhkan sendiri, dan data OpenTelemetry penuh agar agen AI Anda benar-benar dapat membangun, menjalankan, dan mengamati aplikasi Anda."
tags:
  - aspire
  - dotnet
  - ai
  - cli
  - telemetry
  - developer-tools
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "aspire-agentic-development-build-run-observe" >}}).*

Anda tahu momen ketika agen coding AI Anda menulis kode yang solid, Anda bersemangat, kemudian semuanya berantakan saat mencoba *menjalankannya*? Konflik port, phantom process, variabel lingkungan yang salah — tiba-tiba agen Anda membakar token untuk men-debug masalah startup alih-alih membangun fitur.

Tim Aspire baru saja merilis [post yang sangat bijaksana](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) tentang masalah ini, dan jawaban mereka menarik: Aspire 13.2 dirancang tidak hanya untuk manusia, tetapi untuk agen AI.

## Aspire sebagai infrastruktur agen

Inilah yang dibawa Aspire 13.2 ke meja pengembangan agentik:

**Seluruh stack dalam kode bertipe.** AppHost mendefinisikan topologi lengkap — dalam TypeScript atau C# yang dapat dikompilasi:

```typescript
import { createBuilder } from './.modules/aspire.js';

const builder = await createBuilder();

const postgres = await builder.addPostgres("pg").addDatabase("catalog");
const cache = await builder.addRedis("cache");

const api = await builder
  .addNodeApp("api", "./api", "src/index.ts")
  .withHttpEndpoint({ env: "PORT" })
  .withReference(postgres)
  .withReference(cache);

await builder
  .addViteApp("frontend", "./frontend")
  .withReference(api)
  .waitFor(api);

await builder.build().run();
```

**Satu perintah untuk semuanya.** Alih-alih menyulap `docker compose up`, `npm run dev`, dan skrip startup database — semuanya hanya `aspire start`.

**Mode terisolasi untuk agen paralel.** Dengan `--isolated`, setiap jalankan Aspire mendapat port acak sendiri dan rahasia pengguna terpisah.

**Mata agen melalui telemetri.** Aspire CLI mengekspos data OpenTelemetry penuh selama development — trace, metrik, log terstruktur.

## Analogi bowling bumper

Tim Aspire menggunakan analogi yang bagus: pikirkan Aspire sebagai bumper jalur bowling untuk agen AI. Jika agennya tidak sempurna (dan memang tidak akan), bumper mencegahnya melempar ke selokan.

## Kesimpulan

Aspire 13.2 bukan hanya framework aplikasi terdistribusi — ini menjadi infrastruktur agen yang esensial. Baca [post lengkap](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/) dari tim Aspire.
