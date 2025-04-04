import whisper

model = whisper.load_model("medium")
result = model.transcribe("new_au.wav")
print(result['text'])