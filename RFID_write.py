import RPi.GPIO as GPIO
import RFID
from mfrc522 import SimpleMFRC522 

reader = SimpleMFRC522()

try:
    reader.BLOCK_ADDRS=[20]
    reader.SECTOR = 23
    text="24681357"

    print("Place card to write")
    reader.write(text)
    print("Write done")

    # print("Place card to authenticate...")
    # id = reader.read_id()  # Lấy UID (trả về int)

    # # Tính toán số byte cần thiết để biểu diễn UID
    # num_bytes = (id.bit_length() + 7) // 8  # Tính số byte cần thiết
    # uid_bytes = id.to_bytes(num_bytes, 'big')  # Chuyển UID thành bytes
    # uid_list = list(uid_bytes)  # Chuyển thành danh sách byte

    # status = reader.READER.MFRC522_Auth(reader.READER.PICC_AUTHENT1A, 18, reader.KEY, uid_list)

    # if status == reader.READER.MI_OK:
    #     print(f"Authentication successful! UID: {uid_list}")
    # else:
    #     print("Authentication failed!")

finally:
    GPIO.cleanup()