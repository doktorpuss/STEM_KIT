import RPi.GPIO as GPIO
from mfrc522 import MFRC522

# Khởi tạo module RC522
reader = MFRC522()
previous_uid = [0,0,0,0,0]

def read_card():
    print("Đưa thẻ gần đầu đọc...")

    while True:
        # Kiểm tra có thẻ nào gần không
        (status, tag_type) = reader.MFRC522_Request(reader.PICC_REQIDL)
        if status != reader.MI_OK:
            continue  # Không có thẻ nào

        # Đọc UID của thẻ
        (status, uid) = reader.MFRC522_Anticoll()
        if status != reader.MI_OK:
            continue
        # if(uid == previous_uid):
        #     continue

        previous_uid = uid

        print(f"UID của thẻ: {uid}")

        # Chọn thẻ (trả về OK nếu thành công)
        if reader.MFRC522_SelectTag(uid) != reader.MI_OK:
            print("Lỗi chọn thẻ!")
            continue

        # Xác thực với sector 0 (dùng key mặc định)
        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]  # Key mặc định
        if reader.MFRC522_Auth(reader.PICC_AUTHENT1A, 8, key, uid) != reader.MI_OK:
            print("Lỗi xác thực!")
            continue

        # Đọc dữ liệu từ block 8
        # status, data = reader.MFRC522_Read(8)
        # if status == reader.MI_OK:
        #     print(f"Dữ liệu: {data}")
        # else:
        #     print("Lỗi đọc thẻ!")
        for i in range(16) :
            result = reader.MFRC522_Read(i)
            print(f"Raw data[{i}]: {result}")

        # Ngắt kết nối thẻ
        reader.MFRC522_StopCrypto1()
    

try:
    read_card()
except KeyboardInterrupt:
    print("\nDừng chương trình.")
finally:
    GPIO.cleanup()
