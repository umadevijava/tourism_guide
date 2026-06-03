from fastapi import APIRouter, Response, WebSocket, WebSocketDisconnect
from chatbot.helpers.log import get_logger
from ...schemas.chat import ChatRequest

from backend.api.deps import ChatHistoryDep, LamaCppClientDep, VectorDatabaseDep
from backend.api.services.chat_stream import stream_chat_response, stream_rag_response

logger = get_logger(__name__)

router = APIRouter()


@router.delete(
    path="/chat/history",
    status_code=204,
)
async def clear_chat_history(chat_history: ChatHistoryDep):
    """Clear the server-side chat history."""
    chat_history.clear()
    return Response(status_code=204)


@router.websocket(
    path="/chat/stream",
)
async def chat_stream(
    websocket: WebSocket, chat_history: ChatHistoryDep
):
    """WebSocket endpoint for streaming chat responses token by token."""
    await websocket.accept()
    logger.info("WebSocket connection accepted")
    
    from backend.main import get_llm_client, get_vector_index
    import anyio
    
    try:
        while True:
            data = await websocket.receive_json()
            logger.info(f"Received data: {data}")
            query = ChatRequest(**data)
            
            # Lazily initialize and run in thread pool to avoid blocking the main event loop
            llm_client = await anyio.to_thread.run_sync(get_llm_client)
            
            if query.rag:
                index = await anyio.to_thread.run_sync(get_vector_index)
                await stream_rag_response(websocket, llm_client, query, chat_history, index)
            else:
                await stream_chat_response(websocket, llm_client, query, chat_history)
    except WebSocketDisconnect:
        logger.info("WebSocket client disconnected")
    except Exception as e:
        logger.exception(f"Unexpected error in WebSocket handler: {e}")
        raise
