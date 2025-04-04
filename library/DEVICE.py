import threading
import LEDs
import smbus
import time

# Alias for time
delay = time.sleep
# End alias for time

# Khởi tạo bus I2C
bus = smbus.SMBus(1)

# Địa chỉ I2C của PCF điều khiển LED
I2C_ADDR = 0x22

bus.write_byte(I2C_ADDR, 0xF0)

# devices init
DOT = 0x01
FAN = 0x04
BUZZER = 0x08

state = 0xF0

def set(dev):
    global state

    state = state | dev
    bus.write_byte(I2C_ADDR, state)

def reset(dev):
    global state

    state = state & ~dev
    bus.write_byte(I2C_ADDR, state)

def read():
    global state
    
    # Thiết lập chân INPUT ở mức cao (High impedance)
    # Lúc này, trạng thái của chân sẽ phụ thuộc vào điều khiển của công tắc và nút nhấn
    state = 0xF0 | state 
    bus.write_byte(I2C_ADDR, state)

    data = bus.read_byte(I2C_ADDR)
    return (data & 0xF0) >> 4  # Chỉ lấy bit 4-7