import pyautogui
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect number of parameters. Please execute with file name as parameter")
    else:
        filename = sys.argv[1]
        data = open(filename, "r").read()
        time.sleep(2)
        tab_counter = 0
        for d in data:
            if d == "\n":
                tab_counter = 0
                pyautogui.press(d)
                time.sleep(1)
            elif d == " ":
                tab_counter += 1
            else:
                if tab_counter % 4 == 0:
                    for i in range(int(tab_counter/4)):
                        pyautogui.press("tab")
                else:
                    for i in range(tab_counter):
                        pyautogui.press(" ")
                tab_counter = 0
                pyautogui.press(d)


