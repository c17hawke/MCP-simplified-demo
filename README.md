# MCP Demo — MarketIntel

A **FastMCP** server that exposes market-research tools (company overview, competitor discovery, product portfolio, pricing snapshot, and news pulse) powered by the **Tavily** search API. Includes a Python client and an **n8n** workflow integration.

---

## Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| **Python** | ≥ 3.13 | [python.org/downloads](https://www.python.org/downloads/) |
| **uv** | latest | [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/) |
| **Node.js / npm** | LTS | [nodejs.org](https://nodejs.org/) — needed for `npx` |
| **Docker** | latest | [docs.docker.com/get-docker](https://docs.docker.com/get-docker/) — needed for n8n |

### Tavily API Key

The server requires a [Tavily](https://tavily.com/) API key.
1. Sign up at [app.tavily.com](https://app.tavily.com/)
2. Copy your API key from the dashboard.

### Groq API Key

The notebooks use [Groq](https://groq.com/) as the LLM backend.
1. Sign up at [console.groq.com](https://console.groq.com/)
2. Go to **API Keys** → **Create API Key** and copy it.

Copy `.env.example` to `.env` and fill in your keys:

**Windows**
```bash
copy .env.example .env
```

**macOS / Linux**
```bash
cp .env.example .env
```

```env
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxx
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxx
```

---

## Setup Commands

### Verify installed tools

```bash
uv --version
python --version
node --version
npx --version
```

### Set up the Python environment

```bash
uv init
uv venv
```

Activate the virtual environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
uv add -r requirments.txt
```

---

## Running the Server

The server starts an HTTP transport on `http://127.0.0.1:8000/mcp`.

```bash
python server.py
```

---

## Running the Client

```bash
python client.py
```

The client reads `MARKETINTEL_ENDPOINT` from the environment (default: `http://127.0.0.1:8000/mcp`).

---

## Other Commands

### MCP Inspector

Visually inspect and test the MCP server in a browser UI:

```bash
npx @modelcontextprotocol/inspector
```

Then point it to `http://127.0.0.1:8000/mcp`.

---