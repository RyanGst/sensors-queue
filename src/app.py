import logging
import json
import time
from src.start_queue import start_queue
from src.sensor_reader import read_sensor

QUEUE_NAME = 'sensor_data'
DEFAULT_DELAY = 2

def app():
    logging.info("Starting app")
    connection = start_queue()
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    
    while True:
        message = read_sensor()
        channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=json.dumps(message))
        logging.info(f"Sent message: {json.dumps(message)}")
        time.sleep(DEFAULT_DELAY)

if __name__ == "__main__":
    app()
