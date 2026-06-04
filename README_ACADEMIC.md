# Tourism Guide Chatbot

**An Intelligent Conversational AI System for Tourism Guidance and Travel Planning**

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Academic Details](#academic-details)
3. [System Description](#system-description)
4. [Key Features](#key-features)
5. [Technology Stack](#technology-stack)
6. [System Architecture](#system-architecture)
7. [Installation & Setup](#installation--setup)
8. [Usage Guide](#usage-guide)
9. [Project Structure](#project-structure)
10. [Future Enhancements](#future-enhancements)
11. [References](#references)

---

## 📚 Project Overview

**Tourism Guide Chatbot** is an intelligent conversational AI system developed as an academic project for the Master of Computer Applications (MCA) program. The system leverages advanced natural language processing, retrieval-augmented generation (RAG), and semantic search technologies to provide users with accurate, comprehensive, and personalized tourism guidance and travel recommendations.

The chatbot combines three core technologies:

- **Large Language Models (LLMs)**: Local implementation of open-source models for intelligent conversation and reasoning
- **Vector Embeddings & Semantic Search**: Retrieval-Augmented Generation for context-aware responses
- **Persistent Memory Systems**: Conversation history tracking and knowledge base management

### 🎯 Objectives

1. Create an intelligent chatbot system capable of understanding complex tourism-related queries
2. Implement RAG (Retrieval-Augmented Generation) for accurate, source-based responses
3. Develop a user-friendly web interface for seamless tourist interactions
4. Demonstrate proficiency in full-stack development, AI/ML integration, and system design
5. Provide scalable, modular architecture for future enhancements

---

## 👥 Academic Details

| Field | Details |
|-------|---------|
| **Project Name** | Tourism Guide Chatbot |
| **Student Name** | N. Uma Devi |
| **Faculty Guide** | Chakradhar Rao |
| **Department** | Master of Computer Applications (MCA) |
| **Project Type** | Academic Capstone Project |
| **Submission Date** | 2026 |

---

## 🔧 System Description

### Core Functionality

The Tourism Guide Chatbot operates through an integrated pipeline of components:

#### 1. **Knowledge Base Management**
- Ingests tourism-related documents (Markdown, PDFs)
- Processes documents through intelligent chunking strategies
- Maintains document version tracking and incremental updates
- Stores in vector database for efficient retrieval

#### 2. **Intelligent Query Processing**
- Accepts user questions about destinations, attractions, travel tips
- Reformulates queries for optimal retrieval using LLM
- Searches vector database for relevant context
- Maintains conversation history for contextual understanding

#### 3. **Response Generation**
- Synthesizes responses from retrieved documents
- Handles context overflow through advanced strategies
- Maintains conversation state and user context
- Supports multiple reasoning modes (RAG, Reasoning, Web Search)

#### 4. **User Interface**
- Modern React-based web frontend
- Real-time chat interface with streaming responses
- Document upload capability
- Mode selection for different interaction styles

---

## ✨ Key Features

### For End Users

✅ **Intelligent Destination Guidance**
- Comprehensive information about tourist destinations
- Cultural, historical, and natural attraction details
- Travel tips and local recommendations

✅ **Multi-Mode Conversations**
- **RAG Mode**: Context-aware responses from knowledge base
- **Reasoning Mode**: Complex problem-solving and planning
- **Web Search**: Real-time information retrieval

✅ **Document Upload & Search**
- Upload custom tourism guides and travel documents
- Query against uploaded documents
- Persistent knowledge base management

✅ **Conversational Memory**
- Maintains chat history across sessions
- Context-aware responses considering previous interactions
- Intelligent context summarization for long conversations

### For Developers

✅ **Modular Architecture**
- Separated concerns: API, services, database, LLM client
- Pluggable components for easy customization
- Clean interfaces for integration

✅ **Advanced NLP Features**
- Vector embeddings with semantic search
- Query reformulation for improved retrieval
- Hierarchical context summarization

✅ **Scalable Backend**
- PostgreSQL database with Alembic migrations
- Chroma vector database for embeddings
- Async API with real-time streaming

✅ **Production-Ready Code**
- Type hints throughout codebase
- Comprehensive error handling
- Logging and monitoring capabilities

---

## 🛠️ Technology Stack

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.12+ | Core backend language |
| **FastAPI** | ~0.115 | REST API framework with async support |
| **Uvicorn** | Latest | ASGI server for async operations |
| **SQLAlchemy** | 2.0+ | ORM for database operations |
| **Alembic** | Latest | Database migrations |
| **PostgreSQL** | 12+ | Primary database |

### AI/ML
| Technology | Version | Purpose |
|------------|---------|---------|
| **Llama CPP Python** | Latest | Local LLM inference |
| **Llama 3.2 1B** | - | Local language model (GGUF format) |
| **Sentence Transformers** | ~5.1 | Embedding generation |
| **ChromaDB** | ~1.5 | Vector database for embeddings |
| **Unstructured** | ~0.20 | Document parsing |
| **Docling** | ~2.82 | Advanced document processing |

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| **React** | 18+ | UI framework |
| **TypeScript** | 5.0+ | Type-safe JavaScript |
| **Vite** | 7.0+ | Build tool and dev server |
| **TailwindCSS** | 3.0+ | Utility-first CSS |
| **Lucide Icons** | Latest | Icon library |

### Infrastructure
| Technology | Purpose |
|------------|---------|
| **Docker** | Containerization |
| **GitHub** | Version control and CI/CD |
| **Git LFS** | Large file management |

---

## 🏗️ System Architecture

### High-Level Architecture Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INTERFACE (React)                      │
│              - Chat Interface                                    │
│              - Document Upload                                   │
│              - Mode Selection (RAG/Reasoning/Web Search)        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    API GATEWAY (FastAPI)                        │
│    ─────────────────────────────────────────────────────────    │
│    • /chat - Send messages                                      │
│    • /chat/stream - Stream responses                            │
│    • /documents - Upload & manage documents                     │
│    • /health - System health check                              │
│    • /api/docs - Interactive API documentation                  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
        ┌─────────────────────┴─────────────────────┐
        ↓                                           ↓
┌──────────────────────────┐             ┌──────────────────────────┐
│    QUERY PROCESSING      │             │   DOCUMENT MANAGEMENT    │
│    ─────────────────────  │             │    ──────────────────────│
│ • Query Reformulation    │             │ • Text Splitting         │
│ • Context Retrieval      │             │ • Embedding Generation   │
│ • History Management     │             │ • Vector Storage         │
└──────────────────────────┘             └──────────────────────────┘
        ↓                                           ↓
┌──────────────────────────────────────────────────────────────────┐
│           VECTOR SEARCH & CONTEXT ENGINE (ChromaDB)             │
│  - Semantic Search across document embeddings                   │
│  - Document-level metadata tracking                              │
│  - Incremental index updates                                     │
└──────────────────────────────────────────────────────────────────┘
        ↓                                           ↓
┌──────────────────────────┐             ┌──────────────────────────┐
│    LLM INFERENCE         │             │     DATABASE LAYER       │
│    ─────────────────────  │             │    ──────────────────────│
│ • Llama 3.2 1B Model     │             │ • PostgreSQL (chat hist) │
│ • Local Inference        │             │ • ChromaDB (embeddings)  │
│ • Context Synthesis      │             │ • Metadata Storage       │
│ • Stream Generation      │             │                          │
└──────────────────────────┘             └──────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────────────────┐
│                    RESPONSE STREAMING                           │
│              Back to User Interface (Real-time)                 │
└─────────────────────────────────────────────────────────────────┘
```

### Component Interaction Diagram

```
DOCUMENT INGESTION PIPELINE:
───────────────────────────

Raw Documents → Document Loader → Text Splitter → Embeddings → ChromaDB
    (PDFs,         (Docling,         (Smart            (Sentence    (Vector
   Markdown)      Unstructured)     Chunking)      Transformers)    DB)
                                          ↓
                                   Metadata Tracking
                                   (Doc ID, Version)


QUERY PROCESSING PIPELINE:
─────────────────────────

User Query → Query Reformulation → Vector Search → Context Retrieval
  (Chat)      (LLM Rewrite)     (Semantic Match)  (Top-K Results)
                                                        ↓
              Chat History ←────────────────────── Context Selection
              (Memory)                             (Relevance Ranking)
                    ↓
              Response Synthesis → Streaming → Response
              (LLM Generation)    (WebSocket)
```

### Database Schema

```
TABLES:
───────

Chat History:
  - message_id (UUID, PK)
  - user_id (UUID, FK)
  - message_text (TEXT)
  - sender (ENUM: user/assistant)
  - timestamp (DATETIME)
  - conversation_id (UUID, FK)
  - is_streaming (BOOLEAN)

Documents:
  - document_id (UUID, PK)
  - filename (VARCHAR)
  - upload_date (DATETIME)
  - version_hash (VARCHAR)
  - content_hash (VARCHAR)
  - source_type (ENUM)

Vector Embeddings (ChromaDB):
  - embedding_id (UUID)
  - document_id (FK)
  - chunk_text (TEXT)
  - embedding (VECTOR[1536])
  - metadata (JSONB)
    - source_doc_id
    - version_hash
    - chunk_index
    - page_number
```

---

## 📦 Installation & Setup

### Prerequisites

- **Python**: 3.12 or higher
- **Node.js**: 18 or higher
- **PostgreSQL**: 12 or higher
- **Git**: Latest version
- **RAM**: Minimum 8GB (16GB recommended)
- **Storage**: 5GB for models and dependencies

### Step 1: Clone Repository

```bash
git clone https://github.com/umadevijava/tourism_guide.git
cd tourism_guide
```

### Step 2: Backend Setup

#### Create Virtual Environment

```bash
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
```

#### Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### Database Configuration

```bash
# Create PostgreSQL database
createdb tourism_guide

# Run migrations
python -m alembic upgrade head
```

#### Environment Variables

Create `.env` file in project root:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost/tourism_guide

# API
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=True

# LLM Configuration
LLM_MODEL_PATH=./models/Llama-3.2-1B-Instruct-Q5_K_M.gguf
LLM_N_CTX=2048
LLM_N_GPU_LAYERS=0

# Embeddings
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Vector Database
CHROMA_DB_PATH=./vector_store

# CORS
CORS_ORIGINS=["http://localhost:5173","http://localhost:3000"]
```

#### Download LLM Model

```bash
# Create models directory
mkdir models

# Download Llama 3.2 1B GGUF model
cd models
wget https://huggingface.co/models/[model-url]/Llama-3.2-1B-Instruct-Q5_K_M.gguf
cd ..
```

#### Start Backend Server

```bash
# Development mode with auto-reload
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 3: Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Environment variables (.env.local)
VITE_API_URL=http://localhost:8000

# Development server
npm run dev

# Build for production
npm run build
```

### Step 4: Populate Knowledge Base

```bash
# Add tourism documents to docs/ folder
# Supported formats: Markdown, PDF

# Documents will be automatically indexed on startup
# Or trigger manual indexing via API endpoint
```

---

## 💻 Usage Guide

### Starting the Application

#### Terminal 1 - Backend
```bash
cd rag-chatbot-main
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

#### Terminal 2 - Frontend
```bash
cd rag-chatbot-main/frontend
npm run dev
```

#### Access Application
- **Frontend**: http://localhost:5173
- **API Docs**: http://localhost:8000/docs
- **API**: http://localhost:8000

### Using the Chatbot

#### Basic Chat
1. Type your tourism-related query in the chat input
2. Select interaction mode (RAG, Reasoning, Web Search)
3. Upload documents for context (optional)
4. Press Enter or click Send button
5. View streaming response in real-time

#### Document Upload
1. Click "Upload documents" button
2. Select one or multiple files (PDF, Markdown)
3. Monitor upload progress
4. Documents are automatically indexed and searchable

#### Chat Modes

**RAG Mode**: Retrieves context from knowledge base before generating response
```
Query → Vector Search → Retrieved Context → Response Generation
```

**Reasoning Mode**: Uses advanced LLM reasoning without document context
```
Query → LLM Reasoning → Structured Response
```

**Web Search**: Integrates real-time web search results
```
Query → Web Search → Context → Response
```

---

## 📁 Project Structure

```
tourism_guide/
├── README_ACADEMIC.md                 # This file
├── backend/                            # Python backend
│   ├── main.py                        # FastAPI app entry point
│   ├── database.py                    # Database configuration
│   ├── llm_client.py                  # LLM integration
│   ├── vector_database.py             # Vector DB management
│   ├── chat_history.py                # Chat persistence
│   ├── core/
│   │   └── config.py                  # Configuration
│   ├── api/
│   │   ├── routes.py                  # API routes
│   │   ├── deps.py                    # Dependencies
│   │   └── endpoints/
│   │       ├── chat.py                # Chat endpoint
│   │       ├── chat_stream.py         # Streaming endpoint
│   │       ├── documents.py           # Document management
│   │       └── health.py              # Health check
│   ├── schemas/                        # Pydantic models
│   └── alembic/                        # Database migrations
├── frontend/                           # React frontend
│   ├── src/
│   │   ├── App.tsx                    # Main component
│   │   ├── components/
│   │   │   └── chat/
│   │   │       ├── chat-header.tsx
│   │   │       ├── chat-viewport.tsx
│   │   │       ├── chat-input.tsx
│   │   │       └── chat-message.tsx
│   │   ├── hooks/
│   │   │   ├── useChat.ts
│   │   │   └── useDocuments.ts
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   └── websocket.ts
│   │   └── index.css
│   ├── index.html
│   └── vite.config.ts
├── docs/                               # Tourism documentation
│   └── destinations/
│       └── taj-mahal.md               # Sample destination guide
├── models/                             # LLM models
│   └── Llama-3.2-1B-Instruct-Q5_K_M.gguf
├── vector_store/                       # ChromaDB storage
└── tests/                              # Test suite
```

---

## 🚀 Future Enhancements

### Phase 2 Features

1. **Multi-Language Support**
   - Automatic translation of responses
   - Support for 10+ languages
   - Regional currency and unit conversion

2. **Advanced User Personalization**
   - User profiles and preferences
   - Recommendation engine
   - Travel style matching

3. **Real-Time Integration**
   - Flight and hotel pricing APIs
   - Weather integration
   - Local event calendar
   - Restaurant and attraction reviews

4. **Mobile Application**
   - React Native mobile app
   - Offline mode with sync
   - GPS-based local recommendations

5. **Enhanced Analytics**
   - User behavior tracking
   - Popular destination analytics
   - Chatbot performance metrics dashboard

### Phase 3 Features

1. **Voice Interaction**
   - Voice-to-text input
   - Text-to-speech responses
   - Multi-language voice support

2. **AI-Powered Trip Planning**
   - Automatic itinerary generation
   - Budget-aware planning
   - Group travel coordination

3. **Social Features**
   - Travel experience sharing
   - Community reviews
   - Collaborative planning

4. **Advanced Reasoning**
   - Fine-tuned model on tourism domain
   - Multi-hop reasoning
   - Explainable AI for recommendations

---

## 📖 References

### Academic Resources
- Vaswani, A., et al. (2017). "Attention Is All You Need." *NeurIPS*
- Lewis, P., et al. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *NeurIPS*
- Radford, A., et al. (2019). "Language Models are Unsupervised Multitask Learners." OpenAI

### Technical Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Llama.cpp GitHub](https://github.com/ggerganov/llama.cpp)
- [Sentence Transformers](https://www.sbert.net/)

### Tools & Frameworks
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [TailwindCSS Documentation](https://tailwindcss.com/docs)
- [Vite Documentation](https://vitejs.dev/)

---

## 📝 License

This project is submitted as an academic capstone project for MCA evaluation.

---

## 👤 Author

**N. Uma Devi**  
Master of Computer Applications (MCA)  
Faculty Guide: Chakradhar Rao  
Academic Year: 2025-2026

---

**Last Updated**: June 2026  
**Project Status**: Active Development
