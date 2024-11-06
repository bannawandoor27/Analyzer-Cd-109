import pika
import json
from services.log_analyzer import LogAnalyzer
from config import Config
from utils.logger import logger

class RabbitMQListener:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.URLParameters(Config.RABBITMQ_URL))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="log_queue")

    def start_listening(self):
        self.channel.basic_consume(queue="log_queue", on_message_callback=self.on_message, auto_ack=True)
        logger.info("Listening to RabbitMQ queue for log messages.")
        self.channel.start_consuming()

    def on_message(self, ch, method, properties, body):
        message = json.loads(body)
        log_id = message.get("log_id")
        if log_id:
            logger.info(f"Received log ID: {log_id}")
            log_analyzer = LogAnalyzer()
            log_analyzer.process_log(log_id)
        else:
            logger.warning("Received message without log_id.")
