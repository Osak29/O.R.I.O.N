# 🛰️ ORION - Intelligent Voice Assistant

> **O.R.I.O.N** — *Operational Responsive Intelligent Omni-system Navigator*

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 🚀 Overview

**ORION** is a smart voice-controlled assistant inspired by **FRIDAY from Iron Man** in the Marvel Cinematic Universe.  
It is designed to interact naturally with users, execute system-level commands, and automate daily tasks — all through voice or text input.

> ⚡ Goal: Build a realistic, modular, and extensible AI assistant.

---

## ✨ Features

- 🎤 **Voice Recognition** (Speech-to-Text)  
- 🔊 **Text-to-Speech Responses**  
- 🧠 **Command Understanding (NLP-based)**  
- 💻 **System Control**  
  - Open applications  
  - Execute scripts  
- 🌐 **Web Interaction**  
  - Search on Google  
- ⚙️ **Custom Automation**  
- 🧩 **Modular Architecture**

---

## 🧱 Project Structure

```bash
orion_ai/
│
├── main.py
├── config.py
│
├── core/
│   ├── assistant.py
│   ├── brain.py
│   ├── executor.py
│
├── voice/
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│
├── commands/
│   ├── system_commands.py
│   ├── web_commands.py
│   ├── custom_commands.py
│
├── utils/
│   ├── logger.py
│
└── ui/ (optional)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/orion-ai.git
cd orion-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the assistant

```bash
python main.py
```

---

## 🛠️ Tech Stack

- **Python**
- **SpeechRecognition / Vosk**
- **pyttsx3**
- **spaCy / NLP tools**
- **OS & subprocess modules**

---

## 🧠 How It Works

```text
Voice → Text → Intent Detection → Command Execution → Response
```

---

## 📌 Example Commands

- "Orion, open Chrome"
- "Orion, search for artificial intelligence"
- "Orion, what time is it?"

---

## 🎬 Demo / GIF

![Demo GIF](https://media.giphy.com/media/26gssIytJvy1b1THO/giphy.gif)  
*(Replace with your actual GIF showing ORION in action)*

---

## 📈 Roadmap

- [ ] Advanced NLP (intent classification)
- [ ] Offline voice recognition (Vosk)
- [ ] Graphical Interface (HUD style)
- [ ] Memory & context awareness
- [ ] Plugin system

---

## ⚠️ Limitations

- Not a full autonomous AI (yet)
- Requires configuration for voice recognition
- Limited contextual understanding (early stage)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 💡 Inspiration

**ORION is inspired by FRIDAY, the AI assistant from Iron Man.**  
This project aims to bring a similar voice-controlled, intelligent assistant experience to a real-world desktop environment.

---

## 👨‍💻 Author

Developed by **Osak**

---

## 🔥 Final Note

> ORION is not just a project — it's a step toward building your own intelligent system, inspired by one of the most advanced AI assistants in fiction.