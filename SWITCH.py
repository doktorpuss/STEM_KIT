import DEVICE

def read_switch(switch):
    buf = DEVICE.read()
    buf = (buf >> (2-switch)) & 0x01
    return buf
