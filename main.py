import time
from sensor import read_dht
from control import setup_pump,turn_on_pump, turn_off_pump, cleanup
from LCD import show_status, show_error

pump_status = "OFF"

try:
    setup_pump()
    while True:
        humidity, temperature = read_dht()

        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature}C | Humidity: {humidity}%")

            if humidity < 50 and pump_status == "OFF":
                turn_on_pump()
                pump_status = "ON"
            elif humidity >= 60 and pump_status == "ON":
                turn_off_pump()
                pump_status = "OFF"

            show_status(temperature, humidity, pump_status)
        else:
            show_error()

        time.sleep(5)

except KeyboardInterrupt:
    turn_off_pump()
    print("ระบบหยุดแล้ว")

finally:
    cleanup()
