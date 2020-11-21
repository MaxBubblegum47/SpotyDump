import os
import json
import lyricsgenius
genius = lyricsgenius.Genius("dKdv-UTxwXPwypUw5d9n-ZJz9CTxK3R7V0D5BouXuGhfGQpgU8KASPgr6gw00qTm")
from string import whitespace

def spoty_scouting(path):
    file=open("singers_list.txt")

    for artist_name in file:
        numb_canzoni=10

        artist = genius.search_artist(artist_name, numb_canzoni, sort="popularity", include_features=True)
        artist.save_lyrics()

        cartella = artist.name

        path_long = os.path.join(path, cartella)
        os.mkdir(path_long)

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
                        text_file = open(path_long + "/" + song_name_save.replace("/","_"), "w")
                        text_file.write(data['songs'][i]['lyrics'])
                        text_file.close()
        except IOError:
            print("File not accessible")
