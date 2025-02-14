#import LCD
import SONAR
import KEYPAD
import LEDs
import time

# Alias for time
delay = time.sleep

try:
    print("START")
    while True:
        print(f"Number {KEYPAD.waitUntil('#')} ENTER")

except KeyboardInterrupt:
    print("END")

