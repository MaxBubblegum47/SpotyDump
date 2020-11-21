from tkcalendar import Calendar, DateEntry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
import json
import lyricsgenius
genius = lyricsgenius.Genius("insert Genius Token here")
import nltk
import tkinter as tk
from tkinter import filedialog
from string import whitespace
from explore_csv import csv_toTXT
from spotyscrapy import diehard
from scout_lyrics import spoty_scouting

string_date=[]
path=[]

def calendar():
    def scrapy_start():
        start=cal.selection_get()
        cal.see(datetime.date(year=2020, month=11, day=1))
        string_date.append(start)


    def scrapy_end():
        end=cal.selection_get()
        cal.see(datetime.date(year=2020, month=11, day=1))
        string_date.append(end)


    top = tk.Toplevel(root)

    import datetime
    today = datetime.date.today()

    mindate = datetime.date(year=2017, month=1, day=1)
    maxdate = today + datetime.timedelta(days=5)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   cursor="hand1", year=maxdate.year, month=maxdate.month, day=maxdate.day)
    cal.pack(fill="both", expand=True)

    ttk.Button(top, text="Set Start", command=scrapy_start).pack()
    ttk.Button(top, text="Set End", command=scrapy_end).pack()


def save_dir():
    from tkinter import Tk
    from tkinter.filedialog import askdirectory

    path.append(askdirectory(title='Select Folder')) # shows dialog box and return the path


def spotygo():
    string_date.sort()
    print("Beginning: " + str(string_date[0]) + " End: " + str(string_date[1]))

    #calling SpotyCrap.py function diehard
    diehard(string_date[0], string_date[1])

    #calling explore_csv.py function csv_toTXT()
    csv_toTXT()

    #calling scout.py function spoty_scouting()
    spoty_scouting(path[0])


root = tk.Tk()
root.title("Spoty Scrapy")

#country=StringVar(root)
#country.set("us")#default search region
#ttk.OptionMenu(root,country, "us", "it", "global").pack()

ttk.Button(root, text='Days of Search ', command=calendar).pack(padx=60, pady=10)
ttk.Button(root, text='Choose Directory for saving lyrics', command=save_dir).pack(padx=60, pady=10)
ttk.Button(root, text='Go', command=spotygo).pack(padx=60,pady=10)

root.mainloop()
