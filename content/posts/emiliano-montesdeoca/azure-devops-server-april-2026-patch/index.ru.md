---
title: "Azure DevOps Server Патч Апрель 2026 — Исправление Завершения PR и Обновления Безопасности"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server получает Патч 3 с исправлением сбоев завершения PR, улучшенной валидацией при выходе из системы и восстановлением PAT-подключений к GitHub Enterprise Server."
tags:
  - azure-devops
  - devops
  - patches
---

> *Этот пост был переведён автоматически. Оригинальная версия доступна [здесь]({{< ref "azure-devops-server-april-2026-patch.md" >}}).*

Быстрое уведомление для команд, использующих самостоятельно размещённый Azure DevOps Server: Microsoft выпустила [Патч 3 за апрель 2026](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) с тремя целевыми исправлениями.

## Что исправлено

- **Сбои завершения pull request** — исключение нулевой ссылки при автоматическом завершении рабочих элементов могло приводить к сбою слияния PR. Если вы сталкивались с случайными ошибками завершения PR, вероятно, это была причина
- **Валидация перенаправления при выходе** — улучшена валидация при выходе из системы для предотвращения потенциально вредоносных перенаправлений. Это исправление безопасности, которое стоит применить как можно скорее
- **PAT-подключения к GitHub Enterprise Server** — создание подключений с помощью Personal Access Token к GitHub Enterprise Server было сломано, теперь восстановлено

## Как обновить

Скачайте [Патч 3](https://aka.ms/devopsserverpatch3) и запустите установщик. Чтобы проверить, что патч применён:

```bash
<patch-installer>.exe CheckInstall
```

Если вы используете Azure DevOps Server на собственных серверах, Microsoft настоятельно рекомендует поддерживать актуальную версию патчей как для безопасности, так и для надёжности. Ознакомьтесь с [примечаниями к выпуску](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026) для получения полной информации.
