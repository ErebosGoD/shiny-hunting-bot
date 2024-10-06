import time
import pyautogui


def soft_reset(window_title):
    while window_title not in pyautogui.getActiveWindowTitle():
        time.sleep(1)
    keys = ['L', 'R', 'ENTER', 'SPACE']
    for key in keys:
        pyautogui.keyDown(key)
    time.sleep(1)
    for key in keys:
        pyautogui.keyUp(key)


if __name__ == "__main__":
    soft_reset()
