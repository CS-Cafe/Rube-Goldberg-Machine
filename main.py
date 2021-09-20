from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
try:
    while 1:
        time.sleep(3)
        keyboard.press(Key.alt)
        keyboard.press(Key.f4)
except KeyboardInterrupt:
    pass
