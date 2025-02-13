#import LCD
import LEDs
import SEG7 
import time

# Alias for time
delay = time.sleep
millis = time.time
# End alias for time

try:
    SEG7.clear()
    while True:
        try:
            while True:
                inputs=input().split()
                led = int(inputs[0])
                val = int(inputs[1])

                if led == 0:
                    if SEG7.run_flag:
                        SEG7.stop()
                        print("\033[1;32mLEDs STOPED!!!\033[0m")
                    else:
                        SEG7.start()
                        print("\033[1;32mLEDs START\033[0m")
                else:
                    SEG7.update(val , led)

        except ValueError:
            print("\033[1;31mINVALID INPUT\033[0m")


except KeyboardInterrupt:
    SEG7.clear()
