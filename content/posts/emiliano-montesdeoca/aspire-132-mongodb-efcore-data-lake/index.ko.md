---
title: "Aspire 13.2에 MongoDB EF Core와 Azure Data Lake 추가 — 꼭 써봐야 할 두 가지 통합"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Aspire 13.2에 제로 설정 헬스 체크와 서비스 디스커버리를 갖춘 MongoDB Entity Framework Core 및 Azure Data Lake Storage 통합이 추가되었습니다. 실제로 어떻게 사용하는지 살펴봅니다."
tags:
  - dotnet-aspire
  - efcore
  - mongodb
  - azure
  - data-lake
  - cloud-native
---

> *이 글은 자동 번역되었습니다. 원문은 [여기]({{< ref "aspire-132-mongodb-efcore-data-lake.md" >}})를 참조하세요.*

Aspire 13.2가 [두 가지 새로운 데이터베이스 통합](https://devblogs.microsoft.com/aspire/aspire-new-database-integrations/)과 함께 출시되었습니다. 주목할 만한 것은 MongoDB Entity Framework Core와 Azure Data Lake Storage입니다. Aspire 앱에서 MongoDB와 EF Core를 사용하고 싶었거나, 서비스 디스커버리가 포함된 Data Lake 워크로드를 연결해야 했다면, 이번 릴리스가 둘 다 제공합니다.

## Aspire에서 MongoDB가 EF Core를 만나다

이것이 제가 가장 기대하고 있는 통합입니다. Aspire는 한동안 MongoDB를 지원해 왔지만, 항상 원시 드라이버였습니다 — EF Core 없이, `DbContext` 없이, 문서에 대한 LINQ 쿼리 없이. 이제 MongoDB에서 완전한 EF Core 경험을 얻을 수 있으며, Aspire의 자동 헬스 체크와 서비스 디스커버리도 함께 제공됩니다.

설정은 전형적인 Aspire 패턴을 따릅니다. AppHost에서:

```csharp
var mongodb = builder.AddMongoDB("mongodb")
    .WithDataVolume()
    .WithLifetime(ContainerLifetime.Persistent);

var apiService = builder.AddProject<Projects.ApiService>("api")
    .WithReference(mongodb);
```

그런 다음 소비 프로젝트에서 EF Core 통합을 추가합니다:

```bash
dotnet add package Aspire.MongoDB.EntityFrameworkCore
```

그리고 `DbContext`를 등록합니다:

```csharp
builder.AddMongoDbContext<MyDbContext>("mongodb", "mydb");
```

이후로는 표준 EF Core입니다. 엔티티를 정의하고, 다른 프로바이더와 마찬가지로 `DbContext`를 사용하면 됩니다. 커넥션 풀링, OpenTelemetry 트레이스, 헬스 체크는 통합이 백그라운드에서 처리합니다.

원시 드라이버로 MongoDB를 사용하면서 커넥션 문자열을 수동으로 설정하던 .NET 개발자들에게 이것은 반가운 개선입니다. Aspire의 서비스 디스커버리를 잃지 않으면서 완전한 EF Core 추상화를 얻을 수 있습니다.

## Azure Data Lake Storage 합류

두 번째 큰 추가 사항은 [Azure Data Lake Storage (ADLS) 통합](https://aspire.dev/integrations/cloud/azure/azure-storage-datalake/)입니다. 데이터 파이프라인, ETL 프로세스 또는 분석 플랫폼을 구축하고 있다면, 이제 다른 Aspire 의존성과 동일한 방식으로 Data Lake 리소스를 연결할 수 있습니다.

AppHost에서:

```csharp
var storage = builder.AddAzureStorage("azure-storage");
var dataLake = storage.AddDataLake("data-lake");
var fileSystem = storage.AddDataLakeFileSystem("data-lake-file-system");

var analyticsService = builder.AddProject<Projects.AnalyticsService>("analytics")
    .WithReference(dataLake)
    .WithReference(fileSystem);
```

소비 프로젝트에서:

```csharp
builder.AddAzureDataLakeServiceClient("data-lake");
builder.AddAzureDataLakeFileSystemClient("data-lake-file-system");
```

수동 커넥션 문자열 관리도, 크레덴셜 찾기도 필요 없습니다. Aspire가 리소스를 프로비저닝하고 주입합니다. 운영 데이터와 분석 워크로드를 모두 다루는 클라우드 네이티브 .NET 앱을 구축하는 우리에게, Data Lake가 Aspire 모델에서 일급 시민처럼 느껴지게 됩니다.

## 사소하지만 중요한 수정 사항

주요 기능 외에도 몇 가지 주목할 만한 개선 사항이 있습니다:

- **MongoDB 커넥션 문자열 수정** — 데이터베이스 이름 앞의 슬래시가 이제 올바르게 처리됩니다. 우회 방법을 사용하고 있었다면 이제 제거할 수 있습니다
- **SQL Server 내보내기** — `Aspire.Hosting.SqlServer`가 이제 더 세밀한 제어를 위한 추가 서버 구성 옵션을 내보냅니다
- **에뮬레이터 업데이트** — ServiceBus 에뮬레이터 2.0.0, App Configuration 에뮬레이터 1.0.2, CosmosDB 프리뷰 에뮬레이터에 레디니스 체크 추가
- **Azure Managed Redis** — 이제 기본적으로 `rediss://`(Redis Secure)를 사용하여 연결이 기본 암호화됩니다

마지막 항목은 미묘하지만 중요합니다 — 기본 암호화 Redis는 프로덕션에서 설정해야 할 것이 하나 줄어든다는 의미입니다.

## 마무리

Aspire 13.2는 점진적인 릴리스이지만, MongoDB EF Core와 Data Lake 통합은 실질적인 공백을 채웁니다. Aspire에서 MongoDB에 대한 적절한 EF Core 지원을 기다리고 있었거나, Data Lake를 일급 의존성으로 필요로 했다면, [13.2로 업그레이드](https://get.aspire.dev)하고 사용해 보세요. `aspire add` 명령이 필요한 모든 것을 스캐폴딩합니다.

[전체 릴리스 노트](https://aspire.dev/whats-new/aspire-13-2/#-integrations-updates)에서 자세한 내용을 확인하고, [통합 갤러리](https://aspire.dev/integrations/gallery/)에서 전체 목록을 살펴보세요.
