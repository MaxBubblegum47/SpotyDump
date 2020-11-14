from tkinter import *
import json
import lyricsgenius
genius = lyricsgenius.Genius("metti_token_genius_API_qui")
import nltk
import tkinter as tk
from tkinter import filedialog
from string import whitespace

master = Tk()
master.title('Lazy Song')

e1 = Entry(master)
e1.pack(padx=5, pady=10, side=LEFT)

e2 = Entry(master) 
e2.pack(padx=5, pady=20, side=LEFT)

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
    artist = genius.search_artist(artist_name, numb_canzoni, sort="title")
    artist.save_lyrics()
    
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    
    canzone = ''

    with open(file_path) as json_file:
        data = json.load(json_file)
    
    for i in range(numb_canzoni):
        album_name=""

        if (data['songs'][i]['album'] != None):
            album_name = "_" + data['songs'][i]['album']['name']

        song_name_save=data['songs'][i]['title'] + "_" + data['name'] + album_name
        
        
        text_file = open(song_name_save.replace("/","_"), "w")
        text_file.write(data['songs'][i]['lyrics'])
        text_file.close()
    
    #pulire l'entry del testo
    e1.delete(0,'end')
    e2.delete(0,'end')
    
b = Button(master, text = "GO", height = 1 ,width = 5, command = callback)
b.pack(padx=5, pady=20, side=LEFT)
mainloop()
