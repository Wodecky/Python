import shelve

def tablica_wyników():
    wyniki = shelve.open("rekordy.dat")
    wyniki["imiona"] = ["", "", "", "", ""]
    wyniki["punkty"] = [0, 0, 0, 0, 0]
    wyniki.sync()
    wyniki.close()
tablica_wyników()
input("Aby zakończyć naciśnij Enter"
      "")
