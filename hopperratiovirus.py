import pyautogui
import time

#starting thing
pyautogui.hotkey('win', 'r')
pyautogui.write('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSN_1qswtpJwxlEky_FFWLGATmoQ2CmNXezh9RUWKSD&s') #hopper image
pyautogui.press('enter')

#funtion
def func():
    time.sleep(1)
    pyautogui.hotkey('win', 'r')
    pyautogui.press('enter')

#loop
for x in range(200):
    func()