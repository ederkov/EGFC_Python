mes = int(input("Mes (1-12): "))
dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
if 1 <= mes <= 12:
    print("Días:", dias_mes[mes-1])
else:
    print("Error")
