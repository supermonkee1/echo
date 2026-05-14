import speech_recognition as sr
import numpy as np
import winsound
import time
import threading
import pyttsx3
import keyboard
import sounddevice as sd
import requests
import subprocess

from scipy.io.wavfile import write
from faster_whisper import WhisperModel
model = WhisperModel("base", compute_type="float32")

from commands import ai_chat, screenshot
from commands import apps
from commands import search_web
from commands import ai_router
from commands import app_finder
from commands import chat


wake_listener = sr.Recognizer()

def wait_for_wake_word():

    with sr.Microphone() as source:

        print("\n[IDLE - WAITING FOR 'ECHO']")

        wake_listener.adjust_for_ambient_noise(source, duration=0.3)

        audio = wake_listener.listen(source)

    try:

        text = wake_listener.recognize_google(audio).lower()

        print("Heard:", text)

        return "echo" in text

    except:
        return False
is_speaking = False

def speak(text):

    global interrupt_requested

    interrupt_requested = False

    print("Echo:", text)

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)

    engine.say(text)

    engine.startLoop(False)

    while True:

        engine.iterate()

        # ESC interrupt
        if keyboard.is_pressed("esc"):

            interrupt_requested = True

            engine.stop()

            print("\n[RESPONSE INTERRUPTED]")

            break

        # speech finished naturally
        if not engine.isBusy():
            break

    engine.endLoop()

    engine.stop()

def status(text):
    print(f"\n[{text.upper()}]")

def listen():

    sample_rate = 16000
    silence_threshold = 0.01
    silence_duration = 2.0

    audio_chunks = []

    silent_time = 0

    status("listening")

    print("Speak now...")

    with sd.InputStream(
        samplerate=sample_rate,
        channels=1
    ) as stream:

        while True:

            chunk, overflowed = stream.read(1024)

            audio_chunks.append(chunk)

            volume = abs(chunk).mean()

            # Silence detection
            if volume < silence_threshold:
                silent_time += 1024 / sample_rate
            else:
                silent_time = 0

            # Stop after enough silence
            if silent_time >= silence_duration:
                break

    # Combine chunks
    audio = np.concatenate(audio_chunks, axis=0)

    # Save audio
    write("recording.wav", sample_rate, audio)

    status("transcribing")

    segments, info = model.transcribe(
        "recording.wav",
        language="en"
    )

    full_text = ""

    for segment in segments:
        full_text += segment.text

    return full_text.lower().strip()


def startup_sound():

    winsound.Beep(800, 200)

def listening_sound():

    winsound.Beep(1000, 150)

def success_sound():

    winsound.Beep(1200, 120)

def sleep_sound():

    winsound.Beep(500, 350)

def interrupt_sound():

    winsound.Beep(700, 200)

def not_found_sound():

    winsound.Beep(300, 400)

def error_sound():

    winsound.Beep(400, 300)



    target = target.lower()

    for app_name in apps:

        if target in app_name:

            subprocess.Popen(apps[app_name], shell=True)

            return f"Opening {app_name}"

    return "Application not found"





startup_sound()
status("online")
speak("Hello, I'm Echo. Say 'Echo' to wake me up.")
app_finder.scan_apps()

# Main loop
while True:

    try:

        # Listen for wake word
        if not wait_for_wake_word():
            continue

        listening_sound()
        command = listen()
        print("\nYou said:", command)

        status("processing")

        result = ai_router.run(command)

        action = result.get("action")

        
        # Wake word
        

        command = command.replace("echo", "").strip()
 

        
        # Open app
        if action == "open_app":
            
            success_sound()

            target = result.get("target", "")

            response = app_finder.open_app(target)

            speak(response)

            if interrupt_requested:
                interrupt_sound()
                continue

        
        # Screenshot
        elif action == "screenshot":

            success_sound()

            response = screenshot.run()

            speak(response)
            if interrupt_requested:
                interrupt_sound()
                continue
        

        # Search web
        elif action == "search_web":

            query = result.get("query", "")

            success_sound()

            response = search_web.run(query)

            speak(response)
            if interrupt_requested:
                interrupt_sound()
                continue
            

        # Sleep
        elif action == "sleep":
            sleep_sound()

            speak("Going to sleep")

            status("offline")

            break


    
        # Unknown → Chat response
        else:

            response = chat.run(command)

            print("\n[RESPONSE:]")

            speak(response)
            if interrupt_requested:
                interrupt_sound()
                continue
                

    except WhisperModel.UnknownValueError:
        status("could not understand")
        error_sound()
    except Exception as e:
        print(e)
        break