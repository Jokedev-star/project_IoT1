import time
from sensor import read_dht
from control import pump_on, pump_off
from LCD import show_status, show_error

pump_status = "OFF"

try:
    while True:
        humidity, temperature = read_dht()

        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature}C | Humidity: {humidity}%")

            if humidity < 50 and pump_status == "OFF":
                pump_on()
                pump_status = "ON"
            elif humidity >= 60 and pump_status == "ON":
                pump_off()
                pump_status = "OFF"

            show_status(temperature, humidity, pump_status)
        else:
            show_error()

        time.sleep(5)

except KeyboardInterrupt:
    pump_off()
    print("ระบบหยุดแล้ว")
