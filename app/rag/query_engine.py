from config import Config
from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI

class QueryEngine:
    def __init__(self):
        if Config.RAG_MODEL_PROVIDER == "Ollama":
            self.llm = Ollama(model="llama3.2:1b", request_timeout=600)
        else:
            self.llm = OpenAI(model="gpt-4", api_key="YOUR_OPENAI_API_KEY")

    async def aquery(self, prompt):
        return await self.llm.aquery(prompt)
