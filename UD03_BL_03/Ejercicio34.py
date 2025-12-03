import datetime
dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))
try:
    datetime.date(año, mes, dia)
    print("Fecha correcta")
except ValueError:
    print("Fecha incorrecta")
