alumnos = int(input("Número de alumnos: "))
if alumnos >= 100:
    costo = 65 * alumnos
    por_alumno = 65
elif alumnos >= 50:
    costo = 70 * alumnos
    por_alumno = 70
elif alumnos >= 30:
    costo = 95 * alumnos
    por_alumno = 95
else:
    costo = 4000
    por_alumno = costo / alumnos
print("Pago compañía:", costo)
print("Pago por alumno:", por_alumno)
