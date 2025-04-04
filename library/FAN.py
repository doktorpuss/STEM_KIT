import DEVICE

def on():
    DEVICE.set(DEVICE.FAN)

def off():
    DEVICE.reset(DEVICE.FAN)