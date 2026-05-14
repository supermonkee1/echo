import os

# Dictionary of apps

apps = {
    "chrome": "start chrome",

    "youtube": "start chrome https://www.youtube.com",

    "steam": r"C:\Program Files (x86)\Steam\steam.exe",

    "spotify": r"C:\Users\adi\AppData\Roaming\Spotify\Spotify.exe",
    
    "discord": r"C:\Users\adi\AppData\Local\Discord\app-1.0.9003\Discord.exe",
    
    "delta": r"C:\Users\adi\Desktop\DELTARUNE.url",

    "notepad": "start notepad",

    "calculator": "start calculator",

    "roblox": r"C:\Users\adi\Desktop\Roblox Player.exe",

    "ultra": r"C:\Users\adi\Desktop\Ultrakill.url"


}

def run(command):

    for app_name in apps:

        if app_name in command:

            os.system(apps[app_name])

            return f"Opening {app_name}"

    return "Application not found"