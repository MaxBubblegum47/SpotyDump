from tkinter import *
import os
import json
import lyricsgenius
genius = lyricsgenius.Genius("inserisci token qui")
import nltk
import tkinter as tk
from tkinter import filedialog
from string import whitespace


#mega foor loop each line del file text
file=open("singers_list.txt")

for artist_name in file:
    numb_canzoni=10

    artist = genius.search_artist(artist_name, numb_canzoni, sort="popularity", include_features=True)
    artist.save_lyrics()

    #da cambiare se usato da qualche altro utente
    path = "/Users/lorenzostigliano/Desktop/Lyrics"
    cartella = artist.name

    path = os.path.join(path, cartella)
    os.mkdir(path)

    range_song=len(artist.songs)

    try:
        with open("Lyrics_" + str(artist.name).replace(" ","").replace("$","").replace("-","") + ".json") as json_file:
            data = json.load(json_file)

            for i in range(range_song):
                album_name=""

                #aggiustamento che mi dovrebbe evitare bazze stranissime con i nomi degli album buggati
                if (str(data['songs'][i]['album']) == None or "https" in str(data['songs'][i]['album']) or "//" in str(data['songs'][i]['album'])):
                    #non fare niente rimane album_name=""
                    print("Nome album non considerato")
                else:
                    album_name = "_" + str(data['songs'][i]['album'])

                song_name_save = data['songs'][i]['title'] + "_" + artist.name + album_name

                if (data['songs'][i]['lyrics'] != None):
                    text_file = open(path + "/" + song_name_save.replace("/","_"), "w")
                    text_file.write(data['songs'][i]['lyrics'])
                    text_file.close()
    except IOError:
        print("File not accessible")
