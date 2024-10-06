import time
import json
import pyautogui
import cv2
import os
import numpy as np
from soft_reset import soft_reset
from sequence_execution import execute_sequence
from take_screenshot import take_screenshot
from take_reference_screenshot import take_reference_screenshot
from savestate import savestate


def load_config(config_path):
    with open(config_path, "r") as file:
        config = json.load(file)
    return config


def save_config(config_path, config):
    with open(config_path, "w") as file:
        json.dump(config, file, indent=4)


def is_shiny_pixel(current_frame, reference_frame, x, y, threshold=50):
    current_pixel = current_frame[y, x]
    reference_pixel = reference_frame[y, x]

    difference = np.linalg.norm(current_pixel - reference_pixel)

    # print(f"Current pixel: {current_pixel}, Reference pixel: {
    #      reference_pixel}, Difference: {difference}")

    return difference > threshold


def main():
    CONFIG_PATH = "config.json"
    config = load_config(CONFIG_PATH)
    SOFT_RESET_COUNT = config["softResetCount"]
    pixel_x, pixel_y = config["pixelCoordinates"]
    pokemon_is_shiny = False
    emulator = config["emulator"]

    startup_time_after_reset = config["emulatorResetTimeInSeconds"]
    screenshot_time = config["screenshotTimeInSeconds"]
    print("Config loaded successfully!")
    print("Record a button sequence using record_sequence.py")
    input("Press Enter, when you're ready...")

    # put your emulator window title here!

    while emulator not in pyautogui.getActiveWindowTitle():
        time.sleep(1)

    # while pyautogui.getActiveWindowTitle() != "[60/60] melonDS 0.9.5":
    #    time.sleep(1)

    if not os.path.exists(r"screenshots\reference_screenshot.png"):
        soft_reset(emulator)
        time.sleep(startup_time_after_reset)
        execute_sequence('sequence.json', emulator)
        time.sleep(screenshot_time)
        take_reference_screenshot(r"screenshots\reference_screenshot.png")

    try:
        while not pokemon_is_shiny:

            while True:

                soft_reset(emulator)
                time.sleep(startup_time_after_reset)
                execute_sequence('sequence.json', emulator)

                time.sleep(screenshot_time)

                current_screenshot = take_screenshot(
                    r"screenshots\current_screenshot.png")
                reference_image = cv2.imread(
                    r"screenshots\reference_screenshot.png")
                if current_screenshot is not None and reference_image is not None:
                    if is_shiny_pixel(current_screenshot, reference_image, pixel_x, pixel_y):
                        savestate()
                        pokemon_is_shiny = True
                        print("Shiny Pokémon found!")
                        print(f"Soft Resets: {SOFT_RESET_COUNT}")
                        break

                # time.sleep(1)

                SOFT_RESET_COUNT += 1
                print("Current Resets:", SOFT_RESET_COUNT)
    finally:
        config["softResetCount"] = SOFT_RESET_COUNT
        save_config(CONFIG_PATH, config)


if __name__ == "__main__":
    main()
