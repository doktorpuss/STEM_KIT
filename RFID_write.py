import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522 

reader = SimpleMFRC522()

try:
    text="HELLO son"

    print("Place card to write")
    reader.write(text)
    print("Write done")
finally:
    GPIO.cleanup()