# losowe słowa

#wypisuje słowa w losowej kolejności

import random

words = ["python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon", "python"]
lol = []
for i in range(len(words)):
    a = random.choice(words)
    if a not in lol:
        lol.append(a)
        print(a, end=" ")
    words.remove(a)



input("Dawaj Enter")