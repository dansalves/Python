from time import time
import pyautogui
import PIL
import time
import os

'''
pyautogui.press(['win'])
pyautogui.write('remote')
pyautogui.press('enter')

time.sleep(1.5)

pyautogui.doubleClick('CISS DIA.png')

time.sleep(14)

pyautogui.click()

pyautogui.press(['tab'],presses=2)

time.sleep(0.5)

pyautogui.write('425')
pyautogui.press('tab')
pyautogui.write('2550')
pyautogui.press(['enter'],presses=2)

time.sleep(2.5)

pyautogui.press(['enter','alt','r','c'])

time.sleep(0.5)

pyautogui.write('150068')
pyautogui.press(['tab','space'])

time.sleep(0.5)

'''
ljsDIA="7010"

with open('lojasDia.txt','r') as lojas_dia:
    
    for ljsDIA in lojas_dia:
        
        pyautogui.press('tab', presses=5)
        pyautogui.write(ljsDIA)
        pyautogui.press('tab', presses=3)
        pyautogui.press('space')
    
        time.sleep(12)
        
        pyautogui.press('x')
        time.sleep(5)
        pyautogui.write(ljsDIA+'rel')
        time.sleep(4)
        pyautogui.press('tab')
        time.sleep(10)
        pyautogui.write('m')
        time.sleep(5)
        pyautogui.press(['tab','space','f'])
        time.sleep(4)

pyautogui.press('tab', presses=5)
pyautogui.write(ljsDIA)
pyautogui.press('tab', presses=4)
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
    