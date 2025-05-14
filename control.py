from gpiozero import OutputDevice

pump = OutputDevice(18) # ขาที่ควบคุม relay

def setup_pump():
    pass

def turn_on_pump():
    pump.on()

def turn_off_pump():
    pump.off()

def cleanup():
    pump.off()
