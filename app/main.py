from services.rabbitmq_listener import RabbitMQListener
from utils.logger import logger

if __name__ == "__main__":
    logger.info("Starting Log Analyzer Service...")
    rabbitmq_listener = RabbitMQListener()
    rabbitmq_listener.start_listening()
