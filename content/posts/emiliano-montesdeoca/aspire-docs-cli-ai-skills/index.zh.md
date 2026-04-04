---
title: "Aspire 13.2 自带文档 CLI — 你的 AI 代理也能用"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 新增了 aspire docs — 一个无需离开终端即可搜索、浏览和阅读官方文档的 CLI。它也可以作为 AI 代理的工具。这就是为什么这很重要。"
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *本文为自动翻译。查看原文请[点击此处]({{< ref "aspire-docs-cli-ai-skills.md" >}})。*

你知道那种时刻吗——你正深入一个 Aspire AppHost，接入各种集成，然后需要确认 Redis 集成到底需要哪些参数？你 Alt-Tab 切到浏览器，在 aspire.dev 上翻来翻去，眯着眼看 API 文档，然后切回编辑器。上下文没了，心流断了。

Aspire 13.2 刚刚[发布了解决方案](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/)。`aspire docs` CLI 让你直接从终端搜索、浏览和阅读 Aspire 官方文档。而且因为它由可复用的服务支撑，AI 代理和技能可以使用同样的命令来查找文档，而不是幻想出不存在的 API。

## 这到底解决了什么问题

David Pine 在原文中说得很到位：AI 代理在帮助开发者构建 Aspire 应用方面*糟糕透了*。它们推荐 `dotnet run` 而不是 `aspire run`，引用 learn.microsoft.com 来查找实际在 aspire.dev 上的文档，建议过时的 NuGet 包，还有——我个人最喜欢的——幻想出根本不存在的 API。

为什么？因为 Aspire 作为 .NET 专属工具的时间远比它成为多语言工具的时间长，而且 LLM 使用的训练数据早于最新功能。当你给 AI 代理真正查找当前文档的能力时，它就不再猜测，开始变得有用了。

## 三个命令，零个浏览器标签页

CLI 简洁得令人耳目一新：

### 列出所有文档

```bash
aspire docs list
```

返回 aspire.dev 上所有可用的文档页面。需要机器可读的输出？加上 `--format Json`。

### 搜索主题

```bash
aspire docs search "redis"
```

同时搜索标题和内容，使用加权相关性评分。与内部驱动文档工具的搜索引擎完全一样。你会得到带有标题、slug 和相关性分数的排名结果。

### 阅读完整页面（或仅一个章节）

```bash
aspire docs get redis-integration
```

将完整页面以 markdown 格式流式传输到你的终端。只需要一个章节？

```bash
aspire docs get redis-integration --section "Add Redis resource"
```

精准定位。不用滚动 500 行。只看你需要的部分。

## AI 代理的视角

对于我们这些使用 AI 工具进行开发的人来说，这才是真正有趣的地方。同样的 `aspire docs` 命令可以作为 AI 代理的工具——通过技能、MCP 服务器或简单的 CLI 封装。

你的 AI 助手不再根据过时的训练数据编造 Aspire API，而是可以调用 `aspire docs search "postgres"`，找到官方集成文档，阅读正确的页面，给你文档记录的方案。实时的、最新的文档——而不是模型六个月前记住的内容。

背后的架构是有意为之的。Aspire 团队构建了可复用的服务（`IDocsIndexService`、`IDocsSearchService`、`IDocsFetcher`、`IDocsCache`），而不是一次性集成。这意味着同一个搜索引擎为终端中的人类、编辑器中的 AI 代理以及 CI 流水线中的自动化服务。

## 真实场景

**终端快速查询：** 你已经深入到第三个文件，需要 Redis 配置参数。两个命令，九十秒，回去干活：

```bash
aspire docs search "redis" --limit 1
aspire docs get redis-integration --section "Configuration"
```

**AI 辅助开发：** 你的 VS Code 技能封装了 CLI 命令。你问"给我的 AppHost 添加一个 PostgreSQL 数据库"，代理在回答之前先查阅真实文档。没有幻觉。

**CI/CD 验证：** 你的流水线以编程方式根据官方文档验证 AppHost 配置。`--format Json` 输出可以干净地通过管道传递给 `jq` 和其他工具。

**自定义知识库：** 在构建自己的 AI 工具？将结构化 JSON 输出直接导入你的知识库：

```bash
aspire docs search "monitoring" --format Json | jq '[.[] | {slug, title, summary}]'
```

不需要网页抓取。不需要 API 密钥。与文档工具内部使用的完全一样的结构化数据。

## 文档始终是最新的

这是我最欣赏的部分。CLI 不会下载快照——它通过基于 ETag 的缓存查询 aspire.dev。文档一旦更新，你的 CLI 和构建在其之上的所有技能都会反映出来。没有过时的副本，没有"但是 wiki 上说的是..."的尴尬时刻。

## 总结

`aspire docs` 是那种以简洁方式解决真实问题的小功能之一。人类获得了终端原生的文档访问。AI 代理获得了停止猜测、开始引用真实文档的方式。而且一切都由同一个事实来源支撑。

如果你正在使用 .NET Aspire 开发，还没试过这个 CLI，运行 `aspire docs search "你的主题"` 看看感觉如何。然后考虑将这些命令封装到你正在使用的任何 AI 技能或自动化设置中——你的代理会感谢你的。

查看 [David Pine 的深入分析](https://davidpine.dev/posts/aspire-docs-mcp-tools/)了解文档工具是如何构建的，以及[官方 CLI 参考](https://aspire.dev/reference/cli/commands/aspire-docs/)获取所有细节。
