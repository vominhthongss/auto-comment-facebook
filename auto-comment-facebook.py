import pyautogui
import pyperclip
import platform
import time


def type(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


def cmt():
    comments = ["cmt 1", "cmt 2"]
    time.sleep(2)
    for i in range(len(comments)):
        type(comments[i])
        pyautogui.typewrite("\n")
        time.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('l')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('j')
    pyautogui.hotkey('c')


while True:
    cmt()
