from tkinter import *
import os
import json
import lyricsgenius
genius = lyricsgenius.Genius("dKdv-UTxwXPwypUw5d9n-ZJz9CTxK3R7V0D5BouXuGhfGQpgU8KASPgr6gw00qTm")
import nltk
import tkinter as tk
from tkinter import filedialog
from string import whitespace

master = Tk()
master.title('Lazy Song')
master.geometry("830x90")

#e1=artist_name
e1 = Entry(master)
e1.pack(side=LEFT)

#e2=numb_canzoni
e2 = Entry(master)
e2.pack(side=LEFT)

labelText=StringVar()
labelText.set("Artist, Songs's Number (1000 for example to get all songs)")
labelDir=Label(master, textvariable=labelText, height=4)
labelDir.pack(side=LEFT)

def callback():
    print(e1.get())
    artist_name = e1.get()

    if not e2.get().isdigit():
        e2.delete(0,'end')
        e1.delete(0,'end')
        master_warning = Tk()
        master_warning.title('Lazy Song: Warning')
        master_warning.geometry("400x30")
        text=Text(master_warning)
        text.insert(INSERT, "Put some integer in the songs's number entry please")#font terribile
        text.pack()

    numb_canzoni = int(e2.get())
    print(numb_canzoni)

    #operzioni varie di ricerca e salvataggio
    artist = genius.search_artist(artist_name, numb_canzoni, sort="title", include_features=True)
    #artist.name è il vero nome, coretto, quello usato prima era solo per fare la query
    artist.save_lyrics()

    #1. seleziona dove vuoi salvare le canzoni
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

    cartella_artista = artist.name

    path = os.path.join(str(folder_selected), cartella_artista)
    os.mkdir(path)

    #2. seleziona il file .json dell'artista appena scaricato. Questo lo mette sempre nella directory in cui
    #   è presente questo file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    with open(str(file_path)) as json_file:
        data = json.load(json_file)

    for i in range(numb_canzoni):
        album_name=""

        #aggiustamento che mi dovrebbe evitare bazze stranissime con i nomi degli album buggati
        if (str(data['songs'][i]['album']) == None or "https" in str(data['songs'][i]['album']) or "//" in str(data['songs'][i]['album'])):
            #non fare niente rimane album_name=""
            print("Album not Included for safe path policy")
        else:
            album_name = "_" + str(data['songs'][i]['album'])

        song_name_save = data['songs'][i]['title'] + "_" + artist.name + album_name

        if (data['songs'][i]['lyrics'] != None):
            text_file = open(path + "/" + song_name_save.replace("/","_"), "w")
            text_file.write(data['songs'][i]['lyrics'])
            text_file.close()

    #pulire l'entry del testo
    e1.delete(0,'end')
    e2.delete(0,'end')

b = Button(master, text = "GO", height = 1 ,width = 5, command = callback)
b.pack(side=LEFT)
mainloop()

