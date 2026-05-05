---
title: "Windows App Dev CLI v0.3：从终端实现F5调试和面向智能体的UI自动化"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3带来了winapp run（从终端进行调试启动）、winapp ui（UI自动化）以及一个让dotnet run支持打包应用的NuGet包。"
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*本文已自动翻译。如需查看原文，请[点击这里]({{< ref "index.md" >}})。*

Visual Studio的F5体验非常棒。但是，仅仅为了启动和调试一个打包的Windows应用而打开VS，在CI流水线、自动化工作流或AI智能体执行测试时就显得过于繁重了。

Windows App Development CLI v0.3[正式发布](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/)，通过两个核心功能直接解决了这个问题：`winapp run`和`winapp ui`。

## winapp run：随处可用的F5

`winapp run`接受一个未打包的应用文件夹和清单，执行VS在调试启动时所做的一切：注册松散包、启动应用，并在重新部署之间保留`LocalState`。

```bash
# 构建应用，然后作为打包应用运行
winapp run ./bin/Debug
```

支持WinUI、WPF、WinForms、Console、Avalonia等。各模式同时面向开发者和自动化工作流：

- **`--detach`**：启动后立即将控制权返回给终端。非常适合CI/自动化。
- **`--unregister-on-exit`**：应用关闭时清理已注册的包。
- **`--debug-output`**：实时捕获`OutputDebugString`消息和异常。

## 新NuGet包：打包应用的dotnet run支持

面向.NET开发者，新增了一个NuGet包：`Microsoft.Windows.SDK.BuildTools.WinApp`。安装后，`dotnet run`处理整个内循环：构建、准备松散布局包、在Windows中注册和启动——一步完成。

```bash
winapp init
# 或
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui：从命令行实现UI自动化

这是开启智能体场景的功能。`winapp ui`从终端提供对任何正在运行的Windows应用（WPF、WinForms、Win32、Electron、WinUI3）的完整UI自动化访问。

可以实现：

- 列出所有顶层窗口
- 遍历窗口的完整UI自动化树
- 按名称、类型或自动化ID搜索元素
- 单击、调用和设置值
- 截图
- 等待元素出现——非常适合测试同步

将`winapp ui`与`winapp run`结合使用，即可从终端实现完整的构建→启动→验证工作流。智能体可以运行应用、检查UI状态、以编程方式交互并验证结果。

## 其他新功能

- **`winapp unregister`**：测试完成后删除旁加载的包。
- **`winapp manifest add-alias`**：添加别名，从终端按名称启动应用。
- **Tab补全**：一条命令配置PowerShell补全。

## 安装方式

```bash
winget install Microsoft.WinAppCli
# 或
npm install -g @microsoft/winappcli
```

CLI处于公开预览阶段。完整文档请查看[GitHub仓库](https://github.com/microsoft/WinAppCli)，所有详细信息请查看[原始公告](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/)。
