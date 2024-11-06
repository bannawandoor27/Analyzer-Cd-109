import os

class Config:
    RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    RAG_MODEL_PROVIDER = os.getenv("RAG_MODEL_PROVIDER", "Ollama")  # Can be "Ollama" or "OpenAI"
