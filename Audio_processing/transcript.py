import whisper
import wave
import numpy as np
import scipy.signal as signal

model = whisper.load_model("medium")
result = model.transcribe("new_au.wav")
print(result['text'])