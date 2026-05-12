import pyautogui
from datetime import datetime

def run():

    filename = f"screenshots/screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

    pyautogui.screenshot(filename)

    return "Screenshot taken"