# Music-Search-Engine---Lazy-Song  (main.py, spotyscrapy.py, explore_csv.py, scout_lyrics.py)
Il programma Lazy Song permette di decidere un arco temporale in cui cercare i migliori artisti su Spotify e scaricarne in formato .txt un numero arbitrario di canzoni. Al momento per poter cambiare la regione di ricerca e il numero di canzoni bisogna accedere al codice; non è un'operazione complessa, ma presto implementeremo tali possibilità all'interno della gui.

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
