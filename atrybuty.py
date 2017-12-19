# atrybuty

# pozwala edytować atrybuty postaci

atr = [0, 0, 0, 0]

print("Witaj w edytorze atrybutów")
wybór = True
while wybór != 0:
    wybór = input("""
    Który atrybut chcesz zmienić?
    1 - siła
    2 - zdrowie
    3 - mądrość
    4 - zręczność
    
    Aby zakończyć progam wciśnij enter
    """)
    if  wybór == "1":
        b = input("Ile ma wynosić siła?")
        if int(b) + atr[2] + atr[3] + atr[1] <= 30:
            atr[0] = int(b)
            print("Siła zmieniona na", atr[0])
        else:
            print("Suma atrybutów nie może być większa niż 30")

    elif  wybór == "2":
        b = input("Ile ma wynosić zdrowie?")
        if int(b) + atr[2] + atr[3] + atr[0] <= 30:
            atr[1] = int(b)
            print("Zdrowie zmieniona na", atr[1])
        else:
            print("Suma atrybutów nie może być większa niż 30")

    elif  wybór == "3":
        b = input("Ile ma wynosić siła?")
        if int(b) + atr[0] + atr[1] + atr[3] <= 30:
            atr[2] = int(b)
            print("Mądrość zmieniona na", atr[2])
        else:
            print("Suma atrybutów nie może być większa niż 30")

    elif  wybór == "4":
        b = input("Ile ma wynosić zręczność?")
        if int(b) + atr[2] + atr[0] + atr[1] <= 30:
            atr[3] = int(b)
            print("Siła zmieniona na", atr[3])
        else:
            print("Suma atrybutów nie może być większa niż 30")

    elif wybór == "":
        break
        
    else:
        print("Wprowadź poprawną wartość")

