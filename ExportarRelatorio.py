from lib2to3.pygram import python_grammar
import pyautogui
import PIL
import time

pyautogui.press(['win'])
pyautogui.write('remote')
pyautogui.press('enter')

time.sleep(2.5)

pyautogui.click('CISS PRATA.png')
pyautogui.click('OPEN SESSION.png')

time.sleep(12)

pyautogui.click('LOGINPRATA.png')
pyautogui.press(['tab'])
pyautogui.write('2550')
pyautogui.press(['enter'])

time.sleep(2.5)

pyautogui.press(['alt','r','c'])

time.sleep(0.5)

pyautogui.write('150068')
pyautogui.press(['tab','space'])

time.sleep(0.5)

ljP = 1

strMP=str(ljP)

for ljP in range(1,12):
    
    
    pyautogui.press('tab', presses=5)
    pyautogui.write(strMP)
    pyautogui.press('tab', presses=4)
    pyautogui.press('space')
    
    time.sleep(10)
    
    pyautogui.press('x')
    pyautogui.write(strMP+'rel')
    pyautogui.press('tab')
    pyautogui.write('m')
    pyautogui.press(['tab','space','f'])
    
    ljP=int(strMP)
    ljP=+1
    
    time.sleep(0.5)

pyautogui.press('tab', presses=5)
pyautogui.write(strMP)
pyautogui.press('tab', presses=4)
pyautogui.press('space')

time.sleep(10)

pyautogui.press('x')

    