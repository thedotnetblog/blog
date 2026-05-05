---
title: "azd钩子支持Python、TypeScript和.NET：告别Shell脚本"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI现在支持用Python、JavaScript、TypeScript或.NET编写钩子。不再需要仅仅为了运行迁移脚本就切换到Bash。"
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*本文已自动翻译。如需查看原始版本，请[点击此处]({{< ref "index.md" >}})。*

如果你曾经有一个完全用.NET构建的项目，却还需要为azd钩子编写Bash脚本，你一定懂那种痛苦。当项目其他部分都是C#时，为什么要在pre-provisioning步骤中切换到Shell语法呢？

这个问题现在有了官方解决方案。Azure Developer CLI [刚刚发布了钩子的多语言支持](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/)，效果正如预期的那么好。

## 什么是钩子

钩子是在`azd`生命周期关键节点运行的脚本——预置配置之前、部署之后等。它们在`azure.yaml`中定义，无需修改CLI即可注入自定义逻辑。

此前只支持Bash和PowerShell。现在可以使用**Python、JavaScript、TypeScript或.NET**——`azd`会自动处理其余的一切。

## 检测机制

只需将钩子指向一个文件，`azd`就会从文件扩展名推断语言：

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

无需额外配置。如果扩展名不明确，可以添加`kind: python`（或相应语言）来明确指定。

## 各语言的重要细节

### Python

在脚本旁边（或任意父目录中）放置`requirements.txt`或`pyproject.toml`，`azd`会自动创建虚拟环境、安装依赖并运行脚本。

### JavaScript和TypeScript

同样的模式——在脚本附近放置`package.json`，`azd`会先运行`npm install`。对于TypeScript，使用`npx tsx`，无需编译步骤，也不需要`tsconfig.json`。

### .NET

提供两种模式：

- **项目模式**：如果脚本旁边有`.csproj`文件，`azd`会自动运行`dotnet restore`和`dotnet build`。
- **单文件模式**：在.NET 10+上，独立的`.cs`文件可通过`dotnet run script.cs`直接运行，无需项目文件。

## 执行器特定配置

每种语言都支持可选的`config`块：

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

## 对.NET开发者的意义

钩子曾是基于azd的项目中最后一个强制语言切换的地方。现在，整个部署流水线——从应用代码到基础设施脚本再到生命周期钩子——都可以使用同一种语言。你可以在钩子中复用现有的.NET工具，引用共享类库，不再需要维护Shell脚本。

## 总结

这看起来是个小改动，但它切实减少了日常azd工作流程中的摩擦。钩子的多语言支持现已可用——查阅[官方文章](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/)获取完整文档。
