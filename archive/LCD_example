import RPi.GPIO as GPIO
import LCD
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
    FAN.off()
    BUZZER.off()
    SEG7.clear()
    SEG7.stop()
    LCD.noBacklight()

    # the example truely start from here
    LCD.begin()
    LCD.setCursor(0,0)
    LCD.print("Hello")
    LCD.setCursor(0,1)
    LCD.print(1234)
    LCD.print(" ")
    LCD.print(5678)
    while True:
        LCD.noBacklight()
        delay(1)
        LCD.backlight()
        delay(2)

except KeyboardInterrupt:
    LCD.noBacklight()
    LCD.clear()
    SEG7.stop()
    FAN.off()
    BUZZER.off()
    print("end")

finally:
    GPIO.cleanup()

