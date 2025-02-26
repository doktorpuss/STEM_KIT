import RPi.GPIO as GPIO

GPIO_PIN = 18  # Chân GPIO cần phát PWM
FREQUENCY = 50  # Tần số PWM (Hz)
DUTY_CYCLE = 0  # Chu kỳ làm việc (%)

# Cấu hình GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

# Khởi tạo Software PWM
pwm = GPIO.PWM(GPIO_PIN, FREQUENCY)

def start():
    pwm.start(DUTY_CYCLE)

def stop():
    pwm.stop()

def angle(angle):
    DUTY_CYCLE = round((((angle/180)+1)/20)*100)
    pwm.ChangeDutyCycle(DUTY_CYCLE)
