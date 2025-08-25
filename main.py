from fastmcp import FastMCP

mcp = FastMCP("OpenTofu MCP Server")

@mcp.tool
def hello(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}! Welcome to the OpenTofu MCP Server."

if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
