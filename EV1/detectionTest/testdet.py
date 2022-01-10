from PIL.ImageOps import grayscale
from pyautogui import *
import pyautogui
import cv2
import time
import keyboard
import random
import win32api, win32con

img = cv2.imread(r'C:/Users/admin-dam2b/Documents/python/detectionTest/stickman.png')

# myimg = pyautogui.locateOnScreen(img)

# print(myimg)


print("1 minuto para la finalización del programa")
while 1:
    if pyautogui.locateOnScreen(img,region=(0,0,1919,1979), grayscale=True, confidence=0.4) != None:
        print("Te veo pto")
        time.sleep(0.5)
    else:
        print("No te veo :(")
        time.sleep(0.5)
    