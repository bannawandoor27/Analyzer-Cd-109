import os
from enum import Enum

class ModelProvider(Enum):
    """Enum to define available LLM providers."""
    OPENAI = "OpenAI"
    OLLAMA = "Ollama"
    ANTHROPIC = "Anthropic"

class OpenAIModels(Enum):
    """Enum for OpenAI-specific models."""
    GPT_4o = "gpt-4o"
    GPT_4o_MINI = "gpt-4o-mini" 

class OllamaModels(Enum):
    """Enum for Ollama-specific models."""
    LLAMA_3_2 = "llama3.2:latest"
    # Add other Ollama models here as needed

class AnthropicModels(Enum):
    """Enum for Anthropic-specific models."""
    CLAUDE_V1 = "claude-v1"
    CLAUDE_V2 = "claude-v2"
    # Add other Anthropic models here as needed

class Config:
    RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    RAG_MODEL_PROVIDER = os.getenv("RAG_MODEL_PROVIDER", ModelProvider.OLLAMA.value)
    RAG_MODEL = os.getenv("RAG_MODEL",OllamaModels.LLAMA_3_2.value)
    OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY", None)

    @staticmethod
    def get_model_choices():
        """Returns the model choices based on the selected provider."""
        if Config.RAG_MODEL_PROVIDER == ModelProvider.OPENAI.value:
            return [model.value for model in OpenAIModels]
        elif Config.RAG_MODEL_PROVIDER == ModelProvider.OLLAMA.value:
            return [model.value for model in OllamaModels]
        elif Config.RAG_MODEL_PROVIDER == ModelProvider.ANTHROPIC.value:
            return [model.value for model in AnthropicModels]
        else:
            raise ValueError(f"Unsupported model provider: {Config.RAG_MODEL_PROVIDER}")

# Usage
if __name__ == "__main__":
    # Prints the available model choices based on the selected provider
    print("Model Provider:", Config.RAG_MODEL_PROVIDER)
    print("Available Models:", Config.get_model_choices())
