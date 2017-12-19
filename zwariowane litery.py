# Wymieszane litery
# Wymieszane litery
# Komputer wybiera losowo słowo, a potem miesza w nim litery
# Gracz powinien odgadnąć pierwotne słowo

import random

print(
    """
               Witaj w grze 'Wymieszane litery'!

       Uporządkuj litery, aby odtworzyć prawidłowe słowo.
    (Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
    """
)
# utwórz sekwencję słów do wyboru
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
punkty = 0
while True:
    podpowiedź = False
    # wybierz losowo jedno słowo z sekwencji
    word = random.choice(WORDS)
    # utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
    correct = word

    # utwórz 'pomieszaną' wersję słowa
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]

    # rozpocznij grę

    print("Zgadnij, jakie to słowo:", jumble)

    guess = input("\nTwoja odpowiedź: ")
    while guess != correct and guess != "":
        if guess == "podpowiedź":
            print("Pierwsza litera to:", correct[0])
            podpowiedź = True
            guess = input("Twoja odpowiedź: ")
        else:
            print("Niestety, to nie to słowo.")
            guess = input("Twoja odpowiedź: ")

    if guess == correct:
        print("Zgadza się! Zgadłeś!\n")
        if podpowiedź == False:
            punkty += 1
    if guess == "":
        break




print("Dziękuję za udział w grze.")
print("Zdobyte punkty:", punkty)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
