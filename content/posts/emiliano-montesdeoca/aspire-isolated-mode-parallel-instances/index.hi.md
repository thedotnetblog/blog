---
title: "Aspire का Isolated Mode Parallel Development के Port Conflict Nightmare को Fix करता है"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 --isolated mode introduce करता है: random ports, separate secrets, और same AppHost के multiple instances चलाते समय zero collisions। AI agents, worktrees और parallel workflows के लिए perfect।"
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - parallel-development
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "aspire-isolated-mode-parallel-instances" >}}).*

अगर आपने कभी एक ही project के दो instances एक साथ चलाने की कोशिश की है, तो आप pain जानते हैं। Port 8080 already in use है।

Aspire 13.2 इसे एक single flag से fix करता है। James Newton-King ने [पूरी details लिखी हैं](https://devblogs.microsoft.com/aspire/aspire-isolated-mode-parallel-development/)।

## Fix: `--isolated`

```bash
aspire run --isolated
```

हर run को मिलता है:
- **Random ports** — instances के बीच कोई collisions नहीं
- **Isolated user secrets** — connection strings और API keys प्रति instance अलग रहती हैं

## Real scenarios जहाँ यह शानदार है

**Multiple checkouts:**

```bash
# Terminal 1
cd ~/projects/my-app-feature
aspire run --isolated

# Terminal 2
cd ~/projects/my-app-bugfix
aspire run --isolated
```

दोनों बिना conflicts के चलते हैं।

**VS Code में Background agents।** जब Copilot Chat का background agent आपके code पर independently काम करने के लिए git worktree बनाता है, तो isolated mode ensure करता है कि दोनों instances काम करें।

**यह कैसे काम करता है:**

`--isolated` pass करने पर, CLI run के लिए unique instance ID generate करता है। यह दो behaviors drive करता है:
1. **Port randomization** — सभी के लिए random available ports
2. **Secret isolation** — प्रत्येक isolated run को अपना user secrets store मिलता है

## समापन

Isolated mode एक small feature है जो real problem को solve करती है। `aspire update --self` से 13.2 लें।
