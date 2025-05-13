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

## Development Workflow

1. Begin with thorough code analysis and complete context gathering
2. Plan incremental, well-defined changes following professional development practices
3. Implement test-driven development:
   - Write failing test case first
   - Create function stub with proper typing
   - Implement function to pass tests
4. Confirm approval before proceeding to next development phase
5. Document all changes with clear justification in docs.md
6. Ensure code meets project style guidelines and passes all checks
