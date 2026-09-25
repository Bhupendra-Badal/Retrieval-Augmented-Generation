# RAG Project

A simple Retrieval-Augmented Generation (RAG) project that loads documents, creates embeddings, stores them in ChromaDB, and retrieves relevant information for search and question answering.

## 📁 Project Structure

- `data/` — PDF and text documents
- `vector_store/` — ChromaDB vector database
- `notebook/` — Jupyter notebooks for experimentation
- `src/` — Core RAG modules
  - `data_loader.py` — Loads documents
  - `embedding.py` — Creates embeddings
  - `vectorstore.py` — Handles ChromaDB
  - `search.py` — Performs similarity search
- `app.py` — Main application
- `main.py` — Project entry point
- `requirements.txt` — Dependencies

## 🔄 RAG Pipeline

```text
Documents → Chunking → Embeddings → ChromaDB → Similarity Search
