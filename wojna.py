import random

class Karta(object):
    RANKS = ["2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, wartość, kolor):
        self.wartość = wartość
        self.kolor = kolor

    def __str__(self):
        return self.wartość + self.kolor

    @property
    def value(self):
        return Karta.RANKS.index(self.wartość)

class Ręka(object):
    def __init__(self, imię):
        self.imię = imię
        self.karty = []

    @property
    def wartość(self):
        return self.karty[0].value

class Talia(Ręka):
    def stwórz_talię(self):
        for wartość in Karta.RANKS:
            for kolor in Karta.SUITS:
                self.karty.append(Karta(wartość, kolor))
        set(self.karty)
        random.shuffle(self.karty)

    def rozdaj(self, gracze):
        for gracz in gracze:
            gracz.karty.append(self.karty.pop(0))


class Gra(object):
    def __init__(self, imiona):
        self.gracze = []
        for imię in imiona:
            ręka = Ręka(imię)
            self.gracze.append(ręka)
        self.talia = Talia("Talia")



    def porównanie(self):
        maks = []
        for gracz in self.gracze:
            maks.append(gracz.wartość)
        maks = max(maks)
        for gracz in self.gracze:
            print(gracz.imię, gracz.karty[0])
        print("Lista zwycięzców:")
        for gracz in self.gracze:
            if gracz.wartość == maks:
                print(gracz.imię, end=" ")

def main():
    ilość = 0
    while not ilość:
        try:
            ilość = int(input("Ilu jest graczy?"))
        except:
            print("Podana wartość jest niepoprawna!")
    imiona = []
    for i in range(ilość):
        imię = input("Podaj nazwę gracza:")
        imiona.append(imię)

    gra = Gra(imiona)
    gra.talia.stwórz_talię()
    gra.talia.rozdaj(gra.gracze)
    gra.porównanie()

main()
input("Zakończ")


