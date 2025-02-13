import smbus
import time

# Alias for time
delay = time.sleep
# End alias for time

# Khởi tạo bus I2C
bus = smbus.SMBus(1)

# LEDs init
LEDs=[0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
LEDs_state=0x00
# END LEDs init

#LED state definition
LED_ON = 1
LED_OFF = 0
LED_TOGGLE = -1
#END LED state definition

# Địa chỉ I2C của PCF điều khiển led
I2C_ADDR = 0x20

def clear():
    global LEDs_state
    LEDs_state = 0x00
    bus.write_byte(I2C_ADDR,LEDs_state)

def update(num,mode):
    global LEDs_state

    if num > 8 or num < 1:
        print("\033[1;33mINVALID LED\033[0m")
        return
    
    if mode == LED_TOGGLE:
        LEDs_state = LEDs_state ^ LEDs[num-1]
    elif mode == LED_ON:
        LEDs_state = LEDs_state | LEDs[num-1]
    elif mode == LED_OFF:
        LEDs_state = LEDs_state & ~LEDs[num-1]
    else:
        print("\033[1;33mmode INVALID!!!\033[0m")
        return

    bus.write_byte(I2C_ADDR,LEDs_state)