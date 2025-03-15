

a = float(input("p-odaj liczbe: "))
b = float(input("p-odaj liczbe: "))

c = input("podar znak działania: ")
if c == '+':
    d = a + b
    print(f"wynik to {d}")
elif c == '-':
    print(a - b)
    if b - a != a - b:
        print(b - a)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
    if b / a != a / b:
        print(b / a)

