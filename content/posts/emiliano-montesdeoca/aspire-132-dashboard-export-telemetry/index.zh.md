---
title: "Aspire 13.2的Dashboard现在有了遥测API — 这改变了一切"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2带来了更智能的遥测导出、可编程的trace和日志API，以及GenAI可视化改进。了解为什么这对你的调试工作流很重要。"
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

> *本文为自动翻译。查看原始版本，请[点击这里]({{< ref "aspire-132-dashboard-export-telemetry.md" >}})。*

如果你一直在用 .NET Aspire 构建分布式应用，你已经知道dashboard是整个体验中最棒的部分。所有的trace、日志和指标都在一个地方 — 不需要外部的Jaeger，不需要Seq配置，不需要"让我看看另一个终端"的时刻。

Aspire 13.2 刚刚做了重大改进。James Newton-King [发布了更新公告](https://devblogs.microsoft.com/aspire/aspire-dashboard-improvements-export-and-telemetry/)，说实话，单是遥测导出和API功能就值得升级。

## 像正常人一样导出遥测数据

这是我们都经历过的场景：你在调试一个分布式问题，花了二十分钟终于复现了，现在你需要和团队分享发生了什么。之前？截图。复制粘贴trace ID。一如既往的混乱。

Aspire 13.2 添加了一个**管理日志和遥测**对话框，你可以：

- 清除所有遥测（在复现bug之前很有用）
- 将选定的遥测数据导出为标准OTLP/JSON格式的ZIP文件
- 稍后将该ZIP重新导入任何Aspire dashboard

最后一点是杀手级功能。你复现一个bug，导出遥测数据，附加到工作项，你的队友可以导入到自己的dashboard中，看到你所看到的完全一样的内容。不再需要"你能在你的机器上复现吗？"

单个trace、span和日志也在上下文菜单中有了"Export JSON"选项。需要分享一个特定的trace？右键点击，复制JSON，粘贴到PR描述中。搞定。

## 遥测API才是真正的革命性变化

这是最让我兴奋的。Dashboard现在在`/api/telemetry`下暴露了HTTP API，用于编程式查询遥测数据。可用端点：

- `GET /api/telemetry/resources` — 列出有遥测数据的资源
- `GET /api/telemetry/spans` — 带过滤器查询span
- `GET /api/telemetry/logs` — 带过滤器查询日志
- `GET /api/telemetry/traces` — 列出trace
- `GET /api/telemetry/traces/{traceId}` — 获取特定trace的所有span

一切都以OTLP JSON格式返回。这驱动了新的CLI命令`aspire agent mcp`和`aspire otel`，但真正的意义更大：你现在可以构建工具、脚本和AI代理集成，直接查询你应用的遥测数据。

想象一个AI编码代理在调试时能看到你实际的分布式trace。这不再是假设 — 这就是这个API所实现的。

## GenAI遥测变得实用

如果你正在用Semantic Kernel或Microsoft.Extensions.AI构建AI驱动的应用，你会喜欢改进的GenAI遥测可视化器。Aspire 13.2 新增了：

- AI工具描述以Markdown渲染
- Trace页面上的专用GenAI按钮，方便快速访问
- 对截断或非标准GenAI JSON更好的错误处理
- 工具定义之间的点击高亮导航

文章提到VS Code Copilot chat、Copilot CLI和OpenCode都支持配置`OTEL_EXPORTER_OTLP_ENDPOINT`。将它们指向Aspire dashboard，你可以通过遥测数据实时观看你的AI代理思考过程。这是你在其他任何地方都找不到的调试体验。

## 总结

Aspire 13.2将dashboard从"不错的调试UI"转变为"可编程的可观测性平台"。单是导出/导入工作流就能在分布式调试中节省真实时间，而遥测API为AI辅助诊断打开了大门。

如果你已经在用Aspire，升级吧。如果还没有 — 这是一个了解[aspire.dev](https://aspire.dev)的好理由。
