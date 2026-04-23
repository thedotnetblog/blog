---
title: "Python, TypeScript और .NET में azd Hooks: Shell Scripts से मुक्ति"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI अब Python, JavaScript, TypeScript या .NET में hooks लिखने की सुविधा देता है। माइग्रेशन स्क्रिप्ट के लिए Bash की ओर switch करने की जरूरत खत्म।"
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*यह पोस्ट स्वचालित रूप से अनुवादित की गई है। मूल संस्करण के लिए, [यहाँ क्लिक करें]({{< ref "index.md" >}})।*

अगर आपने कभी पूरी तरह .NET में बना प्रोजेक्ट रखा हो और फिर भी azd hooks के लिए Bash scripts लिखनी पड़ी हों, तो वो दर्द आप समझते हैं। जब प्रोजेक्ट का बाकी सब कुछ C# है, तो pre-provisioning step के लिए shell syntax में क्यों जाएं?

वो frustration अब officially solve हो गई है। Azure Developer CLI ने [hooks के लिए multi-language support launch](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/) किया है, और यह उतना ही अच्छा है जितना सुनाई देता है।

## Hooks क्या हैं

Hooks वो scripts हैं जो `azd` lifecycle के key points पर run होती हैं — provisioning से पहले, deployment के बाद, और अन्य। ये `azure.yaml` में define होती हैं और CLI को modify किए बिना custom logic inject करने देती हैं।

पहले सिर्फ Bash और PowerShell support थे। अब **Python, JavaScript, TypeScript या .NET** use कर सकते हैं — बाकी सब `azd` automatically handle करता है।

## Detection कैसे काम करती है

बस hook को एक file पर point करें और `azd` extension से language infer करता है:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

कोई extra config नहीं। अगर extension ambiguous हो तो `kind: python` (या relevant language) explicitly specify कर सकते हैं।

## Language-specific details

### Python

Script के साथ (या किसी parent directory में) `requirements.txt` या `pyproject.toml` रखें। `azd` automatically virtual environment बनाएगा, dependencies install करेगा और script run करेगा।

### JavaScript और TypeScript

Same pattern — script के पास `package.json` रखें और `azd` पहले `npm install` run करेगा। TypeScript के लिए `npx tsx` use होता है, बिना compile step और बिना `tsconfig.json`।

### .NET

दो modes उपलब्ध:

- **Project mode**: Script के पास `.csproj` हो तो `azd` automatically `dotnet restore` और `dotnet build` run करता है।
- **Single-file mode**: .NET 10+ पर standalone `.cs` files सीधे `dotnet run script.cs` से run होती हैं। Project file की जरूरत नहीं।

## Executor-specific configuration

हर language optional `config` block support करती है:

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

## .NET developers के लिए क्यों मायने रखता है

Hooks azd-based project में वो आखिरी जगह थी जो language switch करने पर मजबूर करती थी। अब पूरा deployment pipeline — app code से लेकर lifecycle hooks तक — एक ही language में रह सकता है। Existing .NET utilities hooks में reuse कर सकते हैं, shared libraries reference कर सकते हैं, और shell script maintenance से छुटकारा मिलता है।

## निष्कर्ष

ये उन changes में से एक है जो छोटे लगते हैं लेकिन azd के daily workflow से बहुत friction हटाते हैं। Hooks के लिए multi-language support अभी available है — full documentation के लिए [official post](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/) देखें।
