from abc import ABC, abstractmethod
from typing import List, Union
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModel
import torch


class EmbeddingGenerator(ABC):
    """
    Abstract base class for generating embeddings for input text.
    
    Derived classes must implement the `generate_embedding` method to return the
    vector representation of the input text.
    """
    @abstractmethod
    def generate_embedding(self, text: str) -> List[float]:
        """
        Generates an embedding for the given text.
        
        Args:
            text (str): The input text to be converted to embedding.
        
        Returns:
            List[float]: The generated embedding as a list of floats.
        """
        pass


class SentenceBERTEmbeddingGenerator(EmbeddingGenerator):
    """
    Generates embeddings using the Sentence-BERT model.
    """
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """
        Initializes the Sentence-BERT model.
        
        Args:
            model_name (str): The model name to load from Sentence-Transformers.
        """
        try:
            self.model = SentenceTransformer(model_name)
        except Exception as e:
            raise RuntimeError(f"Error loading Sentence-BERT model: {e}")
    
    def generate_embedding(self, text: str) -> List[float]:
        """
        Generates an embedding using Sentence-BERT.
        
        Args:
            text (str): The input text to be converted to embedding.
        
        Returns:
            List[float]: The generated embedding as a list of floats.
        """
        try:
            return self.model.encode(text).tolist()
        except Exception as e:
            raise RuntimeError(f"Error generating embedding using Sentence-BERT: {e}")


class HuggingFaceEmbeddingGenerator(EmbeddingGenerator):
    """
    Generates embeddings using the Hugging Face BERT model.
    """
    def __init__(self, model_name: str = 'bert-base-uncased'):
        """
        Initializes the Hugging Face model and tokenizer.
        
        Args:
            model_name (str): The pre-trained model name for Hugging Face.
        """
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModel.from_pretrained(model_name)
        except Exception as e:
            raise RuntimeError(f"Error loading Hugging Face model: {e}")
    
    def generate_embedding(self, text: str) -> List[float]:
        """
        Generates an embedding using Hugging Face's BERT model.
        
        Args:
            text (str): The input text to be converted to embedding.
        
        Returns:
            List[float]: The generated embedding as a list of floats.
        """
        try:
            inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
            with torch.no_grad():
                outputs = self.model(**inputs)
            # Mean of the last hidden state to create a fixed-size vector
            return outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
        except Exception as e:
            raise RuntimeError(f"Error generating embedding using Hugging Face BERT: {e}")


class EmbeddingFactory:
    """
    Factory class to instantiate embedding generators based on model type.
    """
    @staticmethod
    def get_embedding_generator(model_type: str) -> EmbeddingGenerator:
        """
        Factory method to create an instance of the requested embedding generator.
        
        Args:
            model_type (str): The type of embedding model ('sentence_bert', 'huggingface_bert').
        
        Returns:
            EmbeddingGenerator: An instance of the appropriate embedding generator class.
        
        Raises:
            ValueError: If the requested model type is not supported.
        """
        if model_type == 'sentence_bert':
            return SentenceBERTEmbeddingGenerator()
        elif model_type == 'huggingface_bert':
            return HuggingFaceEmbeddingGenerator()
        else:
            raise ValueError(f"Unsupported embedding model type: '{model_type}'. Choose from ['sentence_bert', 'huggingface_bert'].")


# Example usage
if __name__ == "__main__":
    # Define the model type (could be 'sentence_bert' or 'huggingface_bert')
    model_type = 'sentence_bert'  # Change this to 'huggingface_bert' to use Hugging Face BERT

    try:
        # Factory creates the appropriate embedding generator based on the model type
        embedding_generator = EmbeddingFactory.get_embedding_generator(model_type)
        
        # Example input text
        input_text = "Retrieval-augmented generation is a powerful concept in NLP."
        
        # Generate the embedding
        embedding = embedding_generator.generate_embedding(input_text)
        
        # Output the embedding (or use it for downstream tasks)
        print(f"Generated embedding: {embedding[:10]}...")  # Print the first 10 values for readability
    except ValueError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")
