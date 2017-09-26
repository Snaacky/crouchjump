import keyboard
import os
from win32gui import GetWindowText, GetForegroundWindow


def main():
    if not does_config_exists():
        print("Config not found. Creating one.")
        create_config()

    result = read_config()
    jump = result[0]
    crouch = result[1]
    toggle = result[2]

    start_loop(jump, crouch, toggle)


def start_loop(jump, crouch, toggle):
    print("Crouchjump (v1.0.1) loaded. Use {} to crouch jump.".format(toggle))

    while True:
        if "PLAYERUNKNOWN'S BATTLEGROUNDS" in GetWindowText(GetForegroundWindow()):
            keyboard.wait(toggle)
            keyboard.press_and_release(jump)
            keyboard.press_and_release(jump)
            keyboard.press_and_release(crouch)
            keyboard.press_and_release(crouch)


def does_config_exists():
    if os.path.exists(os.getcwd() + "\config.ini"):
        return True


def create_config():
    with open("config.ini", "a+") as file:
        file.write("jump=space\n")
        file.write("crouch=c\n")
        file.write("toggle=shift+space")


def read_config():
    with open("config.ini", "r") as file:
        lines = file.readlines()
        jump = lines[0].replace("jump=", "")
        jump = jump.replace("\n", "")
        crouch = lines[1].replace("crouch=", "")
        crouch = crouch.replace("\n", "")
        toggle = lines[2].replace("toggle=", "")
        return jump, crouch, toggle


if __name__ == '__main__':
    main()
