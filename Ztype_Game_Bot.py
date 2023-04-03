import time

import cv2
import easyocr
import numpy as np
import pyautogui as pag
from PIL import Image

IMAGE_PATH = "C:/Users/hammaad/Desktop/ztype.jpg"

skip_words = ['ztype', 'new game', 'settings', 'my stats',
              'phoboslab', 'load your own text', 'wave', 'score']

PREV_RESULT = list()

RESIZE_RATIO = (500, 800)
PAUSE_BUTTON = (375, 405)
RESUME_BUTTON = (800, 1390)
GAME_SCREEN = (800, 800)
PYCHARM_SCREEN = (3000, 800)
ENGLISH_ALPHA = "thequickbrownfoxjumpedoverthelazydog"


def resize_image():
    foo = Image.open(IMAGE_PATH)
    print(f"Size of screenshot= {foo.size}")
    foo = foo.resize(RESIZE_RATIO, Image.ANTIALIAS)
    foo.save(IMAGE_PATH, optimize=True, quality=95)
    foo = Image.open(IMAGE_PATH)
    print(f"Size of resized screenshot= {foo.size}")


def get_ocr_result(prev_result):
    # pause the game
    print(f'Pausing the game....')
    pag.click(PAUSE_BUTTON[0], PAUSE_BUTTON[1])
    reader = easyocr.Reader(['en'], detector='dbnet18')
    result = reader.readtext(IMAGE_PATH, detail=0, batch_size=8)
    result = [block.lower() for block in result if not block.lower().startswith(tuple(skip_words))]
    result.sort(key=len)

    # stuck letter
    if len(prev_result):
        prev_result.sort(key=len, reverse=True)
    for prev_word in prev_result:
        if prev_word in result:
            result.clear()
            result.append(ENGLISH_ALPHA)

    pag.click(RESUME_BUTTON[0], RESUME_BUTTON[1])
    print(f'Resume and Typing this: {result}')
    return result


def transform_image_colour():
    img = cv2.imread(IMAGE_PATH)
    img[np.where((img < [100, 100, 100]).all(axis=2))] = [0, 0, 0]
    img[np.where((img >= [100, 100, 100]).all(axis=2))] = [225, 225, 225]
    cv2.imwrite(IMAGE_PATH, img)
    print("Completed color transformations")


while True:
    pag.press('space')
    im = pag.screenshot(region=(325, 355, 950, 1430), imageFilename=IMAGE_PATH)
    resize_image()
    transform_image_colour()
    pag.click(GAME_SCREEN[0], GAME_SCREEN[1])
    pag.click(PYCHARM_SCREEN[0], PYCHARM_SCREEN[1])
    pag.click(GAME_SCREEN[0], GAME_SCREEN[1])
    ocr_result = get_ocr_result(PREV_RESULT)
    PREV_RESULT = ocr_result
    for word in ocr_result:
        pag.write(word)
        print(f'Typed word: {word}')
        time.sleep(0.25)
#
# while 1:
#     print(pag.position())
