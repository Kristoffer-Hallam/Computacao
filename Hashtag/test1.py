# import time
# from pynput.mouse import Controller, Button

# mouse = Controller()

# print("Move your mouse to the target position...")
# time.sleep(5)

# # Method 1: Two single clicks (most reliable)
# mouse.click(Button.left, 1)
# time.sleep(0.01)   # Adjust if needed
# mouse.click(Button.left, 1)

# print("Two single clicks completed")

import time
from pynput.mouse import Controller, Button

mouse = Controller()

print("Move your mouse to the target position...")
time.sleep(5)

mouse.click(Button.left, 2)

print("Native double-click completed")
