from fastmcp import FastMCP
import httpx

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
    response = httpx.get(jina_url)
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

if __name__ == "__main__":
    mcp.run()