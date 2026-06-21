from src.embeddings.embedder import generate_embedding

text = "AWS DevOps Engineer"

embedding = generate_embedding(text)

print(type(embedding))
print(len(embedding))