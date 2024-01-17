import keyboard
import mouse
import time

click = False

def set_click():
    global click
    if click:
        click = False
        print("Nestrādā")
    else:
        click = True
        print("Strādā")

keyboard.add_hotkey('Alt + C', set_click)

while True:
    if click:
        mouse.double_click(button='left')
        time.sleep(0.01)