# Pipeline orchestration
from modules.audio_io import record_audio, play_audio
from modules.stt import SpeechToText
from modules.llm import LLM
from modules.tts import TextToSpeech
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

def run_pipeline():
    stt = SpeechToText(config['model']['stt_model_path'])
    llm = LLM(config['model']['llm_model_path'], config['device'])
    tts = TextToSpeech(config['model']['tts_model_path'])
    sample_rate = config['audio']['sample_rate']
    chunk_size = config['audio']['chunk_size']

    print("Ready for speech input...")
    audio = record_audio(3, sample_rate, chunk_size)
    text = stt.transcribe(audio, sample_rate)
    print(f"Recognized: {text}")
    response = llm.generate(text)
    print(f"LLM: {response}")
    audio_out = tts.synthesize(response)
    play_audio(audio_out, sample_rate)
