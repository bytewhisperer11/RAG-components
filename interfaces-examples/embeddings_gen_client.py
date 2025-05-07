import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.embeddings.embedding_generator import EmbeddingFactory# Adjust path to match your project structure

def main():
    # Initialize embedding generator using factory
    embedder = EmbeddingFactory.get_embedding_generator(model_type='sentence_bert')
    print("Embedding model initialized.")

    # Input text
    text = "OpenAI builds foundational models for the future of AI."
    print(f"Input text: {text}")

    # Generate embedding vector
    vector = embedder.generate_embedding(text)
    print(f"Generated vector (first 5 dims): {vector[:5]}")

    # Optionally: inspect full dimension count
    print(f"Vector length: {len(vector)}")

if __name__ == "__main__":
    main()
