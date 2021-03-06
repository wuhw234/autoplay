import pyautogui
from python_imagesearch.imagesearch import imagesearch, imagesearch_loop
import time
from sys import platform
pyautogui.FAILSAFE = False 

def inQueue():
    """Runs while user is in queue waiting for match, calls
    autoAccept to accept a match if it is found"""
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
    """Automatically accepts a match if it is found"""
    while True:
        pos = imagesearch("autoplay/images/accept.png")
        if not pos[0] == -1:
            pyautogui.click(pos[0], pos[1])
            break
    time.sleep(1)
    accepted()

def accepted():
    """Checks if the user enters champion selection after a match is accepted"""
    while True:
        accepted = imagesearch("autoplay/images/accepted.png") 
        if accepted[0] == -1:                    # if the screen changes from the accepted screen, break
            break
    time.sleep(1)
    pos = imagesearch("autoplay/images/inqueue.png")           # if you are back in queue, then call autoaccept
    if not pos[0] == -1:
        autoAccept()
    else:
        return

def dodge():
    """Runs when user fails to get into a match"""
    dodge = imagesearch("autoplay/images/inqueue.png")
    if dodge[0] != -1:
        return True
    return False

def inGame():
    """Runs when user successfully enters a game"""
    inGame = imagesearch("autoplay/images/ingame.png")
    if inGame[0] != -1:
        return True
    return False

if __name__ == "__main__":
    inQueue()