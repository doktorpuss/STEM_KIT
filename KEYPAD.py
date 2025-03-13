import RPi.GPIO as GPIO
import time
import threading

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

buffer = ""
buffer_lock = threading.Lock()
process = None
running = False

def raise_col(col):
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
    
    while not noKeyPressed:
        if state_row() == 0:
            noKeyPressed = True
    delay(0.05)
    return key
        

def readUntil(char):
    key = ''
    local_buffer = ""

    while key != char:
        local_buffer += key
        key = waitKey()
        
    return local_buffer

def keypad_process(end_char):
    global buffer, running
    while running:
        key = waitKey() if end_char == '' else readUntil(end_char)
        with buffer_lock:
            buffer += key

def start(end_char=''):
    global process, running
    if process is None or not process.is_alive():
        running = True
        process = threading.Thread(target=keypad_process, args=(end_char,), daemon=True)
        process.start()

def stop():
    global running
    running = False

def available():
    global buffer
    with buffer_lock:
        return len(buffer) > 0

def readBuffer():
    global buffer
    with buffer_lock:
        data = buffer
        buffer = ""  # Xóa buffer sau khi đọc
    return data
