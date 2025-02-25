import RPi.GPIO as GPIO
import time

GPIO_PIN = 18  # Chân GPIO cần phát PWM
FREQUENCY = 10000  # Tần số PWM (Hz)
DUTY_CYCLE = 50  # Chu kỳ làm việc (%)

# Cấu hình GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

# Khởi tạo Software PWM
pwm = GPIO.PWM(GPIO_PIN, FREQUENCY)
pwm.start(DUTY_CYCLE)

try:
    while True:
        while DUTY_CYCLE < 100 :
            pwm.ChangeDutyCycle(DUTY_CYCLE)
            DUTY_CYCLE += 10
            time.sleep(1)  # Giữ chương trình chạy
        while DUTY_CYCLE > 0:
            pwm.ChangeDutyCycle(DUTY_CYCLE)
            DUTY_CYCLE -= 10
            time.sleep(1)  # Giữ chương trình chạy
except KeyboardInterrupt:
    print("Dừng PWM và thoát...")
    pwm.stop()
    GPIO.cleanup()
