---
title: "Agent Skills di .NET Kini Benar-Benar Fleksibel"
date: 2026-04-14
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework kini mendukung tiga cara penulisan skill — file, kelas, dan kode inline — semuanya disusun melalui satu provider. Inilah alasannya penting dan cara menggunakan masing-masing."
tags:
  - ".NET"
  - "Agent Framework"
  - "AI"
  - "Semantic Kernel"
  - "Azure"
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "agent-skills-dotnet-three-authoring-patterns" >}}).*

Jika Anda membangun agen dengan Microsoft Agent Framework, Anda sudah tahu caranya: Anda mendefinisikan skill, menghubungkannya ke provider, dan membiarkan agen menentukan mana yang harus dipanggil. Yang baru adalah *bagaimana* Anda menulis skill tersebut — dan lompatan fleksibilitasnya signifikan.

Pembaruan terbaru memperkenalkan tiga pola authoring berbeda untuk agent skill: **berbasis file**, **berbasis kelas**, dan **didefinisikan kode inline**. Ketiganya terhubung ke satu `AgentSkillsProviderBuilder`, artinya Anda bisa mix and match tanpa logika routing.

## Skill berbasis file: titik awal

Skill berbasis file persis seperti namanya — direktori di disk dengan file `SKILL.md`, skrip opsional, dan dokumen referensi:

```
skills/
└── onboarding-guide/
    ├── SKILL.md
    ├── scripts/
    │   └── check-provisioning.py
    └── references/
        └── onboarding-checklist.md
```

Frontmatter `SKILL.md` mendeklarasikan nama dan deskripsi skill, dan bagian instruksi memberi tahu agen cara menggunakan skrip dan referensi.

Kemudian Anda menghubungkannya dengan `SubprocessScriptRunner.RunAsync`:

```csharp
var skillsProvider = new AgentSkillsProvider(
    Path.Combine(AppContext.BaseDirectory, "skills"),
    SubprocessScriptRunner.RunAsync);
```

## Skill berbasis kelas: kirim via NuGet

Di sinilah yang menarik bagi tim. Skill berbasis kelas mewarisi dari `AgentClassSkill<T>` dan menggunakan atribut seperti `[AgentSkillResource]` dan `[AgentSkillScript]`:

```csharp
public sealed class BenefitsEnrollmentSkill : AgentClassSkill<BenefitsEnrollmentSkill>
{
    public override AgentSkillFrontmatter Frontmatter { get; } = new(
        "benefits-enrollment",
        "Enroll an employee in health, dental, or vision plans.");

    [AgentSkillScript("enroll")]
    private static string Enroll(string employeeId, string planCode)
    {
        bool success = HrClient.EnrollInPlan(employeeId, planCode);
        return JsonSerializer.Serialize(new { success, employeeId, planCode });
    }
}
```

Sebuah tim bisa mengemas ini sebagai paket NuGet. Tambahkan ke proyek, masukkan ke builder, dan bekerja bersama skill berbasis file Anda.

## Skill inline: jembatan cepat

Saat tim lain membangun skill yang persis Anda butuhkan tapi tidak akan siap dalam satu sprint? `AgentInlineSkill` adalah jembatan Anda:

```csharp
var timeOffSkill = new AgentInlineSkill(
    name: "time-off-balance",
    description: "Calculate remaining vacation and sick days.",
    instructions: "1. Minta ID karyawan. 2. Gunakan calculate-balance. 3. Sajikan hasilnya.")
    .AddScript("calculate-balance", (string employeeId, string leaveType) =>
    {
        int remaining = HrDatabase.GetAnnualAllowance(employeeId, leaveType)
                      - HrDatabase.GetDaysUsed(employeeId, leaveType);
        return JsonSerializer.Serialize(new { employeeId, leaveType, remaining });
    });
```

Ketika paket NuGet akhirnya dikirim, Anda mengganti skill inline dengan yang berbasis kelas. Agen tidak tahu perbedaannya.

## Persetujuan skrip: human-in-the-loop

Bagi developer .NET yang membangun agen produksi, inilah bagian yang benar-benar membuka percakapan deployment. Aktifkan `UseScriptApproval` dan agen berhenti sebelum menjalankan skrip apapun:

```csharp
var skillsProvider = new AgentSkillsProviderBuilder()
    .UseFileSkill(Path.Combine(AppContext.BaseDirectory, "skills"))
    .UseSkill(new BenefitsEnrollmentSkill())
    .UseSkill(timeOffSkill)
    .UseFileScriptRunner(SubprocessScriptRunner.RunAsync)
    .UseScriptApproval(true)
    .Build();
```

## Kesimpulan

Agent skills di .NET kini memiliki model authoring yang benar-benar fleksibel. Baik Anda membuat prototip dengan skill berbasis file atau mengirim kemampuan yang dikemas via NuGet, semua pola disusun melalui `AgentSkillsProviderBuilder`.

Lihat [pengumuman asli](https://devblogs.microsoft.com/agent-framework/agent-skills-in-net-three-ways-to-author-one-provider-to-run-them/) dan [contoh GitHub](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/02-agents/AgentSkills).
