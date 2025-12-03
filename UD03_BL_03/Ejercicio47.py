n = int(input("Número: "))
es_primo = True
if n < 2:
    es_primo = False
else:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            es_primo = False
            break
print("Primo" if es_primo else "No primo")
import math