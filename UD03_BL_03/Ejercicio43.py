a = int(input("Número 1: "))
b = int(input("Número 2: "))
for i in range(min(a,b), max(a,b)+1):
    if i % 2 == 0:
        print(i)