"""Error handling utilities."""

from typing import Type, Any, Dict

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class ToolError(Exception):
    """Base exception for all MCP tool errors."""
    
    def __init__(
        self, 
        message: str, 
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail: Dict[str, Any] = None
    ):
        self.message = message
        self.status_code = status_code
        self.detail = detail or {}
        super().__init__(self.message)


def setup_exception_handlers(app: FastAPI) -> None:
    """Set up exception handlers for the FastAPI application.
    
    Args:
        app: The FastAPI application instance.
    """
    
    @app.exception_handler(ToolError)
    async def tool_error_handler(request: Request, exc: ToolError) -> JSONResponse:
        """Handle custom ToolError exceptions."""
        content = {
            "error": exc.message,
            **exc.detail,
        }
        return JSONResponse(
            status_code=exc.status_code,
            content=content,
        )
