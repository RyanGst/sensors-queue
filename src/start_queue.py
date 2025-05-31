import os
import pika
import logging

logging.basicConfig(level=logging.INFO)

def start_queue():
    host = os.environ.get('RABBITMQ_HOST')
    port = os.environ.get('RABBITMQ_PORT', 5672)
    username = os.environ.get('RABBITMQ_USERNAME', 'guest')
    password = os.environ.get('RABBITMQ_PASSWORD', 'guest')

    credentials = pika.PlainCredentials(username, password)
    connection_parameters = pika.ConnectionParameters(host, port, credentials=credentials)
    connection = pika.BlockingConnection(connection_parameters)
    
    logging.info("Connected to queue")
    
    return connection

