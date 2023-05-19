import os
import numpy as np
import pyautogui
import cv2

# Pillow, opencv-python, pyautogui
# Linux - scrot
# DOES NOT WORK ON WAYLAND LINUX


SCRIPT_PATH = os.path.dirname(__file__)
SCREENSHOT_PATH = os.path.join(SCRIPT_PATH, "screenshots")


def take_screenshot(path_to_screenshot):
    tmp_image_path = os.path.join(path_to_screenshot, "image1.png")
    image = pyautogui.screenshot(tmp_image_path)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.path.join(tmp_image_path, "image1.png"), image)


def compare_screenshots():
    pass


def send_alert():
    pass


take_screenshot(SCREENSHOT_PATH)
