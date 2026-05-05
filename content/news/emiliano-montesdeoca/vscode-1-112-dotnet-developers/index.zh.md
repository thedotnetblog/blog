---
title: "VS Code 1.112：.NET 开发者真正应该关注的内容"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "VS Code 1.112 刚刚发布，满载代理升级、集成浏览器调试器、MCP 沙箱和 monorepo 支持。如果你用 .NET 开发，这些是真正重要的内容。"
tags:
  - dotnet
  - visual-studio
  - tooling
  - productivity
  - ai
---

VS Code 1.112 刚落地，说实话？如果你每天都在 .NET 的世界里，这个版本感觉不一样。[官方发布说明](https://code.visualstudio.com/updates/v1_112) 里有很多内容，但让我帮你省点滚动，专注于对我们真正重要的东西。

## Copilot CLI 变得更有用了

这个版本的大主题是**代理自主性** — 给 Copilot 更多空间做它的事，不需要你看管每一步。

### 消息引导和排队

你知道 Copilot CLI 在任务进行到一半时，你突然想起忘了提什么东西的那个时刻吗？以前你只能等。现在你可以在请求还在运行时发送消息 — 要么引导当前响应，要么排队后续指令。

这对那些较长的 `dotnet` 脚手架任务来说太棒了，你看着 Copilot 设置项目然后想"哦等等，我还需要 MassTransit"。

### 权限级别

这是我最兴奋的。Copilot CLI 会话现在支持三个权限级别：

- **默认权限** — 工具在运行前请求确认的常规流程
- **跳过审批** — 自动批准一切并在出错时重试
- **自动驾驶** — 完全自主：批准工具、回答自己的问题、持续到任务完成

如果你在做类似用 Entity Framework、migrations 和 Docker 设置创建新的 ASP.NET Core API 这样的事 — 自动驾驶模式意味着你描述想要什么然后去拿杯咖啡。它会搞定的。

你可以用 `chat.autopilot.enabled` 设置启用自动驾驶。

### 委托前预览更改

当你把任务委托给 Copilot CLI 时，它会创建一个 worktree。以前如果你有未提交的更改，你得检查源代码管理来看什么会受影响。现在聊天视图会在你决定复制、移动或忽略之前直接显示待处理的更改。

小事情，但省去了"等等，我 staging 了什么？"的时刻。

## 不离开 VS Code 就能调试 Web 应用

集成浏览器现在支持**完整调试**。你可以设断点、单步执行代码、检查变量 — 全在 VS Code 内。不用再切换到 Edge DevTools 了。

有一个新的 `editor-browser` 调试类型，如果你已经有 `msedge` 或 `chrome` 的启动配置，迁移只需改 `launch.json` 里的 `type` 字段：

```json
{
  "type": "editor-browser",
  "request": "launch",
  "name": "Debug Blazor App",
  "url": "https://localhost:5001"
}
```

对 Blazor 开发者来说，这是颠覆性的。你已经在终端运行 `dotnet watch` — 现在调试也留在同一个窗口里。

浏览器还获得了独立的缩放级别（终于）、正确的右键上下文菜单，缩放按网站记忆。

## MCP 服务器沙箱

这比你想的更重要。如果你在用 MCP 服务器 — 也许你为 Azure 资源或数据库查询设置了自定义的 — 它们一直以和你的 VS Code 进程相同的权限运行。这意味着对你的文件系统、网络等一切的完全访问。

现在你可以对它们做沙箱处理。在你的 `mcp.json` 中：

```json
{
  "servers": {
    "my-azure-tools": {
      "command": "node",
      "args": ["./mcp-server.js"],
      "sandboxEnabled": true
    }
  }
}
```

当沙箱化的服务器需要访问它没有的东西时，VS Code 会提示你授予权限。比"希望没人做奇怪的事"的方式好太多了。

> **注意：** 沙箱目前在 macOS 和 Linux 上可用。Windows 支持即将到来 — 不过 WSL 等远程场景是可以工作的。

## Monorepo 自定义发现

如果你在 monorepo 中工作（说实话，很多企业 .NET 解决方案最终都变成了 monorepo），这解决了一个真正的痛点。

以前，如果你打开仓库的子文件夹，VS Code 找不到仓库根目录的 `copilot-instructions.md`、`AGENTS.md` 或自定义技能。现在通过 `chat.useCustomizationsInParentRepositories` 设置，它会向上查找到 `.git` 根目录并发现所有内容。

这意味着你的团队可以在 monorepo 中跨所有项目共享代理指令、提示文件和自定义工具，不需要每个人都打开根文件夹。

## /troubleshoot 用于代理调试

有没有设置过自定义指令或技能，然后纳闷为什么没被检测到？新的 `/troubleshoot` 技能读取代理调试日志并告诉你发生了什么 — 哪些工具被使用或跳过了，为什么指令没加载，什么导致了慢响应。

用以下配置启用：

```json
{
  "github.copilot.chat.agentDebugLog.enabled": true,
  "github.copilot.chat.agentDebugLog.fileLogging.enabled": true
}
```

然后在聊天中输入 `/troubleshoot why is my custom skill not loading?`。

你现在还可以导出和导入这些调试日志，当某些东西不按预期工作时，和团队分享很方便。

## 图像和二进制文件支持

代理现在可以从磁盘原生读取图像文件和二进制文件。二进制文件以 hexdump 格式呈现，图像输出（如集成浏览器的截图）以轮播视图显示。

对 .NET 开发者来说：把 UI bug 的截图粘贴到聊天中让代理理解问题所在，或者让它分析 Blazor 组件渲染的输出。

## 自动符号引用

小的生活质量改善：当你复制一个符号名称（类、方法等）并粘贴到聊天中时，VS Code 现在自动将其转换为 `#sym:Name` 引用。这给代理提供了关于该符号的完整上下文，无需手动添加。

如果你想要纯文本，使用 `Ctrl+Shift+V`。

## 插件现在可以启用/禁用

以前禁用 MCP 服务器或插件意味着卸载它。现在你可以开关它们 — 全局和按工作区都可以。在扩展视图或自定义视图中右键单击就行。

npm 和 pypi 的插件现在也可以自动更新了，不过会先请求批准，因为更新意味着在你的机器上运行新代码。

## 总结

VS Code 1.112 明显在大力推进代理体验 — 更多自主性、更好的调试、更严格的安全。对 .NET 开发者来说，集成浏览器调试和 Copilot CLI 改进是最突出的功能。

如果你还没试过为 .NET 项目在自动驾驶模式下运行完整的 Copilot CLI 会话，这个版本是开始的好时机。记得设置你的权限然后让它干活。

[下载 VS Code 1.112](https://code.visualstudio.com/updates/v1_112) 或在 VS Code 内通过**帮助 > 检查更新**进行更新。
