base = float(input("Base: "))
exp = int(input("Exponente: "))
if exp > 0:
    print("Resultado:", base ** exp)
elif exp == 0:
    print("Resultado: 1")
else:
    print("Resultado:", 1 / (base ** abs(exp)))

