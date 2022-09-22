import keyboard
import pyautogui
from time import sleep
from logic.screenshot import make_screenshot, read
from logic.get_monitor import *


SLEEP_TIME = 2


def move_and_click(x: int, y: int):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def main():
    print("Start checking buttons...")

    """
    The function starts the cycle of creating screenshots and
    checks whether the required text is present on these screenshots.
    """
    while True:
        make_screenshot()
        if "Следующая серия" in str(read()[1]):

            # press button "next episode" in full screen
            move_and_click(*BUTTON_NEXT_COORDS)  # (2450, 1360)
            sleep(SLEEP_TIME)

            # press play button
            move_and_click(
                int(monitor.split("x")[0]) // 2, int(monitor.split("x")[1]) // 2
            )
            sleep(SLEEP_TIME)

            # press button full screen
            keyboard.send("f")
            sleep(SLEEP_TIME)

        if "Skip Ad" in str(read()[2]):

            # press button skip ad
            move_and_click(*BUTTON_AD_COORDS)  # (1400, 950)
            sleep(SLEEP_TIME)

            # press button full screen
            keyboard.send("f")
            sleep(SLEEP_TIME)

        if "Пропустить заставку" in str(read()[0]):

            # press button skip opening
            move_and_click(*BUTTON_SKIP_COORDS)  # (90, 1360)
            sleep(SLEEP_TIME)
            pyautogui.moveTo(1555, 966)


if __name__ == "__main__":
    main()
