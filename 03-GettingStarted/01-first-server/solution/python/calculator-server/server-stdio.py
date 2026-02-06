# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server with HTTP transport
mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Run with HTTP transport on port 8080
    mcp.run(transport="http", port=8080)