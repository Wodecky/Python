#cytat
#edytuje cytaty

cytat = input("Dawaj cytat!")

print("\nZ wielkiej:\n"+cytat.upper())
print("\nZ małej:\n"+cytat.lower())
print("\nPierwsza z wielkiej:\n"+cytat.title())
print("\nCenzura:\n"+cytat.replace("Ja", "Ty"))
print("\nZdanie:\n"+cytat.capitalize())
print("\nZamiana:\n"+cytat.swapcase())
print("\nBez specjalnych znaków:\n"+cytat.strip())
input('Enter')