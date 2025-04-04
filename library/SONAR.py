import RPi.GPIO as GPIO
import time

# Định nghĩa chân GPIO
TRIG = 16  # Chân Trigger
ECHO = 6   # Chân Echo

# Cấu hình GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distance():
    # Gửi tín hiệu Trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # Kéo cao 10µs
    GPIO.output(TRIG, False)

    # Đợi Echo lên mức cao
    while GPIO.input(ECHO) == 0:
        pass

    # Đợi Echo xuống mức thấp
    start_time = time.time()
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    # Tính toán khoảng cách
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # Tốc độ âm thanh = 34300 cm/s

    return round(distance, 2)
