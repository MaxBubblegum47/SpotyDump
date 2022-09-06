# NON FUNZIONA PIU'
Praticamente spotify charts non funziona piu' in modo da permettere data scraping

# NOT WORKING ANYMORE
Spotify does not allow anymore data scraping

Il programma SpotyDump permette di decidere un arco temporale in cui cercare i migliori artisti su Spotify e scaricarne in formato .txt un numero arbitrario di canzoni. Al momento per poter cambiare la regione di ricerca e il numero di canzoni bisogna accedere al codice; non è un'operazione complessa, ma presto implementeremo tali possibilità all'interno della gui.

Per cambiare la regione bisogna andare alla riga 15 del file spotyscrapy.py mentre per cambiare il numero di canzoni da scaricare bisogna andare alla riga 11 di scout_lyrics.py e cambiare il valore di numb_canzoni (di default è impostato a 10).

Il programma funziona come segue:
1. Aprire il calendario premendo su "Days of Search"
2. Selezionare il primo giorno del range di ricerca e poi premere su "Set Start" e infine selezionare sull'utlimo giorno di ricerca e premere "Set End". Vi consigliamo di non eccedere nei giorni di ricerca o potrebbe volerci molto tempo per effettuare lo scraping di informazioni da Spotify. Sto progettando un algoritmo di ricerca estremamente più veloce che sta dando ottimi nei benchmark, ma mi riservo di pubblicarlo perché manca di alcune features importanti che spero di implementare al più presto.
3. Premere su "Choose Directory for saving Lyrics" e scegliere la cartella in cui salvare tutto
4. Premere su "Go"

Da questo momento in poi il programma generea un file .csv contenenti informazioni quali: canzoni, artista, album,... da questo file il programma ne estrae tutti i nomi dei cantanti e li inserisce in un file di testo (.txt). Quest'utlimo viene dato in pasto alla parte di programma che si interfaccia con la API di Genius.com e vengono scaricati files .json per ogni artista, contenenti informazioni quali: bio, album, lyrics, ... da questi file json vengono estratte tutte le lyrics e divise per cartelle create con il nome del cantante a cui sono associate le lyrics (il percorso di queste cartelle è quello deciso dall'utente poc'anzi).

Potrebbe succedere che il programma una volta generato il file .json di un determinato artista abbia difficoltà ad individuarlo: questo perché l'algoritmo di creazione del nome del file .json è gestita dalla libreria lyricsgenius e spesso non funziona come dovrebbe. Abbiamo provato a fixare facendo dei test e capendo il pattern con cui vengono i file legati a determinati artisti (soprattutto quelli con caratteri speciali all'interno del nome). Ad ogni modo: abbiamo inserito il file fixer_json.py per poter far selezionare all'utente il file .json da cui estrarre le lyrics qualora qualcosa sia andato storto.

Se vi state chiedendo cosa sia LSstandard.py questo è un programma permette di scaricare le canzoni legate ad un determinato artista in maniera manuale, inserendone il nome e poi il numero di canzoni da scaricare. Questa è stata la base di partenza per sviluppare il programma che abbiamo presentato fino ad ora.

Come potete vedere il programma è frutto di un doppio scraping: prima su spotify e poi su genius. Se avete consigli su librerie grafiche da usare, fatevi avanti: ho usato tkinter, ma non posso dire di essermi trovato molto bene in termini di bellezza estetica del programma; su linux e macOS è visibilmente non malformato, ma su windows da il meglio di se.

Postilla --> timeout=5 ERROR: a volte potrebbe succedere che genius vi cacci a malo modo durante le operazioni di scarping delle lyrics. Sto cercando di sistemare anche questo problema e come workaround al momento ho creato una versione del programma in cui gli si da in pasto una lista di cantanti (scritta a mano o ottenuta con qualche metodo di scraping) e qualora si blocchi su un determinato artista, rilancio il programmo tolgiendo manualmente dal file contenente i cantanti già processati. Non è il massimo, ma funziona per il momento. Il file per fare ciò si chiama LazyTerminator.py e la lista esempio si chiama singers_list.txt

# English

SpotyDump allows you to decide a time frame in which to search for the best artists on Spotify and download an arbitrary number of songs in .txt format. At the moment, in order to change the search region and the number of songs, you need to access the code; that's not complex, but I will implement those possibilities within the gui.

To change the region you have to go to line 15 of the spotyscrapy.py file, while to change the number of songs to download you need to go to line 11 of scout_lyrics.py and change the value of numb_songs (by default it is set to 10).

The program works as follows:
1. Open the calendar by clicking on "Days of Search"
2. Select the first day of the search range and then press on "Set Start" and finally select on the last day of the search and press "Set End". We advise you not to exceed the search days or it may take a long time to scrape information from Spotify. I am designing an extremely faster search algorithm that is performing well in the benchmarks, but I reserve the right to publish it because it lacks some important features that I hope to implement soon.
3. Click on "Choose Directory to save texts" and choose the folder in which to save everything
4. Click on "Go"

From this moment on, the program generates a .csv file containing information such as: songs, artist, album, ... from this file the program extracts all the names of the singers and inserts them in a text file (.txt). The latter is fed to the part of the program that interfaces with the Genius.com API and .json files are downloaded for each artist, containing information such as: bio, album, lyrics, ... from these json files are extracted all the lyrics and divided by folders, they create with the name of the singer to whom the lyrics are associated (the path of these folders is the one decided by the user just now).

It could happen that once the program has generated the .json file of a particular artist, it has difficulty in identifying it: this is because the algorithm for creating the .json file name is managed by the lyricsgenius library and often does not work as it should. We tried to fix it by doing some tests and understanding the pattern with which the files related to certain artists (especially those with special characters in the name) come. Anyway: we have inserted the fixer_json.py file to be able to select the .json file from which to extract the lyrics if something goes wrong.

If you are wondering what LSstandard.py is this is a program that allows you to download the songs related to a certain artist manually, by entering the name and then the number of songs to download. This was the starting point for developing the program we have presented so far.

As you can see, the program is the result of a double scraping: first on spotify and then on genius. If you have any advice on graphics libraries to use, go ahead: I used tkinter, but I can't say that I found myself very well in terms of the aesthetic beauty of the program; on linux and macOS it is not visibly malformed, but on windows it gives its best.

Footnote -> timeout = 5 ERROR: sometimes it could happen that genius kicks you out badly during the lyrics scarping operations. I am also trying to fix this problem and as a workaround at the moment I have created a version of the program in which it is fed a list of singers (handwritten or obtained with some method of scraping) and if it hangs on a particular artist, relaunch the program by manually removing from the file containing the singers already processed. It's not the best, but it works for the moment. The file to do this is called LazyTerminator.py and the example list is called singers_list.txt
