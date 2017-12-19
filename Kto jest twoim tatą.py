# Kto jest Twoim tatą

# Pozwala znaleźć ojca

dict = {"Ja" : "Tata", "Tata" : "Dziadek"}
a = "1"
while a != "":
    a = input("""
    Co chcesz zrobić?
    1 - znaleźć ojca
    2 - dodać ojca
    3 - wymienić ojca
    4 - usunąć ojca
    5 - znaleźć dziadka
    
    Aby zakończyć naciśnij enter
    """)
    if a == "1":
        b = input("Podaj swoje imię")
        if b in dict:
            print(dict[b])
        else:
            print("Brak w bazie")

    elif a == "2":
        dict[input("Podaj swoje imię:")] = input("Podaj imię ojca:")
        print("Dodano ojca")

    elif a == "3":
        b = input("Podaj swoje imię:")
        if b in dict:
            dict[b] = input("Podaj imię ojca:")
        else:
            print("Nie ma co wymieniać")

    elif a == "4":
        b = input("Podaj swoje imię:")
        if b in dict:
            del dict[b]
        else:
            print(" Już go nie było w bazie parówo")

    elif a == "5":
        b = input("podaj swoje imię")
        if b in dict:
            c = dict[b]
            if c in dict:
                print(dict[dict[b]])
            else:
                print("Nie masz dziadka")
        else:
            print("Nie istniejesz")

    else:
        print("Nie rozumiem")

input("Dawaj Enter")
