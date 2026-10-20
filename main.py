import speech_recognition as sr
import webbrowser
import datetime
import subprocess
from google import genai
from google.genai import types

client = genai.Client()

SITES = {
    "youtube": "https://www.youtube.com",
    "tiktok": "https://www.tiktok.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "twitter": "https://www.x.com",
    "whatsapp": "https://web.whatsapp.com",
    "linkedin": "https://www.linkedin.com",
}

def speak(text):
    print("Jarvis:", text)
    safe = text.replace("'", "''")
    subprocess.run([
        "powershell", "-Command",
        f"Add-Type -AssemblyName System.Speech; "
        f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{safe}')"
    ])

def ask_ai(question):
    for model in ["gemini-3.5-flash-lite", "gemini-3.8-flash"]:
        try:
            response = client.models.generate_content(
                model=model,
                contents=question,
                config=types.GenerateContentConfig(
                    system_instruction="You are Jarvis, a voice assistant. Answer in 1-2 short sentences. No markdown."
                ),
            )
            return response.text
        except Exception as e:
            print(f"AI error with {model}:", e)
    return "Sorry, I could not get an answer."

def process(command):
    command = command.lower()
    squashed = command.replace(" ", "")

    if "open" in command:
        for name, url in SITES.items():
            if name in squashed:
                speak(f"Opening {name}")
                webbrowser.open(url)
                return True

    if "time" in command:
        speak(datetime.datetime.now().strftime("It is %I:%M %p"))
    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        return False
    else:
        speak(ask_ai(command))
    return True

r = sr.Recognizer()
r.pause_threshold = 0.5

speak("Jarvis is ready")
running = True
while running:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, phrase_time_limit=4)
        command = r.recognize_google(audio)
        print("You said:", command)
        running = process(command)
    except sr.UnknownValueError:
        print("Didn't catch that")
    except sr.RequestError:
        speak("Internet problem")