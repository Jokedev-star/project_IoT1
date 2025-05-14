import RPi.GPIO as GPIO

PUMP_PIN = 18  # ขาที่ควบคุม relay

def setup_pump():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PUMP_PIN, GPIO.OUT)
    GPIO.output(PUMP_PIN, GPIO.LOW)

def turn_on_pump():
    GPIO.output(PUMP_PIN, GPIO.HIGH)

def turn_off_pump():
    GPIO.output(PUMP_PIN, GPIO.LOW)

def cleanup():
    GPIO.output(PUMP_PIN, GPIO.LOW)
    GPIO.cleanup()
