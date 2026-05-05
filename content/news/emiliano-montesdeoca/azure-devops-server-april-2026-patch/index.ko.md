---
title: "Azure DevOps Server 2026년 4월 패치 — PR 완료 수정 및 보안 업데이트"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure DevOps Server가 패치 3을 받았습니다. PR 완료 실패 수정, 로그아웃 유효성 검사 개선, GitHub Enterprise Server PAT 연결 복원이 포함됩니다."
tags:
  - azure-devops
  - devops
  - patches
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "azure-devops-server-april-2026-patch.md" >}})를 참조하세요.*

셀프 호스팅 Azure DevOps Server를 운영하는 팀들에게 빠른 안내입니다. Microsoft가 세 가지 수정 사항을 포함한 [2026년 4월 패치 3](https://devblogs.microsoft.com/devops/april-patches-for-azure-devops-server/)을 릴리스했습니다.

## 수정된 내용

- **Pull Request 완료 실패** — 작업 항목 자동 완료 중 null 참조 예외로 인해 PR 병합이 실패할 수 있었습니다. 무작위 PR 완료 오류를 겪었다면, 이것이 원인일 가능성이 높습니다
- **로그아웃 리디렉션 유효성 검사** — 잠재적인 악성 리디렉션을 방지하기 위해 로그아웃 시 유효성 검사가 개선되었습니다. 빠르게 적용할 가치가 있는 보안 수정입니다
- **GitHub Enterprise Server PAT 연결** — GitHub Enterprise Server에 대한 Personal Access Token 연결 생성이 작동하지 않았는데, 이제 복원되었습니다

## 업데이트 방법

[패치 3](https://aka.ms/devopsserverpatch3)을 다운로드하고 설치 프로그램을 실행하세요. 패치가 적용되었는지 확인하려면:

```bash
<patch-installer>.exe CheckInstall
```

Azure DevOps Server를 온프레미스에서 운영하고 있다면, Microsoft는 보안과 안정성 모두를 위해 최신 패치를 유지할 것을 강력히 권장합니다. 전체 세부 사항은 [릴리스 노트](https://learn.microsoft.com/azure/devops/server/release-notes/azuredevopsserver?view=azure-devops#azure-devops-server-patch-3-release-date-april-14-2026)를 확인하세요.
