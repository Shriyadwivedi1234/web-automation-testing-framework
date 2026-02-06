import os
from datetime import datetime


def take_screenshot(driver, name):

    folder = "screenshots"

    if not os.path.exists(folder):
        os.mkdir(folder)

    time = datetime.now().strftime("%Y%m%d_%H%M%S")

    file = f"{folder}/{name}_{time}.png"

    driver.save_screenshot(file)
