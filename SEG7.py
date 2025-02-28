import DEVICE
import threading
import smbus
import time

# Alias for time
delay = time.sleep
# End alias for time

# Khởi tạo bus I2C
bus = smbus.SMBus(1)

# Địa chỉ I2C của PCF điều khiển LED
I2C_ADDR = 0x24

# LEDs init
LEDs = [0x1, 0x2, 0x4, 0x8]
LED_value = [-1,-1,-1,-1]
LEDs_state = 0x0
DOTs=[0,0,0,0]
run_flag = False
run_flag_lock = threading.Lock()  # Khóa đồng bộ cho run_flag
# END LEDs init

SEG7_lock = threading.Lock()  # Khóa đồng bộ cho LED_value và LEDs_state

def dot_off():
    DEVICE.set(DEVICE.DOT)

def dot_on():
    DEVICE.reset(DEVICE.DOT)

def SEG7_multiplexing():
    global LED_value, LEDs, run_flag
    print("\033[1;33mDaemon started\033[0m")
    while True:
        with run_flag_lock:
            if not run_flag:
                print("\033[1;31mDaemon stopping...\033[0m")
                break
        for led in range(1, 5):
            with SEG7_lock:
                value = LED_value[led-1]

            set(value, led)
            delay(0.0001)
            reset(led)

# Tạo daemon thread cho Multiplexing
SEG7_thread = None

def start():
    global run_flag, SEG7_thread

    dot_off()

    with run_flag_lock:
        if run_flag:  # Tránh tạo thread mới nếu đã chạy
            print("\033[1;33mDaemon already running.\033[0m")
            return
        run_flag = True

    SEG7_thread = threading.Thread(target=SEG7_multiplexing)
    SEG7_thread.daemon = True  # Đặt chế độ daemon
    SEG7_thread.start()
    print("\033[1;32mDaemon thread started.\033[0m")


def stop():
    global run_flag, SEG7_thread

    dot_off()

    with run_flag_lock:
        if not run_flag:  # Kiểm tra nếu daemon đã dừng
            print("\033[1;33mDaemon is not running.\033[0m")
            return
        run_flag = False
    if SEG7_thread is not None:
        SEG7_thread.join()  # Đợi thread kết thúc
        SEG7_thread = None
    print("\033[1;32mDaemon thread stopped.\033[0m")


def clear():
    bus.write_byte(I2C_ADDR, 0x00)


def update(num, led):
    global LED_value

    if num > 9 or num < -1:
        print("\033[1;33mINVALID VALUE\033[0m")
        return

    if led > 4 or led < 1:
        print("\033[1;33mINVALID LED\033[0m")
        return

    with SEG7_lock:
        LED_value[led - 1] = num


def req(led, val, mode):
    if mode == 1:
        set(val, led)
    elif mode == 0:
        reset(led)
    else:
        print("\033[1;33mINVALID MODE\033[0m")


def set(value, led):
    global LEDs_state

    if value > 9 or value < 0:
        # print("\033[1;33mINVALID VALUE\033[0m")
        bus.write_byte(I2C_ADDR, 0x00)
        return

    if led > 4 or led < 1:
        print("\033[1;33mINVALID LED\033[0m")
        return  
    
    if DOTs[led - 1] == 1:
        dot_on()
    else:
        dot_off()

    LEDs_state = LEDs_state | LEDs[led - 1]
    msg = ((value << 4) & 0xF0) | LEDs_state
    bus.write_byte(I2C_ADDR, msg)

def reset(led):
    global LEDs_state

    if led > 4 or led < 1:
        print("\033[1;33mINVALID LED\033[0m")
        return

    LEDs_state = LEDs_state & ~LEDs[led - 1]
    msg = 0x0F & LEDs_state
    bus.write_byte(I2C_ADDR, msg)
