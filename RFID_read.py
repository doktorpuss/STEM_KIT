import spidev  # Thư viện này được import nhưng không thực sự được sử dụng trực tiếp trong code của bạn
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
attemp = 5  # Số lần thử đọc lại khi thẻ vẫn còn
prev = 0    # Biến lưu UID đã đọc (ban đầu đặt là 0)

try:
    while True:
        print("Waiting for card nearby")
        uid, text = reader.read()  # Chờ và đọc thẻ (blocking)
        if (prev != uid):
            uid_hex = format(uid, 'X')
            print(f"ID: {uid_hex}\n Text: {text}\n")
            prev = uid  # Cập nhật UID đã đọc

        while (uid == prev):  # Vòng lặp kiểm tra xem thẻ còn không
            uid = reader.read_id_no_block()  # Thử đọc ID (không blocking)
            while (not uid) and (attemp > 0):  # Nếu không đọc được và còn số lần thử
                attemp = attemp - 1
                uid = reader.read_id_no_block()  # Thử đọc lại
            if (not uid) and (attemp <= 0):  # Nếu hết số lần thử
                prev = 0  # Đặt prev về 0 để cho phép đọc thẻ mới
            attemp = 5  # Đặt lại số lần thử

finally:
    print("end")
    #Thiếu GPIO.cleanup()
