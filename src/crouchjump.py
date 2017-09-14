import keyboard
import sys
from win32gui import GetWindowText, GetForegroundWindow


def main():
    print("{} loaded. You can crouch jump with shift+space.".format(sys.argv[0]))

    while True:
        if "PLAYERUNKNOWN'S BATTLEGROUNDS" in GetWindowText(GetForegroundWindow()):
            if keyboard.is_pressed("shift+space"):
                keyboard.press_and_release("space")
                keyboard.press_and_release("ctrl")


if __name__ == '__main__':
    main()
