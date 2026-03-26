# Getting Started

## Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| **Hugo (extended)** | `v0.121.0` or later | [gohugo.io/installation](https://gohugo.io/installation/) |
| **Git** | any recent version | [git-scm.com](https://git-scm.com/) |

> **Why extended?** The extended version includes built-in Sass/SCSS processing. The current theme uses plain CSS, but the extended build ensures compatibility if you later add Sass.

### Installing Hugo

**macOS** (Homebrew):

```bash
brew install hugo
```

**Windows** (Chocolatey):

```bash
choco install hugo-extended
```

**Windows** (Winget):

```bash
winget install Hugo.Hugo.Extended
```

**Linux** (Snap):

```bash
snap install hugo
```

**Linux** (binary):

```bash
HUGO_VERSION="0.121.2"
curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" \
  -o hugo.tar.gz
tar -xzf hugo.tar.gz hugo
sudo mv hugo /usr/local/bin/hugo
```

Verify the installation:

```bash
hugo version
# hugo v0.121.2+extended linux/amd64 ...
```

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/thedotnetblog/blog.git
cd blog

# 2. Start the development server
hugo server

# 3. Open in your browser
# → http://localhost:1313
```

The site hot-reloads as you edit content, templates, or CSS.

---

## Running Locally

### Development Server

```bash
hugo server
```

Starts a local server at `http://localhost:1313` with live reload.

### Useful Flags

| Flag | Description |
|------|-------------|
| `--buildDrafts` / `-D` | Include posts with `draft: true` |
| `--buildFuture` / `-F` | Include posts with future dates |
| `--port 8080` | Use a custom port (default: `1313`) |
| `--bind 0.0.0.0` | Allow access from other devices on the network |
| `--disableFastRender` | Full rebuild on every change (slower but more reliable) |

```bash
# Example: run with drafts and future content visible on port 8080
hugo server -D -F --port 8080
```

### Production Build

```bash
hugo --gc --minify
```

Generates the static site into `public/`. That directory is ready to deploy to any static host.
