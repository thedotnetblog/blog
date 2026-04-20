---
title: "C# 15 Mendapatkan Tipe Union — Dan Itu Persis Yang Kita Minta"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 memperkenalkan kata kunci `union` — union diskriminasi yang dipaksakan kompiler dengan pencocokan pola yang lengkap. Seperti apa tampilannya, mengapa penting, dan cara mencobanya hari ini."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "csharp-15-union-types-exhaustive-matching" >}}).*

Inilah yang saya tunggu-tunggu. C# 15 memperkenalkan kata kunci `union` — union diskriminasi yang tepat dengan pencocokan pola lengkap yang dipaksakan kompiler.

Bill Wagner [menerbitkan analisis mendalam](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/).

## Masalah yang diselesaikan union

Sebelum C# 15, mengembalikan "salah satu dari beberapa tipe yang mungkin" dari metode selalu merupakan kompromi. Anda tidak pernah mendapatkan apa yang sebenarnya Anda inginkan: kumpulan tipe tertutup di mana kompiler menjamin Anda telah menangani setiap kasus.

## Sintaksnya sederhana dengan indah

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

Dan inilah keajaibannya — kompiler memaksakan pencocokan lengkap:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

Tidak perlu `_`. Jika Anda nanti menambahkan tipe keempat ke union, setiap ekspresi switch yang tidak menanganinya menghasilkan peringatan.

## Di mana ini menjadi praktis

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Sekarang setiap konsumen dipaksa untuk menangani sukses, error, dan kegagalan validasi.

## Coba hari ini

Tipe union tersedia di .NET 11 Preview 2. Lihat [referensi bahasa lengkap](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union).
