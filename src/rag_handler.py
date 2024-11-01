# src/rag_handler.py
import logging
from llama_index.core import VectorStoreIndex
from utils.file_loader import load_codebase_documents

logger = logging.getLogger(__name__)

def build_semantic_search_index(codebase_directory):
    """
    Build an in-memory semantic search index for the codebase files.
    
    :param codebase_directory: Path to the directory containing codebase files.
    :return: A query engine for semantic search.
    """
    try:
        # Step 1: Load documents
        logger.info(f"Loading documents from directory: {codebase_directory}")
        documents = load_codebase_documents(codebase_directory)
        if not documents:
            logger.warning("No documents found in the codebase directory.")
            return None
        
        # Step 2: Create the semantic search index
        logger.info("Creating semantic search index from loaded documents.")
        index = VectorStoreIndex.from_documents(documents)
        if not index:
            logger.error("Failed to create an index. `VectorStoreIndex.from_documents` returned None.")
            return None
        
        logger.info("Semantic search index built successfully.")
        logger.debug(f"Index details: {index}")
        
        # Step 3: Create and return the query engine
        query_engine = index.as_query_engine()
        if not query_engine:
            logger.error("Failed to initialize query engine from the index.")
            return None
        
        logger.info("Query engine initialized successfully.")
        return query_engine
    except Exception as e:
        logger.critical(f"Failed to build semantic search index: {e}", exc_info=True)
        return None


def query_semantic_search(query_engine, query_text):
    """
    Query the semantic search index with a specific question and retrieve a response.
    
    :param query_engine: The query engine for the semantic search index.
    :param query_text: The question or query string.
    :return: Response text from the query engine.
    """
    if not query_engine:
        logger.error("Query engine is not available for querying.")
        return "Error: Query engine not available."

    try:
        response = query_engine.query(query_text)
        logger.info("Query executed successfully.")
        return response
    except Exception as e:
        logger.error(f"Error querying semantic search index: {e}")
        return "Error: Failed to retrieve response from index."
