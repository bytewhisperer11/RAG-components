from langchain_huggingface.embeddings import HuggingFaceEmbeddings

# Load a public embedding model that does not require authentication
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

text = "This is a test document."
embedding_vector = embeddings.embed_query(text)

print(embedding_vector[:5])  # Print first 5 dimensions
