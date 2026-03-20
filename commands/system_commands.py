import os
import webbrowser

def open_app(command):
    if "chrome" in command:
        os.system("start chrome")
        return "J'ouvre Chrome"
    if "notepad" in command or "bloc-notes" in command:
        os.system("notepad")
        return "J'ouvre le bloc-notes"
    return "Application inconnue"

def search_web(command):
    query = command.replace("cherche", "").strip()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Recherche de {query}"