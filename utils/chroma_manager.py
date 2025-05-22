import chromadb
from google.genai import types

from config import CHROMA_COLLECTION_NAME, CHROMA_PERSIST_DIRECTORY, genai_client, EMBEDDING_MODEL_ID

chroma_client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIRECTORY)
collection = chroma_client.get_or_create_collection(name=CHROMA_COLLECTION_NAME)

def embed_document(text: str):
    result = genai_client.models.embed_content(
        model=EMBEDDING_MODEL_ID,
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT"
        )
    )
    return result.embeddings[0].values

def embed_query(text: str):
    result = genai_client.models.embed_content(
        model=EMBEDDING_MODEL_ID,
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        )
    )
    return result.embeddings[0].values

def add_to_chroma(chunks):
    for i, chunk in enumerate(chunks):
        embedding = embed_document(chunk)
        doc_id = f"doc_{i}"
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[{"source": "uploaded_file"}],
            ids=[doc_id] 
        )

def query_chroma(query, top_k=2):
    query_embedding = embed_query(query)
    results= collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results['documents'][0]

