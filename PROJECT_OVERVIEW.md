# Project Overview & Requirements Specification

**Tourism Guide Chatbot - Academic Capstone Project**

---

## 1. Executive Summary

The **Tourism Guide Chatbot** is an intelligent conversational AI system designed to assist tourists in discovering, planning, and exploring travel destinations. The system combines modern natural language processing, machine learning, and web technologies to provide a seamless user experience for tourism guidance.

### Key Statistics
- **Scope**: Full-stack application with AI/ML backend
- **Development Duration**: 6 months
- **Technology Stack**: Python, FastAPI, React, TypeScript, PostgreSQL, ChromaDB
- **Team Size**: 1 (Academic Project)
- **Model Size**: 1B parameters (optimized for local deployment)

---

## 2. Problem Statement

### Challenges Addressed

1. **Information Fragmentation**
   - Tourism information scattered across multiple sources
   - Difficulty finding accurate, curated destination information
   - Time-consuming manual research required

2. **Lack of Personalization**
   - Generic travel guides don't match individual preferences
   - Limited context awareness in recommendations
   - No conversational interface for travel planning

3. **Scalability & Accessibility**
   - Need for offline-capable systems
   - High costs of cloud-based AI services
   - Limited privacy in cloud-dependent solutions

4. **Information Quality**
   - Challenge in ensuring accuracy of travel information
   - Verification of tourist recommendations
   - Keeping information current and relevant

---

## 3. Proposed Solution

### System Objectives

**Primary Objectives**:
1. ✅ Develop an intelligent chatbot for tourism guidance
2. ✅ Implement RAG for context-aware, accurate responses
3. ✅ Create user-friendly web interface
4. ✅ Ensure local deployment capability
5. ✅ Maintain conversation history and context

**Secondary Objectives**:
1. ✅ Demonstrate full-stack development competency
2. ✅ Implement advanced AI/ML concepts
3. ✅ Provide extensible, modular architecture
4. ✅ Ensure code quality and documentation
5. ✅ Optimize for resource efficiency

### Solution Approach

The solution follows a layered architecture:

```
┌─────────────────────────────────┐
│   Presentation Layer (React)    │  User Interface
├─────────────────────────────────┤
│  API Layer (FastAPI)            │  REST Endpoints
├─────────────────────────────────┤
│  Business Logic Layer           │  Processing & Orchestration
├─────────────────────────────────┤
│  Integration Layer              │  AI/ML & Database
├─────────────────────────────────┤
│  Data Layer                     │  PostgreSQL, ChromaDB
└─────────────────────────────────┘
```

---

## 4. Functional Requirements

### FR1: User Management & Sessions
- **FR1.1**: User can initiate new chat sessions
- **FR1.2**: User can continue previous conversations
- **FR1.3**: System maintains chat history persistently

### FR2: Conversational Interaction
- **FR2.1**: User can send text queries
- **FR2.2**: System provides real-time streaming responses
- **FR2.3**: System maintains conversation context
- **FR2.4**: User can specify interaction mode (RAG/Reasoning/Web Search)

### FR3: Document Management
- **FR3.1**: User can upload tourism documents
- **FR3.2**: System processes and indexes documents
- **FR3.3**: System enables search within uploaded documents
- **FR3.4**: User can manage document collection

### FR4: Knowledge Base
- **FR4.1**: System maintains vector database of embeddings
- **FR4.2**: System performs semantic search on queries
- **FR4.3**: System retrieves relevant context for responses
- **FR4.4**: System updates knowledge base incrementally

### FR5: Response Generation
- **FR5.1**: System generates contextually relevant responses
- **FR5.2**: System supports multiple reasoning modes
- **FR5.3**: System handles context overflow intelligently
- **FR5.4**: System streams responses in real-time

### FR6: API Endpoints
- **FR6.1**: POST `/api/chat` - Send message
- **FR6.2**: WebSocket `/api/chat/stream` - Stream response
- **FR6.3**: POST `/api/documents/upload` - Upload document
- **FR6.4**: GET `/api/documents` - List documents
- **FR6.5**: GET `/api/health` - System health check

---

## 5. Non-Functional Requirements

### NFR1: Performance
- Response latency: < 3 seconds (p95) for RAG queries
- Streaming latency: < 500ms for first token
- Document processing: < 10 seconds per MB
- API throughput: ≥ 100 requests/minute

### NFR2: Scalability
- Support for 1000+ concurrent users
- Horizontal scaling capability
- Efficient vector database indexing
- Memory-efficient embedding storage

### NFR3: Reliability
- System uptime: ≥ 99%
- Data persistence and recovery
- Graceful error handling
- Comprehensive logging

### NFR4: Security
- Authentication & authorization
- Input validation and sanitization
- SQL injection prevention (via ORM)
- HTTPS/WSS for data in transit
- Sensitive data protection

### NFR5: Usability
- Intuitive UI/UX
- Responsive design (mobile-friendly)
- Clear error messages
- Fast page load times
- Accessibility compliance

### NFR6: Maintainability
- Code quality: Type-safe (TypeScript, Python type hints)
- Test coverage: ≥ 80%
- Comprehensive documentation
- Modular, loosely-coupled components
- CI/CD pipeline

---

## 6. System Features & Capabilities

### Core Features

#### Feature 1: Intelligent Destination Guidance
```
User Query: "Tell me about Taj Mahal"
      ↓
System Process:
  1. Parse query semantically
  2. Search vector database
  3. Retrieve top-5 relevant contexts
  4. Synthesize comprehensive response
  5. Stream response to user
      ↓
Response: Detailed information about Taj Mahal, visiting hours,
          travel tips, and nearby attractions
```

#### Feature 2: Multi-Mode Conversation
- **RAG Mode**: Uses knowledge base for factual accuracy
- **Reasoning Mode**: Uses pure LLM reasoning for complex queries
- **Web Search Mode**: Augments responses with real-time web data

#### Feature 3: Document Management
- Upload custom tourism guides
- Automatic text extraction and chunking
- Semantic indexing for retrieval
- Version tracking for updates

#### Feature 4: Conversation Memory
- Persistent chat history
- Context-aware follow-up responses
- Relevant history retrieval
- Automatic summarization for long conversations

#### Feature 5: Real-Time Streaming
- Server-sent events (SSE) for updates
- WebSocket for bi-directional communication
- Progressive response rendering
- Connection recovery

### Technical Features

#### Feature 6: Vector Embeddings
- High-dimensional semantic representations
- Efficient similarity search
- Metadata-filtered retrieval
- Incremental index updates

#### Feature 7: Query Reformulation
```
Original Query: "good places visit"
         ↓
LLM Reformulation: "What are the best tourist places to visit 
                   and why should one visit them?"
         ↓
Enhanced Retrieval Accuracy
```

#### Feature 8: Context Synthesis
- **Create & Refine**: Sequential synthesis through contexts
- **Hierarchical Summarization**: Independent summaries merged hierarchically
- **Automatic Context Overflow Handling**

---

## 7. Technology Justification

### Backend: Python + FastAPI
**Why**:
- Mature ecosystem for ML/AI applications
- Excellent libraries (llama-cpp-python, sentence-transformers)
- Type safety with Python type hints
- FastAPI provides high performance with automatic documentation

### Frontend: React + TypeScript
**Why**:
- Component-based architecture for maintainability
- Rich UI libraries and tools
- Type safety with TypeScript
- Large community and extensive documentation

### Database: PostgreSQL + ChromaDB
**Why**:
- PostgreSQL: Reliable, ACID-compliant relational database
- ChromaDB: Purpose-built for vector embeddings and semantic search
- Both support incremental updates and metadata filtering

### LLM: Llama 3.2 1B (GGUF)
**Why**:
- Open-source and freely available
- Small model (1B) optimized for local deployment
- GGUF format enables quantization and efficiency
- No external API costs or privacy concerns

---

## 8. Data Model

### Core Entities

#### Chat Message
```
{
  id: UUID,
  conversation_id: UUID,
  sender: "user" | "assistant",
  content: string,
  created_at: datetime,
  is_streaming: boolean,
  metadata: {
    mode: "rag" | "reasoning" | "web_search",
    tokens_used: integer,
    response_time_ms: integer
  }
}
```

#### Document
```
{
  id: UUID,
  filename: string,
  uploaded_at: datetime,
  version_hash: string,
  content_hash: string,
  chunk_count: integer,
  metadata: {
    source_type: "pdf" | "markdown",
    page_count: integer,
    file_size_bytes: integer
  }
}
```

#### Vector Embedding
```
{
  id: UUID,
  document_id: UUID,
  chunk_index: integer,
  chunk_text: string,
  embedding: float[1536],  # High-dimensional vector
  metadata: {
    version_hash: string,
    page_number: integer,
    chunk_position: string
  }
}
```

---

## 9. User Workflows

### Workflow 1: Basic Chat
```
User opens app
    ↓
Views welcome screen with Tourism Guide Chatbot intro
    ↓
Types query: "What are top attractions in Goa?"
    ↓
Selects RAG mode (optional)
    ↓
Presses Enter/Send
    ↓
System processes query:
  - Reformulates query
  - Searches vector database
  - Retrieves relevant contexts
  - Generates streaming response
    ↓
Views streamed response in real-time
    ↓
Can ask follow-up questions
```

### Workflow 2: Document Upload
```
User clicks "Upload documents"
    ↓
Selects file(s) from computer
    ↓
Clicks "Upload"
    ↓
System processes:
  - Extracts text from document
  - Splits into chunks
  - Generates embeddings
  - Stores in vector database
    ↓
Shows "Upload successful"
    ↓
User can now ask questions about uploaded content
```

### Workflow 3: Conversation Mode Switching
```
Starts conversation in RAG mode
    ↓
Wants to switch to Reasoning mode
    ↓
Clicks "Reasoning" mode toggle
    ↓
Sends new query
    ↓
System uses pure LLM reasoning without vector search
    ↓
Receives response optimized for reasoning
```

---

## 10. Testing Strategy

### Unit Testing
- Individual function testing
- Mock external dependencies
- Test coverage: ≥ 80%

### Integration Testing
- Component interaction testing
- API endpoint testing
- Database operation testing

### System Testing
- End-to-end workflow testing
- Load testing (100+ concurrent users)
- Stress testing

### User Acceptance Testing
- Real user scenarios
- Performance validation
- UI/UX validation

---

## 11. Deployment Strategy

### Development Environment
- Local setup with virtual environment
- Mock services for testing
- Debug logging enabled

### Production Environment
- Docker containerization
- Kubernetes orchestration (optional)
- PostgreSQL managed database
- CDN for frontend assets
- Environment-specific configurations

### Deployment Checklist
- [ ] Code review and testing
- [ ] Security scanning
- [ ] Performance benchmarking
- [ ] Database migration
- [ ] Backup strategy validation
- [ ] Monitoring setup
- [ ] Documentation finalization

---

## 12. Success Metrics

### User Metrics
- ✅ User satisfaction score: ≥ 4.0/5.0
- ✅ Average session duration: ≥ 5 minutes
- ✅ Query resolution rate: ≥ 90%
- ✅ Return user rate: ≥ 60%

### System Metrics
- ✅ System availability: ≥ 99%
- ✅ Average response time: < 2 seconds
- ✅ Error rate: < 0.1%
- ✅ API uptime: 99.9%

### Development Metrics
- ✅ Code quality score: ≥ 8/10
- ✅ Test coverage: ≥ 80%
- ✅ Documentation completeness: 100%
- ✅ No critical security vulnerabilities

---

## 13. Constraints & Limitations

### Technical Constraints
1. **Memory**: LLM requires ≥ 4GB RAM for inference
2. **Storage**: Vector database requires ≥ 1GB for 10k embeddings
3. **Processing**: Document processing CPU-intensive
4. **Network**: Streaming requires persistent connection

### Functional Constraints
1. **Language**: Currently English-only (future: multilingual)
2. **Context Window**: LLM has 2048 token context limit
3. **Real-time Data**: No live pricing/booking integration (Phase 2)
4. **Scalability**: Single-instance deployment limits

### Business Constraints
1. **Cost**: Free hosting option limited
2. **Data**: Relies on manually uploaded knowledge base
3. **Maintenance**: Requires regular knowledge base updates
4. **Model**: Llama 3.2 1B less capable than larger models

---

## 14. Future Roadmap

### Q3 2026: Phase 1 (Current)
- ✅ Basic RAG chatbot
- ✅ Document upload & management
- ✅ Conversation history
- ✅ Web interface

### Q4 2026: Phase 2
- Real-time API integration (flights, hotels)
- Multi-language support
- Mobile app (React Native)
- Advanced analytics

### Q1 2027: Phase 3
- Voice interaction
- Fine-tuned model
- Social features
- AI trip planning

### Q2 2027: Phase 4
- Augmented Reality features
- Offline mobile mode
- Advanced personalization
- Enterprise features

---

## 15. Conclusion

The **Tourism Guide Chatbot** represents a comprehensive implementation of modern AI/ML concepts within a real-world application context. By combining RAG, vector embeddings, and conversational AI, the system provides an intelligent, scalable solution for tourism guidance while demonstrating proficiency in full-stack development, system design, and software engineering best practices.

---

**Document Version**: 1.0  
**Last Updated**: June 2026  
**Author**: N. Uma Devi  
**Faculty Guide**: Chakradhar Rao
