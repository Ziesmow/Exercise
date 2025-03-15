a = int(input("podaj liczbę: "))
b = int(input("podaj liczbę: "))
c = int(input("podaj liczbę: "))
d = int(input("podaj liczbę: "))
e = int(input("podaj liczbę: "))
niepar = 0
par = 0
liczby = [a, b, c, d, e]
for licz in liczby:
    if licz % 2 == 0:
        par += 1
    else:
        niepar += 1
print(f"nieparzystych jest {niepar}")
print(f"parzystych jest {par}")
