content = """\
---
title: "azd अब आपको AI Agents को Locally Run और Debug करने देता है — March 2026 में क्या बदला"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI ने March 2026 में सात releases ship कीं। मुख्य बातें: AI agents के लिए local run-and-debug loop, project setup में GitHub Copilot integration, और Container App Jobs support।"
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

एक महीने में सात releases। यही Azure Developer CLI (`azd`) team ने March 2026 में deliver किया, और headline feature वही है जिसका मुझे इंतज़ार था: **AI agents के लिए local run-and-debug loop**।

PC Chan ने [पूरा roundup publish किया है](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/), और हालाँकि उसमें काफी कुछ है, लेकिन मुझे जो AI-powered apps build करने वाले .NET developers के लिए वाकई मायने रखता है वह filter करने दें।

## Deploy किए बिना AI agents run और debug करें

यही बड़ी बात है। नया `azure.ai.agents` extension commands का एक set add करता है जो AI agents के लिए एक proper inner-loop experience देता है:

- `azd ai agent run` — आपके agent को locally start करता है
- `azd ai agent invoke` — उसे messages भेजता है (local या deployed)
- `azd ai agent show` — container status और health display करता है
- `azd ai agent monitor` — real time में container logs stream करता है

इससे पहले, एक AI agent को test करने का मतलब था हर बदलाव के बाद Microsoft Foundry में deploy करना। अब आप locally iterate कर सकते हैं, अपने agent के behavior को test कर सकते हैं, और deploy तभी करें जब आप ready हों। अगर आप Microsoft Agent Framework या Semantic Kernel के साथ agents build कर रहे हैं, तो यह आपके daily workflow को बदल देता है।

Invoke command local और deployed दोनों agents के against काम करता है, जिसका मतलब है कि आप same testing workflow use कर सकते हैं चाहे agent कहीं भी run हो। यह वह detail है जो आपको दो sets of test scripts maintain करने से बचाती है।

## GitHub Copilot आपका azd project scaffold करता है

`azd init` अब "Set up with GitHub Copilot (Preview)" option offer करता है। अपने project structure के बारे में manually prompts का जवाब देने की बजाय, एक Copilot agent आपके लिए configuration scaffold करता है। यह कुछ modify करने से पहले dirty working directory check करता है और upfront MCP server tool consent माँगता है।

जब कोई command fail होती है, `azd` अब AI-assisted troubleshooting offer करता है: एक category चुनें (explain, guidance, troubleshoot, या skip), agent को fix suggest करने दें, और retry करें — terminal छोड़े बिना। Complex infrastructure setups के लिए, यह वाकई time saver है।

## Container App Jobs और deployment improvements

कुछ deployment features जो ध्यान देने योग्य हैं:

- **Container App Jobs**: `azd` अब existing `host: containerapp` config के ज़रिये `Microsoft.App/jobs` deploy करता है। आपका Bicep template decide करता है कि target Container App है या Job — कोई extra setup नहीं।
- **Configurable deployment timeouts**: `azd deploy` पर नया `--timeout` flag और `azure.yaml` में `deployTimeout` field। Default 1200-second limit का अंदाज़ा लगाना अब नहीं।
- **Remote build fallback**: जब remote ACR build fail हो, `azd` automatically local Docker/Podman build पर fallback करता है।
- **Local preflight validation**: Bicep parameters Azure को round-trip किए बिना locally validate होते हैं, missing params पहले ही पकड़े जाते हैं।

## Developer experience की polish

कुछ smaller improvements जो मिलकर फर्क डालती हैं:

- JS/TS projects के लिए **Automatic pnpm/yarn detection**
- Python packaging के लिए **pyproject.toml support**
- **Local template directories** — `azd init --template` अब offline iteration के लिए filesystem paths accept करता है
- **`--no-prompt` mode में बेहतर error messages** — सभी missing values एक साथ resolution commands के साथ report होते हैं
- सभी framework build subprocesses (.NET, Node.js, Java, Python) में **Build environment variables** inject होते हैं

वह आखिरी बात subtle लेकिन महत्वपूर्ण है: आपके .NET build को अब `azd` environment variables का access है, जिसका मतलब है कि आप extra scripting के बिना build-time configuration injection कर सकते हैं।

## निष्कर्ष

Local AI agent debugging loop इस release का star है, लेकिन deployment improvements और DX polish का जमावड़ा `azd` को पहले से कहीं ज़्यादा mature feel कराता है। अगर आप Azure पर .NET apps deploy कर रहे हैं — खासकर AI agents — तो यह update install करने लायक है।

हर detail के लिए [पूरे release notes](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) देखें, या [azd install](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) से शुरू करें।
"""

path = "/Users/emiliano/.copilot/copilot-worktrees/blog/emimontesdeoca-unwresting-colby/content/posts/emiliano-montesdeoca/azd-march-2026-local-ai-agent-debugging/index.hi.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Post 5 done")
