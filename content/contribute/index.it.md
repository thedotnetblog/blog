---
title: "Scrivi per The .NET Blog"
description: "Condividi le tue conoscenze con la community .NET. Scopri come diventare autore e inviare il tuo primo articolo."
---

The .NET Blog  una pubblicazione guidata dalla community dove gli sviluppatori condividono approfondimenti, tutorial e storie su .NET, Azure, AI e sviluppo cloud-native. **Accogliamo contributi da sviluppatori di tutti i  che tu stia scrivendo il tuo primo articolo tecnico o sia un relatore esperto.livelli** 

## Come Partecipare

Tutto vive su GitHub e segue un flusso di lavoro basato su pull request. Ecco come iniziare:

### 1. Fai il Fork del Repository

Vai su [github.com/thedotnetblog/blog](https://github.com/thedotnetblog/blog) e crea un fork nel tuo account GitHub.

### 2. Crea il tuo Profilo Autore

Se  il tuo primo contributo, aggiungiti come autore creando una cartella in `content/authors/tuo-username/` con un file `index.md`:

```yaml
---
title: "Il tuo Nome"
id: "tuo-username"
role: "Il tuo ruolo o titolo"
bio: "Una breve biografia su di te."
avatar: "/img/authors/tuo-avatar.jpg"
socials:
  - platform: "GitHub"
    url: "https://github.com/tuo-username"
  - platform: "Twitter"
    url: "https://x.com/tuo-username"
---
```

Aggiungi la tua immagine avatar (quadrata, almeno 200200px) in `static/img/authors/`.

### 3. Scrivi il tuo Articolo

Crea una nuova cartella in `content/posts/tuo-username/slug-del-tuo-articolo/` e aggiungi un file `index.md`:

```yaml
---
title: "Titolo del tuo Articolo"
date: 2025-01-01
author: "tuo-username"
description: "Una breve descrizione del tuo articolo."
tags: ["dotnet", "azure"]
---

Il contenuto del tuo articolo in Markdown...
```

### 4. Apri una Pull Request

Invia le tue modifiche al tuo fork e apri una pull request verso il branch `main`. Il nostro team la esaminer e fornir feedback entro pochi giorni.

## Cosa Cerchiamo

- ** guide passo passo su .NET, Azure, AI, Blazor, Aspire e altroTutorial** 
- ** esplorazioni dettagliate di una tecnologia, pattern o architetturaApprofondimenti** 
- **Storie della  la tua esperienza con .NET in produzionecommunity** 
- **Resoconti di  riassunti di conferenze, meetup o webinareventi** 

## Linee Guida

- Il contenuto deve essere tecnico e pertinente all'ecosistema .NET
- Gli esempi di codice devono essere accurati e testati in un progetto reale
- Includi una descrizione significativa e almeno un tag pertinente
- Gli articoli vengono tradotti automaticamente in tutte le lingue supportate

## Contatti

Apri una issue su [GitHub](https://github.com/thedotnetblog/blog/issues) o contattaci su [X / Twitter](https://x.com/thedotnetblog). Saremmo felici di accoglierti nella community!
