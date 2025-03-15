

i = 1
p = 0
while i <= 120:
    if i % 5 == 0 and i % 11 == 0:
        p += 1
    else:
        print(i)
    i += 1
print(f" tyle liczb zostało pominiętych: {p}")
