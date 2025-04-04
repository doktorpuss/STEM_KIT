import DEVICE

def on():
    DEVICE.set(DEVICE.BUZZER)

def off():
    DEVICE.reset(DEVICE.BUZZER)