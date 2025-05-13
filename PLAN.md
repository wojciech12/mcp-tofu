# MCP Server for OpenTofu - Implementation Plan

This document outlines the implementation plan for building an MCP (Model Context Protocol) server for OpenTofu. The implementation will follow an iterative approach, adding support for the core OpenTofu commands sequentially.

## Project Overview

Our goal is to create an MCP server that can facilitate interactions with OpenTofu, providing a structured interface for AI models to interact with infrastructure-as-code operations. We'll implement support for the main OpenTofu commands:

1. `init` - Prepare working directory for other commands
2. `validate` - Check whether the configuration is valid
3. `plan` - Show changes required by the current configuration
4. `apply` - Create or update infrastructure
5. `destroy` - Destroy previously-created infrastructure

## Current Project Structure

The project has a basic structure with the following components:
- Basic project configuration (pyproject.toml)
- Directory structure for MCP implementation (mcp/, with subdirectories for api, config, models, services, utils)
- Development guidelines (CLAUDE.md)

## Implementation Strategy

We will follow a sequential, test-driven development approach to implement the OpenTofu commands one by one, in their natural order of use.

### Phase 1: Project Setup and Core Structure

**Objective**: Set up the basic MCP server structure and testing framework.

1. Create essential MCP server components:
   - Initialize MCP server structure with FastAPI
   - Set up configuration handling
   - Define base model structures
   - Create utility functions for process management
   - Implement error handling mechanisms

2. Setup testing framework:
   - Configure pytest with anyio for async testing
   - Set up test fixtures for OpenTofu operations
   - Create mocks for OpenTofu command outputs

3. Implement basic OpenTofu runner service:
   - Create a service for executing OpenTofu commands
   - Add path and environment management
   - Implement logging and output capture

**Deliverables**:
- Working MCP server structure
- OpenTofu command execution functionality
- Comprehensive test coverage

### Phase 2: Implement 'init' Command

**Objective**: Support initializing a Terraform/OpenTofu working directory.

1. Create models:
   - InitRequest model with directory and source parameters
   - InitResponse model with status and output fields

2. Implement service layer:
   - Create ToFuInitService for handling initialization logic
   - Implement directory validation and preparation
   - Add backend configuration support

3. Develop API endpoints:
   - Create endpoint for init operation
   - Add parameter validation
   - Implement error handling for common initialization issues

4. Add tests:
   - Test successful initialization scenarios
   - Test error conditions (invalid directory, network issues, etc.)
   - Test backend configuration options

**Deliverables**:
- Working 'init' command implementation
- API documentation
- Test coverage for init command

### Phase 3: Implement 'validate' Command

**Objective**: Support validation of OpenTofu configurations.

1. Create models:
   - ValidateRequest with configuration directory
   - ValidateResponse with validation results

2. Implement service layer:
   - Create ToFuValidateService for handling validation logic
   - Implement configuration parsing and validation
   - Add detailed error reporting

3. Develop API endpoints:
   - Create endpoint for validate operation
   - Add validation for requests
   - Implement proper error responses

4. Add tests:
   - Test with valid configurations
   - Test with invalid configurations
   - Test boundary cases

**Deliverables**:
- Working 'validate' command implementation
- Detailed validation response structure
- Test coverage for validate command

### Phase 4: Implement 'plan' Command

**Objective**: Support generating execution plans.

1. Create models:
   - PlanRequest with configuration options
   - PlanResponse with detailed plan information
   - Resource change models (create, update, delete)

2. Implement service layer:
   - Create ToFuPlanService for handling plan generation
   - Implement plan parsing and interpretation
   - Add support for plan file generation

3. Develop API endpoints:
   - Create endpoint for plan operation
   - Add options for plan detail level
   - Implement structured plan response

4. Add tests:
   - Test plan generation with different configurations
   - Test plan parsing and interpretation
   - Test error conditions

**Deliverables**:
- Working 'plan' command implementation
- Structured plan response format
- Test coverage for plan command

### Phase 5: Implement 'apply' Command

**Objective**: Support applying planned changes to infrastructure.

1. Create models:
   - ApplyRequest with plan reference and options
   - ApplyResponse with execution results
   - Resource state models

2. Implement service layer:
   - Create ToFuApplyService for handling apply operations
   - Implement progress monitoring
   - Add support for approval flows

3. Develop API endpoints:
   - Create endpoint for apply operation
   - Add support for auto-approve option
   - Implement detailed status responses

4. Add tests:
   - Test successful apply operations
   - Test error handling during apply
   - Test idempotency of operations

**Deliverables**:
- Working 'apply' command implementation
- Detailed status reporting
- Test coverage for apply command

### Phase 6: Implement 'destroy' Command

**Objective**: Support destruction of managed infrastructure.

1. Create models:
   - DestroyRequest with target specification
   - DestroyResponse with results
   - Destruction verification models

2. Implement service layer:
   - Create ToFuDestroyService for handling destroy operations
   - Implement safety confirmations
   - Add validation of destruction targets

3. Develop API endpoints:
   - Create endpoint for destroy operation
   - Add safety mechanisms
   - Implement detailed reporting

4. Add tests:
   - Test successful destroy operations
   - Test safety mechanisms
   - Test error handling scenarios

**Deliverables**:
- Working 'destroy' command implementation
- Safety confirmation mechanisms
- Test coverage for destroy command

### Phase 7: Integration and Polish

**Objective**: Ensure all components work together smoothly and improve robustness.

1. Conduct integration testing:
   - Test complete workflows (init → validate → plan → apply → destroy)
   - Verify error propagation across commands
   - Test with complex configurations

2. Enhance error handling:
   - Implement comprehensive error classification
   - Add detailed error messages
   - Create recovery suggestions

3. Improve documentation:
   - Document API endpoints
   - Add usage examples
   - Create troubleshooting guide

4. Performance optimization:
   - Identify bottlenecks
   - Optimize command execution
   - Improve response handling

**Deliverables**:
- Fully integrated MCP server for OpenTofu
- Comprehensive documentation
- Performance benchmarks

## Timeline and Milestones

- Phase 1: 1 week - Basic project setup and core functionality
- Phase 2: 1 week - Implement 'init' command
- Phase 3: 1 week - Implement 'validate' command
- Phase 4: 1.5 weeks - Implement 'plan' command (more complex parsing)
- Phase 5: 1.5 weeks - Implement 'apply' command (with monitoring)
- Phase 6: 1 week - Implement 'destroy' command
- Phase 7: 1 week - Integration, testing, and documentation

Total estimated time: 8 weeks for complete implementation.

## Development Guidelines

Throughout the implementation, we will adhere to the project's development guidelines:

- Use `uv` for package management, never pip
- Ensure all code has proper type hints
- Follow the 88 character line length limit
- Write comprehensive docstrings for all public APIs
- Follow TDD (Test-Driven Development) approach
- Use Pydantic for data validation
- Ensure code passes Ruff format and check validations
- Ensure type correctness with Pyright

## Dependencies

- OpenTofu/Terraform binary availability
- MCP Python SDK (already in dependencies)
- Pydantic for data validation
- FastAPI for API implementation
- Anyio for asynchronous testing

## Next Steps

1. Complete Phase 1 by setting up the core MCP server structure
2. Implement 'init' command functionality
3. Build test suite for implemented features
4. Continue with sequential implementation of remaining commands