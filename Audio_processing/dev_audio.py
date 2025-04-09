import pyaudio
import wave 
import keyboard
import threading

def list_available_input(p):
    # Tìm và list các micro có thể sử dụng
    
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        
        # Kiểm tra thiết bị có phải micro không và có đang hoạt động không
        if device_info["maxInputChannels"] > 0 and device_info["hostApi"] == 0:
            print(f"Index: {i} | Tên: {device_info['name']} \t|Sample Rate: {device_info['defaultSampleRate']} \t| Kênh: {device_info['maxInputChannels']}")
            #print(device_info)
    
    p.terminate()

def find_recorder():
    p = pyaudio.PyAudio()
    dev_id=-1
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        
        if device_info["name"] == "USB PnP Sound Device: Audio (hw:2,0)":
            dev_id = i
            break

    if dev_id == -1:
        print("No sound input found")   

    p.terminate()
    return dev_id

def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("Recording stopped.")
    # Dừng và đóng luồng ghi âm

def record_audio(filename, duration=-1, channels=1, rate=44100, chunk=8192):
    # Khởi tạo PyAudio
    p = pyaudio.PyAudio()

    # Mở luồng ghi âm
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=rate,
                    input_device_index=find_recorder(),
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    # Ghi âm trong khoảng thời gian đã chỉ định hoặc đến khi nhấn Enter
    if duration == -1:
        print("Press Enter to stop recording...")
        while True:
            data = stream.read(chunk)
            frames.append(data)
            if keyboard.is_pressed('enter'):
                break
        print("Recording stopped.")
    else:
        # Tính số lượng chunk cần ghi âm
        # duration = int(input("Enter duration in seconds: "))
        print(f"Recording for {duration} seconds...")
        # Ghi âm trong khoảng thời gian đã chỉ định
        # rate = int(input("Enter sample rate (default 44100): "))
        #Tạo luồng đếm ngược
    t = threading.Thread(target=countdown, args=(duration,))
    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    # Dừng và đóng luồng ghi âm và đêm ngược
    t.join()
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Lưu âm thanh vào file WAV
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
