import chromadb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

chunks = [
    "Operating System is system software.",
    "CPU Scheduling decides which process gets CPU.",
    "Deadlock occurs when two processes wait forever."
]

embeddings = model.encode(chunks)

client = chromadb.Client()

collection = client.create_collection("pdf_chunks")

collection.add(
    embeddings=embeddings.tolist(),
    documents=chunks,
    ids=["1","2","3"]
)

query = "Explain Deadlock"

query_embedding = model.encode(query)

results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=1
)

print(results["documents"])