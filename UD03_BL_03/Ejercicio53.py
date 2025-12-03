
N = int(input("Número de trabajadores: "))
total_empresa = 0
for i in range(N):
    dias = int(input(f"Días trabajados por trabajador {i+1}: "))
    total_horas = 0
    for d in range(dias):
        h = float(input(f"Horas día {d+1}: "))
        total_horas += h
    pago_hora = float(input("Pago por hora: "))
    sueldo = total_horas * pago_hora
    print(f"Sueldo trabajador {i+1}: {sueldo}")
    total_empresa += sueldo
print("Total empresa:", total_empresa)
