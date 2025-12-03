total = 0
for mes in range(1, 13):
    cantidad = float(input(f"Cantidad depositada en el mes {mes}: "))
    total += cantidad
    print(f"Ahorro acumulado hasta mes {mes}: {total}")
print("Total ahorrado en el año:", total)
