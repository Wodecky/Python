import tkinter as tk


class Game(tk.Frame):
    P_COLOURS = ["black", "blue", "green", "red", "yellow"]

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.players = []
        self.create_widgets()
        self.generate_players()

    def create_widgets(self):
        tk.Label(text = "WATWAT").pack()

    def generate_players(self):
        colours = []
        t = tk.Toplevel()
        tk.Label(t,
                 text="Pick colours of players:",
                 padx=10,
                 pady=10).grid()
        for colour in self.P_COLOURS:
            tk.Checkbutton(t,
                           bg=colour,
                           command=colours.append(colour),
                           width=20,
                           indicatoron=False).grid(row=self.P_COLOURS.index(colour)+1)
        print(colours)
        b = tk.Button(master=t,
                      text="Ok",
                      command=self.gen_play_but(set(colours)))
        b.grid(row=6)


    def gen_play_but(self, colours):
        if len(colours) < 2:
            return None
        else:
            for colour in colours:
                self.players.append(Player(colour))
            print(self.players)
            return self.destroy()


class Player(object):
    def __init__(self, colour):
        self.colour = colour
        self.cards = []
        self.cars = 45
        self.last_turn = False
        self.routes = []
        self.points = 0
        self.stations = []
        self.tickets = []
        self.longest = 0

root = tk.Tk()
root.title("Ticket to ride")
app = Game(root)
root.mainloop()
