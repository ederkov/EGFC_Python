horas = []
for dia in range(1, 7):
    h = float(input(f"Horas trabajadas día {dia}: "))
    horas.append(h)
total_horas = sum(horas)
pago_por_hora = float(input("Pago por hora: "))
print("Total horas:", total_horas)
print("Sueldo semanal:", total_horas * pago_por_hora)
