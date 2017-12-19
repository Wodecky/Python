#Komputer zgaduje

#Generuje losową liczbe od 1 do 100, a następnie próbuje zgadnąć co to za liczba

import random
liczba = random.randint(1, 100)
print("Losowa liczba to", liczba)
próby = 0
a=0
b=100
while próby < 10:
    próby += 1
    print("\nPróba", próby)
    strzał = int((a+b)/2)
    print("Twój strzał to:", strzał)
    if liczba == strzał:
        print("Brawo! Zgadłeś")
        break
    elif liczba > strzał:
        print("Za mało")
        a = strzał
    elif liczba < strzał:
        print("Za dużo")
        b = strzał
    else:
        print("Błąd")
if próby == 10:
    print("Przegrałeś!")

input("Dawaj Enter")