import board
import adafruit_dht

dht_device = adafruit_dht.DHT11(board.D4)

def read_dht():
    try:
        humidity = dht_device.humidity
        temperature = dht_device.temperature
        return humidity, temperature
    except:
        return None, None
