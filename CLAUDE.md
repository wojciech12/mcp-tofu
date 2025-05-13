# MCP Server - Claude Guidelines

## Project Overview
This is a Python-based MCP (Model Control Plane) server implementation using Pydantic.ai.

## Commands
Run the following commands for development and testing:
- Start server: `python -m mcp.main`
- Run tests: `pytest`
- Type checking: `mypy .`
- Linting: `ruff check .`
- Formatting: `ruff format .`

## Development Guidelines
- All data models should use Pydantic for validation
- API endpoints should be properly typed
- Follow PEP 8 style guidelines
- Write unit tests for all new functionality
- Document public APIs

## Directory Structure
- `mcp/` - Main package directory
  - `api/` - API endpoints and routing
  - `models/` - Pydantic data models
  - `services/` - Business logic
  - `config/` - Configuration management
  - `utils/` - Utility functions

## Dependencies
- Python 3.9+
- FastAPI
- Pydantic
- SQLAlchemy (for database)
- pytest (for testing)
- mypy (for type checking)
- ruff (for linting)