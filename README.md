# Jarvis Voice Assistant

A Python voice assistant I built as a beginner project. You speak, and Jarvis listens, answers out loud, and opens websites.

## Features
- Listens to your voice with a microphone
- Opens websites (YouTube, TikTok, Facebook, Instagram, WhatsApp, LinkedIn)
- Tells the current time
- Answers any question using the Gemini AI
- Speaks its replies out loud
- Say "stop" or "exit" to close it

## Technologies
- Python 3.12
- SpeechRecognition + PyAudio (voice input)
- Google Gemini API (AI answers)
- Windows built-in voice (voice output)

## How to install
1. Install Python 3.12 (PyAudio does not install on Python 3.14)
2. Create a virtual environment and install the packages:
```
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
3. Get a free API key at aistudio.google.com and save it:
```
setx GEMINI_API_KEY "your-key-here"
```
4. Close and reopen the terminal.

## How to run
```
python main.py
```
Then try: "open YouTube", "what time is it", "what is Python?"

## What I learned
- Using virtual environments and `requirements.txt`
- Working with APIs and keeping API keys out of the code
- Fixing real errors (package versions, build errors, API limits)

## Future ideas
- Add a wake word ("Hey Jarvis")
- Add more commands (weather, open apps)
