import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"Orion: {text}")
    engine.say(text)
    engine.runAndWait()