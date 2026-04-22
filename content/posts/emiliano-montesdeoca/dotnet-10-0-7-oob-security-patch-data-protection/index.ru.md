---
title: "Обновитесь Прямо Сейчас: .NET 10.0.7 Внеплановое Обновление Безопасности (ASP.NET Core Data Protection)"
date: 2026-04-22
author: "Emiliano Montesdeoca"
description: ".NET 10.0.7 — внеплановый релиз, исправляющий уязвимость безопасности в Microsoft.AspNetCore.DataProtection: управляемый аутентифицированный шифратор вычислял HMAC над неправильными байтами, что могло привести к повышению привилегий."
tags:
  - ".NET"
  - "Security"
  - "ASP.NET Core"
  - ".NET 10"
  - "Maintenance & Updates"
---

*Этот пост был автоматически переведён. Для оригинальной версии [нажмите здесь](https://thedotnetblog.com/posts/emiliano-montesdeoca/dotnet-10-0-7-oob-security-patch-data-protection/).*

Это обновление не является опциональным. Если ваше приложение использует `Microsoft.AspNetCore.DataProtection`, необходимо обновиться до 10.0.7.

## Что Произошло

После Patch Tuesday релиза `.NET 10.0.6` пользователи начали сообщать об ошибках дешифрования. В ходе расследования была обнаружена уязвимость **CVE-2026-40372**: тег HMAC-валидации вычислялся над **неправильными байтами**, что могло привести к повышению привилегий.

## Как Исправить

```bash
dotnet add package Microsoft.AspNetCore.DataProtection --version 10.0.7
```

Затем **пересоберите и переразверните** приложение.

Оригинальное объявление Рахула Бхандари: [.NET 10.0.7 Out-of-Band Security Update](https://devblogs.microsoft.com/dotnet/dotnet-10-0-7-oob-security-update/).
