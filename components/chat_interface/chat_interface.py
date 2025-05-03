from abc import ABC, abstractmethod
from langchain.chat_models import ChatOpenAI, ChatAnthropic
from config import OPENAI_API_KEY, OPENAI_TEMPERATURE, ANTHROPIC_API_KEY, ANTHROPIC_TEMPERATURE

# 1. Define the ChatModel interface
class ChatModel(ABC):
    @abstractmethod
    def chat(self, input_text: str) -> str:
        """Method to interact with the chat model."""
        pass

# 2. Concrete Class for OpenAI Chat Model
class OpenAIChatModel(ChatModel):
    def __init__(self):
        # Using separate config values for OpenAI
        self.model = ChatOpenAI(temperature=OPENAI_TEMPERATURE, api_key=OPENAI_API_KEY)

    def chat(self, input_text: str) -> str:
        """Interact with the OpenAI chat model."""
        return self.model.chat(input_text)

# 3. Concrete Class for Anthropic Chat Model
class AnthropicChatModel(ChatModel):
    def __init__(self):
        # Using separate config values for Anthropic
        self.model = ChatAnthropic(temperature=ANTHROPIC_TEMPERATURE, api_key=ANTHROPIC_API_KEY)

    def chat(self, input_text: str) -> str:
        """Interact with the Anthropic chat model."""
        return self.model.chat(input_text)

# 4. ChatFactory to choose the correct model
class ChatFactory:
    """
    Factory class to instantiate the correct chat model (OpenAI, Anthropic, etc.) based on the model name.
    """
    
    @staticmethod
    def get_chat_model(model_name: str) -> ChatModel:
        """
        Returns the correct ChatModel based on the model name.
        
        Args:
            model_name (str): Name of the model to be instantiated.
        
        Returns:
            ChatModel: The corresponding model object.
        """
        if model_name == "OpenAI":
            return OpenAIChatModel()
        elif model_name == "Anthropic":
            return AnthropicChatModel()
        else:
            raise ValueError(f"Unknown model: {model_name}")

# Example of usage
if __name__ == "__main__":
    # Choose the chat model (e.g., "OpenAI", "Anthropic")
    model_name = "OpenAI"

    # Get the model from the factory
    chat_model = ChatFactory.get_chat_model(model_name)

    # Interact with the model
    response = chat_model.chat("Hello, how are you?")
    print(response)
