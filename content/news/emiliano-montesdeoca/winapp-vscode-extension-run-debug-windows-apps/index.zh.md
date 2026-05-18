---
title: "WinApp VS Code扩展：无需离开编辑器即可运行、调试和打包Windows应用"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "WinApp VS Code扩展将完整的Windows应用开发CLI直接带入VS Code——无需Visual Studio即可运行、使用包标识调试、打包和签名Windows应用（WPF、WinUI、.NET、C++）。"
tags:
  - VS Code
  - Windows
  - WinUI
  - .NET
  - WPF
  - Developer Tooling
  - Desktop
---

*本文已自动翻译。要查看原始版本，请[点击此处]({{< ref "index.md" >}})。*

如果你曾经尝试过在VS Code中开发Windows应用，你一定熟悉那个时刻。你正在流畅地编写代码，在喜欢的编辑器里工作——突然需要为某个Windows API获取包标识。或者需要创建MSIX。或者需要签名一个包。于是你不得不打开Visual Studio，或者在深夜搜索"msix packaging without visual studio"。

这种摩擦现在消失了。[WinApp VS Code扩展](https://marketplace.visualstudio.com/items?itemName=Microsoft-WinAppCLI.winapp)进入了公开预览——它将完整的[Windows应用开发CLI](https://github.com/microsoft/WinAppCli)直接集成到VS Code中。无需单独安装，无需Visual Studio。

## F5启动获得包标识

Windows API的问题在于——通知、后台任务、设备端AI功能、共享目标——许多都要求应用具有**包标识**。没有它，这些API根本无法工作。

传统上，获取包标识意味着构建完整的MSIX安装程序或从Visual Studio启动。WinApp扩展通过自定义`winapp`调试类型彻底改变了这一点。

在`launch.json`中添加以下配置：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "winapp",
            "request": "launch",
            "name": "WinApp: Launch and Attach"
        }
    ]
}
```

按F5。扩展会找到你的构建输出和清单，通过`winapp run`为应用赋予包标识，并附加调试器。.NET应用使用`coreclr`（需要C# Dev Kit），C/C++使用`cppvsdbg`，Node/Electron使用内置调试器。

你可以配置`preLaunchTask`，让项目在每次按F5之前自动构建——与Visual Studio的构建并启动流程相同，只是在VS Code中。

## 命令面板中的完整工具集

打开`Ctrl+Shift+P`，输入`WinApp`，即可获得完整的工具集：

- **Initialize Project** — 使用Windows SDK和/或Windows App SDK配置项目
- **Run Application** — 以具有包标识的松散布局打包应用启动
- **Create MSIX Package** — 使用证书和运行时选项打包应用
- **Update Manifest Assets** — 从单个源图像自动生成所有必需的应用图标
- **Generate / Install Certificate** — 开发证书管理
- **Sign Package** — 签名MSIX或可执行文件
- **Run SDK Tool** — 直接运行`makeappx`、`signtool`、`mt`或`makepri`

也不需要安装WinApp CLI。它已捆绑在扩展中。

## 支持多种框架

这不仅仅是.NET WPF/WinUI的工具。该扩展支持：

- **.NET**: WPF、WinForms、Console、WinUI 3
- **C/C++**: Win32、CMake、MSBuild
- **Electron** / Node.js
- **Rust**
- **Tauri**
- **Flutter**

这种广泛支持是刻意为之的。VS Code是Web和跨平台开发者的聚集地。如果你正在构建需要Windows打包的Tauri或Electron应用，这个扩展无需你采用Visual Studio就能满足需求。

## 对.NET开发者的意义

我大量使用VS Code——这是我编写Markdown、管理配置、编辑小项目和运行终端的地方。但对于.NET Windows桌面开发，一旦需要与打包相关的任何操作，Visual Studio一直是唯一的真正选择。

这个扩展填补了这一空白。现在可以在VS Code中完成完整的.NET Windows桌面开发周期——编辑、构建、使用包标识运行、调试、打包、签名——无需离开编辑器。这是真正的生产力提升。

## 快速上手

```bash
code --install-extension Microsoft-WinAppCLI.winapp
```

或者在扩展视图（`Ctrl+Shift+X`）中搜索**WinApp**。

要求：
- Windows 10或更高版本
- VS Code 1.109.0或更高版本
- 适用于应用语言的调试器扩展

查看[Chiara Mooney的完整公告](https://devblogs.microsoft.com/ifdef-windows/announcing-the-winapp-vs-code-extension-run-debug-and-package-windows-apps-in-vs-code/)了解更多详情。

## 总结

WinApp VS Code扩展是.NET Windows桌面开发者的福音——他们一直在VS Code中工作，却不得不切换到Visual Studio进行打包工作。F5启动获得包标识、从命令面板打包MSIX、内置证书管理——这是正确的功能组合。

在下一个WPF或WinUI项目中试试看。你一直在绕过的摩擦刚刚大幅减少了。
