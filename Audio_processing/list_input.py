import pyaudio
import wave

def list_available_input(p):
    # Tìm và list các micro có thể sử dụng
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        
        # Kiểm tra thiết bị có phải micro không và có đang hoạt động không
        if device_info["maxInputChannels"] > 0 and device_info["hostApi"] == 0:
            print(f"Index: {i} | Tên: {device_info['name']} \t|Sample Rate: {device_info['defaultSampleRate']} \t| Kênh: {device_info['maxInputChannels']}")
            #print(device_info)
p = pyaudio.PyAudio()
list_available_input(p)
p.terminate()
