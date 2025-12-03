while True:
    inf = int(input("Límite inferior: "))
    sup = int(input("Límite superior: "))
    if inf < sup: break
suma = 0
fuera = 0
igual = False
while True:
    n = int(input("Número (0 para terminar): "))
    if n == 0: break
    if inf < n < sup:
        suma += n
    else:
        fuera += 1
    if n == inf or n == sup:
        igual = True
print("Suma dentro:", suma)
print("Fuera:", fuera)
print("Algún número igual a los límites:", igual)
