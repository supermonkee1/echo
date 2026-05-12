# Echo

Echo is a Python-based desktop voice assistant for Windows.

It can:
- Listen for voice commands
- Respond using text-to-speech
- Open applications
- Take screenshots
- Use a wake word system
- Continuously listen for commands

## Features

- Wake word: `Echo`
- Voice recognition using SpeechRecognition
- Text-to-speech responses using pyttsx3
- Modular command system
- Screenshot support
- Generic app launcher
- Continuous listening loop

---

# Current Commands

Examples:

- `echo open chrome`
- `echo open steam`
- `echo screenshot`
- `echo sleep`

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/supermonkee1/echo.git
cd echo
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Echo

```bash
python main.py
```

---

# Project Structure

```text
Echo/
├── commands/
├── screenshots/
├── venv/
├── main.py
├── README.md
└── .gitignore
```

---

# Future Plans

- Local AI integration
- Better wake word detection
- Smarter command parsing
- Memory system
- GUI
- Timers and reminders
- Screen understanding

---

# Technologies Used

- Python 3.11
- SpeechRecognition
- pyttsx3
- pyautogui
- Ollama (planned)

---

# License

This project is open-source.