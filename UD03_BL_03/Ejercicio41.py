cant = int(input("Cantidad de números: "))
pos = neg = ceros = 0
for i in range(cant):
    n = float(input("Número: "))
    if n > 0: pos += 1
    elif n < 0: neg += 1
    else: ceros += 1
print("Positivos:", pos, "Negativos:", neg, "Ceros:", ceros)

