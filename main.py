import speech_recognition as sr
import pyttsx3
from commands import ai_chat
from commands import ai_chat, screenshot
from commands import apps
listener = sr.Recognizer()

def status(text):
    print(f"\n[{text.upper()}]")

def speak(text):

    print("Echo:", text)

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.setProperty('rate', 170)

    engine.say(text)
    engine.runAndWait()

    engine.stop()

speak("Echo online")

while True:

    try:

        # LISTEN ONLY
        with sr.Microphone() as source:

            status("listening")

            listener.adjust_for_ambient_noise(source, duration=0.5)

            audio = listener.listen(source)

        # PROCESS AFTER microphone closes
        command = listener.recognize_google(audio).lower()

        print("You said:", command)

        # WAKE WORD
        if "echo" in command:

            command = command.replace("echo", "").strip()

            print(f"processing: {command}")    

            # SLEEP
            if "sleep" in command:

                speak("Going to sleep")

                break

            # SCREENSHOT
            elif "screenshot" in command:

                response = screenshot.run()
                speak(response)

            # CHROME
            elif "open" in command:

                response = apps.run(command)
                speak(response)

            else:
                status("thinking")

                response = ai_chat.run(command)

                speak(response)

        else:
            status("wake word not detected")

    except sr.UnknownValueError:
        status("could not understand")

    except Exception as e:
        print(e)