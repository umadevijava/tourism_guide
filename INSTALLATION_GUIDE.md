# Installation, Setup & Deployment Guide

**Tourism Guide Chatbot - Complete Setup Instructions**

---

## 1. System Requirements

### Minimum Requirements
- **OS**: Windows 10, Ubuntu 20.04, macOS 11+
- **CPU**: Quad-core processor (Intel/AMD/Apple Silicon)
- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: 10GB free space
- **GPU**: Optional (NVIDIA CUDA or Apple Metal for acceleration)

### Recommended Setup
- **OS**: Ubuntu 22.04 LTS or Windows 11
- **CPU**: 8+ cores
- **RAM**: 16GB minimum
- **Storage**: SSD with 20GB+ free space
- **GPU**: NVIDIA RTX 3060 or better (6GB+ VRAM)

### Network Requirements
- Stable internet (for initial setup and model downloads)
- Can work offline after setup
- Port availability: 8000 (backend), 5173 (frontend)

---

## 2. Prerequisites Installation

### 2.1 Python Installation

#### Windows
```powershell
# Download from https://www.python.org/downloads/
# Or use Windows Package Manager
winget install Python.Python.3.12

# Verify installation
python --version  # Should be 3.12+
pip --version
```

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install python3.12 python3.12-dev python3.12-venv

# Verify
python3.12 --version
```

#### macOS
```bash
# Using Homebrew
brew install python@3.12

# Verify
python3.12 --version
```

### 2.2 Node.js Installation

#### Windows
```powershell
winget install OpenJS.NodeJS.LTS
# Or download from https://nodejs.org/
```

#### Ubuntu/Debian
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs

# Or using nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
nvm use 18
```

#### macOS
```bash
brew install node
```

### 2.3 PostgreSQL Installation

#### Windows
```powershell
# Download installer from https://www.postgresql.org/download/windows/
# Or use chocolatey
choco install postgresql

# After installation, add to PATH
# Test: psql --version
```

#### Ubuntu/Debian
```bash
sudo apt install postgresql postgresql-contrib

# Start service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Verify
sudo -u postgres psql --version
```

#### macOS
```bash
brew install postgresql
brew services start postgresql

# Verify
psql --version
```

### 2.4 Git Installation

```bash
# Windows
winget install Git.Git

# Ubuntu/Debian
sudo apt install git

# macOS
brew install git

# Verify
git --version
```

---

## 3. Repository Setup

### 3.1 Clone Repository

```bash
git clone https://github.com/umadevijava/tourism_guide.git
cd tourism_guide
```

### 3.2 Project Structure Verification

```bash
# Verify directory structure
ls -la

# Expected directories:
# backend/          - Python backend
# frontend/         - React frontend
# docs/             - Documentation
# models/           - LLM models (empty initially)
# vector_store/     - ChromaDB (empty initially)
# tests/            - Test suite
```

---

## 4. Backend Setup

### 4.1 Create Virtual Environment

#### Windows (PowerShell)
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# If you get execution policy error, run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Linux/macOS
```bash
# Create virtual environment
python3.12 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

### 4.2 Install Python Dependencies

```bash
# Upgrade pip
pip install --upgrade pip setuptools wheel

# Install project dependencies
pip install -r requirements.txt

# Verify installation
pip list | grep -E "fastapi|sqlalchemy|chromadb|torch"
```

### 4.3 Database Setup

#### Create PostgreSQL Database

```bash
# Windows (cmd or PowerShell)
psql -U postgres

# macOS/Linux
sudo -u postgres psql

# In PostgreSQL console
CREATE DATABASE tourism_guide;
CREATE USER tourism_user WITH PASSWORD 'secure_password_123';
ALTER ROLE tourism_user SET client_encoding TO 'utf8';
ALTER ROLE tourism_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE tourism_user SET default_transaction_deferrable TO on;
ALTER ROLE tourism_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE tourism_guide TO tourism_user;
\q
```

#### Run Database Migrations

```bash
# Navigate to backend directory (if not already there)
cd backend

# Create alembic revision
alembic revision --autogenerate -m "Initial schema"

# Apply migrations
alembic upgrade head

# Verify tables created
psql -U tourism_user -d tourism_guide -c "\dt"
```

### 4.4 Environment Configuration

Create `.env` file in project root:

```env
# ============================================
# Database Configuration
# ============================================
DATABASE_URL=postgresql://tourism_user:secure_password_123@localhost:5432/tourism_guide

# ============================================
# API Configuration
# ============================================
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=True
API_RELOAD=True

# ============================================
# LLM Configuration
# ============================================
LLM_MODEL_PATH=./models/Llama-3.2-1B-Instruct-Q5_K_M.gguf
LLM_N_CTX=2048
LLM_N_BATCH=512
LLM_N_GPU_LAYERS=0        # Change to 30+ if using NVIDIA GPU
LLM_VERBOSE=False

# ============================================
# Embeddings Configuration
# ============================================
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
EMBEDDING_BATCH_SIZE=32

# ============================================
# Vector Database Configuration
# ============================================
CHROMA_DB_PATH=./vector_store
CHROMA_PERSIST_DIRECTORY=./vector_store/docs_index

# ============================================
# CORS Configuration
# ============================================
CORS_ORIGINS=["http://localhost:5173","http://localhost:3000","http://localhost:8000"]

# ============================================
# Logging Configuration
# ============================================
LOG_LEVEL=INFO
LOG_FORMAT=json
```

### 4.5 Download LLM Model

The Llama model is required for the chatbot to function. Download it manually:

```bash
# Create models directory
mkdir -p models

# Download the model (approx 869 MB)
# Option 1: Using wget
cd models
wget https://huggingface.co/lmstudio-community/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q5_K_M.gguf
cd ..

# Option 2: Using curl
curl -L -o models/Llama-3.2-1B-Instruct-Q5_K_M.gguf \
  https://huggingface.co/lmstudio-community/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q5_K_M.gguf

# Verify download
ls -lh models/
```

### 4.6 Start Backend Server

```bash
# Activate virtual environment (if not already active)
# Windows: .\.venv\Scripts\Activate.ps1
# Linux/Mac: source .venv/bin/activate

# Start Uvicorn server
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# Expected output:
# INFO:     Uvicorn running on http://0.0.0.0:8000
# INFO:     Application startup complete.
```

### 4.7 Verify Backend

```bash
# Open new terminal and test API
curl http://localhost:8000/health

# Expected response:
# {"status":"ok","timestamp":"2026-06-04T10:30:00Z"}

# Access API documentation
# Open browser: http://localhost:8000/docs
```

---

## 5. Frontend Setup

### 5.1 Install Node Dependencies

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Verify installation
npm list | head -20
```

### 5.2 Environment Configuration

Create `frontend/.env.local`:

```env
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000
VITE_DEBUG=true
```

### 5.3 Start Frontend Development Server

```bash
# From frontend directory
npm run dev

# Expected output:
#   VITE v7.3.1  ready in 2495 ms
#   ➜  Local:   http://localhost:5173/
#   ➜  Network: use --host to expose
```

### 5.4 Access Application

Open browser and navigate to:
```
http://localhost:5173
```

---

## 6. Knowledge Base Population

### 6.1 Add Tourism Documents

Create documents in the `docs/destinations/` directory:

```bash
# Create example document
mkdir -p docs/destinations

# Create a markdown file
cat > docs/destinations/taj-mahal.md << 'EOF'
# Taj Mahal

## Overview
Taj Mahal is one of the most iconic monuments in India, located in Agra.

## Best Time to Visit
- October to March
- Avoid summer (April-June)

## Entry Fees
- Indian citizens: ₹50
- Foreign tourists: $20 USD

## Opening Hours
- 6:00 AM to 7:00 PM daily
- Closed on Fridays for prayers

## Nearby Attractions
- Agra Fort
- Mehtab Bagh
- Itmad-ud-Daulah's Tomb

[More details...]
EOF
```

### 6.2 Automatic Indexing

Documents in `docs/` directory are automatically indexed on backend startup. To verify:

```bash
# Check API for indexed documents
curl http://localhost:8000/api/documents

# Expected: List of indexed documents with metadata
```

### 6.3 Add Documents via UI

1. Open http://localhost:5173
2. Click "Upload documents" button
3. Select PDF or Markdown files
4. Monitor upload progress
5. System automatically indexes files

---

## 7. Testing the System

### 7.1 Test Backend API

```bash
# Health check
curl http://localhost:8000/health

# Send chat message
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Tell me about Taj Mahal",
    "mode": "rag"
  }'

# List documents
curl http://localhost:8000/api/documents

# Access API docs
# Open: http://localhost:8000/docs
```

### 7.2 Test Frontend

1. Open http://localhost:5173
2. Type: "What are the top attractions in Goa?"
3. Select "RAG Mode"
4. Click Send
5. Observe streaming response

### 7.3 Test Document Upload

1. Create a test document (test.md)
2. Click "Upload documents"
3. Select test.md
4. Wait for upload completion
5. Ask question about uploaded content

---

## 8. Production Deployment

### 8.1 Build Frontend

```bash
cd frontend

# Build production bundle
npm run build

# Output in frontend/dist/
ls -la dist/
```

### 8.2 Backend Deployment

```bash
# Option 1: Using Gunicorn
pip install gunicorn

gunicorn backend.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --access-logfile - \
  --error-logfile -

# Option 2: Using Docker (if available)
docker build -t tourism-guide:latest .
docker run -p 8000:8000 tourism-guide:latest
```

### 8.3 Nginx Configuration (Optional)

Create `nginx.conf`:

```nginx
upstream backend {
    server localhost:8000;
}

upstream frontend {
    server localhost:5173;
}

server {
    listen 80;
    server_name tourism-guide.example.com;

    # Frontend
    location / {
        proxy_pass http://frontend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
    }

    # Backend API
    location /api {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
    }

    # WebSocket
    location /api/chat/stream {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

---

## 9. Troubleshooting

### 9.1 Common Issues

**Issue: Module not found (llama_cpp_python)**
```bash
# Solution: Reinstall with build tools
pip uninstall llama_cpp_python -y
pip install --no-cache-dir llama_cpp_python
```

**Issue: PostgreSQL connection refused**
```bash
# Solution: Check if service is running
# Windows:
net start postgresql-x64-15

# Linux:
sudo systemctl status postgresql

# macOS:
brew services list
```

**Issue: Port already in use**
```bash
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux:
lsof -i :8000
kill -9 <PID>
```

**Issue: Model file not found**
```bash
# Solution: Verify model path
ls -la models/Llama-3.2-1B-Instruct-Q5_K_M.gguf

# If missing, download again (see section 4.5)
```

### 9.2 Performance Issues

**LLM Inference Slow**
- Increase GPU layers: `LLM_N_GPU_LAYERS=30` (if GPU available)
- Reduce context: `LLM_N_CTX=1024`
- Enable quantization (already using Q5_K_M)

**Memory Usage High**
- Reduce batch size: `LLM_N_BATCH=256`
- Reduce embedding batch: `EMBEDDING_BATCH_SIZE=16`
- Close unnecessary applications

---

## 10. Monitoring & Logs

### 10.1 View Backend Logs

```bash
# Real-time logs
tail -f backend.log

# Filter by level
grep "ERROR" backend.log

# View last 100 lines
tail -100 backend.log
```

### 10.2 Database Monitoring

```bash
# Check database size
psql -U tourism_user -d tourism_guide -c "SELECT pg_size_pretty(pg_database_size('tourism_guide'));"

# View active connections
psql -U tourism_user -d tourism_guide -c "SELECT * FROM pg_stat_activity;"

# Backup database
pg_dump -U tourism_user tourism_guide > backup_$(date +%Y%m%d_%H%M%S).sql
```

### 10.3 Vector DB Monitoring

```bash
# Check ChromaDB storage
du -sh vector_store/

# View collection stats
python -c "
import chromadb
client = chromadb.PersistentClient(path='vector_store')
collection = client.get_collection(name='documents')
print(f'Total embeddings: {collection.count()}')
"
```

---

## 11. Maintenance Tasks

### 11.1 Regular Backups

```bash
# Automated daily backup
cat > backup.sh << 'EOF'
#!/bin/bash
BACKUP_DIR="./backups"
mkdir -p $BACKUP_DIR
pg_dump -U tourism_user tourism_guide | gzip > \
  $BACKUP_DIR/backup_$(date +%Y%m%d_%H%M%S).sql.gz
EOF

chmod +x backup.sh
./backup.sh
```

### 11.2 Update Dependencies

```bash
# Check for updates
pip list --outdated

# Update specific package
pip install --upgrade <package_name>

# Update all packages (use with caution)
pip install --upgrade -r requirements.txt
```

### 11.3 Clear Cache & Logs

```bash
# Clear old logs
find . -name "*.log" -mtime +30 -delete

# Clear ChromaDB cache
rm -rf vector_store/__pycache__

# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +
```

---

## 12. Performance Optimization

### 12.1 Backend Optimization

```python
# backend/core/config.py

class Settings:
    # Connection pooling
    DB_POOL_SIZE = 10
    DB_MAX_OVERFLOW = 20
    
    # LLM optimization
    LLM_N_BATCH = 512          # Larger batch for speed
    LLM_N_GPU_LAYERS = 30      # Use GPU if available
    
    # Cache settings (future)
    CACHE_TTL = 3600           # 1 hour
    MAX_CACHE_SIZE = 1000      # Items
```

### 12.2 Frontend Optimization

```bash
# Build with optimizations
npm run build

# Analyze bundle size
npm run build -- --analyze

# Enable gzip compression (nginx)
gzip on;
gzip_types text/plain text/css application/json;
```

---

## 13. Checklist

### Pre-Deployment
- [ ] All dependencies installed
- [ ] Environment variables set
- [ ] Database initialized and migrated
- [ ] Model file downloaded
- [ ] Backend tests passing
- [ ] Frontend builds successfully
- [ ] API endpoints responding
- [ ] WebSocket connections working

### Post-Deployment
- [ ] Health checks passing
- [ ] Documents indexed
- [ ] Chat functionality working
- [ ] Response streaming working
- [ ] Error handling functional
- [ ] Logs being recorded
- [ ] Performance acceptable
- [ ] Backups configured

---

**Document Version**: 1.0  
**Last Updated**: June 2026  
**Author**: N. Uma Devi  
**Faculty Guide**: Chakradhar Rao
