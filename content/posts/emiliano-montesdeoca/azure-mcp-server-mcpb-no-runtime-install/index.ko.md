---
title: "Azure MCP Server 이제 .mcpb — 런타임 없이 설치하기"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server가 MCP Bundle(.mcpb)로 제공됩니다 — 다운로드하고 Claude Desktop에 드래그하면 끝. Node.js, Python, .NET 불필요."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*이 게시물은 자동 번역되었습니다. 원문을 보려면 [여기를 클릭하세요]({{< ref "index.md" >}}).*

MCP 서버 설정에서 번거로웠던 것이 무엇인지 아시나요? 런타임이 필요했습니다. npm 버전에는 Node.js, pip/uvx에는 Python, dotnet 버전에는 .NET SDK.

[Azure MCP Server가 이를 바꿨습니다](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). 이제 `.mcpb` — MCP Bundle — 로 제공되며 설정은 드래그 앤 드롭입니다.

## MCP Bundle이란?

VS Code 확장(`.vsix`)이나 브라우저 확장(`.crx`)처럼 생각하세요. 단, MCP 서버용입니다. `.mcpb` 파일은 서버 바이너리와 모든 종속성을 포함한 독립적인 ZIP 아카이브입니다.

## 설치 방법

**1. 플랫폼용 번들 다운로드**

[GitHub Releases 페이지](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server)에서 OS와 아키텍처에 맞는 `.mcpb` 파일을 다운로드합니다.

**2. Claude Desktop에 설치**

가장 쉬운 방법: 확장 설정 페이지(`☰ → 파일 → 설정 → 확장`)가 열린 상태에서 `.mcpb` 파일을 Claude Desktop 창에 드래그 앤 드롭합니다. 서버 세부 정보를 확인하고 설치를 클릭합니다.

**3. Azure 인증**

```bash
az login
```

끝입니다. Azure MCP Server는 기존 Azure 자격 증명을 사용합니다.

## 할 수 있는 것

AI 클라이언트에서 직접 100개 이상의 Azure 서비스 도구에 접근:
- Cosmos DB, Storage, Key Vault, App Service, Foundry 쿼리 및 관리
- 모든 작업을 위한 `az` CLI 명령 생성
- Bicep 및 Terraform 템플릿 생성

## 시작하기

- **다운로드**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **저장소**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **문서**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

[전체 게시물](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/)을 확인하세요.
