N = int(input("Número de trabajadores: "))
total_empresa = 0
for i in range(N):
    horas = float(input(f"Horas trabajadas por trabajador {i+1}: "))
    pago_hora = float(input(f"Pago por hora del trabajador {i+1}: "))
    sueldo = horas * pago_hora
    print(f"Sueldo trabajador {i+1}: {sueldo}")
    total_empresa += sueldo
print("Total pagado por la empresa:", total_empresa)
