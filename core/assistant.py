from voice.speech_to_text import listen
from voice.text_to_speech import speak
from core.brain import Brain

class Assistant:
    def __init__(self):
        self.brain = Brain()

    def run(self):
        speak("Orion est prête.")

        while True:
            command = listen()
            if command:
                response = self.brain.process(command)
                speak(response)