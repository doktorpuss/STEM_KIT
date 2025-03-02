import spidev
import time

spi = spidev.SpiDev(0, 0)  # Mở bus 0, chip select 0
spi.max_speed_hz = 100000  # Tốc độ SPI (có thể chỉnh tùy ý, ví dụ 1.35MHz)

def read_mcp3208(channel):
    # channel trong khoảng [0..7]
    # Lệnh đọc MCP3208 ở chế độ single-ended thường dùng 3 byte:
    #   Byte gửi đi 1: 0b00000110 (0x06) hoặc 0b00000111 (0x07) nếu channel >= 4
    #   Byte gửi đi 2: (channel & 0x03) << 6
    #   Byte gửi đi 3: 0 (để nhận lại dữ liệu)
    # Đây là 1 cách, có nhiều biến thể, miễn đúng timing SPI là được.

    cmd1 = 6 | (channel >> 2)         # 0b0110 + bit cao của channel
    cmd2 = (channel & 0x03) << 6      # dời 2 bit thấp của channel sang trái 6
    response = spi.xfer2([cmd1, cmd2, 0])
    print([cmd1,cmd2],bin)

    # response[0] thường là byte "rác" hoặc phản hồi 1 phần
    # response[1] chứa 4 bit cao (bit 11..8), response[2] chứa 8 bit thấp (bit 7..0)
    print(response,hex)
    adc_value = ((response[1] & 0x0F) << 8) | response[2]
    return adc_value

try:
    while True:
        for i in range (8):
            value = read_mcp3208(i)  # Đọc kênh 0
            voltage = (value * 5) / 4095  # Chuyển sang điện áp (nếu VREF=3.3V)
            print(f"Channel: {i}, ADC: {value}, Voltage: {voltage:.3f} V")
            time.sleep(1)

except KeyboardInterrupt:
    spi.close()
    print("Đã thoát.")
