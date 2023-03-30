import pyautogui
import bot
import numpy


def get_money():
    image = pyautogui.screenshot("image_test.png", region=(200, 0, 600, 100))

    found_thing = pyautogui.locate("images/numbers/0.png", image, grayscale=True)

    return found_thing


if __name__ == "__main__":

    bot.timer(5)

    print(get_money())

    bot.small_beep()
