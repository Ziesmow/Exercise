list1 = [10, 34, 6, 2, 37, 5, 97, 23, 13, 24]
list2 = []
for liczba in list1:
    if liczba % 2 == 0:
        list2.insert(0, liczba)
    else:
        list2.append(liczba)
print(list1)
print(list2)
