#Jaka to liczba

#Generuje losową liczbe od 1 do 100. Użytkownik musi zgadnąć co to za liczba

import random

def ask_number(question, low, high):
    """Poproś o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def main():
    a = random.randint(1, 100)
    próby = 0

    while próby < 10:
        próby += 1
        print("\nPróba", próby)
        strzał = ask_number("Zgaduj\n", 1, 100)
        if a == strzał:
            print("Brawo! Zgadłeś")
            break
        elif a > strzał:
            print("Za mało")
        elif a < strzał:
            print("Za dużo")
        else:
            print("Błąd")
    if próby == 10:
        print("Przegrałeś!")

main()
input("Dawaj Enter")