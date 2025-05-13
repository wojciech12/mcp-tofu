"""Model Control Plane (MCP) server main entry point."""

import logging
import sys
from typing import List

from fastapi import FastAPI, APIRouter

from mcp.config.settings import Settings
from mcp.utils.errors import setup_exception_handlers

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Model Control Plane",
    description="API for managing model execution and lifecycle",
    version="0.1.0",
)

# Setup exception handlers
setup_exception_handlers(app)

# Initialize API routers
api_router = APIRouter()

# Import and include API routers here
# app.include_router(some_router, prefix="/api/v1")


@app.get("/health", tags=["Health"])
async def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    
    settings = Settings()

    logger.info("Starting MCP server...")
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
