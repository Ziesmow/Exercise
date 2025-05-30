i = 0
a = []
while i < 5:
    a.append(int(input("podaj liczbę: ")))
    i += 1
if a[i - 1] > a[i - 2] > a[i - 3] > a[i - 4] > a[i - 5]:
    print("liczby są w porządku rosącym ")
else:
    print("liczby nie są w porządku rozącym ")

