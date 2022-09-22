import mss.tools
import cv2  # opencv-python
import pytesseract
from logic.get_monitor import *


pytesseract.pytesseract.tesseract_cmd = "D:\\Tesseract\\tesseract.exe"


def make_screenshot():
    """
    The function creates a screenshot and saves it in the 'screenshots' directory
    """
    with mss.mss() as sct:
        skip_sct = "logic/screenshots/skip.png".format(**BUTTON_SKIP_SIZE)
        next_sct = "logic/screenshots/next.png".format(**BUTTON_NEXT_SIZE)
        ad_sct = "logic/screenshots/ad.png".format(**BUTTON_AD_SIZE)

        next_img = sct.grab(BUTTON_NEXT_SIZE)
        skip_img = sct.grab(BUTTON_SKIP_SIZE)
        ad_img = sct.grab(BUTTON_AD_SIZE)

        mss.tools.to_png(skip_img.rgb, skip_img.size, output=skip_sct)
        mss.tools.to_png(next_img.rgb, next_img.size, output=next_sct)
        mss.tools.to_png(ad_img.rgb, ad_img.size, output=ad_sct)


def read():
    """Read text from screenshots in 'screenshot' directory"""
    img_next = cv2.imread("logic/screenshots/next.png")
    img_next = cv2.cvtColor(img_next, cv2.COLOR_BGR2RGB)

    img_skip = cv2.imread("logic/screenshots/skip.png")
    img_skip = cv2.cvtColor(img_skip, cv2.COLOR_BGR2RGB)

    img_ad = cv2.imread("logic/screenshots/ad.png")
    img_ad = cv2.cvtColor(img_ad, cv2.COLOR_BGR2RGB)

    ai_next = pytesseract.image_to_string(img_next, lang="rus", config="--psm 7")
    ai_skip = pytesseract.image_to_string(img_skip, lang="rus", config="--psm 7")
    ai_ad = pytesseract.image_to_string(img_ad, config="--psm 7")
    return ai_skip, ai_next, ai_ad
