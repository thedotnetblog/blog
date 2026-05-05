---
title: "azd现在可以在本地运行和调试AI代理了 — 2026年3月都有哪些变化"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI在2026年3月发布了七个版本。亮点：AI代理的本地运行和调试循环、GitHub Copilot项目设置集成、Container App Jobs支持。"
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *本文为自动翻译。查看原始版本，请[点击这里]({{< ref "azd-march-2026-local-ai-agent-debugging.md" >}})。*

一个月七个版本。这是Azure Developer CLI (`azd`) 团队在2026年3月发布的成果，而头条功能正是我一直在等的：**AI代理的本地运行和调试循环**。

PC Chan [发布了完整摘要](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/)，虽然内容很多，但让我筛选出对构建AI驱动应用的.NET开发者真正重要的部分。

## 不用部署就能运行和调试AI代理

这是最大的亮点。新的 `azure.ai.agents` 扩展添加了一组命令，为AI代理提供了完整的内循环体验：

- `azd ai agent run` — 在本地启动你的代理
- `azd ai agent invoke` — 向其发送消息（本地或已部署的）
- `azd ai agent show` — 显示容器状态和健康状况
- `azd ai agent monitor` — 实时流式传输容器日志

以前，测试AI代理意味着每次修改都要部署到Microsoft Foundry。现在你可以在本地迭代，测试代理行为，准备好了再部署。

## GitHub Copilot为你配置azd项目

`azd init` 现在提供了"Set up with GitHub Copilot (Preview)"选项。无需手动回答关于项目结构的提示，Copilot代理为你生成配置。当命令失败时，`azd` 提供AI辅助的问题排查——全程不需要离开终端。

## Container App Jobs和部署改进

- **Container App Jobs**：`azd`现在通过现有的`host: containerapp`配置部署`Microsoft.App/jobs`。
- **可配置的部署超时**：`azd deploy`的新`--timeout`标志和`azure.yaml`中的`deployTimeout`字段。
- **远程构建回退**：当ACR构建失败时，`azd`自动回退到本地Docker/Podman构建。
- **本地预检验证**：部署前在本地验证Bicep参数。

## 开发体验改进

- **自动检测pnpm/yarn** — JS/TS项目
- **pyproject.toml支持** — Python打包
- **本地模板目录** — `azd init --template`接受文件系统路径
- **更好的错误消息** — `--no-prompt`模式
- **构建环境变量** — 注入到所有框架构建子进程（.NET、Node.js、Java、Python）

## 总结

本地AI代理调试循环是这个版本的明星，但部署改进和DX优化的积累使`azd`比以往更加成熟。如果你在Azure上部署.NET应用——特别是AI代理——这次更新值得关注。

查看[完整发行说明](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/)了解所有细节。
