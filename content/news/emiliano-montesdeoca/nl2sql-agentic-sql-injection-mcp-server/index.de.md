---
title: "NL2SQL ist die SQL-Injection des agentischen Zeitalters"
date: 2026-06-03
author: "Emiliano Montesdeoca"
description: "Bevor Sie einen Agenten mit natürlicher Sprache Ihre Datenbank abfragen lassen, lesen Sie dies. NL2SQL wirkt einfach, bis Sie über Schema-Vollständigkeit, Indeterminismus und das nachdenken, was SQL MCP Server tatsächlich löst."
tags:
  - Azure SQL
  - AI
  - Agents
  - MCP
  - SQL MCP Server
  - Security
---

Es gibt eine Version des NL2SQL-Versprechens, die perfekt klingt: Benutzer stellen Fragen in natürlicher Sprache, Agenten generieren SQL, Daten kommen zurück. Weniger Bildschirme, weniger Abfragen, weniger Code. Einfach.

Dann denken Sie fünf weitere Minuten darüber nach.

## Die Probleme, über die niemand in der Demo spricht

**Schemas wurden nicht dafür entworfen, Dinge zu erklären.** Kryptische Tabellennamen, inkonsistente Spaltennamen, technisch gültige Beziehungen, die ohne zusätzliche Prädikate semantisch ungültig sind — das ist normal bei Unternehmensdatenbanken. Das sind keine Bugs, das ist einfach die angesammelte Geschichte von Geschäftsänderungen. Aber wenn Sie ein Modell bitten, Absicht aus einem Schema abzuleiten, das nicht dafür entworfen wurde, Absicht zu kommunizieren, wird das Modell es trotzdem versuchen. Es gibt nicht auf. Es generiert seine bestmögliche Abfrage und gibt Ergebnisse mit Zuversicht zurück.

**Modelle sind nicht deterministisch.** Stellen Sie dieselbe Frage zur gleichen Datenbank zweimal und Sie könnten unterschiedliches SQL erhalten. Das Modell berechnet Wahrscheinlichkeiten, und leichte Kontextvariationen treiben unterschiedliche Ausgaben. Sie können sich nicht durch Tests zu einer Garantie vorarbeiten, dass der Agent immer die richtige Abfrage generiert.

**Benutzerüberprüfung skaliert nicht.** "Überprüfen Sie einfach jede Abfrage vor der Ausführung" klingt sicher. Aber das setzt voraus, dass Benutzer sowohl im Datenmodell als auch in SQL Experten sind — genau die Menschen, die die natürlichsprachliche Schnittstelle nicht brauchten. Es führt auch zu kognitiver Überlastung und einer neuen Klasse von Bestätigungsverzerrung, bei der Benutzer, die von der Abfragekomplexität überwältigt sind, ungültige Abfragen genehmigen, anstatt sie zu untersuchen.

**Und dann gibt es Injection.** In der traditionellen SQL-Entwicklung löste Parametrisierung Injection, weil Benutzereingaben Parameter füllten, nicht die SQL-Struktur. Mit NL2SQL generiert das Modell das SQL selbst. Der Prompt, der Schema-Kontext, der Konversationsverlauf und abgerufene Daten beeinflussen alle, was ausgeführt wird. Wenn jemand einen Prompt erstellt, der ändert, was das Modell generiert, das ist Injection — nicht auf Parameterebene, sondern auf der Ebene der Abfragegenerierung. Und anders als das Löschen einer Tabelle (offensichtlich, wiederherstellbar) erzeugt NL2SQL-Injection Abfragen, die falsche Ergebnisse ohne sichtbaren Fehler zurückgeben. Geschäftsentscheidungen werden auf falschen Daten getroffen.

## Was SQL MCP Server tatsächlich löst

Hier macht der Artikel seinen nützlichsten praktischen Punkt. Anstatt einem Agenten beliebigen Schema-Zugriff zu geben und das Beste zu hoffen, stellt SQL MCP Server eine **kuratierte API-Oberfläche** auf Basis von [Data API builder](https://learn.microsoft.com/en-us/azure/data-api-builder/overview) bereit.

Der Unterschied ist wichtig: Der Agent generiert kein SQL. Er ruft benannte Endpunkte auf, die vordefinierte Ergebnisformen zurückgeben. Das SQL wird einmal von einem Entwickler geschrieben und ist deterministisch. Das Nicht-Determinismus des Agenten ist auf die Auswahl *welches* Endpunkt aufgerufen wird, nicht auf das Konstruieren beliebiger Abfragen beschränkt.

Das ist analog zu dem, was Parametrisierung bei der SQL-Injection im traditionellen App-Modell getan hat — Sie entfernen die Fähigkeit, beliebige Abfragen aus nicht vertrauenswürdiger Eingabe zu konstruieren.

## Die richtige Frage

Der Artikel sagt nicht "benutze NL2SQL nie." Er sagt: Sei bewusst darüber, *wo* du es anwendest und *was* du exponierst. Für explorative Analyse in einer kontrollierten Umgebung, mit einem begrenzten Schema und Nur-Lese-Zugriff, könnte NL2SQL in Ordnung sein. Für Produktionssysteme, bei denen Geschäftsentscheidungen von den Ergebnissen abhängen, ist eine kuratierte API-Schicht deutlich sicherer.

Ehrlichkeit: Manche Probleme werden wirklich besser mit strukturierten Abfragen hinter benannten Endpunkten gelöst als mit natürlicher Sprache zu SQL. SQL MCP Server gibt Ihnen diese Option, ohne die agentische Schnittstelle vollständig aufzugeben.

Originalbeitrag: [Considering NL2SQL? Should your database really be the prompt? How can SQL MCP Server help?](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-nl2sql/)
