import KEYPAD
import time

KEYPAD.start()  # Bắt đầu tiến trình đọc phím

try:
    while True:
        data = KEYPAD.readBuffer()
        # data = KEYPAD.waitKey()
        # data = KEYPAD.readUntil('#')
        if data:
            print(f"Received: {data}")
        print("time")
        time.sleep(2)

except KeyboardInterrupt:
    KEYPAD.stop()  # Dừng tiến trình khi thoát chương trình
    print("\nStopped reading keypad.")
