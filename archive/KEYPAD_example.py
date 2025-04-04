import archive.KEYPAD_pure as KEYPAD_pure
import time

KEYPAD_pure.start()  # Bắt đầu tiến trình đọc phím

try:
    while True:
        data = KEYPAD_pure.readBuffer()
        # data = KEYPAD.waitKey()
        # data = KEYPAD.readUntil('#')
        if data:
            print(f"Received: {data}")
        print("time")
        time.sleep(1)

except KeyboardInterrupt:
    KEYPAD_pure.stop()  # Dừng tiến trình khi thoát chương trình
    print("\nStopped reading keypad.")

