import smbus
import RPi.GPIO as GPIO
import time

# Alias for GPIO
pinMode = GPIO.setup

readPin  = GPIO.input 
writePin = GPIO.output

OUTPUT = GPIO.OUT
INPUT  = GPIO.IN

HIGH = GPIO.HIGH
LOW  = GPIO.LOW
# END alias for GPIO

# Alias for time
delay = time.sleep
# End alias for time

# declare LED pins
LED_1 = 17
BUTTON = 27
# End declare LED pins

GPIO.setmode(GPIO.BCM) 

pinMode(LED_1,OUTPUT)
pinMode(BUTTON,INPUT)

try:
	print("LED Blinking")
	while True:
		if readPin(BUTTON) == HIGH:
			writePin(LED_1,HIGH)
		else:
			writePin(LED_1,LOW)

except KeyboardInterrupt:
	print("STOP")

finally:
	GPIO.cleanup()
