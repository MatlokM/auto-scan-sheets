import os
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import PySimpleGUI as sg
import time
import SheetToList


def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, relative_path)


# Variables to Change
#ENTRYID = "article"
SITE = "https://listmoz.com/"
ENTRYID = "add-field"
WAITTIME = 2

# Static Variables
driver = webdriver.Chrome(ChromeDriverManager().install())
location = ""
barcodes = []

# Opens Site
driver.get(SITE)

# GUI
sg.theme('LightBlue')
layout = [[sg.Text('Please Login and Navigate to the [specified area for client] before continuing', font="Arial 16")],
        [sg.T("")],
        [sg.T("")],
        [sg.Text('Use the button below to locate the spreadsheet on your system.')],
        [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],
        [sg.Button("Submit")]]


# Window
window = sg.Window("AutoScanSheet", layout, size=(800, 300))
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Submit":
        location = (values["-IN-"])
        barcodes = SheetToList.sheetToList(location)
        entry = driver.find_element(By.ID, ENTRYID)
        for i in barcodes:
            entry.send_keys(int(i))
            entry.send_keys(Keys.RETURN)
            time.sleep(WAITTIME)
        break
window.close()
