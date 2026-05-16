---
title: "Azure Data Studio Is Retired: Move Your Azure SQL Workflow to VS Code"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio retired February 6 2025, with support ending February 28 2026. Here is the complete migration path to VS Code with the MSSQL extension."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

[Azure Data Studio retired on February 6, 2025](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), with support ending February 28, 2026 — the recommended replacement is VS Code with the MSSQL extension.

## What to install

Three things to get started:

- **MSSQL extension** — search "SQL Server (mssql)" in the VS Code Marketplace
- **SQL Database Projects extension** — schema-as-code, build validation, guided publish
- **.NET 8 SDK** — required by the build system; missing SDK is the most common first-run issue

## Migrating your ADS connections and settings

The MSSQL extension ships an **ADS Migration Toolkit** that handles the one-time migration in a guided flow: saved connections, connection groups, settings, and key bindings are all imported automatically.

## Restoring F5 muscle memory

ADS users rely on F5 to run queries. Install the **MSSQL Database Management Keymap** extension to get ADS-style key bindings back, including F5.

## SQL Database Projects: schema as code

Right-click a project → **Publish** → configure target → review the generated T-SQL script → deploy. The script preview before deployment is the key safety feature. Item templates generate stubs for tables, stored procedures, and views — the same workflow as SSDT.

Common gotcha: a **target platform mismatch** in the `.sqlproj` file will cause build errors if the project was created against a different SQL Server version.

## Schema Compare and Schema Designer

The extension also includes **Schema Compare** (diff your project against the deployed database) and **Schema Designer** (visual schema editing without writing DDL by hand).

## Microsoft Fabric developers

The setup is identical, but start from the **Fabric portal** and connect the database to Git first before opening it in VS Code. Microsoft has a dedicated guide: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## Wrapping up

The migration is a one-time guided flow, not a manual rebuild. Install the three tools, run the ADS Migration Toolkit, restore your key bindings, and you're back to normal in under 10 minutes.

See the [full article](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) for step-by-step screenshots and the Fabric-specific walkthrough.
