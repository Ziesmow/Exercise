i = 0
ile = 0
ile7 = 0
while i <= 1000:
    if i % 6 == 0:
        print(i)
        ile += 1
        if '7' in str(i):
            ile7 += 1
            print(f"ta liczba powyżej ma siódemkę")
    i += 1
print(f"tyle jest liczb podzielnych przeez 6 w 1000: {ile}")
