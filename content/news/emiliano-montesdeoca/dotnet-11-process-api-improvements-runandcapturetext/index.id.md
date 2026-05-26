---
title: ".NET 11 Akhirnya Memperbaiki API Proses"
date: 2026-05-26
author: "Emiliano Montesdeoca"
description: "System.Diagnostics.Process mendapatkan pembaruan terbesar dalam beberapa tahun. RunAndCaptureTextAsync, KillOnParentExit, API SafeProcessHandle, dan kontrol penuh atas pengalihan handle standar — tidak ada lagi boilerplate deadlock."
tags:
  - .NET
  - .NET 11
  - Performance
  - Process API
---

Setiap pengembang .NET yang pernah perlu menjalankan proses dan menangkap outputnya telah menulis beberapa variasi dari boilerplate berbahaya yang sama: pembacaan async dari stdout, pembacaan async dari stderr, `WaitForExitAsync`, jangan lupa menguras kedua stream atau akan terjadi deadlock. Ini adalah jebakan yang sudah dikenal bertahun-tahun.

.NET 11 akhirnya memperbaiki ini dengan benar.

## RunAndCaptureTextAsync

Penambahan utama: satu metode statis yang memulai proses, menangkap stdout dan stderr, dan menunggu keluar tanpa deadlock.

```csharp
var result = await Process.RunAndCaptureTextAsync("dotnet", "--version");
Console.WriteLine(result.StandardOutput);
```

Satu panggilan. Tanpa pengosongan stream manual. Tanpa `WaitForExit` yang ditempatkan dengan hati-hati. Jika Anda hanya perlu menjalankan sesuatu dan mendapatkan outputnya, inilah API yang Anda inginkan.

Ada juga `Process.RunAsync` untuk kasus di mana Anda ingin menunggu keluar tanpa menangkap output.

## KillOnParentExit

Masalah umum dengan proses yang dijalankan: jika proses induk crash atau dihentikan, proses anak terus berjalan sebagai yatim piatu. `KillOnParentExit` memungkinkan Anda mendeklarasikan saat proses dimulai bahwa proses anak harus dihentikan ketika proses induk keluar.

Ini adalah fitur yang ada dengan cara khusus platform (job objects di Windows, prctl di Linux) tetapi memerlukan p/invoke atau pustaka pihak ketiga untuk digunakan dari .NET. Sekarang ini adalah properti kelas satu pada `ProcessStartInfo`.

## API Berbasis SafeProcessHandle

Permukaan API ringan baru dibangun di sekitar `SafeProcessHandle` daripada kelas `Process` lengkap. Kelas `Process` lengkap membawa banyak status dan sulit untuk dipangkas — jalur `SafeProcessHandle` lebih ramah trimmer untuk aplikasi yang perlu meminimalkan ukuran output (WASM, native AOT).

## Kontrol Penuh atas Pewarisan Handle

Pembaruan ini juga menambahkan kontrol granular atas handle mana yang diwarisi proses anak dan bagaimana handle standar dialihkan. Sebelumnya Anda bisa mengalihkan stdin/stdout/stderr tetapi tidak bisa menentukan dengan tepat handle mana yang akan diwarisi di tingkat OS. API baru mengekspos kontrol tersebut.

## Mengapa Ini Penting

Kelas `Process` digunakan dalam tooling, sistem build, test runner, dan aplikasi apa pun yang memanggil executable lain. Permukaan API lama berasal dari .NET Framework dan mulai menunjukkan usianya. Ini bukan perubahan yang merusak — API lama masih berfungsi — tetapi kode baru harus lebih memilih permukaan baru.

Untuk aplikasi yang dipangkas atau skenario kompilasi AOT, jalur `SafeProcessHandle` sangat disambut. Kelas `Process` lama membawa banyak kode yang berat refleksi yang mempersulit pemangkasan.

Posting asli: [Process API Improvements in .NET 11](https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/)
