from contextlib import asynccontextmanager

from . import state
import uvicorn
from .api.routes import api_router
from .core.config import settings
from .database import create_db_engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chatbot.helpers.log import get_logger
from .llm_client import create_llm_client

logger = get_logger(__name__)


def get_llm_client():
    """Get or initialize the LLM client (lazy initialization)."""
    if state.llm_client is None:
        logger.info("Initializing LLM client on first use...")
        state.llm_client = create_llm_client(settings.MODEL_FOLDER)
    return state.llm_client


def get_vector_index():
    """Get or initialize the vector index (lazy initialization)."""
    if state.index is None:
        logger.info("Initializing vector index on first use...")
        from .vector_database import init_index
        state.index = init_index(settings.VECTOR_STORE_PATH)
    return state.index


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize global state
    logger.info("Starting up...")
    state.engine = create_db_engine()
    logger.info("Database engine initialized")
    
    # Defer LLM client initialization to avoid blocking startup
    state.llm_client = None
    logger.info("LLM client deferred - will be initialized on first use")
    
    # Defer vector index initialization to avoid blocking startup
    state.index = None
    logger.info("Vector index deferred - will be initialized on first use")

    yield

    # Cleanup
    if state.engine:
        state.engine.dispose()
        logger.info("Database engine disposed")
    if state.llm_client:
        state.llm_client.close()
        logger.info("LLM client closed")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

# Note: A single Uvicorn worker is probably what you would want to use when using a distributed container
# management system like Kubernetes.

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.HOST,
        port=settings.PORT,
        # log_config=None,
        # workers=max(1, os.cpu_count() - 1),
        workers=1,
    )
