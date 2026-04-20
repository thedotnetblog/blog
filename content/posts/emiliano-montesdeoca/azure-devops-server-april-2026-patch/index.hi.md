---
title: "Azure DevOps Server अप्रैल 2026 पैच — PR Completion फिक्स और Security अपडेट"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server को Patch 3 मिला है जिसमें PR completion विफलताओं का फिक्स, बेहतर sign-out validation, और GitHub Enterprise Server PAT कनेक्शन की बहाली शामिल है।"
tags:
  - azure-devops
  - devops
  - patches
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "azure-devops-server-april-2026-patch" >}}).*

self-hosted Azure DevOps Server चला रही teams के लिए एक ज़रूरी सूचना: Microsoft ने [अप्रैल 2026 के लिए Patch 3](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/) release किया है जिसमें तीन targeted fixes हैं।

## क्या ठीक किया गया

- **Pull request completion failures** — work item auto-completion के दौरान एक null reference exception से PR merges fail हो सकती थीं। अगर आपको random PR completion errors आती थीं, तो संभवतः यही कारण था
- **Sign-out redirect validation** — sign-out के दौरान संभावित malicious redirects को रोकने के लिए बेहतर validation। यह एक security fix है जिसे जल्दी लागू करना उचित है
- **GitHub Enterprise Server PAT connections** — GitHub Enterprise Server में Personal Access Token connections बनाना टूटा हुआ था, अब यह ठीक हो गया है

## Update कैसे करें

[Patch 3](https://aka.ms/devopsserverpatch3) download करें और installer चलाएं। यह verify करने के लिए कि patch लागू हुआ है:

```bash
<patch-installer>.exe CheckInstall
```

अगर आप Azure DevOps Server on-premises चला रहे हैं, तो Microsoft दृढ़ता से सुरक्षा और विश्वसनीयता दोनों के लिए नवीनतम patch पर रहने की सलाह देता है। पूरी जानकारी के लिए [release notes](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026) देखें।
