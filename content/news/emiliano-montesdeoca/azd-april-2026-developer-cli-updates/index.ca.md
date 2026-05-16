---
title: "Actualitzacions d'Azure Developer CLI (azd) per a l'abril de 2026"
date: 2026-05-08
author: "Emiliano Montesdeoca"
description: "azd va llançar cinc versions l'abril de 2026, encapçalades pel suport de hooks en múltiples llenguatges per a Python, JavaScript, TypeScript i .NET, a més de la vista prèvia pública d'azd update, comprovacions prèvies de quota d'IA i molt més."
tags:
  - .NET
  - Azure Developer CLI
  - DevOps
  - Cloud
---

*Aquesta publicació ha estat traduïda automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

[Azure Developer CLI (azd) va llançar cinc versions l'abril de 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) (de la 1.23.14 a la 1.24.2), amb el gran protagonisme dels hooks que ara s'executen en Python, JavaScript, TypeScript i .NET — no només en Bash i PowerShell.

## Hooks en múltiples llenguatges a azure.yaml

Els hooks ara poden apuntar a fitxers `.py`, `.js`, `.ts` o `.cs` a més dels scripts de shell. Cada llenguatge obté resolució automàtica de dependències:

- **Python** — detecta `requirements.txt` o `pyproject.toml`, crea un virtualenv i instal·la les dependències abans d'executar-se. Configura el nom de l'entorn amb `virtualEnvName`.
- **JavaScript / TypeScript** — detecta `package.json` i executa `npm install` automàticament. TypeScript s'executa mitjançant `npx tsx` sense necessitat d'un pas de compilació. Tria el gestor de paquets amb el bloc de configuració `packageManager`.
- **.NET** — executa fitxers `.cs` amb `dotnet run`. S'admeten scripts d'un sol fitxer a .NET 10+. Configura el framework de destinació mitjançant el bloc `configuration/framework`.

Això significa que els equips que ja treballen en un d'aquests llenguatges ja no necessiten mantenir un hook de Bash o PowerShell separat només per connectar esdeveniments del cicle de vida del proveïment.

## azd update arriba a la vista prèvia pública

`azd update` està ara en vista prèvia pública a totes les plataformes. Una única comanda gestiona l'actualització independentment de com es va instal·lar azd originalment — sense haver de rastrejar rutas de Homebrew, WinGet o MSI per separat.

## Mode no interactiu mitjançant AZD_NON_INTERACTIVE

Establir `AZD_NON_INTERACTIVE=true` (o usar `--non-interactive` / `--no-prompt`) ara produeix fallades consistents i deterministes en pipelines de CI/CD quan una entrada requerida no es pot resoldre automàticament. Anteriorment, el comportament era inconsistent entre comandes.

## Comprovació prèvia de quota de models d'IA

`azd provision` valida la quota d'Azure Cognitive Services abans d'intentar proveir recursos de models d'IA. Les implementacions que fallarien per límits de quota ara mostren l'error aviat en el procés en lloc de fer-ho a mig proveïment.

## "Corregeix aquest error" a la resolució de problemes de Copilot

La integració de resolució de problemes de Copilot a azd guanya la capacitat d'aplicar directament una correcció suggerida — no només descriure-la. Quan l'agent identifica un problema corregible, pot fer el canvi in situ.

## Proveïdors de proveïment personalitzats i resolució de secrets de Key Vault

Els autors d'extensions ara poden registrar backends d'infraestructura alternatius amb `WithProvisioningProvider()`. Per separat, azd resol automàticament les referències `@Microsoft.KeyVault(...)` abans de passar la configuració a les extensions, eliminant la necessitat de resolució manual de secrets en proveïdors personalitzats.

## Exclusions de plantilles i mode de vigilància

Dos nous fitxers d'ignorats ofereixen un control més fi sobre el maneig de fitxers:
- **`.azdignore`** — exclou fitxers només per a col·laboradors (documentació, configuracions de CI) de les còpies de plantilles perquè els usuaris finals obtinguin un projecte net.
- **`.azdxignore`** — exclou directoris de disparar reconstruccions durant `azd x watch`, reduint el soroll durant el desenvolupament iteratiu.

## Comprovació prèvia de noms reservats i opció docker.network

azd ara adverteix quan els noms de recursos previstos contindrien paraules reservades d'Azure (`MICROSOFT`, `WINDOWS` o el prefix `LOGIN`) abans de començar el proveïment. Una nova opció `docker.network` passa `--network` a `docker build`, útil en entorns de proxy corporatiu que requereixen una xarxa Docker específica.

## Correccions de seguretat

El paquet MSI de Windows ara inclou verificació de signatura de codi. Una correcció separada tanca una filtració de variables d'entorn que podia exposar valors entre els límits de comandes d'extensió.

---

Un mes intens — el suport de hooks en múltiples llenguatges en particular elimina un punt de fricció real per als equips que no treballen principalment en Bash. Consulta les [notes de versió completes](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-april-2026/) per al registre de canvis complet de les cinc versions.
