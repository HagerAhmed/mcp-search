# Context7 Clone (FastMCP)

This project is a clone of **Context7**, an MCP server built as part of the DataTalks.Club Agentic AI homework. It demonstrates how to build a Model Context Protocol (MCP) server using **FastMCP**, `uv` for dependency management, and integrates tools for web scraping and documentation searching.

## Project Objectives

1.  **Project Setup**: Initialize using `uv` and install `fastmcp`.
2.  **MCP Server**: Create an MCP server with `Start Code` and identify the transport mechanism.
3.  **Web Scraper**: Implement a tool to download web page content using **Jina Reader** (`r.jina.ai`).
4.  **Documentation Search**: Index and search a GitHub repository's documentation (specifically `fastmcp` docs).

## Getting Started

### Prerequisites

- Python 3.10+
- `uv` package manager

```bash
pip install uv
```

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository_url>
    cd mcp-context7
    ```

2.  Install dependencies:
    ```bash
    uv sync
    ```

3.  Download the `fastmcp` documentation zip:
    - [Download `fastmcp-main.zip`](https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip)
    - Place it in the root directory.

### Running the Server

Run the MCP server with:

```bash
fastmcp run main.py
```

## Features

### Web Scraper Tool

Uses Jina Reader to fetch markdown content from URLs.

### Search Tool

Located in `mcp-searchtool/`, this tool indices the `fastmcp` documentation for local search.

See [mcp-searchtool/README.md](mcp-searchtool/README.md) for detailed usage instructions.
