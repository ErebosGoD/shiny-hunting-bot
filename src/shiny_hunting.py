import time
import pyautogui
import cv2
import numpy as np
from soft_reset import soft_reset
from sequence_execution import execute_sequence
from take_screenshot import take_screenshot
from take_reference_screenshot import take_reference_screenshot
from savestate import savestate


def is_shiny_pixel(current_frame, reference_frame, x, y, threshold=50):
    current_pixel = current_frame[y, x]
    reference_pixel = reference_frame[y, x]

    difference = np.linalg.norm(current_pixel - reference_pixel)

    print(f"Current pixel: {current_pixel}, Reference pixel: {
          reference_pixel}, Difference: {difference}")
    
    return difference > threshold


def select_pixel_from_file(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
        coordinates = line.split(',')
        if len(coordinates) == 2:
            return int(coordinates[0]), int(coordinates[1])
    raise ValueError("Invalid coordinate format in file")


def main():
    SOFT_RESET_COUNT = 0

    pokemon_is_shiny = False
    pixel_x, pixel_y = select_pixel_from_file(r"coordinates.txt")
    print("Coordinates read successfully!")
    print("Record a button sequence using record_sequence.py")
    input("Press Enter, when you're ready...")

    # put your emulator window title here!
    while pyautogui.getActiveWindowTitle() != "[60/60] melonDS 0.9.5":
        time.sleep(1)

    soft_reset()
    time.sleep(10)
    execute_sequence('sequence.json')

    time.sleep(4.55)
    take_reference_screenshot(r"screenshots\reference_screenshot.png")

    while not pokemon_is_shiny:

        while True:

            soft_reset()
            time.sleep(10)
            execute_sequence('sequence.json')

            time.sleep(4.6)

            current_screenshot = take_screenshot(
                r"screenshots\current_screenshot.png")
            reference_image = cv2.imread(
                r"screenshots\reference_screenshot.png")
            if current_screenshot is not None and reference_image is not None:
                if is_shiny_pixel(current_screenshot, reference_image, pixel_x, pixel_y):
                    savestate()
                    pokemon_is_shiny = True
                    print("Shiny Pokémon found!")
                    break

            time.sleep(1)

            SOFT_RESET_COUNT += 1
            print("Current Resets:", SOFT_RESET_COUNT)
        if pokemon_is_shiny:
            print(f"Soft Resets: {SOFT_RESET_COUNT}")
            break


if __name__ == "__main__":
    main()