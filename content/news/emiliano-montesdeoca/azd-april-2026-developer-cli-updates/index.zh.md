---
title: "Azure Developer CLI (azd) 2026年4月更新"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd 在 2026 年 4 月发布了五个版本，重点是对 Python、JavaScript、TypeScript 和 .NET 的多语言钩子支持，以及 azd update 公开预览版、AI 配额预检查等功能。"
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}}).*

[Azure Developer CLI (azd) 在 2026 年 4 月发布了五个版本](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/)（1.23.14 至 1.24.2），重大主题是钩子现在可在 Python、JavaScript、TypeScript 和 .NET 中运行——而不仅限于 Bash 和 PowerShell。

## azure.yaml 中的多语言钩子

除 shell 脚本外，钩子现在可以指向 `.py`、`.js`、`.ts` 或 `.cs` 文件。每种语言都可自动解析依赖关系：

- **Python** — 检测 `requirements.txt` 或 `pyproject.toml`，创建 virtualenv 并在运行前安装依赖。通过 `virtualEnvName` 配置环境名称。
- **JavaScript / TypeScript** — 检测 `package.json` 并自动运行 `npm install`。TypeScript 通过 `npx tsx` 执行，无需编译步骤。通过 `packageManager` 配置块选择包管理器。
- **.NET** — 使用 `dotnet run` 运行 `.cs` 文件。在 .NET 10+ 上支持单文件脚本。通过 `configuration/framework` 块配置目标框架。

这意味着已在这些语言之一中工作的团队，不再需要仅为了连接预配生命周期事件而单独维护 Bash 或 PowerShell 钩子。

## azd update 进入公开预览

`azd update` 现已在所有平台上推出公开预览版。单个命令即可处理更新，无论 azd 最初是如何安装的——不再需要单独追踪 Homebrew、WinGet 或 MSI 的路径。

## 通过 AZD_NON_INTERACTIVE 实现非交互模式

设置 `AZD_NON_INTERACTIVE=true`（或使用 `--non-interactive` / `--no-prompt`）现在会在 CI/CD 管道中产生一致、确定性的失败，当必需的输入无法自动解析时。此前各命令的行为不一致。

## AI 模型配额预检查

`azd provision` 在尝试预配 AI 模型资源之前，会验证 Azure 认知服务配额。因配额限制而失败的部署现在会在流程早期显示错误，而不是在预配进行到一半时才报错。

## Copilot 问题排查中的"修复此错误"

azd 的 Copilot 问题排查集成获得了直接应用建议修复的能力——而不仅仅是描述它。当代理识别出可修复的问题时，它可以直接在原地进行更改。

## 自定义预配提供程序和 Key Vault 密钥解析器

扩展作者现在可以使用 `WithProvisioningProvider()` 注册替代基础结构后端。另外，azd 在将配置传递给扩展之前会自动解析 `@Microsoft.KeyVault(...)` 引用，无需在自定义提供程序中手动解析密钥。

## 模板和监视模式的排除项

两个新的忽略文件对文件处理提供了更精细的控制：
- **`.azdignore`** — 从模板副本中排除仅供贡献者使用的文件（文档、CI 配置），使最终用户获得干净的项目脚手架。
- **`.azdxignore`** — 排除在 `azd x watch` 期间触发重新构建的目录，减少迭代开发过程中的噪音。

## 保留名称预检查和 docker.network 选项

azd 现在会在预配开始之前，当预测的资源名称包含 Azure 保留词（`MICROSOFT`、`WINDOWS` 或 `LOGIN` 前缀）时发出警告。新的 `docker.network` 选项将 `--network` 传递给 `docker build`，在需要特定 Docker 网络的企业代理环境中非常有用。

## 安全修复

Windows MSI 包现在包含代码签名验证。另一项修复关闭了可能在扩展命令边界之间暴露值的环境变量泄漏问题。

---

这是繁忙的一个月——多语言钩子支持尤其消除了不主要使用 Bash 的团队的一个真实摩擦点。有关所有五个版本的完整更改日志，请参阅[完整发行说明](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/)。
