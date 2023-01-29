import mouse
import pyautogui
import keyboard
import win32api 

clickPoints = []

def click(nextPos):
    pyautogui.moveTo(nextPos[0], nextPos[1])
    mouse.click('left')

def register(x, y):
    global clickPoints
    clickPoints.append([x, y])

def getPositions():
    leftDown = False
    while True:
        if (win32api.GetAsyncKeyState(0x01)&0x8000 > 0):
            if not leftDown:
                leftDown = True
                x, y = pyautogui.position()
                register(x, y)
        else:
            leftDown = False
        if keyboard.is_pressed('enter'):
                return
    
def startClicking():
    global clickPoints
    while True:
        for point in clickPoints:
            click(point)
            if keyboard.is_pressed('esc'):
                return
            if keyboard.is_pressed('home'):
                while True:
                    if keyboard.is_pressed('end'):
                        break
                    if keyboard.is_pressed('esc'):
                        return

getPositions()
startClicking()