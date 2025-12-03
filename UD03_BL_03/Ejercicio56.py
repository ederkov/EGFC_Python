N = int(input("Cantidad de primos a mostrar: "))
primos = []
num = 2
while len(primos) < N:
    es_primo = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)
    num += 1
print("Primos:", primos)
