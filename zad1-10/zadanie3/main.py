a = int(input("podaj liczbę całkowitą: "))
if a % 3 == 0:
    if a % 5 == 0:
        print("liczba jest podzielna przez 3 i 5")
    else:
        print("liczba jest podzielna przez 3 i nie przez 5")
if a % 5 != 0:
    if a % 3 != 0:
        print("liczba nie jest przez ani 5 ani 3 podzielna")
if a % 5 == 0:
    if a % 3 != 0:
        print("liczba nie jest podzielna przez 3 ale jest przez 5")
