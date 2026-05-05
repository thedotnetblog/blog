---
title: "Les MCP Apps ont une API fluide — Créez des interfaces riches pour outils IA en .NET en trois étapes"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "La nouvelle API de configuration fluide pour les MCP Apps sur Azure Functions vous permet de transformer n'importe quel outil MCP .NET en une application complète avec des vues, des permissions et des politiques CSP en quelques lignes de code."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "mcp-fluent-api-azure-functions-dotnet.md" >}}).*

Les outils MCP sont parfaits pour donner des capacités aux agents IA. Mais que faire si votre outil doit montrer quelque chose à l'utilisateur — un tableau de bord, un formulaire, une visualisation interactive ? C'est là qu'interviennent les MCP Apps, et elles sont devenues beaucoup plus faciles à créer.

Lilian Kasem de l'équipe Azure SDK [a présenté la nouvelle API de configuration fluide](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) pour les MCP Apps sur Azure Functions .NET, et c'est le genre d'amélioration de l'expérience développeur qui fait se demander pourquoi ce n'était pas déjà aussi simple.

## Qu'est-ce que les MCP Apps ?

Les MCP Apps étendent le Model Context Protocol en permettant aux outils d'embarquer leurs propres vues UI, assets statiques et contrôles de sécurité. Au lieu de simplement retourner du texte, votre outil MCP peut rendre des expériences HTML complètes — tableaux de bord interactifs, visualisations de données, formulaires de configuration — le tout invocable par des agents IA et présenté aux utilisateurs par les clients MCP.

Le problème était que tout câbler manuellement nécessitait une connaissance approfondie de la spécification MCP : URIs `ui://`, types MIME spéciaux, coordination des métadonnées entre outils et ressources. Pas difficile, mais fastidieux.

## L'API fluide en trois étapes

**Étape 1 : Définissez votre fonction.** Un outil MCP Azure Functions standard :

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Étape 2 : Promouvez-la en MCP App.** Dans le démarrage de votre programme :

```csharp
builder.ConfigureMcpTool("HelloApp")
    .AsMcpApp(app => app
        .WithView("assets/hello-app.html")
        .WithTitle("Hello App")
        .WithPermissions(McpAppPermissions.ClipboardWrite | McpAppPermissions.ClipboardRead)
        .WithCsp(csp =>
        {
            csp.AllowBaseUri("https://www.microsoft.com")
               .ConnectTo("https://www.microsoft.com");
        }));
```

**Étape 3 : Ajoutez votre vue HTML.** Créez `assets/hello-app.html` avec l'interface dont vous avez besoin.

C'est tout. L'API fluide gère toute la plomberie du protocole MCP — génère la fonction de ressource synthétique, définit le type MIME correct et injecte les métadonnées qui connectent votre outil à sa vue.

## La surface de l'API est bien conçue

Quelques éléments que j'apprécie particulièrement :

**Les sources de vues sont flexibles.** Vous pouvez servir du HTML depuis des fichiers sur disque ou intégrer des ressources directement dans votre assembly pour des déploiements autonomes :

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**Le CSP est composable.** Vous autorisez explicitement les origines dont votre app a besoin, en suivant le principe du moindre privilège. Appelez `WithCsp` plusieurs fois et les origines s'accumulent :

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**Contrôle de visibilité.** Vous pouvez rendre un outil visible uniquement pour le LLM, uniquement pour l'UI de l'hôte, ou les deux. Vous voulez un outil qui ne fait que rendre de l'UI et ne devrait pas être appelé par le modèle ? Facile :

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## Pour commencer

Ajoutez le package preview :

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

Si vous construisez déjà des outils MCP avec Azure Functions, c'est juste une mise à jour de package. Le [quickstart MCP Apps](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp) est le meilleur point de départ si vous découvrez le concept.

## Pour conclure

Les MCP Apps sont l'un des développements les plus passionnants dans l'espace des outils IA — des outils qui ne font pas que *faire des choses* mais peuvent aussi *montrer des choses* aux utilisateurs. L'API fluide supprime la complexité du protocole et vous permet de vous concentrer sur l'essentiel : la logique de votre outil et son interface.

Lisez le [post complet](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) pour la référence complète de l'API et des exemples.
