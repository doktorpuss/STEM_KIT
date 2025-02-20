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

GPIO.setmode(GPIO.BCM)

#declare keypad pins
COL_1 = 27
COL_2 = 17
COL_3 = 4

ROW_1 = 25
ROW_2 = 24
ROW_3 = 22
ROW_4 = 23
#end declare keypad pins

#pin declare on RPi
pinMode(COL_1,OUTPUT)
pinMode(COL_2,OUTPUT)
pinMode(COL_3,OUTPUT)
pinMode(ROW_1,INPUT)
pinMode(ROW_2,INPUT)
pinMode(ROW_3,INPUT)
pinMode(ROW_4,INPUT)

#keymapping
keymap=[['1','2','3',],
        ['4','5','6',],
        ['7','8','9',],
        ['*','0','#',]]

def raise_col(col):
    global COL_1,COL_2,COL_3

    if col==COL_1:
        writePin(COL_1,HIGH)
        writePin(COL_2,LOW)
        writePin(COL_3,LOW)
    elif col==COL_2:
        writePin(COL_2,HIGH)
        writePin(COL_1,LOW)
        writePin(COL_3,LOW)
    elif col==COL_3:
        writePin(COL_3,HIGH)
        writePin(COL_2,LOW)
        writePin(COL_1,LOW)

def state_row():
    global ROW_1,ROW_2,ROW_3,ROW_4

    if readPin(ROW_1):
        return 1
    if readPin(ROW_2):
        return 2
    if readPin(ROW_3):
        return 3
    if readPin(ROW_4):
        return 4
    return 0

def state_col(row):
    while True:
        writePin(COL_3,LOW)
        delay(0.01)
        if(state_row() == 0):
            writePin(COL_3,HIGH)
            return 3

        writePin(COL_2,LOW)
        delay(0.01)
        if(state_row() ==0):
            writePin(COL_2,HIGH)
            return 2

        writePin(COL_1,LOW)
        delay(0.01)
        if(state_row() ==0):
            writePin(COL_1,HIGH)
            return 1
        
        #Nếu chưa xác định được cột thì lặp lại
        writePin(COL_1,HIGH)
        writePin(COL_2,HIGH)
        writePin(COL_3,HIGH)
        
def waitKey():
    writePin(COL_1,HIGH)
    writePin(COL_2,HIGH)
    writePin(COL_3,HIGH)

    noKeyPressed = True
    while noKeyPressed:
        row = state_row()
        if row != 0:
            noKeyPressed = False
            col = state_col(row)
            key = keymap[row-1][col-1]
            #print(f"KEY {key} PRESSED")
    
    while not noKeyPressed:
        if state_row() == 0:
            #print("RELEASED")
            noKeyPressed =True
    delay(0.05)
    return key
        
def readUntil(char):
    key = ''
    buffer = ""

    while key != char :
        buffer = buffer + key
        key = waitKey()
        
    return buffer
