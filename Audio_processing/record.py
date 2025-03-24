import pyaudio
import wave
# import time


p = pyaudio.PyAudio()

# Cấu hình để mở mic
FRAME_PER_BUFFER = 8192    # Each buffer contain 7350 frames
RATE = 44100               # Sampling at 44,1kHz
FORMAT = pyaudio.paInt16   # 2 byte format
CHANNELS = 1               # mono audio signal

stream = p.open(
    format = FORMAT,
    rate = RATE,
    channels = CHANNELS,
    frames_per_buffer = FRAME_PER_BUFFER,
    input_device_index = 2,
    input = True 
)

# Thu âm trong 10s
duration = 10
n_buffer_per_second = int(RATE / FRAME_PER_BUFFER)
n_buffer_need = n_buffer_per_second * duration
frames = [] 

try:
    print("Bắt đầu thu âm")
        # if ( (i+1) % n_buffer_per_second ) == 0: print(duration - int((i+1) / n_buffer_per_second))
    while True:
        data = stream.read(FRAME_PER_BUFFER,exception_on_overflow=False)
        frames.append(data)

except KeyboardInterrupt:
    # Ghi lại frame vào file âm thanh
    obj = wave.open("new_au.wav","wb")

    obj.setframerate(RATE)
    obj.setnchannels(CHANNELS)
    obj.setsampwidth(p.get_sample_size(FORMAT))

    obj.writeframes(b"".join(frames))
    obj.close()

    stream.close()
    p.terminate()