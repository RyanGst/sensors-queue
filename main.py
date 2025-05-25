#!/usr/bin/env python3
# Fixed DHT11 reader for Raspberry Pi
import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18)

print("DHT11 Temperature and Humidity Sensor")
print("Press Ctrl+C to exit\n")

while True:
    try:
        # Read temperature and humidity
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        
        if temperature_c is not None and humidity is not None:
            temperature_f = temperature_c * (9 / 5) + 32
            print(f"Temp: {temperature_f:.1f}°F / {temperature_c:.1f}°C    Humidity: {humidity:.1f}%")
        else:
            print("Sensor returned None values")
            
    except RuntimeError as error:
        # DHT sensors are finicky, errors are common
        print(f"Reading error: {error.args[0]}")
        
    except Exception as error:
        print(f"Unexpected error: {error}")
        dhtDevice.exit()
        break
        
    time.sleep(2.0)  # DHT11 needs at least 2 seconds between reads