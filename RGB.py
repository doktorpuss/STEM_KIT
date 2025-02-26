import RPi.GPIO as GPIO
import time

RGB_RED = 19  # Chân GPIO cần phát PWM
RGB_GREEN = 13  # Chân GPIO cần phát PWM
RGB_BLUE = 12  # Chân GPIO cần phát PWM
FREQUENCY = 10000  # Tần số PWM (Hz)

# Cấu hình GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RGB_RED, GPIO.OUT)
GPIO.setup(RGB_GREEN, GPIO.OUT)
GPIO.setup(RGB_BLUE, GPIO.OUT)

# Khởi tạo Software PWM
RED = GPIO.PWM(RGB_RED, FREQUENCY)
GREEN = GPIO.PWM(RGB_GREEN, FREQUENCY)
BLUE = GPIO.PWM(RGB_BLUE, FREQUENCY)

def start():
    RED.start(0)
    BLUE.start(0)
    GREEN.start(0)

def color(r,g,b):
    r = (r/255) * 100
    g = (g/255) * 100
    b = (b/255) * 100

    RED.ChangeDutyCycle(r)
    GREEN.ChangeDutyCycle(g)
    BLUE.ChangeDutyCycle(b)

def stop():
    RED.stop()
    GREEN.stop()
    BLUE.stop()

