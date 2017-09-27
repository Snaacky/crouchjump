import configparser
import keyboard
import os
from win32gui import GetWindowText, GetForegroundWindow

config = configparser.RawConfigParser()


def main():
    '''
    Checks for config, if non-existent, creates one. If config exists,
    it will read the options from it and pass them to start_loop.
    '''
    if not os.path.exists(os.getcwd() + "\config.ini"):
        print("Config not found. Creating one.")
        create_config()
    else:
        config.read('config.ini')

    jump = config.get("crouchjump", "jump")
    crouch = config.get("crouchjump", "crouch")
    toggle = config.get("crouchjump", "toggle")

    start_loop(jump, crouch, toggle)


def start_loop(jump, crouch, toggle):
    '''
    An infinite loop that takes the configuration options, waits for a toggle,
    and if alt-tabbed into PUBG, will send the crouch jump keypresses.
    '''
    print("Crouchjump (v1.0.2) loaded. Use {} to crouch jump.".format(toggle))

    while True:
        if "PLAYERUNKNOWN'S BATTLEGROUNDS" in GetWindowText(GetForegroundWindow()):
            keyboard.wait(toggle)
            keyboard.press_and_release(jump)
            keyboard.press_and_release(jump)
            keyboard.press_and_release(crouch)
            keyboard.press_and_release(crouch)


def create_config():
    '''
    Creates default configuration.
    '''
    config.add_section('crouchjump')
    config.set('crouchjump', 'jump', 'space')
    config.set('crouchjump', 'crouch', 'c')
    config.set('crouchjump', 'toggle', 'shift+space')

    with open("config.ini", "w") as config_file:
        config.write(config_file)


if __name__ == '__main__':
    main()
