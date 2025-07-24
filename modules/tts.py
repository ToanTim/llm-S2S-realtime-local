# TTS inference (Coqui TTS example)
from TTS.api import TTS

class TextToSpeech:
    def __init__(self, model_path):
        self.tts = TTS(model_path)

    def synthesize(self, text):
        return self.tts.tts(text)
