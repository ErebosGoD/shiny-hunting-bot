import time
import pyautogui


def savestate():
    keys = ['SHIFT', 'F1']
    for key in keys:
        pyautogui.keyDown(key)
    time.sleep(1)
    for key in keys:
        pyautogui.keyUp(key)


if __name__ == "__main__":
    savestate()
