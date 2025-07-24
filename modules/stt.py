# Whisper STT logic
import whisper

class SpeechToText:
    def __init__(self, model_path):
        self.model = whisper.load_model(model_path)

    def transcribe(self, audio, sample_rate):
        return self.model.transcribe(audio, fp16=False)["text"]
