# src/utils/file_loader.py
import os
from llama_index.core import Document
import logging

logger = logging.getLogger(__name__)

def load_codebase_documents(directory_path):
    """
    Reads all text files in a directory and loads them as Document objects.
    
    :param directory_path: Path to the directory containing code files.
    :return: A list of Document objects.
    """
    documents = []
    try:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith(".txt") or file.endswith(".py"):  # Adjust extensions as needed
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        documents.append(Document(text=content, doc_id=file_path))
                        logger.info(f"Loaded document from {file_path}")
    except Exception as e:
        logger.error(f"Failed to load documents from directory {directory_path}: {e}")
    
    if not documents:
        logger.warning("No documents were loaded from the directory.")
    return documents
