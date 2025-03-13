import RPi.GPIO as GPIO
# import LCD
import SONAR
#import KEYPAD
import SERVO
import LEDs
import RGB
import RFID
import SEG7
import FAN
import BUZZER
import BUTTON
import SWITCH
import time

# Alias for time
delay = time.sleep
millis = time.time

try:
    count = 0
    LEDs.clear()
    SERVO.stop()
    RGB.stop()
    FAN.on()
    BUZZER.off()
    SEG7.clear()
    SEG7.start()
    # SEG7.dot_on()
    while True:
        inputs = input().split()
        if len(inputs) == 2:
            SEG7.update(int(inputs[0]),int(inputs[1]))

            if SEG7.DOTs[count] == 0:
                SEG7.DOTs[count] = 1
            else:
                SEG7.DOTs[count] = 0
            
            count += 1
            if count > 3:
                count = 0
            
        else:
            print("wrong format")
except KeyboardInterrupt:
    SEG7.stop()
    FAN.off()
    BUZZER.off()
    print("end")

finally:
    GPIO.cleanup()

