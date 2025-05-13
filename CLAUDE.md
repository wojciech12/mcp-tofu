# MCP Server for OpenTofu - Development Guidelines

This document contains critical information about working with this codebase. Follow these guidelines precisely.

## Project Overview

This is a Python-based MCP (Model Control Plane) server implementation using MCP (the official Python SDK for Model Context Protocol servers and clients)

## Core Development Rules

1. Package Management
   - ONLY use uv, NEVER pip
   - Installation: `uv add package`
   - Running tools: `uv run tool`
   - Upgrading: `uv add --dev package --upgrade-package package`
   - FORBIDDEN: `uv pip install`, `@latest` syntax

2. Code Quality
   - Type hints required for all code
   - Public APIs must have docstrings
   - Functions must be focused and small
   - Follow existing patterns exactly
   - Line length: 88 chars maximum

3. Testing Requirements
   - Framework: `uv run --frozen pytest`
   - Async testing: use anyio, not asyncio
   - Coverage: test edge cases and errors
   - New features require tests
   - Bug fixes require regression tests

## Git commit messages

- Use imperative mood (e.g., "Add feature" not "Added feature")
- Keep subject line concise (50 chars or less)
- Start with capital letter and don't end with period
- Separate subject from body with a blank line for detailed explanations

## Pull Requests

- Create a detailed message of what changed. Focus on the high level description of
  the problem it tries to solve, and how it is solved. Don't go into the specifics of the
  code unless it adds clarity.

## Python Tools

## Code Formatting

1. Ruff
   - Format: `uv run --frozen ruff format .`
   - Check: `uv run --frozen ruff check .`
   - Fix: `uv run --frozen ruff check . --fix`
   - Critical issues:
     - Line length (88 chars)
     - Import sorting (I001)
     - Unused imports
   - Line wrapping:
     - Strings: use parentheses
     - Function calls: multi-line with proper indent
     - Imports: split into multiple lines

2. Type Checking
   - Tool: `uv run --frozen pyright`
   - Requirements:
     - Explicit None checks for Optional
     - Type narrowing for strings
     - Version warnings can be ignored if checks pass

3. Running: `uv run -m mcp.app`

4. Pre-commit
   - Config: `.pre-commit-config.yaml`
   - Runs: on git commit
   - Tools: Prettier (YAML/JSON), Ruff (Python)
   - Ruff updates:
     - Check PyPI versions
     - Update config rev
     - Commit config first

## Error Resolution

1. Best Practices
   - Check git status before commits
   - Run formatters before type checks
   - Keep changes minimal
   - Follow existing patterns
   - Document public APIs
   - Test thoroughly

## Development Guidelines

- All data models should use Pydantic for validation
- API endpoints should be properly typed
- Follow PEP 8 style guidelines
- Write unit tests for all new functionality
- Document public APIs

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
