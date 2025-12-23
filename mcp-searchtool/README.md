# FastMCP Search Tool

This project provides a search utility for **FastMCP**, a high-level framework for building Model Context Protocol (MCP) servers in Python.

It allows you to locally index and search the FastMCP documentation and examples to quickly find relevant information about building MCP servers, using resources, and managing contexts.

## Key Features
- **Local Indexing**: Indexes content directly from the `fastmcp-main.zip` repository archive.
- **Fast Retrieval**: Uses `minsearch` for efficient text-based search.
- **CLI Interface**: Simple command-line tool to query documentation.

## Technical Details

This tool indexes and searches the `fastmcp` documentation directly from a zip file.

## Prerequisites

The tool requires `minsearch`. It should be installed in your environment:

```bash
pip install minsearch
```

## Setup

Ensure the `fastmcp-main.zip` file is located in the parent directory (`../fastmcp-main.zip`).

You can [download the zip file from here](https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip).

## Usage

You can run the search script directly from the command line.

### Basic Search

Run the script without arguments to search for a default query ("how to create a resource"):

```bash
python search.py
```

### Custom Query

Pass your search query as an argument:

```bash
python search.py "demo"
```

```bash
python search.py "how to use resources"
```

## How it Works

1.  **Loading**: The script reads `.md` and `.mdx` files directly from `../fastmcp-main.zip` without extracting them to disk.
2.  **Indexing**: Content is indexed using `minsearch` with a simple TF-IDF / Cosine Similarity model.
3.  **Searching**: Queries are run against the index to return the top 5 most relevant documents.
