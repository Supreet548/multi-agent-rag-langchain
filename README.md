# Multi-Agent RAG System

A Multi-Agent Retrieval-Augmented Generation (RAG) system built using LangChain, Google Gemini, and ChromaDB.

The application ingests PDF documents, stores embeddings in a vector database, and uses specialized agents to answer user questions.

## Features

* PDF Document Ingestion
* Chroma Vector Database
* Google Gemini LLM
* Google Embeddings
* Retrieval-Augmented Generation (RAG)
* Supervisor Agent Routing
* Multiple Specialized Agents

## Architecture

```text
User Query
    │
    ▼
Supervisor Agent
    │
    ├── Definition Agent
    ├── Code Agent
    └── Troubleshooting Agent
            │
            ▼
         Retriever
            │
            ▼
         ChromaDB
            │
            ▼
      PDF Documents
```

## Project Structure

```text
app/
├── agents/
├── models/
├── rag/
├── config/
└── main.py

data/
├── sample.pdf

.env.example
requirements.txt
README.md
```

## Setup

### Clone Repository

```bash
git clone <repository-url>
cd multi-agent-rag-langchain
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
MODEL_CHAT=gemini-2.5-flash
MODEL_EMBED=models/embedding-001
```

## Build Vector Database

```bash
python -m app.rag.ingest
```

## Run Application

```bash
python -m app.main
```

## Example Questions

```text
What is OAuth?

Show API request example.

What are the available endpoints?

Why am I getting 401 Unauthorized?
```

## Future Improvements

* LangGraph Integration
* FastAPI API Layer
* Agent Memory
* Multi-Document Support
* Streaming Responses
