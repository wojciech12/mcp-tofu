# MCP Server for OpenTofu - Development Guidelines

This document contains critical information about working with this codebase. Follow these guidelines precisely.

## Project Overview

This is a DevOps-focused MCP (Model Context Protocol) server implementation for OpenTofu using **fastmcp v2** framework. The server provides quick access to infrastructure-as-code best practices while facilitating AI model interactions with OpenTofu operations.

**Key Technologies:**
- fastmcp v2 (Python MCP server framework)
- OpenTofu binary integration
- context7 MCP for accessing latest documentation
- Embedded DevOps best practices and security validations

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
   - Framework: `just test` (uses pytest with uv)
   - Async testing: use anyio, not asyncio
   - Coverage: test edge cases and errors
   - New features require tests
   - Bug fixes require regression tests

# Git Workflow

## Git and GitHub Commands

- `gh pr create --draft`: Create draft pull request
- `gh pr ready <pr-number>`: Mark PR as ready for review
- `gh pr merge <pr-number> --squash`: Squash and merge PR
- `gh pr edit <pr-number> --add-reviewer <username>`: Add reviewer to PR

## Branch Naming Conventions

Use descriptive prefixes followed by descriptive names with dashes:

- `feature/` - for adding new functionality or capabilities
- `bugfix/` - for fixing bugs or issues in the codebase
- `chore/` - for maintenance tasks, updates, or routine work
- `refactor/` - for code restructuring without changing functionality
- `experiment/` - for testing new ideas or proof-of-concept work
- `docs/` - for documentation updates or additions
- `aidev/` - for AI-assisted development or automation tasks

## Commit Messages

- Use imperative mood (e.g., "Add feature" not "Added feature")
- Keep subject line concise (50 chars or less)
- Start with capital letter and don't end with period
- Separate subject from body with a blank line for detailed explanations
- For security updates, prefix with "Security:" or document vulnerability fixes
- NEVER mention co-authored-by or tool used to create the commit

## Pull Requests

- Create detailed message focusing on high-level problem and solution
- You MUST squash and merge PRs, NEVER only merge
- Use `gh` command line tool for PR operations

## Python Tools

## Code Formatting

1. Ruff
   - Format: `just ruff` (formats Python files)
   - Check: `uv run --frozen ruff check .`
   - Fix: `uv run --frozen ruff check . --fix`
   - Full formatting: `just fmt` (runs prettier + ruff)
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

3. Running: `uv run -m mcp_tofu` (fastmcp v2 server)

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

**FastMCP v2 Specific:**
- Follow fastmcp v2 patterns (see atproto_mcp example)
- Use fastmcp decorators for tool definitions
- Implement proper MCP tool parameter validation
- Follow MCP protocol compliance

**General Guidelines:**
- All data models should use Pydantic for validation
- MCP tools should be properly typed and documented
- Follow PEP 8 style guidelines
- Write unit tests for all new functionality
- Document public APIs
- Embed DevOps best practices in all OpenTofu operations

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
