---
title: "Bookmark Studio Visual Studio Bookmarks में Slot-Based Navigation और Sharing लाता है"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Mads Kristensen का नया Bookmark Studio extension keyboard-driven slot navigation, bookmark manager, colors, labels, और export/share capabilities Visual Studio bookmarks में जोड़ता है।"
tags:
  - visual-studio
  - extensions
  - productivity
  - developer-tools
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "bookmark-studio-visual-studio-extension" >}}).*

Visual Studio में Bookmarks हमेशा से... ठीक-ठाक रहे हैं। आप एक set करते हैं, अगले पर navigate करते हैं, भूल जाते हैं कि कौन सा bookmark क्या है।

Mads Kristensen ने [Bookmark Studio release किया](https://devblogs.microsoft.com/visualstudio/bookmark-studio-evolving-bookmarks-in-visual-studio/), एक experimental extension जो exactly उन gaps को fill करता है।

## Slot-based navigation

Core addition: bookmarks अब slots 1–9 को assign किए जा सकते हैं और `Alt+Shift+1` से `Alt+Shift+9` के साथ directly jump किया जा सकता है। यह bookmarks को "मेरे कहीं कुछ bookmarks हैं" से "Slot 3 मेरा API controller है, Slot 5 service layer है" में बदल देता है।

## Bookmark Manager

एक नई tool window आपके सभी bookmarks को name, file, location, color, या slot के आधार पर filtering के साथ एक जगह दिखाती है।

## Labels, Colors, और Folders के साथ Organization

Bookmarks में optionally labels, colors हो सकते हैं और folders में group किए जा सकते हैं। सभी metadata per solution stored है।

## Export और Share

Bookmark Studio bookmarks को plain text, Markdown, या CSV के रूप में export करने देता है:
- Pull request descriptions में bookmark paths शामिल करें
- Teammates के साथ investigation breadcrumbs share करें
- Repos या branches के बीच bookmark sets move करें

[Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.BookmarkStudio) से grab करें।
