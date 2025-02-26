import RPi.GPIO as GPIO
# import LCD
import SONAR
#import KEYPAD
import SERVO
import LEDs
import RGB
import RFID
import SEG7
import time

# Alias for time
delay = time.sleep

try:
    SEG7.start()
    SEG7.update(1,1)
    SEG7.update(2,2)
    SEG7.update(3,3)
    SEG7.update(4,4)

    RGB.start()

    LEDs.clear()

    SERVO.start()

    while True:
        SERVO.angle(180)

        RGB.color(102,250,255)
        LEDs.update(1,1)
        delay(1)
        RGB.color(255,34,166)
        LEDs.update(2,1)
        delay(1)
        RGB.color(255,231,0)
        LEDs.update(3,1)
        delay(1)
        RGB.color(0,250,255)
        LEDs.update(4,1)
        delay(1)
        RGB.color(102,0,255)
        LEDs.update(5,1)
        delay(1)
        RGB.color(102,250,0)
        LEDs.update(6,1)
        delay(1)
        RGB.color(0,0,255)
        LEDs.update(7,1)
        delay(1)
        RGB.color(0,255,0)
        LEDs.update(8,1)
        delay(1)

        SERVO.angle(90)
        
        RGB.color(102,250,255)
        LEDs.update(8,0)
        delay(1)
        RGB.color(255,34,166)
        LEDs.update(7,0)
        delay(1)
        RGB.color(255,231,0)
        LEDs.update(6,0)
        delay(1)
        RGB.color(0,250,255)
        LEDs.update(5,0)
        delay(1)
        RGB.color(102,0,255)
        LEDs.update(4,0)
        delay(1)
        RGB.color(102,250,0)
        LEDs.update(3,0)
        delay(1)
        RGB.color(0,0,255)
        LEDs.update(2,0)
        delay(1)
        RGB.color(0,255,0)
        LEDs.update(1,0)
        delay(1)

        SERVO.angle(0)
        delay(5)
except KeyboardInterrupt:
    LEDs.clear()
    SERVO.stop()
    RGB.stop()
    SEG7.stop()
finally:
    print("end")
    GPIO.cleanup()




        # color(102,250,255)
        # time.sleep(5)
        # color(255,34,166)
        # time.sleep(5)
        # color(255,231,0)
        # time.sleep(5)
