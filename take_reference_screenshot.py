from PIL import ImageGrab
import cv2
import numpy as np


def take_reference_screenshot(path):
    screenshot = ImageGrab.grab()
    screenshot.save(path)
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
