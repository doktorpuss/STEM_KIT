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

LEDs.clear()
LCD.begin()
LCD.clear()
LCD.noBacklight()
SERVO.stop()
SEG7.clear()
SEG7.dot_off()
RGB.stop()
FAN.off()
BUZZER.off()
