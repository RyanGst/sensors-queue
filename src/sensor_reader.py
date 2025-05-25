#!/usr/bin/env python3
# Fixed DHT11 reader for Raspberry Pi
import time
import board
import adafruit_dht
import logging

logging.basicConfig(level=logging.INFO)

dhtDevice = adafruit_dht.DHT11(board.D18)

logging.info("DHT11 Temperature and Humidity Sensor")
logging.info("Press Ctrl+C to exit\n")

def read_sensor():
    while True:
        try:
            # Read temperature and humidity
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            
            if temperature_c is not None and humidity is not None:
                temperature_f = temperature_c * (9 / 5) + 32
                logging.info(f"Temp: {temperature_f:.1f}°F / {temperature_c:.1f}°C    Humidity: {humidity:.1f}%")
            else:
                logging.info("Sensor returned None values")
                
        except RuntimeError as error:
            logging.error(f"Reading error: {error.args[0]}")
            
        except Exception as error:
            logging.error(f"Unexpected error: {error}")
            dhtDevice.exit()
            break
            
        time.sleep(2.0)