# Opiekun zwierzaka
# Wirtualny pupil, którym należy się opiekować

import random

class Critter(object):
    """Wirtualny pupil"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = random.randrange(1,8)
        self.boredom = random.randrange(1,8)

    def __str__(self):
        return "Poziom głodu {0} wynosi {1}, a znudzenia {2}".format(str(self.name), str(self.hunger), str(self.boredom))

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m

    def talk(self):
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.\n")
        self.__pass_time()

    def eat(self, food):
        print("Mniam, mniam.  Dziękuję.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Hura!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
    crit = Critter(crit_name)
    crit1 = Critter("Bobo")
    crit2 = Critter("Ja")
    lista = [crit, crit1, crit2]

    choice = None
    while choice != "0":
        print \
            ("""
        Opiekun zwierzaka

        0 - zakończ
        1 - słuchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoim zwierzakiem
        """)

        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli
        if choice == "0":
            print("Do widzenia.")

        # słuchaj swojego zwierzaka
        elif choice == "1":
            for i in lista:
                i.talk()

        # nakarm swojego zwierzaka
        elif choice == "2":
            food = int(input("Jak dużo jedzenia dajesz zwierzakom?"))
            for i in lista:
                i.eat(food)

        # pobaw się ze swoim zwierzakiem
        elif choice == "3":
            fun = int(input("Jak długo bawisz się ze zwierzakiem?"))
            for i in lista:
                i.play(fun)

        elif choice == "kod":
            print(crit)

        # nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")


main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
