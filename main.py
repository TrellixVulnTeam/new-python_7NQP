import pyautogui
import time
pyautogui.FAILSAFE=False
for i in range(0,250):
    time.sleep(2)
    pyautogui.typewrite('Bondhu')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite('Tui shera  !')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite('Best expression')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite('Best Acting')
    pyautogui.press('enter')