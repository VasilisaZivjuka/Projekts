import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import keyboard
import mouse

# automātiska klikera kods
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

# izskaidrošanas instrukcija priekš lietotāja
print("Labdien, spelētajs, tagad tev ir pieejams automātiskais klikeris, ko var aktivēt ar komandu Alt+C") 
time.sleep(2) 
print("Vari ievadīt spēles saiti un spēlēt vieglāk") 
url = input('Spēles saite: ')
time.sleep(3)
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
driver.get(url)
time.sleep(5)
input()