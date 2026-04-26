---
title: "SQL Server 2025 エージェント対応データベース：1つのエンジンでセキュリティ、バックアップ、MCP"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "Polyglot Taxシリーズの最終回は、本番環境の難しい問題に取り組みます：リレーショナル、JSON、グラフ、ベクターデータ全体での統一Row-Level Security、そしてMCP統合。"
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*この投稿は自動翻訳されています。オリジナル版は[こちら](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/)をクリックしてください。*

Aditya BadramrajuのPolyglot Taxシリーズを興味深く読んできました。パート4はシリーズを締めくくり、この架構を本番環境で信頼できるかどうかを実際に決める部分に取り組みます。

## すべてのデータモデルに対する1つのセキュリティモデル

1つのRow-Level Securityポリシーがすべてのデータモデルをカバー。監査人への証明が1つで済む。

## 統一バックアップ = アトミックリカバリ

ポリグロットスタックでは、5つのデータベースのPoint-in-Timeリカバリを協調させることは一貫性の悪夢です。1つのデータベースなら、定義上アトミックです。

## MCP統合：ハンドコードされたミドルウェア不要

SQL Server 2025はSQL MCPサーバーを直接サポート。エージェントはツールを呼び出し、エンジンが自動的にテナント分離とカラムマスキングを強制します。

オリジナルポスト（Aditya Badramraju著）: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/)。
