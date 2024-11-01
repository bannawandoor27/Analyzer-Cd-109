import websocket
import json
import logging.config
import yaml
from message_processor import process_message
from rag_handler import build_semantic_search_index

# Load logging configuration from YAML file
with open("config/logging.yaml", "r") as f:
    config = yaml.safe_load(f)
    logging.config.dictConfig(config)

# Initialize the logger
logger = logging.getLogger(__name__)

# Define the path to the codebase directory for indexing
CODEBASE_DIRECTORY = r"C:\Users\hasan\Desktop\works\rosterly_pegasus_backend"

class WebSocketClient:
    def __init__(self):
        """Initialize the WebSocket client and build the semantic search index."""
        try:
            logger.info("Building index for the codebase...")
            self.query_engine = build_semantic_search_index(CODEBASE_DIRECTORY)
            if self.query_engine is None:
                logger.critical("Query engine could not be initialized. Terminating client initialization.")
                raise ValueError("Query engine could not be initialized.")
            logger.info("Query engine initialized successfully.")
        except Exception as e:
            logger.critical(f"Failed to initialize query engine: {e}")
            raise

    def on_open(self, ws):
        """Log when WebSocket connection is opened."""
        logger.info("Connected to WebSocket server.")

    def on_message(self, ws, message):
        """Log and process the received message, querying the semantic search index."""
        logger.info("Received message from WebSocket server.")
        logger.debug(f"Raw message content: {message}")
        
        # Try to parse and process the message
        try:
            parsed_message = json.loads(message)
            logger.info("Message parsed successfully.")
            process_message(parsed_message, self.query_engine)
        except json.JSONDecodeError:
            logger.error("Failed to parse message as JSON.")
        except Exception as e:
            logger.error(f"Error processing message or querying index: {e}")

    def on_error(self, ws, error):
        """Log any WebSocket errors."""
        logger.error(f"WebSocket encountered an error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        """Log when WebSocket connection is closed."""
        logger.info(f"WebSocket connection closed with status: {close_status_code}, message: {close_msg}")

    def run(self):
        """Establish WebSocket connection and set up callbacks."""
        logger.info("Attempting to connect to WebSocket server...")
        ws = websocket.WebSocketApp(
            'ws://65.2.167.52:8080',
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        ws.run_forever()

# Initialize and run the WebSocket client
if __name__ == '__main__':
    logger.info("Starting WebSocket client.")
    try:
        client = WebSocketClient()
        client.run()
    except Exception as e:
        logger.critical(f"WebSocket client encountered a critical error: {e}")
