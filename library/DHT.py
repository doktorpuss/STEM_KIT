TEMP_FILE = "/home/pi/Documents/code/temperature.txt"
HUM_FILE = "/home/pi/Documents/code/humidity.txt"

def temperature():
    try:
        with open(TEMP_FILE, "r+") as file:
            data = file.read().strip()
            file.seek(0)
            file.truncate(0)  # Xóa nội dung file sau khi đọc
            return float(data) if data else 0.0
    except (FileNotFoundError, ValueError):
        return 0.0

def humidity():
    try:
        with open(HUM_FILE, "r+") as file:
            data = file.read().strip()
            file.seek(0)
            file.truncate(0)  # Xóa nội dung file sau khi đọc
            return float(data) if data else 0.0
    except (FileNotFoundError, ValueError):
        return 0.0
