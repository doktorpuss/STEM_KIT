import spidev  # Thư viện này được import nhưng không thực sự được sử dụng trực tiếp trong code của bạn
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
attemp = 5  # Số lần thử đọc lại khi thẻ vẫn còn
prev = 0    # Biến lưu UID đã đọc (ban đầu đặt là 0)

def read_block(blockAddr):
    global prev,attemp

    reader.BLOCK_ADDRS=[blockAddr]
    reader.SECTOR = blockAddr // 4 + 3

    uid, text = reader.read()  # Chờ và đọc thẻ (blocking)

    if uid and (prev != uid):
        uid_hex = format(uid, 'X')
        print(f"ID: {uid_hex}\nText: {text}\n")
        prev = uid  # Cập nhật UID đã đọc

        while (uid == prev):  # Vòng lặp kiểm tra xem thẻ còn không
            uid = reader.read_id_no_block()  # Thử đọc ID (không blocking)
            while (not uid) and (attemp > 0):  # Nếu không đọc được và còn số lần thử
                attemp = attemp - 1
                uid = reader.read_id_no_block()  # Thử đọc lại
            if (not uid) and (attemp <= 0):  # Nếu hết số lần thử
                prev = 0  # Đặt prev về 0 để cho phép đọc thẻ mới
            attemp = 5  # Đặt lại số lần thử

def read_sector(sector):
    global prev,attemp

    offset = sector*4
    reader.SECTOR = offset + 3
    if sector == 0:
        reader.BLOCK_ADDRS = [1,2]
    elif (sector > 0) :
        reader.BLOCK_ADDRS = [offset , offset+1 , offset+2]
    uid, text = reader.read()  # Chờ và đọc thẻ (blocking)

    if uid and (prev != uid):
        uid_hex = format(uid, 'X')
        print(f"ID: {uid_hex}\nText: {text}\n")
        prev = uid  # Cập nhật UID đã đọc

        while (uid == prev):  # Vòng lặp kiểm tra xem thẻ còn không
            uid = reader.read_id_no_block()  # Thử đọc ID (không blocking)
            while (not uid) and (attemp > 0):  # Nếu không đọc được và còn số lần thử
                attemp = attemp - 1
                uid = reader.read_id_no_block()  # Thử đọc lại
            if (not uid) and (attemp <= 0):  # Nếu hết số lần thử
                prev = 0  # Đặt prev về 0 để cho phép đọc thẻ mới
            attemp = 5  # Đặt lại số lần thử

def read_full():
    global prev,attemp

    reader.SECTOR = 0
    reader.BLOCK_ADDRS = [1,2]
    uid, text = reader.read()  # Chờ và đọc thẻ (blocking)
    uid_hex = format(uid, 'X')

    print(f"ID: {uid_hex}\nSECTOR: 0\t Text: {text}")

    for i in range(16):
        if i!=0 :
            offset = i*4
            reader.SECTOR = offset + 3
            reader.BLOCK_ADDRS = [offset , offset+1 , offset+2]
            uid, text = reader.read()
            print(f"SECTOR: {i}\t Text: {text}")

    if uid and (prev != uid):
        prev = uid  # Cập nhật UID đã đọc

        while (uid == prev):  # Vòng lặp kiểm tra xem thẻ còn không
            uid = reader.read_id_no_block()  # Thử đọc ID (không blocking)
            while (not uid) and (attemp > 0):  # Nếu không đọc được và còn số lần thử
                attemp = attemp - 1
                uid = reader.read_id_no_block()  # Thử đọc lại
            if (not uid) and (attemp <= 0):  # Nếu hết số lần thử
                prev = 0  # Đặt prev về 0 để cho phép đọc thẻ mới
            attemp = 5  # Đặt lại số lần thử

def write_block(blockAddr,msg):
    reader.write(msg)
try:
    while True:
        print("READ CARD")
        read_full()

finally:
    print("end")
    #Thiếu GPIO.cleanup()
