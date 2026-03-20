from commands.system_commands import open_app, search_web
from datetime import datetime

class Brain:
    def process(self, text):
        text = text.lower()
        if "ouvre" in text:
            return open_app(text)
        elif "cherche" in text:
            return search_web(text)
        elif "heure" in text:
            return f"Il est {datetime.now().strftime('%H:%M')}"
        else:
            return "Je n'ai pas compris."