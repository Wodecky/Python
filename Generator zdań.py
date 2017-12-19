# GUI

#Moja kopia programu Mad Lib

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Utwórz własne zdanie"
              ).grid(row = 0, column = 0, columnspan = 1, sticky = W)

        Label(self,
              text = "Podmiot"
              ).grid(row = 1, column = 0, sticky = W)
        self.podmiot = Entry(self)
        self.podmiot.grid(row = 2, column = 0, sticky = W)

        Label(self,
              text="Orzeczenie"
              ).grid(row=1, column=1, sticky=W)
        self.orzeczenie = Entry(self)
        self.orzeczenie.grid(row=2, column=1, sticky=W)

        Label(self,
              text="Okolicznik"
              ).grid(row=1, column=2, sticky=W)
        self.okolicznik = Entry(self)
        self.okolicznik.grid(row=2, column=2, sticky=W)

        Label(self,
              text="Przydawka"
              ).grid(row=1, column=3, sticky=W)
        self.przydawka = Entry(self)
        self.przydawka.grid(row=2, column=3, sticky=W)

        Label(self,
              text="Dopełnienie"
              ).grid(row=1, column=4, sticky=W)
        self.dopełnenie = Entry(self)
        self.dopełnenie.grid(row=2, column=4, sticky=W)

        Label(self,
              text = "Zdanie ma być:"
              ).grid(row = 3, column = 0, sticky = W)

        self.typ = StringVar()
        self.typ.set(None)

        typy = ["Oznajmujące", "Pytające", "Wykrzyknienie"]
        column = 0
        for part in typy:
            Radiobutton(self,
                        text=part,
                        variable=self.typ,
                        value=part
                        ).grid(row=4, column=column, sticky=W)
            column += 1

        Button(self,
               text="Kliknij, aby wyświetlić zdanie",
               command=self.zdanie
               ).grid(row=5, column=0, columnspan = 2, sticky=W)

        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=6, column=0, columnspan=4)

    def zdanie(self):
        #generowanie zdania
        podmiot = self.podmiot.get()
        orzeczenie = self.orzeczenie.get()
        okolicznik = self.okolicznik.get()
        przydawka = self.przydawka.get()
        dopełnienie = self.dopełnenie.get()
        typ = self.typ.get()

        zdanie = podmiot + " " + orzeczenie + " " + okolicznik + " " + przydawka + ' ' + dopełnienie

        if typ == "Pytające":
            zdanie = "Czy " + zdanie + "?"

        elif typ == "Wykrzyknienie":
            zdanie += "!"
            zdanie.upper()

        elif typ == "Oznajmujące":
            zdanie += "."

        #wyświetlanie zdania
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, zdanie)

# część główna
root = Tk()
root.title("Generator zdań")
app = Application(root)
root.mainloop()





