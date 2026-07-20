import chromadb
from sentence_transformers import SentenceTransformer

# ---------------------------------
# Load Embedding Model
# ---------------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------------------------
# Sample Chunks
# (Later these will come from your PDF)
# ---------------------------------
chunks = [
    "Operating System is system software.",
    "CPU Scheduling decides which process gets CPU.",
    "Deadlock occurs when two processes wait forever."
]

# ---------------------------------
# Generate Embeddings
# ---------------------------------
embeddings = model.encode(chunks)

# ---------------------------------
# Create ChromaDB Client
# ---------------------------------
client = chromadb.Client()

# ---------------------------------
# Create Collection
# ---------------------------------
collection = client.create_collection("pdf_chunks")

# ---------------------------------
# Store Chunks in ChromaDB
# ---------------------------------
collection.add(
    embeddings=embeddings.tolist(),
    documents=chunks,
    ids=["1", "2", "3"]
)

# ---------------------------------
# User Question
# ---------------------------------
query = "What is Deadlock?"

# ---------------------------------
# Convert Question into Embedding
# ---------------------------------
query_embedding = model.encode(query)

# ---------------------------------
# Search Similar Chunks
# ---------------------------------
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)

# ---------------------------------
# Print Retrieved Chunks
# ---------------------------------
print("Retrieved Chunks:\n")

for doc in results["documents"][0]:
    print(doc)
    print()

# ---------------------------------
# Combine Retrieved Chunks
# ---------------------------------
context = "\n".join(results["documents"][0])

# ---------------------------------
# Create Prompt
# ---------------------------------
prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}
"""

print("=" * 50)
print("Prompt Sent to LLM")
print("=" * 50)

print(prompt)