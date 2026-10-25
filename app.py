from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch




##Example usage

if __name__ == "__main__":
    # pipeline = EmbeddingPipeline()
    # docs = load_all_documents("data")
    # chunks = pipeline.chunk_documents(docs)
    # vectors = pipeline.embed_chunks(chunks)

    # print(type(vectors))
    # print(vectors.shape)
    
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)
    store.load()
    # print(store.query("What is attention mechanism?", top_k=3))
    
    rag_search = RAGSearch()
    query = "What is attention mechanism?"
    summary = rag_search.search_and_summarize(query, top_k = 3)
    print("Summary:", summary)
    