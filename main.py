import os
import subprocess

import keyboard

SCAN_TARGETS = {
    79: "discord:", #Numpad1
    80: "roblox:", #Numpad2
    81: "roblox-studio:", #Numpad3
    75: "steam:", #Numpad4
    76: "https://www.google.com", #Numpad5
    77: "https://www.youtube.com", #Numpad6
    71: "https://www.instagram.com", #Numpad7
    73: "modrinth:", #Numpad8
}

VSCODE_SCAN = 72


def launch(target):
    try:
        os.startfile(target)
    except OSError:
        pass


def launch_vscode():
    try:
        subprocess.Popen(
            ["code"],
            shell=True,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
    except OSError:
        pass


def on_press(event):
    if not event.is_keypad:
        return
    if event.scan_code == VSCODE_SCAN:
        launch_vscode()
        return
    target = SCAN_TARGETS.get(event.scan_code)
    if target:
        launch(target)


def main():
    keyboard.on_press(on_press)
    try:
        keyboard.wait()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()