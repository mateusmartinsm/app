import pyautogui as ag
from os import system
from time import sleep


system('./main &')
sleep(1)
ag.click(x=1207, y=421)
ag.typewrite('a')
ag.press('tab', 2)
ag.typewrite('b')
ag.press('tab')
ag.typewrite('c')
ag.press('tab')
ag.typewrite('d')
ag.press('tab')
ag.typewrite('e')
ag.press('tab')
ag.typewrite('f')
ag.click(x=1425, y=873)
sleep(3)
ag.click(x=908, y=585)
