import pyautogui
from python_imagesearch.imagesearch import imagesearch, imagesearch_loop
import time
from sys import platform
from autoaccept import inQueue
pyautogui.FAILSAFE = False

def login(username, password): #todo - return false if it fails

    uname = imagesearch_loop("images/username.png", 3)
    pyautogui.click(uname[0], uname[1])
    pyautogui.write(username)

    pwd = imagesearch("images/password.png")
    pyautogui.click(pwd[0], pwd[1])
    pyautogui.write(password)

    login = imagesearch("images/login.png")
    pyautogui.click(login[0], login[1])

    time.sleep(5)
    invalid = imagesearch("images/invalid.png")
    if invalid[0]!=-1:
        if platform == "win32":
            pyautogui.hotkey('alt', 'f4')
        elif platform == "linux" or "linux2":
            pyautogui.hotkey('alt', 'f4')
        elif platform == "darwin":
            pyautogui.hotkey('command', 'w')
        return False

    return True

def play(mode, primary, secondary, autoPlay):
    if not autoPlay:
        return
    play = imagesearch_loop("images/play.png", 1, 0.9)
    x = imagesearch("images/rankedsolo.png")
    pvp = imagesearch("images/pvp.png")
    pyautogui.click(pvp[0], pvp[1])
    while x[0] == -1:
        pyautogui.click(play[0], play[1])
        x = imagesearch("images/rankedsolo.png")

    if (mode == "Ranked Solo/Duo"):
        rankedsolo = imagesearch_loop("images/rankedsolo.png", 0.5)
        pyautogui.click(rankedsolo[0], rankedsolo[1])
    elif (mode == "Ranked Flex"):
        rankedflex = imagesearch_loop("images/rankedflex.png", 0.5)
        pyautogui.click(rankedflex[0], rankedflex[1])
    elif (mode =="Draft Pick"):
        draftpick = imagesearch_loop("images/draftpick.png", 0.5)
        pyautogui.click(draftpick[0], draftpick[1])
    elif (mode == "Blind Pick"):
        blindpick = imagesearch_loop("images/blindpick.png", 0.5)
        pyautogui.click(blindpick[0], blindpick[1])

    confirm = imagesearch("images/confirm.png")
    pyautogui.click(confirm[0], confirm[1])

    if mode != "Blind Pick":
        selectfirstrole = imagesearch_loop("images/firstrole.png", 0.5)
        pyautogui.click(selectfirstrole[0], selectfirstrole[1])
        primaryrole = imagesearch_loop(f"images/{primary}.png", 0.5)
        pyautogui.click(primaryrole[0], primaryrole[1])

        selectsecondrole = imagesearch_loop("images/secondrole.png", 0.5)
        pyautogui.click(selectsecondrole[0], selectsecondrole[1])
        secondaryrole = imagesearch_loop(f"images/{secondary}.png", 0.5)
        pyautogui.click(secondaryrole[0], secondaryrole[1])
    
    queue = imagesearch_loop("images/queue.png", 1)
    time.sleep(1)
    pyautogui.click(queue[0], queue[1])

    inQueue()
 