---
title: "Agent Harnesses Itu Penting Karena Prompts Saja Tidak Cukup"
date: 2026-06-20
author: "Emiliano Montesdeoca"
description: "Walkthrough claw dan harness Microsoft Agent Framework yang baru adalah pengingat berguna bahwa agen nyata membutuhkan runtime shell di sekitar model: tools, planning, memory, sessions, dan execution loop yang praktis."
tags:
  - Agent Framework
  - AI
  - .NET
  - Developer Experience
  - Microsoft Foundry
---

Salah satu kesalahan termudah dalam pengembangan agen adalah berpikir bahwa prompt adalah produknya.

Bukan.

Walkthrough **agent harness dan claw** baru dari tim Microsoft Agent Framework berharga karena tetap fokus pada bagian yang benar-benar menentukan apakah suatu agen terasa dapat digunakan: runtime shell di sekitar model.

Itu termasuk:

- tools
- planning
- session state
- memory
- execution modes
- console atau antarmuka yang dapat digunakan untuk iterasi

Di situlah agen berhenti menjadi demo pintar dan mulai terasa seperti perangkat lunak.

## Pola harness adalah pola yang praktis

Yang saya suka di sini adalah betapa mudahnya ide ini didekati.

Anda mulai dengan chat client.

Kemudian Anda membungkusnya ke dalam harness dengan instruksi dan tools.

Kemudian Anda menjalankannya melalui shell yang mendukung planning, todos, sessions, dan interaksi streaming.

Itu adalah pola yang sehat karena memisahkan concerns dengan jelas:

- model menangani penalaran
- harness menangani perilaku runtime
- aplikasi memutuskan tools dan pengalaman mana yang penting

## Ini sangat cocok dengan cara pengembang .NET membangun sistem

Ide harness juga cocok dengan pola pikir .NET.

Kami biasanya lebih baik ketika perilaku runtime bersifat eksplisit dan dapat dikomposisikan. Middleware, pipelines, options, providers, dan adapters semuanya terasa alami di dunia ini.

Itulah mengapa saya pikir Agent Framework memiliki peluang bagus untuk diterima oleh pengembang .NET. Ia tidak memaksa semua orang ke dalam satu abstraksi ajaib. Ia memberikan potongan runtime terstruktur yang dapat Anda hubungkan bersama.

## Pendapat saya

Bagian paling berguna dari postingan ini adalah pengingat bahwa agen membutuhkan lebih dari sekadar model yang baik dan string instruksi yang cerdas.

Mereka membutuhkan runtime shell yang memberi mereka struktur, memory, akses tool, planning, dan loop pengembang yang dapat digunakan.

Itulah yang diberikan harness kepada Anda.

Dan sejujurnya, itulah mengapa pola ini layak diperhatikan.

Postingan asli: [Meet your agent harness and claw](https://devblogs.microsoft.com/agent-framework/meet-your-agent-harness-and-claw/)