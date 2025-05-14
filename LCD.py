from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)  # ✅ ใช้ address เดียวกับ lcd_test.py

def show_status(temperature, humidity, pump_status):
    lcd.clear()
    lcd.write_string(f"Temp: {temperature}C")
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"Hum:{humidity}% Pump:{pump_status}")

def show_error():
    lcd.clear()
    lcd.write_string("Sensor Error")
