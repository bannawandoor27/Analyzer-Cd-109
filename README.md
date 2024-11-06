# Log Analyzer Service

This service listens to a RabbitMQ queue for new log IDs, fetches log data from MongoDB, analyzes it using a RAG module, and updates the analysis result in MongoDB.

## Setup Instructions

1. Set up MongoDB, RabbitMQ, and configure `.env` file as necessary.
2. Build and run the Docker container:

    ```bash
    docker build -t log-analyzer-service .
    docker run -d log-analyzer-service
    ```

3. Environment variables are configured in `app/config.py`.

## Project Structure

... (Add detailed structure information here) ...
