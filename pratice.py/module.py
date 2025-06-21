import pyautogui

# width, height = pyautogui.size()
# print(width, height)
# x, y = pyautogui.position()

# print(x,y)

pyautogui.moveTo(1764, 761, duration=1)
# pyautogui.doubleClick()

# pyautogui.moveRel(-778, 66, duration=1)  # Move 100px to the right
screenshot = pyautogui.screenshot()
screenshot.save("myscreen.png")
