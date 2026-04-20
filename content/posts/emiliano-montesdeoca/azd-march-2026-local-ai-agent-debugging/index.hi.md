---
title: "azd अब AI Agents को Locally Run और Debug करने देता है — मार्च 2026 में क्या बदला"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI ने मार्च 2026 में सात releases ship किए। Highlights: AI agents के लिए local run-and-debug loop, project setup में GitHub Copilot integration, और Container App Jobs support।"
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "azd-march-2026-local-ai-agent-debugging" >}}).*

एक महीने में सात releases। यही है Azure Developer CLI (`azd`) team ने मार्च 2026 में push किया, और headline feature वह है जिसका मैं इंतज़ार कर रहा था: **AI agents के लिए local run-and-debug loop**।

## Deploy किए बिना AI agents run और debug करें

यह बड़ा है। नया `azure.ai.agents` extension commands का set देता है:

- `azd ai agent run` — agent को locally start करें
- `azd ai agent invoke` — इसे messages भेजें (local या deployed)
- `azd ai agent show` — container status और health दिखाएं
- `azd ai agent monitor` — container logs real time में stream करें

पहले, AI agent test करने का मतलब था हर बार Microsoft Foundry में deploy करना। अब आप locally iterate कर सकते हैं।

## GitHub Copilot आपका azd project scaffold करता है

`azd init` अब "Set up with GitHub Copilot (Preview)" option offer करता है। Copilot agent आपके project structure के लिए configuration scaffold करता है।

## Container App Jobs और deployment improvements

- **Container App Jobs**: `azd` अब existing `host: containerapp` config के माध्यम से `Microsoft.App/jobs` deploy करता है
- **Configurable deployment timeouts**: `azd deploy` पर नया `--timeout` flag
- **Remote build fallback**: जब remote ACR build fail हो, तो `azd` automatically local Docker/Podman build पर fall back करता है
- **Local preflight validation**: Bicep parameters locally validate होते हैं deploy करने से पहले

## समापन

Local AI agent debugging loop इस release का star है। [पूरे release notes](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) देखें।
