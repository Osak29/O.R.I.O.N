import requests
from commands.system_commands import open_app, search_web
from datetime import datetime

class Brain:
    def __init__(self):
        self.history = []

    def ask_ollama(self, prompt):
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "num_predict": 120,
                        "temperature": 0.7
                    }
                }
            )
            return response.json()["response"]

        except Exception as e:
            return f"Erreur Ollama : {e}"

    def process(self, text):
        text = text.lower()

        # COMMANDES RAPIDES
        if "ouvre" in text:
            return open_app(text)

        elif "cherche" in text:
            return search_web(text)

        elif "heure" in text:
            return f"Il est {datetime.now().strftime('%H:%M')}"

        elif len(text.split()) <= 2:
            return "Peux-tu préciser ta demande ?"
        
        # IA (OLLAMA)
        else:
            self.history.append(f"Utilisateur: {text}")

            prompt = (
                "Tu es Orion, un assistant intelligent, clair et utile.\n"
                "Réponds en français.\n\n"
                + "\n".join(self.history[-6:]) +
                "\nOrion:"
            )

            response = self.ask_ollama(prompt)

            self.history.append(f"Orion: {response}")

            return response