# Echo

A modular local AI voice assistant for Windows built with Python.

Echo combines local speech recognition, AI intent routing, conversational AI, and desktop automation into a fully offline-capable assistant architecture.

---

# Features

## Voice Interaction

* Wake-word activation (`Echo`)
* Continuous microphone listening
* Silence-based automatic recording stop
* Interruptible speech output
* Voice feedback sounds

## AI Systems

* Local AI intent routing using Gemma
* Conversational responses using Phi-3
* Structured JSON action parsing
* Natural language command understanding

## Desktop Automation

* Dynamic Windows app launching
* Screenshot capture
* Web searching
* Sleep/shutdown mode

## Architecture

* Modular command system
* Separate routing and chat models
* Local Whisper GPU speech recognition
* Turn-based assistant flow
* Easily expandable command structure

---

# AI Stack

| System              | Model / Tool   |
| ------------------- | -------------- |
| Speech Recognition  | Faster-Whisper |
| Intent Routing      | Gemma 2B       |
| Conversation        | Phi-3          |
| Automation          | Python         |
| Local Model Runtime | Ollama         |

---

# Current Capabilities

Echo can currently:

* Open installed Windows applications
* Understand natural language requests
* Search the web
* Take screenshots
* Hold short conversations
* Respond to wake-word activation
* Run fully locally on the computer

Examples:

```text
Echo open chrome
Echo launch steam
Echo search for python tutorials
Echo take a screenshot
Echo who made minecraft
```

---

# Project Structure

```text
Echo/
│
├── commands/
│   ├── ai_router.py
│   ├── app_finder.py
│   ├── chat.py
│   ├── screenshot.py
│   ├── search_web.py
│   └── __init__.py
│
├── tests/
├── screenshots/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## 1. Clone The Repository

```powershell
git clone https://github.com/supermonkee1/echo.git
cd echo
```

---

## 2. Create Virtual Environment

```powershell
python -m venv venv
```

Activate:

```powershell
venv\Scripts\activate
```

---

## 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## 4. Install Ollama

Install Ollama from:

[https://ollama.com/](https://ollama.com/)

---

## 5. Download AI Models

```powershell
ollama run gemma:2b
```

```powershell
ollama run phi3
```

---

# Running Echo

```powershell
python main.py
```

Say:

```text
Echo
```

to activate the assistant.

---

# Future Plans

* Better interruption system
* Smarter memory/context
* Dynamic tool registry
* Improved fuzzy app matching
* GUI interface
* Screen understanding
* Streaming responses
* More desktop controls
* Faster wake-word detection

---

# Notes

Echo is currently optimized for:

* Windows 11
* NVIDIA GPU acceleration
* Local/offline AI usage

This project is still actively evolving.

---


# Credits

Built using:

* Python
* Faster-Whisper
* Ollama
* Gemma
* Phi-3
* pyttsx3
* sounddevice

