import os
import pickle
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from utils.logger import logger

class VectorIndexService:
    def __init__(self, codebase_directory, index_file_path="vector_store_index.pkl"):
        self.codebase_directory = codebase_directory
        self.index_file_path = index_file_path
        self.index: VectorStoreIndex = self.load_or_create_index()

    def load_or_create_index(self):
        try:
            if os.path.exists(self.index_file_path):
                logger.info("Loading existing vector index from pickle file.")
                with open(self.index_file_path, "rb") as f:
                    return pickle.load(f)
            else:
                logger.info("Vector index pickle file not found. Creating a new index.")
                return self._create_and_store_index()
        except Exception as e:
            logger.error(f"Error loading or creating vector index: {e}")
            raise

    def _create_and_store_index(self):
        try:
            Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

            reader = SimpleDirectoryReader(input_dir=self.codebase_directory, recursive=True, required_exts=[".py"])
            documents = reader.load_data()

            index = VectorStoreIndex.from_documents(documents)

            with open(self.index_file_path, "wb") as f:
                pickle.dump(index, f)

            index.storage_context.persist()
            logger.info("Vector index created and stored successfully.")
            return index
        except Exception as e:
            logger.error(f"Error creating vector index: {e}")
            raise
