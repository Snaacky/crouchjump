import keyboard
from win32gui import GetWindowText, GetForegroundWindow

print("Crouchjump.py loaded. Use shift+space to crouch jump.")

while True:
    if "PLAYERUNKNOWN'S BATTLEGROUNDS" in GetWindowText(GetForegroundWindow()):
        keyboard.wait("shift+space")
        keyboard.press_and_release("space")
        keyboard.press_and_release("space")
        keyboard.press_and_release("c")
        keyboard.press_and_release("c")