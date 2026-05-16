---
title: "Actualizaciones de Azure Developer CLI (azd) para abril de 2026"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd lanzó cinco versiones en abril de 2026, con soporte de hooks en varios lenguajes para Python, JavaScript, TypeScript y .NET, además de la vista previa pública de azd update, comprobaciones previas de cuota de IA y más."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "index.md" >}}).*

[Azure Developer CLI (azd) lanzó cinco versiones en abril de 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (1.23.14 a 1.24.2), con el gran protagonismo de los hooks que ahora se ejecutan en Python, JavaScript, TypeScript y .NET, no solo en Bash y PowerShell.

## Hooks en varios lenguajes en azure.yaml

Los hooks ahora pueden apuntar a archivos `.py`, `.js`, `.ts` o `.cs` además de scripts de shell. Cada lenguaje obtiene resolución automática de dependencias:

- **Python** — detecta `requirements.txt` o `pyproject.toml`, crea un virtualenv e instala las dependencias antes de ejecutarse. Configura el nombre del entorno con `virtualEnvName`.
- **JavaScript / TypeScript** — detecta `package.json` y ejecuta `npm install` automáticamente. TypeScript se ejecuta mediante `npx tsx` sin necesidad de un paso de compilación. Elige tu gestor de paquetes con el bloque de configuración `packageManager`.
- **.NET** — ejecuta archivos `.cs` con `dotnet run`. Se admiten scripts de un solo archivo en .NET 10+. Configura el framework de destino mediante el bloque `configuration/framework`.

Esto significa que los equipos que ya trabajan en uno de estos lenguajes ya no necesitan mantener un hook de Bash o PowerShell separado solo para conectar eventos del ciclo de vida del aprovisionamiento.

## azd update llega a vista previa pública

`azd update` está ahora en vista previa pública en todas las plataformas. Un único comando gestiona la actualización independientemente de cómo se instaló azd originalmente: sin tener que rastrear rutas de Homebrew, WinGet o MSI por separado.

## Modo no interactivo mediante AZD_NON_INTERACTIVE

Establecer `AZD_NON_INTERACTIVE=true` (o usar `--non-interactive` / `--no-prompt`) ahora produce fallos consistentes y deterministas en pipelines de CI/CD cuando una entrada requerida no puede resolverse automáticamente. Anteriormente, el comportamiento era inconsistente entre comandos.

## Comprobación previa de cuota de modelos de IA

`azd provision` valida la cuota de Azure Cognitive Services antes de intentar aprovisionar recursos de modelos de IA. Las implementaciones que fallarían por límites de cuota ahora muestran el error al inicio del proceso en lugar de a mitad del aprovisionamiento.

## "Corregir este error" en la solución de problemas de Copilot

La integración de solución de problemas de Copilot en azd gana la capacidad de aplicar directamente una corrección sugerida, no solo describirla. Cuando el agente identifica un problema corregible, puede realizar el cambio in situ.

## Proveedores de aprovisionamiento personalizados y resolución de secretos de Key Vault

Los autores de extensiones ahora pueden registrar backends de infraestructura alternativos con `WithProvisioningProvider()`. Por separado, azd resuelve automáticamente las referencias `@Microsoft.KeyVault(...)` antes de pasar la configuración a las extensiones, eliminando la necesidad de resolución manual de secretos en proveedores personalizados.

## Exclusiones de plantillas y modo de vigilancia

Dos nuevos archivos de ignorados ofrecen un control más fino sobre el manejo de archivos:
- **`.azdignore`** — excluye archivos solo para colaboradores (documentación, configuraciones de CI) de las copias de plantillas para que los usuarios finales obtengan un proyecto limpio.
- **`.azdxignore`** — excluye directorios de disparar reconstrucciones durante `azd x watch`, reduciendo el ruido durante el desarrollo iterativo.

## Comprobación previa de nombres reservados y opción docker.network

azd ahora advierte cuando los nombres de recursos predichos contienen palabras reservadas de Azure (`MICROSOFT`, `WINDOWS` o el prefijo `LOGIN`) antes de comenzar el aprovisionamiento. Una nueva opción `docker.network` pasa `--network` a `docker build`, útil en entornos de proxy corporativo que requieren una red Docker específica.

## Correcciones de seguridad

El paquete MSI de Windows ahora incluye verificación de firma de código. Una corrección separada cierra una fuga de variables de entorno que podía exponer valores entre los límites de comandos de extensión.

---

Un mes cargado — el soporte de hooks en múltiples lenguajes en particular elimina un punto de fricción real para equipos que no trabajan principalmente en Bash. Consulta las [notas de versión completas](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) para el registro de cambios completo de las cinco versiones.
