import time
import pyautogui

# Funktion zum Ausführen der Soft-Reset-Sequenz (L+R+Start+Select gleichzeitig)


def soft_reset():
    # ENTER und SPACE entsprechen hier Start und Select, ggf. anpassen
    keys = ['L', 'R', 'ENTER', 'SPACE']
    for key in keys:
        pyautogui.keyDown(key)
    time.sleep(1)  # Halte die Tasten für eine Sekunde gedrückt
    for key in keys:
        pyautogui.keyUp(key)


if __name__ == "__main__":
    soft_reset()
