minutos = int(input("Duración en minutos: "))
dia = input("Día (domingo/otro): ").lower()
turno = input("Turno (mañana/tarde): ").lower()
costo = 0
if minutos <= 5:
    costo = minutos * 1
elif minutos <= 8:
    costo = 5*1 + (minutos-5)*0.8
elif minutos <= 10:
    costo = 5*1 + 3*0.8 + (minutos-8)*0.7
else:
    costo = 5*1 + 3*0.8 + 2*0.7 + (minutos-10)*0.5
if dia == "domingo":
    costo *= 1.03
elif turno == "mañana":
    costo *= 1.15
else:
    costo *= 1.10
print("Costo total:", round(costo,2))

