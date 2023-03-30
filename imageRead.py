import timeit

import pyautogui
import bot
import time


def test_time_function(function):
    t0 = time.time()
    function()
    t1 = time.time()
    print(f"Time required {t1-t0}")

    return t1-t0


def high_performance_time_function(function, tries):
    t0 = timeit.timeit(function, number=tries, globals=globals())
    print(f"Function called {tries} requires {t0}. If only one try: {t0/tries}.")
    return t0/tries


def get_wave(level, wave):
    # Has a timing of 0.0309 or 0.031 seconds. Worst 0.035

    mi = match_image(level, wave)

    image = pyautogui.screenshot("image_test.png", region=(900, 0, 1000, 100))

    found_thing = pyautogui.locate(mi, image, grayscale=True)

    if found_thing:
        print(f"Found wave {wave} of level {level}.\n")
        return True
    else:
        return False


def match_image(level, wave):

    # Example: "images/level/0/3.png"

    folder_images = "images/level/"
    level = f"{level}/"
    wave = f"{wave}.png"

    return folder_images + level + wave


if __name__ == "__main__":

    bot.timer(2)

    print(match_image(12, 3))

    bot.small_beep()
