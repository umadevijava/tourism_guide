from fastapi import APIRouter

from backend.api.endpoints import chat, chat_stream, health
# Documents endpoint temporarily disabled due to slow imports (chatbot.memory_builder)
# from backend.api.endpoints import documents

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(chat.router, prefix="", tags=["chat"])
# api_router.include_router(documents.router, prefix="", tags=["documents"])
api_router.include_router(chat_stream.router, prefix="", tags=["chat-stream"])
