import csv
import os

def csv_toTXT():
    lista = []

    with open("spmooddata.csv") as csv_file:
        csv_reader=csv.reader(csv_file, delimiter=",")
        line_count=0
        for row in csv_reader:
            print(row[1])
            lista.append(row[1])
            #print(f'Column names are {", ".join(row)}')
            line_count += 1

        print(f'Processed {line_count} lines.')
        lista.sort()
        lista = list(dict.fromkeys(lista))

        if "" in lista:
            lista.remove("")

        with open("singers_list.txt", "w") as file:
            for singer in lista:
                file.write("%s\n" % singer)
        print(lista)
