from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

chunks = [
    "Operating System is system software.",
    "CPU Scheduling decides which process gets CPU.",
    "Deadlock occurs when two processes wait forever."
]

embeddings = model.encode(chunks)

print("Total Chunks:", len(chunks))
print("Total Embeddings:", len(embeddings))
print("Embedding Size:", len(embeddings[0]))

print("\nFirst Embedding (first 10 values):")
print(embeddings[0][:10])