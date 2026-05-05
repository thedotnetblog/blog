---
title: "Azure Smart Tier 正式发布 — 无需生命周期规则即可自动优化 Blob Storage 成本"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Blob Storage smart tier 现已正式发布，根据实际访问模式自动在 hot、cool 和 cold 层之间移动对象 — 无需生命周期规则。"
tags:
  - azure
  - storage
  - blob-storage
  - cost-optimization
  - cloud-native
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "azure-smart-tier-blob-storage-ga.md" >}})。*

如果你曾经花时间调整 Azure Blob Storage 的生命周期策略，然后看着它们在访问模式变化时土崩瓦解，那这篇文章就是为你准备的。微软刚刚宣布了 Azure Blob 和 Data Lake Storage 的 [smart tier 正式发布](https://azure.microsoft.com/en-us/blog/optimize-object-storage-costs-automatically-with-smart-tier-now-generally-available/) — 这是一项完全托管的分层功能，根据实际使用情况自动在 hot、cool 和 cold 层之间移动对象。

## Smart tier 实际做了什么

概念很简单：smart tier 持续评估存储账户中每个对象的最后访问时间。频繁访问的数据保持在 hot 层，不活跃的数据在 30 天后移到 cool 层，再过 60 天移到 cold 层。当数据被再次访问时，立即提升回 hot 层。循环重新开始。

无需配置生命周期规则。无需预测访问模式。无需手动调优。

在预览期间，微软报告称 **超过 50% 的 smart tier 管理容量根据实际访问模式自动转移到了更冷的层级**。对于大型存储账户来说，这是一笔可观的成本节省。

## 为什么这对 .NET 开发者很重要

如果你正在构建生成日志、遥测数据、分析数据或任何类型的不断增长的数据资产的应用 — 说实话，谁不是呢 — 存储成本会很快累积起来。传统的做法是编写生命周期管理策略，测试它们，然后在应用的访问模式变化时重新调整。Smart tier 完全消除了这个工作流。

一些实用的场景：

- **应用遥测和日志** — 调试时是 hot，几周后几乎不再访问
- **数据管道和 ETL 输出** — 处理期间频繁访问，之后大多处于 cold 状态
- **用户生成内容** — 最近上传的是 hot，较老的内容逐渐变冷
- **备份和归档数据** — 偶尔因合规需要访问，大部分时间处于闲置状态

## 如何设置

启用 smart tier 是一次性配置：

- **新账户**：在创建存储账户时选择 smart tier 作为默认访问层（需要区域冗余）
- **现有账户**：将 blob 访问层从当前默认值切换到 smart tier

小于 128 KiB 的对象保持在 hot 层，不产生监控费用。其他所有对象按照标准 hot/cool/cold 容量费率计费，没有层级转换费用，没有提前删除罚金，没有数据检索成本。每个对象的月度监控费用涵盖编排服务。

## 需要了解的权衡

Smart tier 的分层规则是固定的（30 天 → cool，90 天 → cold）。如果你需要自定义阈值 — 比如某个特定工作负载在 7 天后移到 cool — 生命周期规则仍然是正确的选择。而且不要混用：避免对 smart tier 管理的对象使用生命周期规则，因为它们可能会产生冲突。

## 总结

这算不上革命性的改变，但它解决了一个实实在在的运维痛点。如果你管理着不断增长的 blob storage 账户，并且厌倦了维护生命周期策略，[启用 smart tier](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-smart) 让 Azure 来处理吧。目前在几乎所有区域公有云区域都可以使用。
