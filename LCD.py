import smbus
import time

# Địa chỉ I2C của module LCD (thay đổi nếu cần sau khi kiểm tra bằng i2cdetect)
I2C_ADDR = 0x27
LCD_WIDTH = 16  # Độ rộng của màn hình LCD (16x2)

# Các lệnh điều khiển LCD
LCD_CHR = 1  # Chế độ gửi dữ liệu
LCD_CMD = 0  # Chế độ gửi lệnh
LCD_BACKLIGHT = 0x08  # Bật đèn nền LCD
ENABLE = 0b00000100  # Enable bit

# Định nghĩa dòng trên LCD
LCD_LINE_1 = 0x80  # Địa chỉ của dòng 1
LCD_LINE_2 = 0xC0  # Địa chỉ của dòng 2

# Khởi tạo bus I2C
bus = smbus.SMBus(1)

# Hàm gửi dữ liệu đến LCD
def lcd_byte(bits, mode):
    # Chia dữ liệu thành 2 nửa: high nibble và low nibble
    high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT
    
    # Gửi high nibble
    bus.write_byte(I2C_ADDR, high)
    lcd_toggle_enable(high)
    
    # Gửi low nibble
    bus.write_byte(I2C_ADDR, low)
    lcd_toggle_enable(low)

def lcd_toggle_enable(bits):
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(0.0005)

# Hàm khởi tạo LCD
def begin():
    lcd_byte(0x33, LCD_CMD)  # Chế độ 4-bit
    lcd_byte(0x32, LCD_CMD)  # Chế độ 4-bit
    lcd_byte(0x06, LCD_CMD)  # Đặt con trỏ tăng
    lcd_byte(0x0C, LCD_CMD)  # Bật màn hình, tắt con trỏ
    lcd_byte(0x28, LCD_CMD)  # Chế độ 4-bit, 2 dòng
    lcd_byte(0x01, LCD_CMD)  # Xóa màn hình
    time.sleep(0.005)

    
# Hàm hiển thị văn bản trên LCD
def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for char in message:
        lcd_byte(ord(char), LCD_CHR)

def backlight():
    global LCD_BACKLIGHT
    LCD_BACKLIGHT = 0x08
    bus.write_byte(I2C_ADDR,LCD_BACKLIGHT)

def noBacklight():
    global LCD_BACKLIGHT
    LCD_BACKLIGHT = 0x00
    bus.write_byte(I2C_ADDR,LCD_BACKLIGHT)

def setCursor(col,row):
    if row == 0 :
        cursor = LCD_LINE_1 + col
    elif row == 1:
        cursor = LCD_LINE_2 + col
    lcd_byte(cursor, LCD_CMD)

def clear():
    lcd_byte(0x01, LCD_CMD)  # Xóa màn hình

def print(data):
    data = str(data)  # Chuyển đổi dữ liệu sang chuỗi nếu không phải string
    for char in data:
        lcd_byte(ord(char), LCD_CHR)
