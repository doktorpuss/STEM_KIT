#import LCD
#import SONAR
#import KEYPAD
#import LEDs
import RFID
import time

# Alias for time
delay = time.sleep

try:
    print("Waiting for card")
    while True:

        # Hàm card_available() chỉ check có card nào đọc được không?
        # Nếu có, hàm sẽ trả về uid là int nếu không hàm sẽ trả về uid None
        # Nên phối hợp với điều kiện "if uid!=None" để bỏ qua trường hợp không có thể mà không dừng hoạt động của hệ thống
    
        uid = RFID.card_available()
        if uid != None:
            
        # Các hàm đọc dữ liệu sẽ trả về một chuỗi str là dữ liệu đọc từ địa chỉ tương ứng của thẻ
        # Riêng read_full() sẽ trả về list[str] để có thể dễ phân vùng các sector 
        # Do phải request từng sector nên read_full() cũng phải chờ đọc lâu hơnhơn 

            sector = RFID.read_full(uid)
            for i in range(len(sector)):
                print(f"SECTOR {i} :{sector[i]}")
            print("\n\n=====================READ SECTOR=====================")

            print(f"Sector 1: {RFID.read_sector(uid,1)}")
            print("\n\n=====================READ BLOCKs=====================")

            print(f"Block 8: {RFID.read_block(uid,8)}")
            print(f"Block-3: {RFID.read_block(uid,-3)}")
            print("\n\n=======================FINISH========================")
            
            RFID.halt_til_card_leaves(uid)

            #Chờ thẻ mới được đọc
            print("====================INSERT NEW CARD======================")
            
            # Hàm wait_for_card() giống card_available(), sẽ trả lại uid của thẻ khả dụng
            # Nhưng sẽ tạm dừng hệ thống cho tới khi có thẻ đọc được

            uid = RFID.wait_for_card()
            print(f"Sector 1: {RFID.read_sector(uid,1)}")
            print("\n\n=====================READ BLOCKs=====================")
            
            RFID.halt_til_card_leaves(uid)
            # Hàm halt_til_card_leaves() sẽ chờ thẻ rời khỏi module, tránh đọc thẻ lại liên tục
            # Tuy nhiên, khi sử dụng sẽ tạm dừng hệ thống cho đến khi thẻ được rút rara

finally:
    print("end")
    #Thiếu GPIO.cleanup()
