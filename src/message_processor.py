
import logging
from rag_handler import query_semantic_search

logger = logging.getLogger(__name__)

def process_message(parsed_message, query_engine):
    """
    Processes the parsed message and queries the semantic search index if required.
    
    :param parsed_message: Parsed message content as a dictionary.
    :param query_engine: The query engine for semantic search.
    """
    try:
        query_text = parsed_message.get("message", "No message field found")
        response = query_semantic_search(query_engine, query_text)
        logger.info(f"Processed message with response: {response}")
    except Exception as e:
        logger.error(f"Error processing message: {e}")
