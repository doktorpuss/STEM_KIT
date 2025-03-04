import SEG7

SEG7.start()
SEG7.dot_update(1,1)
SEG7.update(1,1)

try:
    while True:
        pass

except KeyboardInterrupt:
    SEG7.stop()
finally:
    SEG7.stop()