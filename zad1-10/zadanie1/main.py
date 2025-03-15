a = 0
b = -1
c = 0
reszta = []
maxc = 0

a = input("pobaj liczbę a: ")
b = input("pobaj liczbę b: ")
c = input("pobaj liczbę c: ")
a = int(a)
b = int(b)
c = int(c)    
liczby = [a, b, c]
for liczba in liczby:
    if liczba < 0 :
        print("podaj liczby a, b, c  > 0")
        a = input("pobaj liczbę a: ")
        b = input("pobaj liczbę b: ")
        c = input("pobaj liczbę c: ")
        a = int(a)
        b = int(b)
        c = int(c)  
        continue
reszta = []
maxc = a
for lico in liczby:
    
    if lico > maxc:
        maxc = lico
reszta = []
for resz in liczby:
    if maxc == resz:
        pass
    else:
        reszta.append(resz)
i = 0
while(i < maxc):
    print(reszta[0] + reszta[1])
    i += 1
