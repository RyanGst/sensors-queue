from src.sensor_reader import read_sensor
import logging

logging.basicConfig(level=logging.INFO)

def app():
    logging.info("Starting app")
    read_sensor()
    logging.info("App finished")

if __name__ == "__main__":
    app()
