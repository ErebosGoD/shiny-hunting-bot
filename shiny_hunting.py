import time
import os
import pyautogui
import cv2
import numpy as np
import json
from PIL import ImageGrab
from soft_reset import soft_reset
from sequence_execution import execute_sequence
from shinyHuntingBot.take_screenshot import take_screenshot, take_reference_screenshot

# Variable für die Region des Pokémon-Kampfs

SCREENSHOT_PATH = "current_screenshot.png"
SOFT_RESET_COUNT = 0


# Funktion zum Vergleichen von Screenshots


def is_shiny(current_frame, reference_frame, threshold=0.012):
    # Unterschied berechnen
    diff = cv2.absdiff(current_frame, reference_frame)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    non_zero_count = np.count_nonzero(thresh)
    total_pixels = thresh.size
    difference_ratio = non_zero_count / total_pixels
    print(f"Difference ratio: {difference_ratio}")
    return difference_ratio < threshold

# Funktion zur Auswahl der Region aus einer Textdatei


def select_region_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        regions = []
        for line in lines:
            coordinates = line.strip().split(',')
            if len(coordinates) == 4:
                regions.append(tuple(map(int, coordinates)))
    return regions

# Hauptprogramm


def main():
    global SOFT_RESET_COUNT
    pokemon_is_shiny = False
    # Benutzer die Sequenz aufzeichnen lassen
    print("Mache eine Tastensequenz-Aufzeichnung und speichere sie als 'sequence.json'.")
    input("Drücke Enter, wenn du bereit bist...")

    # Warten, bis der erste Kampf beginnt
    input("Drücke Enter, wenn der erste Kampf beginnt...")

    # reference_screenshot = take_reference_screenshot(
    # "reference_screenshot.png")

    while pokemon_is_shiny == False:

        while True:
            # Soft-Reset ausführen und neuen Kampf starten
            soft_reset()
            time.sleep(10)  # Warten, bis das Spiel neu gestartet ist
            # Aufgezeichnete Sequenz laden
            execute_sequence('sequence.json')

            # Warten, bis der Emulator im Vordergrund ist
            while pyautogui.getActiveWindowTitle() != "[60/60] melonDS 0.9.5":
                time.sleep(1)

            # Warten, bis der Emulator geladen hat (ggf. anpassen)
            time.sleep(4.5)

            # Neuen Screenshot aufnehmen und vergleichen
            current_screenshot = take_screenshot(SCREENSHOT_PATH)
            reference_image = cv2.imread("reference_screenshot.png")
            if is_shiny(current_screenshot, reference_image):
                # Schillerndes Pokémon gefunden
                pokemon_is_shiny = True
                print("Schillerndes Pokémon gefunden!")
                break

            # Aktuellen Screenshot als neuen Referenz-Screenshot speichern
            reference_screenshot = current_screenshot

            time.sleep(1)  # Kurze Pause, um den Prozess stabil zu halten

            SOFT_RESET_COUNT += 1
        if pokemon_is_shiny:
            print(f"Anzahl der Soft Resets: {SOFT_RESET_COUNT}")
            break


if __name__ == "__main__":
    main()
