# System Architecture & Technical Design

**Tourism Guide Chatbot - Technical Architecture Documentation**

---

## 1. Architectural Overview

### 1.1 System Architecture Pattern

The Tourism Guide Chatbot follows a **Layered Architecture** with **Separation of Concerns**:

```
┌───────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                         │
│              (React + TypeScript Frontend)                    │
│  - Chat Interface Component                                   │
│  - Document Upload Interface                                  │
│  - Mode Selection Toggle                                      │
│  - Real-time Message Streaming                               │
└──────────────────────────┬──────────────────────────────────┘
                           │ HTTP/WebSocket
┌──────────────────────────▼──────────────────────────────────┐
│                      API GATEWAY LAYER                        │
│              (FastAPI REST & WebSocket Server)               │
│  - Request routing and validation                            │
│  - Response serialization                                     │
│  - Authentication & authorization                            │
│  - CORS and security headers                                 │
└──────────────────────────┬──────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
┌───────▼──────────┐ ┌────▼───────┐ ┌──────▼────────┐
│  Chat Service    │ │   Document │ │   Search      │
│  - Message       │ │   Service  │ │   Service     │
│    processing    │ │  - Upload  │ │  - Query      │
│  - History mgmt  │ │  - Storage │ │    processing │
│  - Response gen  │ │  - Indexing│ │  - Retrieval  │
└───────┬──────────┘ └────┬───────┘ └──────┬────────┘
        │                 │                │
        └─────────────────┼────────────────┘
                          │
┌─────────────────────────▼────────────────────────────────────┐
│                  INTEGRATION LAYER                           │
│      (LLM, Embeddings, Vector DB, Persistence)             │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  LLM        │  │  Embeddings  │  │  Document    │       │
│  │  Inference  │  │  Generation  │  │  Processing  │       │
│  │  (Llama)    │  │  (Sentence   │  │  (Docling,   │       │
│  │             │  │   Transformers)  │  Unstructured)      │
│  └─────────────┘  └──────────────┘  └──────────────┘       │
└─────────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┴──────────────────┐
        │                                     │
┌───────▼──────────────────┐       ┌────────▼──────────────┐
│   DATA LAYER             │       │   SEARCH LAYER        │
│   ┌──────────────────┐   │       │   ┌────────────────┐  │
│   │  PostgreSQL      │   │       │   │  ChromaDB      │  │
│   │  - Chat history  │   │       │   │  - Embeddings  │  │
│   │  - Documents     │   │       │   │  - Metadata    │  │
│   │  - User data     │   │       │   │  - Similarity  │  │
│   │  - Metadata      │   │       │   │    Search      │  │
│   └──────────────────┘   │       │   └────────────────┘  │
└──────────────────────────┘       └───────────────────────┘
```

### 1.2 Component Interaction Flow

```
USER REQUEST FLOW:
─────────────────

1. User Input
   └─→ React Component
       └─→ API Service
           └─→ FastAPI Endpoint
               └─→ Service Layer
                   ├─→ LLM Integration
                   ├─→ Vector Search
                   └─→ Database Query
                       └─→ Response Assembly
                           └─→ WebSocket Stream
                               └─→ React Display
```

---

## 2. Component Details

### 2.1 Frontend Components (React)

#### Chat Interface Component
```typescript
// Location: frontend/src/components/chat/

Structure:
  ChatHeader
    ├─ Logo & Branding
    ├─ New Chat Button
    ├─ Chat History
    └─ Settings

  ChatViewport
    ├─ Welcome Screen
    ├─ Message Display
    ├─ Loading States
    └─ Error Messages

  ChatInput
    ├─ Text Input Field
    ├─ Mode Selectors (RAG/Reasoning/Web Search)
    ├─ Document Upload Button
    └─ Send Button

  ChatMessage
    ├─ User Message
    ├─ Assistant Message
    ├─ Markdown Rendering
    └─ Streaming Indicator
```

#### State Management
```typescript
// Using React Hooks for state management

App State:
  - messages: Message[]
  - isStreaming: boolean
  - modes: ChatModes
  - documents: Document[]
  - error: string | null
  - uploadingFile: UploadState | null
```

### 2.2 API Layer (FastAPI)

#### Route Structure
```
/api
├── /chat
│   ├── POST   - Send message (one-shot)
│   ├── GET    - Get chat history
│   └── DELETE - Clear history
│
├── /chat/stream
│   └── WebSocket - Stream responses
│
├── /documents
│   ├── POST   - Upload document
│   ├── GET    - List documents
│   ├── DELETE - Delete document
│   └── GET /{id} - Get document details
│
├── /health
│   └── GET - System health check
│
└── /api/docs
    └── GET - Interactive API documentation (Swagger UI)
```

#### Request/Response Models
```python
# Pydantic Models for type safety

ChatRequest:
  - message: str
  - mode: ChatMode (enum: "rag" | "reasoning" | "web_search")
  - conversation_id: UUID (optional)

ChatResponse:
  - id: str
  - text: str
  - sender: str
  - timestamp: datetime
  - metadata: dict

DocumentUploadRequest:
  - file: UploadFile
  - description: str (optional)

DocumentMetadata:
  - id: UUID
  - filename: str
  - size: int
  - uploaded_at: datetime
  - status: str
```

### 2.3 Service Layer (Business Logic)

#### Chat Service
```python
# backend/api/services/chat_stream.py

Methods:
  - process_message(message: str) -> str
  - get_chat_history() -> List[Message]
  - clear_history() -> None
  - reformulate_query(query: str) -> str
  - retrieve_context(query: str) -> List[Context]
  - generate_response(context: List[Context]) -> str
  - stream_response(response_generator) -> AsyncIterator[str]
```

#### Document Service
```python
# backend/api/services/document_service.py

Methods:
  - upload_document(file: UploadFile) -> Document
  - process_document(doc_id: UUID) -> ProcessingResult
  - generate_embeddings(chunks: List[str]) -> List[Embedding]
  - index_document(doc_id: UUID, embeddings: List) -> None
  - search_documents(query: str, top_k: int) -> List[Chunk]
  - delete_document(doc_id: UUID) -> None
  - update_document(doc_id: UUID, file: UploadFile) -> Document
```

#### Vector Search Service
```python
# backend/api/services/vector_search.py

Methods:
  - semantic_search(query_embedding: List[float], top_k: int) -> List[Result]
  - index_embeddings(embeddings: List[Embedding]) -> None
  - update_index(old_id: UUID, new_embedding: List) -> None
  - delete_from_index(doc_id: UUID) -> None
  - get_similar_chunks(embedding: List[float], threshold: float) -> List[Chunk]
```

### 2.4 Integration Layer (AI/ML)

#### LLM Integration
```python
# backend/llm_client.py

LLMClient Class:
  - __init__(model_path: str, context_size: int)
  - generate(prompt: str, max_tokens: int) -> str
  - stream_generate(prompt: str) -> Iterator[str]
  - get_embeddings(text: str) -> List[float]
  - encode_query(query: str) -> str
  - handle_context_overflow(contexts: List[str]) -> str

Configuration:
  - Model: Llama 3.2 1B (GGUF format)
  - Context Window: 2048 tokens
  - Quantization: Q5_K_M (5-bit)
  - GPU Layers: Configurable (0 = CPU only)
```

#### Embedding Generation
```python
# Integration with Sentence Transformers

EmbeddingClient Class:
  - __init__(model_name: str)
  - encode(texts: List[str]) -> List[List[float]]
  - encode_single(text: str) -> List[float]
  - get_similarity(embedding1, embedding2) -> float
  - batch_encode(texts: List[str], batch_size: int) -> List[Embeddings]

Configuration:
  - Model: sentence-transformers/all-MiniLM-L6-v2
  - Embedding Dimension: 384
  - Batch Processing: Yes
  - GPU Support: Yes (if available)
```

#### Document Processing
```python
# Integration with Docling & Unstructured

DocumentProcessor Class:
  - extract_text(file_path: str) -> str
  - chunk_text(text: str, chunk_size: int) -> List[str]
  - extract_metadata(file_path: str) -> dict
  - parse_pdf(pdf_path: str) -> DocumentContent
  - parse_markdown(md_path: str) -> DocumentContent

Features:
  - Smart text chunking (semantic boundaries)
  - Metadata extraction
  - Multi-format support (PDF, Markdown, etc.)
  - Table and image reference preservation
```

### 2.5 Data Access Layer (Database)

#### PostgreSQL Integration
```python
# backend/database.py

Database Models:
  ┌─────────────────────────────────┐
  │    ChatMessage                  │
  ├─────────────────────────────────┤
  │ id: UUID (PK)                   │
  │ conversation_id: UUID (FK)      │
  │ sender: Enum(user/assistant)    │
  │ content: Text                   │
  │ created_at: DateTime            │
  │ is_streaming: Boolean           │
  │ metadata: JSONB                 │
  └─────────────────────────────────┘

  ┌─────────────────────────────────┐
  │    Document                     │
  ├─────────────────────────────────┤
  │ id: UUID (PK)                   │
  │ filename: String                │
  │ uploaded_at: DateTime           │
  │ version_hash: String            │
  │ content_hash: String            │
  │ status: Enum(active/deleted)    │
  └─────────────────────────────────┘

  ┌─────────────────────────────────┐
  │    DocumentChunk                │
  ├─────────────────────────────────┤
  │ id: UUID (PK)                   │
  │ document_id: UUID (FK)          │
  │ chunk_index: Integer            │
  │ text: Text                      │
  │ version_hash: String            │
  │ metadata: JSONB                 │
  └─────────────────────────────────┘
```

#### ChromaDB Integration
```python
# backend/vector_database.py

Collection Structure:
  documents
    ├─ embeddings: List[List[float]]
    ├─ metadatas: List[Metadata]
    ├─ documents: List[str]
    └─ ids: List[str]

Methods:
  - add(ids, embeddings, documents, metadatas)
  - query(query_embeddings, n_results, where)
  - delete(ids)
  - update(ids, embeddings, documents, metadatas)
  - get(ids, where, limit)
```

---

## 3. Data Flow Diagrams

### 3.1 Query Processing Flow

```
┌─────────────┐
│ User Query  │
└──────┬──────┘
       │
       ▼
┌──────────────────────┐
│ Input Validation     │
│ - Sanitization       │
│ - Length Check       │
│ - Format Check       │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Query Reformulation  │
│ (LLM Rewrite)        │
│                      │
│ "good places visit"  │
│  ↓                   │
│ "What are the best   │
│  tourist places to   │
│  visit?"             │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Generate Query       │
│ Embedding            │
│ (Sentence Trans.)    │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Vector Search        │
│ (ChromaDB)           │
│ Top-K: 5             │
│ Similar Chunks       │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Retrieve Context     │
│ - Rerank by          │
│   relevance          │
│ - Filter metadata    │
│ - Deduplicate        │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Build Prompt         │
│ + Chat History       │
│ + Retrieved Context  │
│ + System Instructions│
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ LLM Inference        │
│ (Llama 3.2 1B)       │
│ Stream Tokens        │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Response Streaming   │
│ (WebSocket)          │
│ Token by Token       │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Save to History      │
│ (PostgreSQL)         │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│ Display to User      │
│ (React)              │
└──────────────────────┘
```

### 3.2 Document Ingestion Flow

```
┌──────────────────┐
│ File Upload      │
│ (React)          │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Receive Upload   │
│ (FastAPI)        │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Validate File    │
│ - Format         │
│ - Size           │
│ - Virus Scan     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Store Document   │
│ (PostgreSQL)     │
│ Generate Hash    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Extract Text     │
│ (Docling/        │
│  Unstructured)   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Smart Chunking   │
│ Chunk Size: 512  │
│ Overlap: 128     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Generate         │
│ Embeddings       │
│ (Sentence Tran.) │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Index Chunks     │
│ (ChromaDB)       │
│ Store Metadata   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Update Status    │
│ Document Active  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Notify User      │
│ Success Message  │
└──────────────────┘
```

---

## 4. Database Schema (Detailed)

### 4.1 Chat History Table

```sql
CREATE TABLE chat_messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    conversation_id UUID NOT NULL,
    sender ENUM('user', 'assistant') NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_streaming BOOLEAN DEFAULT FALSE,
    metadata JSONB DEFAULT '{}',
    
    FOREIGN KEY (conversation_id) REFERENCES conversations(id),
    INDEX idx_conversation_id (conversation_id),
    INDEX idx_created_at (created_at)
);

CREATE TABLE conversations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR(255),
    
    INDEX idx_user_id (user_id)
);
```

### 4.2 Document Management Tables

```sql
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    filename VARCHAR(255) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    version_hash VARCHAR(64) NOT NULL,
    content_hash VARCHAR(64) NOT NULL,
    status ENUM('active', 'processing', 'deleted') DEFAULT 'processing',
    metadata JSONB DEFAULT '{}',
    
    UNIQUE(filename, version_hash),
    INDEX idx_status (status),
    INDEX idx_uploaded_at (uploaded_at)
);

CREATE TABLE document_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID NOT NULL,
    chunk_index INTEGER NOT NULL,
    text TEXT NOT NULL,
    version_hash VARCHAR(64),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (document_id) REFERENCES documents(id),
    INDEX idx_document_id (document_id),
    INDEX idx_version_hash (version_hash)
);
```

### 4.3 Vector Database (ChromaDB)

```python
# ChromaDB Collection Structure

{
    "id": "chunk_uuid",
    "embedding": [0.123, 0.456, ..., 0.789],  # 384-dimensional
    "document": "Text content of chunk...",
    "metadata": {
        "document_id": "doc_uuid",
        "chunk_index": 0,
        "page_number": 1,
        "version_hash": "abc123...",
        "source_document": "taj-mahal.md",
        "created_at": "2026-06-04T10:30:00Z"
    }
}
```

---

## 5. API Specifications

### 5.1 Chat Endpoint

```
POST /api/chat
├─ Request:
│  {
│    "message": "Tell me about Taj Mahal",
│    "mode": "rag",
│    "conversation_id": "uuid" (optional)
│  }
├─ Response:
│  {
│    "id": "message_uuid",
│    "text": "Taj Mahal is...",
│    "sender": "assistant",
│    "timestamp": "2026-06-04T10:30:00Z",
│    "metadata": {
│      "mode": "rag",
│      "tokens_used": 145,
│      "response_time_ms": 1250
│    }
│  }
└─ Status Codes:
   200: Success
   400: Invalid request
   500: Server error
```

### 5.2 WebSocket Endpoint

```
WebSocket /api/chat/stream
├─ Connect Message:
│  {
│    "type": "query",
│    "message": "Tell me about Goa",
│    "mode": "rag"
│  }
├─ Server Response (streaming):
│  {
│    "type": "token",
│    "content": "Goa"
│  }
│  {
│    "type": "token",
│    "content": " is"
│  }
│  {
│    "type": "token",
│    "content": " a..."
│  }
│  {
│    "type": "complete",
│    "metadata": {...}
│  }
└─ Disconnect: Automatic or manual
```

### 5.3 Document Upload Endpoint

```
POST /api/documents/upload
├─ Request:
│  - Content-Type: multipart/form-data
│  - File: Binary file content
│  - Description: Optional string
├─ Response:
│  {
│    "id": "document_uuid",
│    "filename": "goa-guide.pdf",
│    "size": 2048000,
│    "status": "processing",
│    "uploaded_at": "2026-06-04T10:30:00Z"
│  }
└─ Status Codes:
   200: Accepted for processing
   400: Invalid file
   413: File too large
```

---

## 6. Security Considerations

### 6.1 Input Validation
```python
# Validate all user inputs
- Query length: 1-5000 characters
- File size: Max 50MB
- File types: PDF, Markdown only
- SQL injection prevention (SQLAlchemy ORM)
- XSS prevention (React escaping)
```

### 6.2 Authentication & Authorization
```
- API endpoints protected with API keys (future)
- JWT tokens for user sessions (future)
- Rate limiting: 100 requests/minute per IP
- CORS policy: Whitelist origins
```

### 6.3 Data Protection
```
- Database: SSL/TLS encryption
- API: HTTPS/WSS only
- Sensitive logs: Masked in output
- File uploads: Virus scanning (future)
```

---

## 7. Performance Optimization

### 7.1 Query Optimization
- Vector search: O(log n) with indexing
- Query reformulation: Cached templates
- Context retrieval: Batch processing
- Response streaming: Progressive rendering

### 7.2 Database Optimization
- Indexes on frequently queried columns
- Connection pooling (5-20 connections)
- Query result caching (Redis, future)
- Materialized views for complex queries

### 7.3 Model Optimization
- GGUF quantization (5-bit)
- Batch inference support
- Streaming token generation
- GPU support when available

---

## 8. Error Handling & Logging

### 8.1 Error Handling Strategy
```python
# Graceful error handling at each layer

Level 1: Input Validation
  └─ Validation errors → 400 Bad Request

Level 2: Service Logic
  └─ Business logic errors → 422 Unprocessable Entity

Level 3: External Systems
  └─ LLM/DB errors → 503 Service Unavailable

Level 4: Unexpected Errors
  └─ System errors → 500 Internal Server Error
```

### 8.2 Logging Infrastructure
```python
# Structured logging with context

Log Levels:
  - DEBUG: Development debugging
  - INFO: General application flow
  - WARNING: Potential issues
  - ERROR: Failures
  - CRITICAL: System critical issues

Log Fields:
  - timestamp
  - level
  - logger_name
  - message
  - context (request_id, user_id, etc.)
  - stack_trace (for errors)
```

---

**Document Version**: 1.0  
**Last Updated**: June 2026  
**Author**: N. Uma Devi  
**Faculty Guide**: Chakradhar Rao
