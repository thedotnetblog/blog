---
title: ".NET Aspire 13.2想成为你AI智能体的好朋友"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2全力投入智能体开发 — 结构化CLI输出、隔离运行、自愈环境以及完整的OpenTelemetry数据，让你的AI智能体能够真正构建、运行和观察你的应用。"
tags:
  - aspire
  - dotnet
  - ai
  - cli
  - telemetry
  - developer-tools
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "aspire-agentic-development-build-run-observe" >}})。*

你知道那种感觉吗？你的AI编码智能体写出了不错的代码，你很兴奋，然后当它试图*运行*这个东西时一切都崩溃了？端口冲突、幽灵进程、错误的环境变量 — 突然你的智能体在排查启动问题上烧掉了大量token，而不是构建功能。

Aspire团队刚刚发布了一篇关于这个问题的[深思熟虑的文章](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/)，他们的答案很有说服力：Aspire 13.2的设计不仅面向人类，更面向AI智能体。

## 问题是真实存在的

AI智能体在写代码方面令人难以置信。但交付一个可工作的全栈应用涉及的远不止生成文件。你需要按正确的顺序启动服务、管理端口、设置环境变量、连接数据库，以及在出问题时获得反馈。目前，大多数智能体通过试错来处理所有这些 — 运行命令、读取错误输出、再试一次。

我们叠加Markdown指令、自定义技能和提示来引导它们，但这些是不可预测的，无法编译，而且仅仅解析就要消耗token。Aspire团队抓住了核心洞察：智能体需要**编译器和结构化API**，而不是更多的Markdown。

## Aspire作为智能体基础设施

以下是Aspire 13.2为智能体开发带来的内容：

**整个技术栈用类型化代码描述。** AppHost用可编译的TypeScript或C#定义你的完整拓扑 — API、前端、数据库、缓存：

```typescript
import { createBuilder } from './.modules/aspire.js';

const builder = await createBuilder();

const postgres = await builder.addPostgres("pg").addDatabase("catalog");
const cache = await builder.addRedis("cache");

const api = await builder
  .addNodeApp("api", "./api", "src/index.ts")
  .withHttpEndpoint({ env: "PORT" })
  .withReference(postgres)
  .withReference(cache);

await builder
  .addViteApp("frontend", "./frontend")
  .withReference(api)
  .waitFor(api);

await builder.build().run();
```

智能体可以读取这些来理解应用拓扑、添加资源、连接组件，并*通过构建来验证*。编译器会立即告诉它哪里出了问题。不需要猜测，不需要在配置文件上反复试错。

**一个命令统治所有。** 智能体不再需要在`docker compose up`、`npm run dev`和数据库启动脚本之间来回切换，一切只需`aspire start`。所有资源按正确顺序、在正确的端口、用正确的配置启动。长时间运行的进程也不会挂起智能体 — Aspire负责管理它们。

**并行智能体的隔离模式。** 使用`--isolated`，每次Aspire运行都会获得自己的随机端口和独立的用户密钥。多个智能体在git worktree中工作？它们不会冲突。这对于VS Code的后台智能体等创建并行环境的工具来说意义重大。

**通过遥测赋予智能体视野。** 这是真正强大的地方。Aspire CLI在开发期间暴露完整的OpenTelemetry数据 — 追踪、指标、结构化日志。你的智能体不是只读控制台输出然后祈祷一切顺利。它可以跨服务追踪失败的请求、分析慢端点，并精确定位问题所在。这是开发循环中的生产级可观察性。

## 保龄球护栏类比

Aspire团队用了一个很棒的类比：把Aspire想象成AI智能体的保龄球道护栏。如果智能体不够完美（它确实不会完美），护栏会防止它打出沟球。技术栈定义防止配置错误，编译器捕获错误，CLI处理进程管理，遥测提供反馈循环。

将此与Playwright CLI之类的工具结合，你的智能体就可以真正*使用*你的应用 — 点击流程、检查DOM、在遥测中发现问题、修复代码、重启并重新测试。构建、运行、观察、修复。这就是我们一直追求的自主开发循环。

## 入门

Aspire新手？从[get.aspire.dev](https://get.aspire.dev)安装CLI并遵循[入门指南](https://aspire.dev/get-started/first-app)。

已经在使用Aspire？运行`aspire update --self`获取13.2，然后将你最喜欢的编码智能体指向你的仓库。有了Aspire的护栏，你可能会惊讶于它能走多远。

## 总结

Aspire 13.2不再仅仅是一个分布式应用框架 — 它正在成为必不可少的智能体基础设施。结构化的技术栈定义、一键启动、隔离的并行运行和实时遥测，为AI智能体提供了从编写代码到交付应用所需的一切。

阅读Aspire团队的[完整文章](https://devblogs.microsoft.com/aspire/agentic-dev-aspirations/)获取所有细节和演示视频。
