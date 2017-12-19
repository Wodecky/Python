#rzut monetą

#rzuca 100 razy monetą, a następnie podaje liczbę wyrzuconych orłów i reszek

import random

orzeł = 0
reszka = 0
rzut = 0

while rzut < 100:
    rzut += 1
    if random.randint(0, 1):
        orzeł += 1
    else:
        reszka += 1

print("Wyrzucono", orzeł, "orłów i", reszka, "reszek")

input("Dawaj Enter")


