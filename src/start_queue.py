import pika
import logging

logging.basicConfig(level=logging.INFO)

def start_queue():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    
    logging.info("Connected to queue")
    
    return connection

