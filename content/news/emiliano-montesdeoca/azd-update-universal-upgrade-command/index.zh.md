---
title: "azd update — 一个命令搞定所有包管理器"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI 现在有了一个通用的更新命令，无论你是通过 winget、Homebrew、Chocolatey 还是安装脚本安装的，都能正常工作。"
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "azd-update-universal-upgrade-command.md" >}})。*

你知道那个每隔几周就会弹出来的"azd 有新版本可用"提示吗？就是那个你总是忽略掉的，因为你根本想不起来当初是用 winget、Homebrew 还是半年前跑的那个 curl 脚本安装的 `azd`。好了，这个问题终于解决了。

Microsoft 刚刚发布了 [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) — 一个命令就能将 Azure Developer CLI 更新到最新版本，不管你最初是怎么安装的。Windows、macOS、Linux — 都一样。就一个命令。

## 工作原理

```bash
azd update
```

就这么简单。如果你想提前体验新功能，可以切换到每日 Insiders 构建：

```bash
azd update --channel daily
azd update --channel stable
```

这个命令会自动检测你当前的安装方式，并在后台使用对应的更新机制。再也不用纠结"等等，这台机器上我用的是 winget 还是 choco 来着？"

## 一个小前提

`azd update` 从版本 1.23.x 开始提供。如果你用的是更早的版本，需要用原来的安装方式做最后一次手动更新。之后，`azd update` 就能接管一切了。

用 `azd version` 查看你当前的版本。如果需要全新安装，[安装文档](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) 可以帮到你。

## 为什么这很重要

这是一个小小的生活质量改善，但对于我们这些每天都在用 `azd` 把 AI Agent 和 Aspire 应用部署到 Azure 的人来说，保持最新意味着更少的"这个 bug 在最新版本里已经修复了"的尴尬时刻。少操心一件事。

阅读 [完整公告](https://devblogs.microsoft.com/azure-sdk/azd-update/) 和 Jon Gallant 的 [深入分析](https://blog.jongallant.com/2026/04/azd-update) 了解更多。
