import Adafruit_DHT
import time

# กำหนดชนิดเซ็นเซอร์และขา GPIO
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # เปลี่ยนเป็น GPIO ที่คุณต่อ DATA ไว้ เช่น GPIO4 (ขา 7)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print(f"อุณหภูมิ: {temperature:.1f}°C | ความชื้น: {humidity:.1f}%")
    else:
        print("อ่านค่าจากเซ็นเซอร์ไม่สำเร็จ ลองอีกครั้ง...")

    time.sleep(2)  # หน่วงเวลา 2 วินาที
