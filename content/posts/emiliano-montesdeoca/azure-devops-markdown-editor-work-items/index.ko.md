---
title: "Azure DevOps가 드디어 모두가 불평하던 Markdown 편집기를 고쳤다"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Azure DevOps 작업 항목의 Markdown 편집기가 미리보기와 편집 모드의 명확한 구분을 얻었습니다. 작은 변경이지만 정말 성가신 워크플로 문제를 해결합니다."
tags:
  - azure-devops
  - devops
  - productivity
  - developer-tools
---

> *이 글은 자동 번역되었습니다. 원본은 [여기]({{< ref "azure-devops-markdown-editor-work-items.md" >}})에서 확인하세요.*

Azure Boards를 사용한다면 아마 이런 경험이 있을 겁니다: 작업 항목 설명을 읽고 있는데, 인수 기준을 확인하는 중에 실수로 더블클릭을 합니다. 쾅 — 편집 모드에 들어갔습니다. 아무것도 편집하고 싶지 않았는데. 그냥 읽고 있었을 뿐인데.

Dan Hellem이 [수정을 발표](https://devblogs.microsoft.com/devops/improving-the-markdown-editor-for-work-items/)했는데, 작아 보이지만 일상 워크플로에서 진짜 마찰을 제거하는 변경입니다.

## 무엇이 바뀌었나

작업 항목 텍스트 필드의 Markdown 편집기가 이제 **기본적으로 미리보기 모드**로 열립니다. 콘텐츠를 읽고 상호작용할 수 있습니다 — 링크 따라가기, 포맷 확인 — 실수로 편집 모드에 들어갈 걱정 없이.

실제로 편집하고 싶을 때 필드 상단의 편집 아이콘을 클릭합니다. 완료하면 명시적으로 미리보기 모드로 돌아갑니다. 단순하고, 의도적이고, 예측 가능합니다.

## 보이는 것보다 더 중요한 이유

[커뮤니티 피드백 스레드](https://developercommunity.visualstudio.com/t/Markdown-editor-for-work-item-multi-line/10935496)가 길었습니다. 더블클릭으로 편집하는 동작은 2025년 7월 Markdown 편집기와 함께 도입되었고, 불만은 거의 즉시 시작되었습니다.

Azure Boards로 스프린트 계획, 백로그 개선, 코드 리뷰를 하는 팀에게 이런 미세한 마찰은 누적됩니다.

## 배포 상태

이미 일부 고객에게 배포되고 있으며 앞으로 2~3주에 걸쳐 전체로 확대됩니다.

## 마무리

모든 개선이 헤드라인 기능이 될 필요는 없습니다. 때로 최고의 업데이트는 단순히 성가신 것을 제거하는 것입니다. 이것이 바로 그런 것 — 작업 항목을 평화롭게 읽고 싶은 사람들을 위해 Azure Boards를 덜 적대적으로 만드는 작은 UX 수정입니다.
