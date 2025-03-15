
a = int(input("podaj liczbe: "))
if a > 0:
    a += 1
    print(a)
elif a < 0:
    a -= 1
    print(a)
if a % 2 == 0:
    print(f"liczba {a} jest parzysta")
else:
    print(f"liczba {a} nie jest parzysta")
