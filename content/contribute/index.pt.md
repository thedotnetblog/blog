---
title: "Escreva para The .NET Blog"
description: "Compartilhe seu conhecimento com a comunidade .NET. Saiba como se tornar um autor e enviar seu primeiro artigo."
---

#The .NET Blog  uma publica
o impulsionada pela comunidade onde desenvolvedores compartilham insights, tutoriais e histrrrias sobre .NET, Azure, IA e desenvolvimento cloud-native. **Recebemos contribuieeeees de desenvolvedores de todos os  seja vocNeis escrevendo seu primeiro artigo t** cnico ou um palestrante experiente.

## Como Participar

Tudo fica no GitHub e segue um fluxo de trabalho com pull requests. Veja como comear:

### 1. Faa um Fork do Repositrrrio

Acesse [github.com/thedotnetblog/blog](https://github.com/thedotnetblog/blog) e faa um fork para sua conta do GitHub.

### 2. Crie seu Perfil de Autor

#Se esta  sua primeira contribui
o, adicione-se como autor criando uma pasta em `content/authors/seu-usuario/` com um arquivo `index.md`:

```yaml
---
title: "Seu Nome"
id: "seu-usuario"
role: "Seu cargo ou tulo"
bio: "Uma breve biografia sobre voc."
avatar: "/img/authors/seu-avatar.jpg"
socials:
  - platform: "GitHub"
    url: "https://github.com/seu-usuario"
  - platform: "Twitter"
    url: "https://x.com/seu-usuario"
---
```

Adicione sua imagem de avatar (quadrada, mimo 200200px) em `static/img/authors/`.

### 3. Escreva seu Artigo

Crie uma nova pasta em `content/posts/seu-usuario/slug-do-seu-artigo/` e adicione um arquivo `index.md`:

```yaml
---
title: "Tulo do seu Artigo"
date: 2025-01-01
author: "seu-usuario"
#description: "Uma descri
o em uma frase do seu artigo."
tags: ["dotnet", "azure"]
---

O contedo do seu artigo em Markdown...
```

### 4. Abra um Pull Request

Envie suas alteraeeeees para o seu fork e abra um pull request contra a branch `main`. Nossa equipe vai revisar e dar feedback em poucos dias.

## O que Buscamos

- ** guias passo a passo sobre .NET, Azure, IA, Blazor, Aspire e maisTutoriais** 
#- **Anlises  exploraAprofundadas** eeeees detalhadas de uma tecnologia, padr
o ou arquitetura
#- **Histrrrias da  sua experiComunidadencia construindo com .NET em produ** 
o
- **Resumos de  resumos de conferEventosncias, meetups ou webinars** 

## Diretrizes

- O contedo deve ser tcnico e relevante para o ecossistema .NET
- Exemplos de cdddigo devem ser precisos e testados em um projeto real
#- Inclua uma descri
o significativa e pelo menos uma tag relevante
#- Os artigos s
o traduzidos automaticamente para todos os idiomas suportados

## Contato

Abra uma issue no [GitHub](https://github.com/thedotnetblog/blog/issues) ou entre em contato no [X / Twitter](https://x.com/thedotnetblog). Adorarmos themes -lo na comunidade!
