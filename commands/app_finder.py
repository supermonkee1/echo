import os
import subprocess

# Start Menu locations
SEARCH_PATHS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(
        r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
    )
]

apps = {}

def scan_apps():

    global apps

    apps.clear()

    for base_path in SEARCH_PATHS:

        for root, dirs, files in os.walk(base_path):

            for file in files:

                if file.endswith(".lnk"):

                    app_name = file.replace(".lnk", "").lower()

                    full_path = os.path.join(root, file)

                    apps[app_name] = full_path

def open_app(target):

    target = target.lower()

    for app_name in apps:

        if target in app_name:

            subprocess.Popen(apps[app_name], shell=True)

            return f"Opening {app_name}"

    return "Application not found"