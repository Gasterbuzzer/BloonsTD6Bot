import pytesseract
import numpy

import cv2
from PIL import ImageGrab


def imToString():
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    while (True):
        # ImageGrab-To capture the screen image in a loop.
        # Bbox used to capture a specific area.
        cap = ImageGrab.grab(bbox=(365, 17, 557, 61))

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        tesstr = pytesseract.image_to_string(
            cv2.cvtColor(numpy.array(cap), cv2.COLOR_BGR2HSV),
            lang='eng')
        print(tesstr)


def get_money():
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

    cap = ImageGrab.grab(bbox=(365, 17, 557, 61))
    text = ""

    while text == "":
        text = pytesseract.image_to_string(
            cv2.cvtColor(numpy.array(cap), cv2.COLOR_BGR2HSV),
            lang='eng')

    text = text.replace(')', '')

    text = int(text)

    return text


if __name__ == "__main__":
    strs = "205)"
    strs = strs.replace(')', '')

    print(int(strs))
