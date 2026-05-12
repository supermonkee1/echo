import speech_recognition as sr
from commands import ai_chat
from commands import ai_chat, screenshot
from commands import apps
import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

model = WhisperModel("base", compute_type="float32")

import threading
import pyttsx3
import keyboard

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
    duration = 5

    status("listening")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1
    )

    sd.wait()

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


while True:

    try:

        # LISTEN ONLY
        if not wait_for_wake_word():
            continue


        command = listen()

        print(f"heard: {command}")

        # WAKE WORD
        

        command = command.replace("echo", "").strip()

        print("processing...")    

            # SLEEP
        if "sleep" in command:

                speak("Going to sleep")

                status("sleeping")

                break

            # SCREENSHOT
        elif "screenshot" in command:

                response = screenshot.run()
                speak(response)

                if interrupt_requested:
                    continue
                    
                

            # CHROME
        elif "open" in command:

                response = apps.run(command)
                speak(response)

                if interrupt_requested:
                    continue


        else:
                status("thinking")

                response = ai_chat.run(command)

                speak(response)

                if interrupt_requested:
                    continue


        

    except WhisperModel.UnknownValueError:
        status("could not understand")

    except Exception as e:
        print(e)
        break