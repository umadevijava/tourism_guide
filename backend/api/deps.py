"""
Defines dependencies used by the endpoints.
"""

from typing import Annotated, Generator, TYPE_CHECKING

from chatbot.bot.client.lama_cpp_client import LamaCppClient
from chatbot.bot.conversation.chat_history import ChatHistory
if TYPE_CHECKING:
    from chatbot.bot.memory.vector_database.chroma import Chroma
from .. import state
from ..chat_history import chat_history
from fastapi import Depends
from sqlmodel import Session


def get_llm_client() -> Generator[LamaCppClient, None, None]:
    """
    Dependency to get the LLM client instance.
    """
    from ..main import get_llm_client as _get_llm_client
    yield _get_llm_client()


def get_chat_history() -> Generator[ChatHistory, None, None]:
    """
    Dependency to get the chat history instance.
    """
    yield chat_history


def get_index() -> Generator["Chroma", None, None]:
    """
    Dependency to get the vector database index instance.
    """
    from ..main import get_vector_index
    yield get_vector_index()


def get_db_session() -> Generator[Session, None, None]:
    """
    Create a new database session and close the session after the operation has ended.
    """
    with Session(state.engine) as session:
        yield session


LamaCppClientDep = Annotated[LamaCppClient, Depends(get_llm_client)]
ChatHistoryDep = Annotated[ChatHistory, Depends(get_chat_history)]
VectorDatabaseDep = Annotated["Chroma", Depends(get_index)]  # Using string for TYPE_CHECKING compatibility
SessionDep = Annotated[Session, Depends(get_db_session)]
