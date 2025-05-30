b = 0
while True:
    a = int(input("podaj liczbę: "))
    if 2 * a <= 10:
        break
    print(2 * a)
    b += a
print(f"suma podanych liczb to {b}")
