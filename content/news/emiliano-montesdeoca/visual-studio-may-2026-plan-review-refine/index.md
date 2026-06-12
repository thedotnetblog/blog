---
title: "Visual Studio’s May Update Is Really About Better Control Between Idea and Change"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: "The May Visual Studio update adds the Plan agent, better skill management, context window visibility, and stronger multi-file diff experiences. The common theme is better control over the AI-assisted inner loop."
tags:
  - Visual Studio
  - GitHub Copilot
  - AI
  - Developer Tools
  - Productivity
---

The most interesting thing about the Visual Studio May update is not one isolated feature.

It is the shared direction.

The release keeps improving the space between:

- an idea
- a plan
- a generated change
- a review
- a refined result

That is the part of AI-assisted development that determines whether the workflow feels trustworthy or chaotic.

## The feature list is varied, but the intent is consistent

On paper, this release includes a mix of things:

- the new Plan agent
- skill management improvements
- context window visibility
- multi-file summary diff
- Copilot-related workflow cleanup
- MSVC updates on the C++ side

That can look like a grab bag.

I do not think it is.

The through-line is pretty clear: **Visual Studio is trying to give developers more control over AI-assisted work without slowing them down.**

That is exactly the right tradeoff to pursue.

## The Plan agent is the philosophical center of the release

Even though other features matter, I still think the Plan agent is the most revealing part of this update.

It makes explicit something many of us have felt while using coding agents:

starting quickly is not always the same as moving effectively.

The release doubles down on that by making planning, review, and controlled implementation a more natural sequence.

That is healthy.

## The multi-file diff work is quietly a big improvement

I also think the multi-file summary diff deserves more credit than it will probably get.

When agents change several files at once, the review experience becomes the product.

If reviewing the changes feels messy, developers trust the workflow less.

If reviewing the changes feels coherent, developers are more likely to keep using the tool.

That is why a unified summary view matters so much. It lowers the cognitive cost of saying yes or no to generated work.

## The context window indicator is a smarter addition than it sounds

I also like the context usage indicator.

This may sound like a small detail, but it solves a very real AI workflow problem: not knowing when the tool is about to start forgetting the earlier part of the conversation.

Making that visible is a good design choice.

It does not magically expand the model context. But it makes the limit observable, which is often the next best thing.

## My take

This update is really about giving developers more visibility and control over the AI-assisted loop.

Not more novelty.
Not more chaos.
More control.

That is exactly the right place to invest if the goal is to make AI tooling feel more trustworthy inside a serious IDE workflow.

Original post: [Visual Studio May Update – Plan, Review, Refine](https://devblogs.microsoft.com/visualstudio/visual-studio-may-update-plan-review-refine/)