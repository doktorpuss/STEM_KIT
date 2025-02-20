import spidev  # Thư viện này được import nhưng không thực sự được sử dụng trực tiếp trong code của bạn
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
attemp = 3  # Số lần thử đọc lại khi thẻ vẫn còn
recent_uid = 0    # Biến lưu UID đã đọc (ban đầu đặt là 0)

def halt_til_card_leaves(uid):
    global recent_uid,attemp

    while (uid == recent_uid):  # Vòng lặp kiểm tra xem thẻ còn không
        uid = reader.read_id_no_block()  # Thử đọc ID (không blocking)
        while (not uid) and (attemp > 0):  # Nếu không đọc được và còn số lần thử
            attemp = attemp - 1
            uid = reader.read_id_no_block()  # Thử đọc lại
        if (not uid) and (attemp <= 0):  # Nếu hết số lần thử
            recent_uid = 0  # Đặt recent_uid về 0 để cho phép đọc thẻ mới
        attemp = 3  # Đặt lại số lần thử

def wait_for_card():
    global recent_uid

    recent_uid = reader.read_id()

    return recent_uid

def card_available():
    global recent_uid

    recent_uid = reader.read_id_no_block()
    if not recent_uid:
        return None
    
    return recent_uid

def read_block(uid,blockAddr):
    #Kiểm tra tính hợp lệ của block
    if (blockAddr > 63) or (blockAddr < 0):
        return "UNAVAILABLE BLOCK"

    reader.BLOCK_ADDRS=[blockAddr]
    reader.SECTOR = (blockAddr // 4)*4 + 3

    id, text = reader.read()  # Đọc thẻ

    if(uid == id):
        return text
    return "CARD LEFT BEFORE DONE READING"


def read_sector(uid,sector):
    #Đồng bộ hóa với ràng buộc: 
    #   Sector 0 là sector trạng thái
    #   Sector đầu là sector 1,
    sector = sector - 1 

    #Kiểm tra tính hợp lệ của sector
    if (sector > 15) or (sector < 0):
        return "UNAVAILABLE SECTOR"
    
    #Xác định sector's key và các block trong sector
    offset = sector*4
    reader.SECTOR = offset + 3
    if sector == 0:
        reader.BLOCK_ADDRS = [1,2]
    elif (sector > 0) :
        reader.BLOCK_ADDRS = [offset , offset+1 , offset+2]

    id, text = reader.read()  # Đọc thẻ

    if(uid == id):
        return text
    return "CARD LEFT BEFORE DONE READING"

def read_full(uid):
    buf=["LOSS"]

    reader.SECTOR = 0
    reader.BLOCK_ADDRS = [1,2]
    id, text = reader.read()  # Chờ và đọc thẻ (blocking)
    
    if(uid == id):
        buf.append(text)
        
        for i in range(16):
            if i!=0 :
                offset = i*4
                reader.SECTOR = offset + 3
                reader.BLOCK_ADDRS = [offset , offset+1 , offset+2]
                id, text = reader.read()
                if(id == uid):
                    buf.append(text)  
                else:
                    return buf
        buf[0]="GOOD"  
    return buf 

def write_block(blockAddr,msg):
    reader.write(msg)
