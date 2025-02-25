import RPi.GPIO as GPIO
#import LCD
#import SONAR
#import KEYPAD
#import LEDs
import RFID
import time

# Alias for time
delay = time.sleep

try:
    block_to_write = 1
    msg = "2bahsudh"
    print("Waiting for card")
    while True:
        uid = RFID.card_available()
        if uid != None:
            RFID.write_block(uid,block_to_write,msg)
            print("WRITE DONE")
            print("remove card and read writen data")
            RFID.halt_til_card_leaves(uid)
            uid = RFID.wait_for_card()
            print(f"BLOCK {block_to_write} data: {RFID.read_block(uid,block_to_write)}")
            RFID.halt_til_card_leaves(uid)
            # for i in range(20):
            #     RFID.write_block(uid,i,msg)
            
            # RFID.halt_til_card_leaves(uid)
    

finally:
    print("end")
    GPIO.cleanup()
