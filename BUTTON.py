import DEVICE

def read_button(button):
    buf = DEVICE.read()
    buf = (buf >> (2-button)) & 0x01
    return buf
