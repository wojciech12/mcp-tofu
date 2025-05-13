# MCP Server - Claude Guidelines

## Project Overview
This is a Python-based MCP (Model Control Plane) server implementation using Pydantic.ai.

## Commands
Run the following commands for development and testing:
- Start server: `python -m mcp.main`
- Run tests: `pytest`
- Type checking: `pyright`
- Linting: `ruff check .`
- Formatting: `ruff format .`

## Git commit messages

- Use imperative mood (e.g., "Add feature" not "Added feature")
- Keep subject line concise (50 chars or less)
- Start with capital letter and don't end with period
- Separate subject from body with a blank line for detailed explanations

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

Use uv for the dependency management and virtual env management:

- Python 3.9+
- pydantic-ai
- pytest (for testing)
- mypy (for type checking)
- ruff (for linting)

## Code style

- Python: snake_case for functions/variables, PascalCase for classes
- Imports: Use isort with combine-as-imports
- Error handling: Use custom ToolError for tool errors
- Types: Add type annotations for all parameters and returns
- Classes: Use dataclasses and abstract base classes

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
