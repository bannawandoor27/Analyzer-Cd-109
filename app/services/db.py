from pymongo import MongoClient
from config import Config
from utils.logger import logger

class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client["log_database"]
        self.collection = self.db["logs"]

    def fetch_log(self, log_id):
        return self.collection.find_one({"_id": log_id})

    def update_log(self, log_id, analysis_result):
        result = self.collection.update_one(
            {"_id": log_id}, {"$set": {"analysis": analysis_result}}
        )
        logger.info(f"Updated log ID {log_id} with analysis result.")
