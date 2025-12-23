from fastmcp import FastMCP
import requests
from search import load_documents, build_index, search

# Initialize the index on startup
documents = load_documents("../fastmcp-main.zip")
index = build_index(documents)

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

def _download_webpage_impl(url: str) -> str:
    """Core implementation for downloading web page content.
    
    Args:
        url: The URL of the web page to download
        
    Returns:
        The web page content converted to markdown
    """
    jina_url = f"https://r.jina.ai/{url}"
    response = requests.get(jina_url)
    response.raise_for_status()
    return response.text

@mcp.tool
def download_webpage(url: str) -> str:
    """Download and convert web page content to markdown using Jina Reader.
    
    Args:
        url: The URL of the web page to download
        
    Returns:
        The web page content converted to markdown
    """
    return _download_webpage_impl(url)

@mcp.tool
def search_fastmcp_docs(query: str) -> str:
    """Search the FastMCP documentation.
    
    Args:
        query: The search query (e.g. "how to create resources")
        
    Returns:
        Top 5 relevant documentation snippets
    """
    results = search(query, index)
    
    output = []
    for i, result in enumerate(results):
        output.append(f"Result {i+1}:")
        output.append(f"Filename: {result['filename']}")
        output.append(f"Content: {result['content'][:500]}...")
        output.append("-" * 40)
        
    return "\n".join(output)

if __name__ == "__main__":
    mcp.run()