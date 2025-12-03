suma = 0
count = 0
while True:
    n = float(input("Número (0 para terminar): "))
    if n == 0:
        break
    suma += n
    count += 1
print("Suma:", suma, "Media:", suma/count if count>0 else 0)
