#import LCD

import LEDs
import time

# Alias for time
delay = time.sleep

try:
    while True:
        LEDs.update(1,1)
        delay(1)
        LEDs.update(2,1)
        delay(1)
        LEDs.update(3,1)
        delay(1)
        LEDs.update(4,1)
        delay(1)

        
        LEDs.update(1,0)
        delay(1)
        LEDs.update(2,0)
        delay(1)
        LEDs.update(3,0)
        delay(1)
        LEDs.update(4,0)
        delay(1)

except KeyboardInterrupt:
    LEDs.clear()

