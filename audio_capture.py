import sounddevice  as sd
import numpy as np


def audio_callback(indata,frames,time,status):
    """"callback function to process the audio in real time"""
    print("audio data: ",indata)


def capture_capture(duration=10, sample_rate=44100):
    """function to capture audio data """
    stream= sd.inputstream(callback= audio_callback,samplerate= sample_rate,channels=2)
    with stream:
        sd.sleep(int(duration*1000))