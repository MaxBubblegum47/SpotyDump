#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:13:24 2020

@author: lorenzostigliano
"""

# questo file praticamente serve solamente per fare dei test di estrazione delle canzoni dal
# file .json

import json
import lyricsgenius
genius = lyricsgenius.Genius("inserire token qui")
import nltk
import tkinter as tk
from tkinter import filedialog

#parte per la ricerca delle canzoni di un artista
max_songs = 300
artist_name = "fra quintale"

#artist = genius.search_artist(artist_name, max_songs, sort="title")
#artist.save_lyrics()

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

canzone = ''

with open(file_path) as json_file:
    data = json.load(json_file)
    
    for i in range(max_songs):
        album_name=""

        if (data['songs'][i]['album'] != None):
            album_name = "_" + data['songs'][i]['album']['name']
        
        song_name_save=str(data['songs'][i]['title'])
        
        
        if (data['songs'][i]['lyrics'] != None):
            text_file = open(song_name_save.replace("/","_") + "_" + data['name'] + album_name, "w") #puoi anche fare artist.name
            text_file.write(data['songs'][i]['lyrics'])
            text_file.close()

# ho lasciato questo commmento perché stavo provando la tokenizzazione
#tokens = nltk.word_tokenize(canzone)

#print(tokens)
