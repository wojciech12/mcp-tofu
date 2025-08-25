# FastMCP v2 - Context7 MCP Library Information

## Library Identification

**Context7-compatible library ID**: `/jlowin/fastmcp`

- **Name**: FastMCP
- **Description**: FastMCP is a Python framework for building Model Context Protocol (MCP) servers and clients, simplifying the creation of LLM-integrated applications with features like deployment, authentication, and dynamic tool generation.
- **Code Snippets**: 1030
- **Trust Score**: 9.3

## Key Usage Patterns

### Basic Server Creation

```python
from fastmcp import FastMCP

mcp = FastMCP("OpenTofu MCP Server")

@mcp.tool
def hello(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}! Welcome to the OpenTofu MCP Server."

if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
```

### Transport Options

- **STDIO**: `mcp.run()` or `mcp.run(transport="stdio")` (default)
- **SSE**: `mcp.run(transport="sse", host="127.0.0.1", port=8000)`
- **HTTP**: `mcp.run(transport="http", host="127.0.0.1", port=8000)`

### Installation

```bash
uv add fastmcp
```

## Context for This Project

This library was selected for the mcp-tofu project because:

- Highest trust score (9.3) among fastmcp options
- Most comprehensive documentation (1030 code snippets)
- Active maintenance and development
- Full MCP protocol compliance
- Supports multiple transport types (STDIO, SSE, HTTP)

## Development Notes

- Follow fastmcp v2 patterns for tool definitions
- Use `@mcp.tool` decorator for tool registration
- Proper type hints required for all parameters
- Use Context parameter for advanced tool capabilities
- Server automatically detects instances named 'mcp', 'server', or 'app'
