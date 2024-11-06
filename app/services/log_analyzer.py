from rag.rag_module import RAGModule
from services.db import MongoDBClient
from utils.logger import logger

class LogAnalyzer:
    def __init__(self):
        self.db_client = MongoDBClient()
        self.rag_module = RAGModule()

    def process_log(self, log_id):
        log_data = self.db_client.fetch_log(log_id)
        if log_data:
            logger.info(f"Fetched log data for ID: {log_id}")
            analysis_result = self.rag_module.analyze_log(log_data["message"])
            logger.info(f"Analysis complete for log ID: {log_id}")
            self.db_client.update_log(log_id, analysis_result)
        else:
            logger.warning(f"No log data found for ID: {log_id}")
