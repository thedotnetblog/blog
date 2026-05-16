---
title: "Die Monkey Work der Migration mit Agentic Platform Engineering beseitigen"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Git-Ape führt durch die Migration eines echten AWS Terraform-Deployments zu Azure Bicep — dabei wird die Deployment-Intention extrahiert und die Architektur neu gemappt, anstatt eine 1:1-Syntaxkonvertierung durchzuführen."
tags:
  - .NET
  - Azure
  - Migration
  - Platform Engineering
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

[Removing the Monkey Work of Migration with Agentic Platform Engineering](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) — eine Schritt-für-Schritt-Anleitung von Git-Ape (git agentic platform engineering tool), das ein echtes AWS-Terraform-Repo zu Azure migriert, mit Fokus auf Intent-Extraktion statt zeilenweiser Konvertierung.

## Die Eingabe: contoso-migration

Die Quelle ist ein echtes Terraform-Projekt (`contoso-migration`), das eine Next.js-App auf AWS bereitstellt — EC2 für Compute, ALB für Load Balancing, S3 für Artefakte und IAM-Schlüssel für Identität. Kosten: ~34 $/Monat. Das Ziel ist nicht, dieselbe Infrastruktur auf Azure zu reproduzieren; es geht darum herauszufinden, was das Deployment eigentlich tun soll, und das mit nativen Azure-Diensten neu aufzubauen.

## Schritt 1: Validierung und Authentifizierung

Git-Ape beginnt damit, alle erforderlichen CLI-Tools zu validieren — `az`, `aws`, `gh`, `jq`, `git` — und aktive Auth-Sessions zu bestätigen, bevor etwas angerührt wird. Keine Teilausführungen.

## Schritt 2: Intent-Extraktion

Der Agent liest das gesamte Quell-Repository über die GitHub API und extrahiert den Deployment-Intent: Laufzeit (Node.js), Compute-Typ, Ingress-Muster, Artefakt-Handling, Identitätsmodell, Netzwerk und Monitoring. Dies ist der entscheidende Schritt — es wird ein semantisches Modell dessen erstellt, was das Deployment tut, nicht welche Terraform-Keywords es verwendet.

## Schritt 3: Service-Mapping

AWS-Dienste werden auf Azure-Äquivalente abgebildet:
- EC2 → App Service (Linux, Node 20 LTS)
- ALB → Integriertes App Service Load Balancing
- IAM-Rollen/Schlüssel → Managed Identity
- Terraform → Bicep + GitHub Actions

## Schritt 4: Kritik-Agent

Vor der Ausgabegenerierung läuft ein Kritik-Agent und erkennt zwei blockierende Probleme:

1. **Build-on-Startup-Antimuster** — das ursprüngliche Terraform führte `npm install && npm run build` auf EC2 beim Start aus. Fix: In CI bauen, ein fertiges Artefakt deployen.
2. **Unnötiger Blob Storage** — S3 wurde für Artefakt-Staging verwendet, das mit korrektem CI/CD eliminiert werden könnte. Der Kritik-Agent hat es vollständig entfernt.

## Schritt 5: Generierte Ausgabe

Das Ergebnis sind ~80 Zeilen Bicep statt der ursprünglichen 200+ Zeilen Terraform. Der Agent erstellte ein neues GitHub-Repo mit `infra/main.bicep` und `.github/workflows/deploy.yml` und entfernte alle AWS-spezifischen Dateien.

## Vergleich der Sicherheitslage

Die Migration ergab auch eine bedeutende Sicherheitsverbesserung:

| AWS-Original | Azure-Ausgabe |
|---|---|
| Nur HTTP | Nur HTTPS, TLS 1.2 |
| SSH offen für 0.0.0.0/0 | Keine SSH-Exposition |
| IAM-Zugriffsschlüssel | OIDC + Managed Identity |
| Kein Monitoring | Application Insights |

Kosten: ~13 $/Monat vs. ursprüngliche 34 $/Monat.

## Was dies von einem Syntax-Konverter unterscheidet

Der Kritik-Agent-Schritt ist das, was dies von einer mechanischen Übersetzung trennt. Er erkannte Muster, die auf AWS funktioniert hätten, aber auf Azure falsch wären — und korrigierte sie, anstatt sie zu replizieren. Die Ausgabe ist kein "AWS in Azure-Syntax"; es ist ein Azure-natives Deployment, das dasselbe Ziel sauberer erreicht.

Siehe die [vollständige Anleitung](https://devblogs.microsoft.com/all-things-azure/removing-the-monkey-work-of-migration-using-agentic-platform-engineering/) für die vollständige Agent-Ablaufverfolgung und generierte Dateien.
