---
title: "SQL Server 2025 com a base de dades preparada per a agents: seguretat, còpies de seguretat i MCP en un sol motor"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "La part final de la sèrie Polyglot Tax tracta els problemes difícils de producció: una política de Row-Level Security unificada sobre dades relacionals, JSON, grafs i vectors, més els rastres d'auditoria xifrats i la integració MCP que fan que SQL Server 2025 sigui realment preparat per a agents."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*Aquest post ha estat traduït automàticament. Per a la versió original, [fes clic aquí](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

He seguit la sèrie Polyglot Tax d'Aditya Badramraju amb molt d'interès. Les parts 1-3 van construir un cas convincent per a SQL Server 2025 com una base de dades realment multimodel — JSON, grafs, vectors i dades relacionals en un sol motor amb un planificador de consultes unificat. La part 4 tanca la sèrie amb les parts que realment determinen si confiaries en aquesta arquitectura en producció.

Spoiler: la història de producció és sòlida.

## Un Sol Model de Seguretat per a Tots els Models de Dades

Això és el que passa amb els stacks poliglotes: quan un auditor pregunta "demostra que el Tenant A no pot veure les dades del Tenant B", has de respondre aquesta pregunta per a cada base de dades de manera independent. Cinc bases de dades, cinc models de seguretat, cinc proves.

Amb SQL Server 2025, defineixes una sola política de Row-Level Security i cobreix tots els models de dades:

```sql
CREATE FUNCTION dbo.fn_TenantFilter(@TenantID INT)
RETURNS TABLE WITH SCHEMABINDING
AS RETURN SELECT 1 AS fn_result
WHERE @TenantID = CAST(SESSION_CONTEXT(N'TenantID') AS INT);

CREATE SECURITY POLICY TenantIsolation
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Customers,     -- Relational
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Events,        -- JSON data
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Relationships, -- Graph edges
ADD FILTER PREDICATE dbo.fn_TenantFilter(TenantID)
ON dbo.Embeddings     -- Vector data
WITH (STATE = ON);
```

A partir d'aquí, qualsevol consulta — joins relacionals, consultes de camins JSON, travessies de graf, cerques de similitud vectorial — es filtra automàticament per tenant. El motor injecta el predicat a la planificació abans que cap dada surti de l'emmagatzematge. El teu codi no necessita `WHERE TenantID = @id` per tot arreu. Proves la política una sola vegada.

Les capes es combinen encara més: Dynamic Data Masking per a les columnes que no haurien de mostrar els valors complets a certs rols, Always Encrypted per al xifrat de punta a punta (fins i tot els DBAs no el poden llegir), i els stored procedures com a frontera de permisos perquè els agents només cridin allò que has exposat explícitament.

Aquesta és la part de l'arquitectura que realment importa en un SaaS amb requisits de compliment. Una política, una prova.

## Còpia de Seguretat Unificada = Recuperació Atòmica

Una instrucció, tots els models de dades, un punt en el temps coherent:

```sql
BACKUP DATABASE MultiModelApp
TO URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH COMPRESSION, ENCRYPTION (ALGORITHM = AES_256, SERVER CERTIFICATE = BackupCert);

RESTORE DATABASE MultiModelApp
FROM URL = 'https://storage.blob.core.windows.net/backups/MultiModelApp.bak'
WITH STOPAT = '2026-02-01 10:30:00';
```

En un stack poliglota, la recuperació point-in-time a través de cinc bases de dades significa coordinar cinc operacions de restauració i esperar que els timestamps encaixin dins d'un o dos segons. Per a dades financeres, aquesta inconsistència de dos segons és inacceptable. Amb una sola base de dades, un sol registre de transaccions i una sola restauració — la recuperació és atòmica per definició.

## Taules Ledger per a Rastreig d'Auditoria a Prova de Manipulacions

Per a sectors regulats, necessites més que "tenim logs". Necessites prova criptogràfica que aquells logs no han estat modificats:

```sql
CREATE TABLE FinancialTransactions (
    TransactionID INT PRIMARY KEY,
    AccountID INT NOT NULL,
    Amount MONEY NOT NULL,
    TransactionType NVARCHAR(20),
    TransactionDate DATETIME2 DEFAULT SYSUTCDATETIME()
)
WITH (SYSTEM_VERSIONING = ON, LEDGER = ON);
```

Cada insert, update i delete queda hashat criptogràficament dins d'una estructura tipus blockchain. Pots demostrar a un auditor — matemàticament — que una fila no ha estat manipulada des que es va escriure. En un stack poliglota, aquesta capacitat no existeix de manera uniforme a totes les teves bases de dades.

## Integració MCP: Agents Sense Middleware Fet a Mà

Això és cap on anava la sèrie: SQL Server 2025 dona suport directe al SQL MCP Server, cosa que significa que els teus agents poden cridar la base de dades mitjançant tool calls en llenguatge natural sense que hagis d'escriure middleware per a cada operació.

Combina això amb els stored procedures com a frontera de permisos i amb Row-Level Security aplicada al motor, i tens un model on:

1. L'agent crida una eina, per exemple "obté el context del client per al compte 12345"
2. MCP ho tradueix al stored procedure que has definit
3. El motor SQL aplica l'aïllament de tenant i l'emmascarament de columnes automàticament
4. L'agent rep exactament les dades que té permís de veure

No hi ha capa de middleware. No hi ha risc d'injecció de consultes ad hoc. El motor gestiona l'autorització, no l'agent.

## Per Què Això Importa Als Desenvolupadors .NET

Si estàs construint serveis .NET amb SQL Server com a magatzem principal, el missatge d'aquesta sèrie és: no necessites afegir Redis per a la caché, ni una base de dades de graf per a les relacions, ni un magatzem vectorial per a les embeddings. SQL Server 2025 s'encarrega de tot això — amb una coherència operativa millor que un stack poliglota i una seguretat unificada que realment es pot auditar.

La integració MCP significa que els teus agents de Semantic Kernel o els fluxos de Microsoft Agent Framework poden interactuar amb la capa de dades a través del mateix SQL MCP Server, amb les mateixes garanties de seguretat que imposaries a les consultes humanes.

## Tancant

La sèrie Polyglot Tax val la pena llegir-la de cap a cap. Les parts 1-3 demostren la història del planificador de consultes. La part 4 demostra la història de producció. Per als desenvolupadors .NET que construeixen aplicacions agent-first o AI-augmented sobre Azure SQL, aquesta arquitectura mereix una consideració seriosa.

Publicació original d'Aditya Badramraju: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).