import random
damn = 1
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z']
while True:
    ala = random.choice(alfabet)
    a = input("podaj znak: ")
    for al in alfabet :
        if ala == al and a == al:
            print(f"to było {ala}")
            print(f" zgadywałeś {damn}")
            exit(0)
    damn += 1

