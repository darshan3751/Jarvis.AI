# 🤖 Jarvis AI Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green.svg)
![LLM](https://img.shields.io/badge/LLM-Groq%20%7C%20Cohere-orange.svg)

Welcome to **Jarvis AI Assistant** — a powerful, modernized, desktop-based virtual assistant written in Python. Designed with an advanced custom Graphical User Interface, Jarvis is built to serve as your intelligent companion for PC automation, real-time web searches, conversational AI capabilities, and high-quality image generation.

---

## ✨ Key Features

- **🗣️ Advanced Speech-to-Text & Text-to-Speech:** Uses cutting edge voice recognition and seamless Edge-TTS to provide fluid, real-time voice interactions.
- **🧠 Intelligent Decision Making Model (DMM):** Parses user queries dynamically to decide whether to chat, search the web, automate tasks, or generate images based on context.
- **💻 Robust PC Automation:** Open/close desktop applications, write/read emails, manage system settings, play videos, and control your workflow hands-free.
- **🌐 Realtime Web Search Engine:** Scrapes and synthesizes live data from Google natively when you need up-to-date information.
- **🎨 On-Demand Image Generation:** Integrated text-to-image AI capabilities, allowing you to generate visuals purely from voice commands.
- **🖥️ Beautiful Custom GUI:** Built with PyQt5, featuring dynamic status indicators (Listening, Thinking, Answering) and threaded operations to ensure a highly responsive user experience.
- **⚡ Supercharged by Groq & Cohere:** Backed by incredibly fast LLM APIs that ensure latency is kept to an absolute minimum.

---

## 🛠️ Architecture Overview

The software is structured in a highly modular way:
- **`Frontend/`**: Houses all graphical components and GUI loops driven by PyQt5.
- **`Backend/`**: Contains the core logic scripts:
  - `Model.py`: The LLM decision-making engine.
  - `Automation.py`: The core automation handler for PC tasks.
  - `RealtimeSearchEngine.py`: Handles Google searches and scraping.
  - `Chatbot.py`, `SpeechToText.py`, `TextToSpeech.py`, `ImageGeneration.py`
- **`Main.py`**: The main execution loop utilizing threading daemon processes to handle background AI queries and foreground GUI updating simultaneously.

---

## 🚀 Getting Started

### Prerequisites

You must have **Python 3.10+** installed. You will also need valid API keys for:
- Groq (For super-fast chat completions)
- Cohere (For alternative NLP operations)
- HuggingFace (For Image Generation)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/darshan3751/Jarvis.AI.git
   cd Jarvis.AI
   ```

2. **Install all dependencies:**
   ```bash
   pip install -r Requirements.txt
   ```

3. **Configure the Environment:**
   Create a `.env` file in the root directory (refer to the code for required keys). You will need variables like:
   ```env
   Username=YourName
   Assistantname=Jarvis
   GroqAPIKey=your_groq_api_key
   CohereAPIKey=your_cohere_api_key
   HFAPIKey=your_huggingface_api_key
   ```
   *(Ensure you replace these with your actual keys)*

4. **Run Jarvis:**
   ```bash
   python Main.py
   ```

---

## 📸 Sneak Peek
*(Developers can add screenshots of the PyQt5 GUI in action here)*

---

## 💡 Future Roadmap
- Deeper integration with Smart Home IoT devices.
- Multi-modal support (uploading images for context).
- Web-based Dashboard companion app.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
