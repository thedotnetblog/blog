---
title: 'Visual Studio 扩展团队应该停止按习惯发布，开始按管道发布'
date: 2026-07-23
author: 'Emiliano Montesdeoca'
description: '一个可重复的 VSIX 版本管理和发布的 GitHub Actions 流程现在足够简单，手动发布步骤很难再合理化。'
tags:
  - visual-studio
  - vsix
  - github-actions
  - ci-cd
  - developer-tooling
---

原文来源：[Automating your Visual Studio extension builds with GitHub Actions](https://devblogs.microsoft.com/visualstudio/automating-your-visual-studio-extension-builds-with-github-actions/)

如果你维护 Visual Studio 扩展，并且仍然手动进行大部分发布工作，现在是时候现代化的信号来了。

文章中展示的工作流是故意实用的：标记版本、构建、将测试工件发布到 gallery，然后将稳定版本发布到 Marketplace。没有沉重的平台仪式，只有确定性的发布行为。

我最喜欢的是版本控制被当作管道状态来处理，而不是发布前的检查清单项。这一个决定消除了数量令人惊讶的错误：不匹配的元数据、陈旧的程序集版本和不一致的发布说明。

在 gallery 发布和 Marketplace 发布之间的分离在运维上也是成熟的。团队需要一个放置快速验证构建的地方，而这些构建不带有正式发布的语义。把所有内容直接推送到 Marketplace 是高摩擦的，并鼓励有风险的捷径。

### 扩展团队的一个强发布模式

- **在拉取请求和主分支提交上**，生成 CI VSIX 工件并发布到 gallery 供测试人员使用。
- **在标记的发布上**，将已签名和验证的包发布到 Marketplace。
- **保持 token 处理最小化**，使用专用密钥和最小权限范围。

我的个人观点：**扩展生态系统在 CI 纪律方面落后于应用生态系统**，因为小团队认为手动工作流是可管理的。它们在不可管理之前是可管理的。一次匆忙的补丁、一个损坏的包、一次忘记的清单更新——信任就会下降。

这些可重用的操作很有用，因为它们将重复的发布逻辑编码一次，让团队专注于扩展质量，而非打包机制。

仍然需要工程判断。你应该在 Marketplace 发布后面设置质量门控，并将发布清单视为审计过的发布制品。但基线管道复杂度现在已经足够低，纯手动发布主要是技术债务。

如果你领导扩展开发，**现在就跨仓库标准化这个流程**。你会获得更好的可追溯性、更简单的上手体验和更少的单人发布瓶颈。

### 建议的推广方式

- **从一个扩展的构建加 gallery 发布开始。**
- **在验证了你的清单源约定后引入版本标记。**
- **只有在密钥管理和发布门控到位后，再加入 Marketplace 发布。**

这不是为了追求 DevOps 时尚。而是为了安装你的工具并期望更新能正常工作的用户的可靠性。

稳定的扩展生态系统是用与稳定应用相同的方式构建的：使用无聊的、可重复的自动化来消除人工猜测。