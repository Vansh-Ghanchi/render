import os
import chromadb
from sentence_transformers import SentenceTransformer

_model = None
_collection = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer('all-MiniLM-L6-v2')
    return _model

def get_collection():
    global _collection
    if _collection is None:
        client = chromadb.PersistentClient(path="./chroma_store")
        _collection = client.get_or_create_collection("course_materials")
    return _collection

def load_all_docs(folder="./docs"):
    collection = get_collection()
    existing = collection.get()
    if existing["ids"] and len(existing["ids"]) > 0:
        print("Documents already exist in collection. Skipping re-Indexing.")
        return

    for filename in os.listdir(folder):
        if not filename.endswith(".txt"):
            continue
        with open(os.path.join(folder, filename), "r", encoding="utf-8") as f:
            text = f.read()


        chunks = []
        i = 0
        while i < len(text):
            chunk = text[i : i+400]
            chunks.append(chunk)
            i += 400
        
        model = get_model()
        embeddings = model.encode(chunks).tolist()
        collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=[f"{filename}_{j}" for j in range(len(chunks))]
        )



def retrieve(query: str, n=3) -> str:
    model = get_model()
    collection = get_collection()
    query_emb = model.encode([query]).tolist()
    results = collection.query(query_embeddings=query_emb, n_results=n)
    if not results or not results["documents"] or not results["documents"][0]:
        return ""
    return "\n\n".join(results["documents"][0])