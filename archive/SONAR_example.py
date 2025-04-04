import SONAR

try:
    while True:
        dist = SONAR.distance()
        print(dist)

except KeyboardInterrupt:
    print("END")

