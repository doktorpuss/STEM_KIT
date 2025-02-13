import RPi.GPIO as GPIO
import time

# Alias for GPIO
pinMode = GPIO.setup
readPin  = GPIO.input 
writePin = GPIO.output

OUTPUT = GPIO.OUT
INPUT  = GPIO.IN

HIGH = GPIO.HIGH
LOW  = GPIO.LOW
# END alias for GPIO

# Alias for time
delay = time.sleep
# End alias for time

# declare STEPPER pins
COIL_1 = 6
COIL_2 = 13
COIL_3 = 19
COIL_4 = 26
FAN_P_PIN = 18
FAN_M_PIN = 12
# End declare STEPPER pins

GPIO.setmode(GPIO.BCM) 

# Đặt chế độ cho các chân
pinMode(COIL_1, OUTPUT)
pinMode(COIL_2, OUTPUT)
pinMode(COIL_3, OUTPUT)
pinMode(COIL_4, OUTPUT)
pinMode(FAN_P_PIN, OUTPUT)
pinMode(FAN_M_PIN, OUTPUT)


# Setup PWM
FAN_P = GPIO.PWM(FAN_P_PIN, 100)
FAN_M = GPIO.PWM(FAN_M_PIN, 100)

# Initialize PWM
FAN_P.start(0)  # PWM bắt đầu với độ rộng xung 0%
FAN_M.start(0)

# Biến trạng thái cuộn dây
state = 0x1

# Hàm điều khiển các chân GPIO
def pin_run():
    t_delay = 0.005

    writePin(COIL_1, HIGH )
    writePin(COIL_2, LOW )
    writePin(COIL_3, LOW )
    writePin(COIL_4, LOW )
    delay(t_delay)

    writePin(COIL_1, LOW )
    writePin(COIL_2, HIGH )
    writePin(COIL_3, LOW )
    writePin(COIL_4, LOW )
    delay(t_delay)

    writePin(COIL_1, LOW )
    writePin(COIL_2, LOW )
    writePin(COIL_3, HIGH )
    writePin(COIL_4, LOW )
    delay(t_delay)

    writePin(COIL_1, LOW )
    writePin(COIL_2, LOW )
    writePin(COIL_3, LOW )
    writePin(COIL_4, HIGH )
    delay(t_delay)

# Chương trình chính
try:
    while True:
        #pin_run()
        for duty in range (0,101,5):
            FAN_P.ChangeDutyCycle(duty)
            delay(0.5)
        
        for duty in range (100,-1,-5):
            FAN_P.ChangeDutyCycle(duty)
            delay(0.5)

except KeyboardInterrupt:
    print("STOP")
finally:
    FAN_P.stop()  # Dừng PWM nếu đã khởi động
    FAN_M.stop()
    GPIO.cleanup()  # Giải phóng GPIO
