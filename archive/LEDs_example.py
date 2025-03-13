#import LCD
import LEDs
import time

try:
    print("\033[1;32mLEDs START\033[0m")
    LEDs.clear()
    while True:
        try:
            while True:
                LED_num = int(input("toggle LED:"))
                LED_mode = int(input("mode: "))
                LEDs.update(LED_num,LED_mode)

        except ValueError:
            LEDs.clear()
            print("\033[1;31mINVALID INPUT\033[0m")


except KeyboardInterrupt:
    LEDs.clear()
    print("\033[1;32mLEDs STOPED!!!\033[0m")