import time
import pyautogui
import cv2
import numpy as np
from soft_reset import soft_reset
from sequence_execution import execute_sequence
from take_screenshot import take_screenshot
from take_reference_screenshot import take_reference_screenshot

SCREENSHOT_PATH = "current_screenshot.png"
SOFT_RESET_COUNT = 0


def is_shiny_pixel(current_frame, reference_frame, x, y, threshold=50):
    # Extrahiere die Pixelwerte an der Position (x, y)
    current_pixel = current_frame[y, x]
    reference_pixel = reference_frame[y, x]

    # Berechne die euklidische Distanz zwischen den Pixeln
    difference = np.linalg.norm(current_pixel - reference_pixel)

    print(f"Current pixel: {current_pixel}, Reference pixel: {
          reference_pixel}, Difference: {difference}")

    # Vergleiche die Differenz mit dem Schwellenwert
    return difference > threshold


def select_region_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        regions = []
        for line in lines:
            coordinates = line.strip().split(',')
            if len(coordinates) == 4:
                regions.append(tuple(map(int, coordinates)))
    return regions


def main():
    global SOFT_RESET_COUNT

    PIXEL_X = 1951
    PIXEL_Y = 316
    pokemon_is_shiny = False
    print("Record a button sequence using record_sequence.py")
    input("Press Enter, when you're ready...")

    while pyautogui.getActiveWindowTitle() != "[60/60] melonDS 0.9.5":
        time.sleep(1)

    soft_reset()
    time.sleep(10)
    execute_sequence('sequence.json')

    time.sleep(4.55)
    take_reference_screenshot("reference_screenshot.png")

    while not pokemon_is_shiny:

        while True:

            soft_reset()
            time.sleep(10)
            execute_sequence('sequence.json')

            time.sleep(4.6)

            current_screenshot = take_screenshot(SCREENSHOT_PATH)
            reference_image = cv2.imread("reference_screenshot.png")
            if current_screenshot is not None and reference_image is not None:
                if is_shiny_pixel(current_screenshot, reference_image, PIXEL_X, PIXEL_Y):

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
