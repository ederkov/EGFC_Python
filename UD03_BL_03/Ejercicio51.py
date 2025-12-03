pago = 10
total = 0
for mes in range(1, 21):
    print(f"Mes {mes}: {pago} euros")
    total += pago
    pago *= 2
print("Total pagado en 20 meses:", total)
