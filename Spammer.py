import pyautogui, time
time.sleep(4)
for c in range(100):
    pyautogui.typewrite("TESTE")
    pyautogui.press("enter")
