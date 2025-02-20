import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522 

reader = SimpleMFRC522()

try:
    reader.BLOCK_ADDRS=[12]
    text="nng"

    print("Place card to write")
    reader.write(text)
    print("Write done")
finally:
    GPIO.cleanup()