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

# devices init
DOT = 0x80
FAN = 0x20
BUZZER = 0x10

state = 0x0

try:
    LEDs.clear()
    bus.write_byte(I2C_ADDR, 0xFF)
    while True:
        pass
    
except KeyboardInterrupt:
    bus.write_byte(I2C_ADDR, 0x00)
    print("STOP")