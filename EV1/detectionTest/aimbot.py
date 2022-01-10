from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (255, 219, 195)

xstart=660
ystart=369
xend=1260
yend=790
#BIG SCREEN
# xstart=0
# ystart=0
# xend=1900
# yend=1900

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(xstart,ystart,xend,yend)) #0,0,width,height

    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):

            r, g, b = pic.getpixel((x, y))

            if b == 195 and r == 255 and g == 219:
                click(x+xstart,y+ystart)
                time.sleep(0.05)
                break