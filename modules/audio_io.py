import sounddevice as sd
import numpy as np

# Audio input/output helpers

def record_audio(duration, sample_rate, chunk_size):
    print(f"Recording {duration}s of audio...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    return audio.flatten()

def play_audio(audio, sample_rate):
    print("Playing audio...")
    sd.play(audio, samplerate=sample_rate)
    sd.wait()
