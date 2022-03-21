import pyautogui
import PIL
import time
import os


pyautogui.press(['win'])
pyautogui.write('remote')
pyautogui.press('enter')

time.sleep(1.5)

pyautogui.click('CISS PRATA.png')
pyautogui.click('OPEN SESSION.png')

time.sleep(12)

pyautogui.click()
pyautogui.press(['tab'])
pyautogui.write('2550')
pyautogui.press(['enter'],presses=2)

time.sleep(2.5)

pyautogui.press(['alt','r','c'])

time.sleep(0.5)

pyautogui.write('150068')
pyautogui.press(['tab','space'])

time.sleep(0.5)

ljP = 1

for ljP in range(1,12):

    strMP=str(ljP)
    
    pyautogui.press('tab', presses=5)
    pyautogui.write(strMP)
    pyautogui.press('tab')
    pyautogui.write('4')
    pyautogui.press('tab', presses=3)
    pyautogui.press('space')
    
    time.sleep(10)
    
    pyautogui.press('x')
    time.sleep(0.5)
    pyautogui.write(strMP+'rel')
    pyautogui.press('tab')
    pyautogui.write('m')
    pyautogui.press(['tab','space','f'])
    
    ljP=int(strMP)
    ljP=+1
    
    time.sleep(0.5)

strMP=str(ljP)    

pyautogui.press('tab', presses=5)
pyautogui.write(strMP)
pyautogui.press('tab')
pyautogui.write('5')
pyautogui.press('tab', presses=3)
pyautogui.press('space')

time.sleep(10)

pyautogui.press('x')

time.sleep(0.5)

pyautogui.press(['tab'],presses=6)
pyautogui.press(['m','enter'])

time.sleep(0.5)

pyautogui.press('d')
time.sleep(1)
pyautogui.hotkey('shift','f10')
time.sleep(1)
pyautogui.press(['a','b'])
    