from PIL import ImageGrab
import cv2
import numpy as np


def select_region_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        regions = []
        for line in lines:
            coordinates = line.strip().split(',')
            if len(coordinates) == 4:
                regions.append(tuple(map(int, coordinates)))
    return regions


def take_screenshot(path):
    POKEMON_SCREEN_REGION = None
    regions = select_region_from_file('regions.txt')
    print(f"Die ausgewählten Regionen sind: {regions}")
    screenshot = ImageGrab.grab(bbox=POKEMON_SCREEN_REGION)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, screenshot)
    return screenshot


def take_reference_screenshot(path):
    POKEMON_SCREEN_REGION = None
    regions = select_region_from_file('regions.txt')
    print(f"Die ausgewählten Regionen sind: {regions}")
    screenshot = ImageGrab.grab(bbox=POKEMON_SCREEN_REGION)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, screenshot)
    return screenshot
