# zgadnij słowo

# komputer losuje słowo które urzytkownik musi odgadnąć wiedząć ile ma liter i dowiadując się czy znajduje się
# z nim 5 z nich

import random

WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
word = random.choice(WORDS)

print("Słowo ma", len(word), "liter")
for i in range(5):
    if input("Zgadnij literę") in word:
        print("Tak")
    else:
        print("Nie")

if input("Zgaduj słowo") == word:
    print("Brawo! Wygrałeś!")
else:
    print("Przegryw!")

input("Dawaj Enter")