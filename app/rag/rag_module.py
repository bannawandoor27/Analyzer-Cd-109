from rag.query_engine import QueryEngine
from utils.logger import logger

class RAGModule:
    def __init__(self):
        self.query_engine = QueryEngine()

    async def analyze_log(self, log_message):
        prompt = (
            "Analyze the following error log in detail. Provide:\n\n"
            "1. A concise restatement of the issue described by the log message.\n"
            "2. A technical breakdown of the potential causes, including any relevant background information.\n"
            "3. Step-by-step solutions or troubleshooting steps for resolving the issue, with code examples if applicable.\n"
            "4. Suggestions for preventive measures or best practices to avoid similar issues in the future.\n\n"
            f"Log Message: {log_message}\n\n"
            "Ensure that the response is precise, thorough, and includes actionable insights and solutions."
        )
        response = await self.query_engine.aquery(prompt)
        return response
