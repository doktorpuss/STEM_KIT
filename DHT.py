import adafruit_dht
import board
import time

# Khởi tạo cảm biến DHT11 (hoặc DHT22 nếu bạn sử dụng cảm biến này)
dhtDevice = adafruit_dht.DHT11(board.D26)  # Thay D26 bằng chân GPIO bạn dùng

def Temperature():
    try:
        Temp = dhtDevice.temperature
    except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print("\033[1;31mHTemperature failed\033[0m")
            print(error.args[0])
    return Temp

def Humidity():
    try:
        Humid = dhtDevice.humidity
    except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print("\033[1;31mHumidity failed\033[0m")
            print(error.args[0])
    return Humid
