#jaka to liczba GUI

#program jaka to liczba z wykorzystaniem GUI

from tkinter import *
import random


class Application(Frame):
    def __init__(self, master):
        """ Inicjalizuj ramkę. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.licznik = 0

    def create_widgets(self):
        Label(self,
              text = "Zgadnij liczbę(1-100)"
              ).grid(row = 0, column = 0, sticky = W)

        self.strzał_ent = Entry(self)
        self.strzał_ent.grid(row = 1, column = 0, sticky = W)

        Label(self,
              text = "Liczba strzałów",
              ).grid(row = 0, column = 1, sticky = W)

        self.licznik_txt = Text(self, width = 10, height = 1)
        self.licznik_txt.grid(row = 1, column = 1, sticky = W)

        self.przycisk = Button(self,
               text = "Zgaduję",
               command = self.sprawdź)
        self.przycisk.grid(row = 2, column = 0, sticky = W)
        self.rezultat = Text(self, width = 25, height = 1)
        self.rezultat.grid(row = 2, column = 1, sticky = W)

    def blokada(self):
        self.przycisk.config(state = DISABLED)

    def liczydło(self):
        self.licznik += 1
        self.licznik_txt.delete(0.0, END)
        self.licznik_txt.insert(0.0, self.licznik)
        if self.licznik == 10:
            self.blokada()

    def sprawdź(self):
        strzał = 0

        try:
            strzał = int(self.strzał_ent.get())
            if strzał in range(1, 101):
                if strzał > liczba:
                    self.rezultat.delete(0.0, END)
                    self.rezultat.insert(0.0, "Za dużo")
                    self.liczydło()

                elif strzał < liczba:
                    self.rezultat.delete(0.0, END)
                    self.rezultat.insert(0.0, "Za mało")
                    self.liczydło()

                elif strzał == liczba:
                    self.rezultat.delete(0.0, END)
                    self.rezultat.insert(0.0, "Trafiłeś!")
                    self.liczydło()
                    self.blokada()
            elif strzał > 100 or strzał < 1:
                self.rezultat.delete(0.0, END)
                self.rezultat.insert(0.0, "Liczba spoza zakresu")
        except:
            self.rezultat.delete(0.0, END)
            self.rezultat.insert(0.0, "Musisz podać liczbę")





liczba = random.randrange(1, 101)

root = Tk()
root.title("Jaka to liczba")
app = Application(root)
root.mainloop()
