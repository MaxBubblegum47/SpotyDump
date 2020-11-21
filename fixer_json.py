from tkinter import *
import os
import json
import nltk
import tkinter as tk
from tkinter import filedialog
from string import whitespace

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

with open(str(file_path)) as json_file:
    data = json.load(json_file)
try:
    for i in range(100):
        album_name=""

        #aggiustamento che mi dovrebbe evitare bazze stranissime con i nomi degli album buggati
        if (str(data['songs'][i]['album']) == None or "https" in str(data['songs'][i]['album']) or "//" in str(data['songs'][i]['album'])):
            #non fare niente rimane album_name=""
            print("Album not Included for safe path policy")
        else:
            album_name = "_" + str(data['songs'][i]['album'])

        song_name_save = data['songs'][i]['title'] + "_" + data['name'] + album_name

        if (data['songs'][i]['lyrics'] != None):
            text_file = open(song_name_save.replace("/","_"), "w")
            text_file.write(data['songs'][i]['lyrics'])
            text_file.close()
except IndexError:
    print("ciao")
