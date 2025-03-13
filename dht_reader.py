import adafruit_dht
import board
import time

# Khởi tạo cảm biến DHT
dhtDevice = adafruit_dht.DHT11(board.D26)  # Thay D26 bằng chân GPIO của bạn
TEMP_FILE = "/home/pi/Documents/code/temperature.txt"
HUM_FILE = "/home/pi/Documents/code/humidity.txt"

while True:
    try:
        # Đọc dữ liệu từ DHT
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity

        if temperature is None or humidity is None:
            raise RuntimeError("Dữ liệu không hợp lệ")
    
    except RuntimeError as error:
        print("Lỗi đọc DHT:", error)  # In lỗi nếu có để kiểm tra
        temperature = 0.0
        humidity = 0.0
    except Exception as error:
        print("Lỗi không xác định:", error)
        temperature = 0.0
        humidity = 0.0
        break  # Thoát vòng lặp nếu có lỗi nghiêm trọng
    
    # Ghi dữ liệu nhiệt độ
    with open(TEMP_FILE, "w") as temp_file:
        temp_file.write(f"{temperature}")
    
    # Ghi dữ liệu độ ẩm
    with open(HUM_FILE, "w") as hum_file:
        hum_file.write(f"{humidity}")
        
    print(f"Đã ghi: {temperature}°C, {humidity}%")  # Debug
    
    time.sleep(0.0001)  # Cứ sau 2 giây ghi dữ liệu một lần
