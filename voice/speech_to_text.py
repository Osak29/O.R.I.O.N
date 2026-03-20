import vosk
import sys
import sounddevice as sd
import queue
import json

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen():
    model = vosk.Model("models/vosk-model-small-fr-0.22")
    rec = vosk.KaldiRecognizer(model, 16000)
    
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Orion écoute...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print(f"Vous avez dit : {text}")
                    return text