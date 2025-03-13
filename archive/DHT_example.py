import DHT
import RGB
import time

try:
    RGB.start()
    RGB.color(90, 90, 90)

    while True:
        print(f"T: {DHT.temperature()} \tH: {DHT.humidity()}")
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    RGB.stop()