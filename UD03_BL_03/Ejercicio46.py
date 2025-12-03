base = float(input("Base: "))
exp = int(input("Exponente positivo: "))
resultado = 1
for i in range(exp):
    resultado *= base
print("Resultado:", resultado)
