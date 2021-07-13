import pyautogui
from python_imagesearch.imagesearch import imagesearch, imagesearch_loop
import time
from sys import platform
pyautogui.FAILSAFE = False 

def inQueue():
    while True:
        autoAccept()
        print("in champ select")
        #now you are in champ select
        while True:
            if inGame():
                print("in game")
                return
            if dodge():
                print("someone dodged")
                inQueue()

def autoAccept():
    while True:
        pos = imagesearch("./accept.png")
        if not pos[0] == -1:
            pyautogui.click(pos[0], pos[1])
            break
    time.sleep(1)
    accepted()

def accepted():
    while True:
        accepted = imagesearch("./accepted.png") 
        if accepted[0] == -1:                    # if the screen changes from the accepted screen, break
            break
    time.sleep(1)
    pos = imagesearch("./inqueue.png")           # if you are back in queue, then call autoaccept
    if not pos[0] == -1:
        autoAccept()
    else:
        return

def dodge():
    dodge = imagesearch("./inqueue.png")
    if dodge[0] != -1:
        return True
    return False

def inGame():
    inGame = imagesearch("./ingame.png")
    if inGame[0] != -1:
        return True
    return False

if __name__ == "__main__":
    inQueue()