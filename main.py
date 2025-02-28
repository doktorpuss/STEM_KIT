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
    while True:
        print(f"SW1: {SWITCH.read_switch(1)}\tSW2: {SWITCH.read_switch(2)}\tBT1: {BUTTON.read_button(1)}\tBT2: {BUTTON.read_button(2)}")
        count += 1
        delay(1)
        if (count % 10) == 0:
            FAN.on()
            BUZZER.off()
        elif (count % 10) == 5:
            FAN.off()
            BUZZER.on()
except KeyboardInterrupt:
    FAN.off()
    BUZZER.off()
    print("end")

finally:
    GPIO.cleanup()




        # color(102,250,255)
        # time.sleep(5)
        # color(255,34,166)
        # time.sleep(5)
        # color(255,231,0)
        # time.sleep(5)
