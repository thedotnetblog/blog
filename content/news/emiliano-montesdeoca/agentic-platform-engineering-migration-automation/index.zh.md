---
title: "用 Agentic Platform Engineering 消除迁移的重复性工作"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape 演示了将真实的 AWS Terraform 部署迁移到 Azure Bicep 的过程——提取部署意图并重新映射架构，而不是进行 1:1 的语法转换。"
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*本文已自动翻译。要查看原始版本，[请点击此处]({{< ref "index.md" >}}).*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — Git-Ape（git 智能体平台工程工具）将真实的 AWS Terraform 仓库迁移到 Azure 的演练，专注于提取部署意图而非逐行转换。

## 输入：contoso-migration

源项目是一个真实的 Terraform 项目（`contoso-migration`），在 AWS 上部署 Next.js 应用——EC2 用于计算，ALB 用于负载均衡，S3 用于制品，IAM 密钥用于身份认证。成本：约 34 美元/月。目标不是在 Azure 上复现相同的基础设施；而是弄清楚这个部署实际上要做什么，然后用 Azure 原生服务重新构建它。

## 步骤 1：验证与认证

Git-Ape 首先验证所有必需的 CLI 工具——`az`、`aws`、`gh`、`jq`、`git`——并在进行任何操作之前确认活跃的认证会话。不做部分运行。

## 步骤 2：意图提取

智能体通过 GitHub API 读取整个源仓库，并提取部署意图：运行时（Node.js）、计算类型、入口模式、制品处理、身份模型、网络和监控。这是关键步骤——它构建了一个关于部署做什么的语义模型，而不是它使用了哪些 Terraform 关键字。

## 步骤 3：服务映射

AWS 服务映射到 Azure 等效服务：
- EC2 → App Service（Linux，Node 20 LTS）
- ALB → App Service 内置负载均衡
- IAM 角色/密钥 → Managed Identity
- Terraform → Bicep + GitHub Actions

## 步骤 4：评审智能体

在生成输出之前，评审智能体运行并发现两个阻塞问题：

1. **启动时构建反模式** — 原始 Terraform 在 EC2 启动时运行 `npm install && npm run build`。修复：在 CI 中构建，部署已就绪的制品。
2. **不必要的 Blob Storage** — S3 用于制品暂存，通过适当的 CI/CD 可以完全省去。评审智能体将其彻底删除。

## 步骤 5：生成的输出

结果是约 80 行 Bicep，而不是原来的 200 多行 Terraform。智能体创建了一个新的 GitHub 仓库，包含 `infra/main.bicep` 和 `.github/workflows/deploy.yml`，并删除了所有 AWS 特定文件。

## 安全态势对比

迁移还带来了显著的安全升级：

| AWS 原始 | Azure 输出 |
|---|---|
| 仅 HTTP | 仅 HTTPS，TLS 1.2 |
| SSH 对 0.0.0.0/0 开放 | 无 SSH 暴露 |
| IAM 访问密钥 | OIDC + Managed Identity |
| 无监控 | Application Insights |

成本：约 13 美元/月，而原来是 34 美元/月。

## 与语法转换器的区别

评审智能体步骤是将其与机械翻译区分开来的关键。它发现了在 AWS 上可行但在 Azure 上会出错的模式——并修复了它们而不是复制它们。输出不是"Azure 语法的 AWS"；而是以更简洁方式实现同一目标的 Azure 原生部署。

请查看[完整演练](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/)以获取完整的智能体追踪和生成的文件。
