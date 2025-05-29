import logging
import random

logging.basicConfig(level=logging.INFO)

logging.info("Fake Temperature and Humidity Sensor")

def read_fake_sensor() -> tuple[float, float]:
    return random.randint(20, 30), random.randint(40, 50)