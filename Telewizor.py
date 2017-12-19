# Telewizor

#Można zmieniać kanały i głośność

class Rtv(object):
    def __init__(self, kanał = 1, głośność = 10):
        self.__kanał = kanał
        self.__głośność = głośność

    @property
    def kanał(self):
        return self.__kanał

    @property
    def głośność(self):
        return self.__głośność

    @kanał.setter
    def kanał(self, nowy_kanał):
        if nowy_kanał not in [str(x) for x in range(1, 21)]:
            print("Nie ma takiego kanału")
        else:
            self.__kanał = nowy_kanał
            print("Kanał zmieniony na", self.kanał)

    @głośność.setter
    def głośność(self, nowa_głośność):
        if nowa_głośność > 20:
            print("Nie można zwiększyć głośności powyżej 20\nAktualna głośność wynosi", self.__głośność)
        elif nowa_głośność < 0:
            print("Nie można zmniejszyć głośności poniżej 0\nAktualna głośność wynosi", self.__głośność)
        else:
            self.__głośność = nowa_głośność
            print("Głośńość zmieniona na", nowa_głośność)

def main():
    telewizor = Rtv()
    choice = None
    while choice != "0":
        choice = input("""
        Co chcesz zrobić?
        0 - Wyłączyć TV
        1 - Zmienić kanał
        2 - zwiększyć głośność
        3 - zmniejszyć głośnoć""")

        if choice == "0":
            print("koniec programu")

        if choice == "1":
            telewizor.kanał = input("Jaki kanał chcesz ustawić?")

        if choice == "2":
            telewizor.głośność += int(input("O ile chcesz zwiększyć głośność?"))

        if choice == "3":
            telewizor.głośność -= int(input("O ile chcesz zmniejszyć głośność?"))


main()
input("coś")


