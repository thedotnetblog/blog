---
title: ".NET 10 Ships with Ubuntu 26.04 LTS — Here's What's New"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) launched today with .NET 10 as a first-class supported toolchain. Native AOT, chiseled containers, Linux 7.0 — here's what you need to know."
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

It's Ubuntu LTS day. [Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) launched today, and as with every Ubuntu LTS, it ships with the latest .NET LTS — in this case, [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/).

If you deploy .NET apps on Linux, this is the release cycle you care about. LTS on LTS — five years of support for the OS, matching .NET 10's own long-term support window.

## Install .NET 10 in two commands

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

That's it. .NET is one of the [officially supported toolchains on Ubuntu](https://ubuntu.com/toolchains) — not a third-party add-on. Microsoft and Canonical work together to make sure it works on day one.

## Try it immediately

Here's the thing I love about this: you can pull an `ubuntu:resolute` container image and be running C# in under a minute.

```bash
docker run --rm -it ubuntu:resolute
apt update
apt install -y dotnet-sdk-10.0
dotnet run - << 'EOF'
using System.Runtime.InteropServices;
Console.WriteLine($"Hello {RuntimeInformation.OSDescription} from .NET {RuntimeInformation.FrameworkDescription}");
EOF
```

That `dotnet run -` with a heredoc is a file-based app pattern — no project file, no directory, just C# piped to stdin. Honest, if you haven't tried file-based apps yet, it's worth a look.

## Containers: update `-noble` to `-resolute`

The new container images use the `resolute` tag. Migration is a one-liner:

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

All existing image flavors — including [Chiseled](https://devblogs.microsoft.com/dotnet/announcing-dotnet-chiseled-containers/) — are available. The Chiseled images are still my go-to for production: minimal attack surface, no shell, no package manager, just the runtime. Update the tag and rebuild.

## Native AOT: 3ms startup, 1.4MB binary

Ubuntu 26.04 ships a dedicated AOT package:

```bash
apt install -y dotnet-sdk-aot-10.0 clang
```

Here's what you get when you publish a simple app:

```bash
dotnet publish app.cs
# artifacts/app/app — 1.4MB native binary
```

Startup time:
```
real 0m0.003s
```

3 milliseconds. For a full ASP.NET Core web service, the self-contained binary is around 13MB. That's a completely self-contained deployable with no runtime dependency whatsoever.

For cloud-native workloads where cold-start time matters — Functions, containers, serverless — this is a legitimate game changer.

## What changed in Ubuntu 26.04 that affects .NET

Three things worth knowing:

1. **Linux 7.0** — The .NET team will start Linux 7.0 testing once they get 26.04 VMs in the lab. No breaking changes expected, but they'll verify.

2. **Post-quantum cryptography** — Ubuntu 26.04 introduces PQC support, and .NET 10 [added post-quantum cryptography APIs](https://devblogs.microsoft.com/dotnet/post-quantum-cryptography-in-dotnet/) as well. Good alignment.

3. **cgroup v1 removed** — Ubuntu 26.04 drops cgroup v1. .NET added cgroup v2 support years ago, so this is a non-event. But if you're on an older runtime, double-check.

## Need .NET 8 or 9?

Those are available via the [dotnet-backports PPA](https://launchpad.net/~dotnet/+archive/ubuntu/backports):

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0  # or dotnet-sdk-9.0
```

Support is "best-effort" — not the same guarantee as the LTS package in the main archive — but the packages are there and they work.

## Wrapping up

Every two years, the Ubuntu LTS + .NET LTS alignment gives you a solid, long-support foundation for production workloads. Ubuntu 26.04 with .NET 10 is that foundation for the next cycle.

If you're containerizing .NET apps, update your Dockerfiles. If you're deploying on bare metal or VMs, `apt install dotnet-sdk-10.0` and you're done.

Read the [full post from Richard Lander](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) for the complete installation walkthrough and container details.
