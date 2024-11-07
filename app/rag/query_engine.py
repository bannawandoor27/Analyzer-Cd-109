from vector_index.vector_index_service import VectorIndexService
from config import Config
from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI
from utils.logger import logger

class QueryEngine:
    def __init__(self):
        self.llm = self._initialize_llm()
        self.vector_index = VectorIndexService(codebase_directory=Config.CODEBASE_DIRECTORY).index

    def _initialize_llm(self):
        try:
            if Config.RAG_MODEL_PROVIDER == "Ollama":
                logger.info("Initializing Ollama model.")
                return Ollama(model="llama3.2:latest", request_timeout=600)
            elif Config.RAG_MODEL_PROVIDER == "OpenAI":
                if not Config.OPEN_AI_API_KEY:
                    raise ValueError("OPEN_AI_API_KEY is not set in environment.")
                logger.info("Initializing OpenAI model.")
                return OpenAI(model="gpt-4o-mini", api_key=Config.OPEN_AI_API_KEY)
            else:
                raise ValueError(f"Unsupported model provider: {Config.RAG_MODEL_PROVIDER}")
        except Exception as e:
            logger.error(f"Error initializing LLM: {e}")
            raise

    async def aquery(self, prompt):
        logger.info(f"Executing async query with prompt: {prompt}")
        try:
            response = await self.vector_index.as_query_engine(llm=self.llm).aquery(prompt)
            logger.info("Query completed successfully.")
            return response
        except Exception as e:
            logger.error(f"Query execution failed: {e}")
            raise
