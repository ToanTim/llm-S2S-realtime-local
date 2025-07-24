import sys
from modules.controller import run_pipeline
from TTS.utils.manage import ModelManager
if __name__ == "__main__":
    #run_pipeline()
    manager = ModelManager()
    path = manager.download_model("tts_models/en/ljspeech/tacotron2-DDC")