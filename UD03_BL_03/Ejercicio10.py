parcial1 = float(input("Parcial 1: "))
parcial2 = float(input("Parcial 2: "))
parcial3 = float(input("Parcial 3: "))
examen = float(input("Examen final: "))
trabajo = float(input("Trabajo final: "))
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
nota_final = promedio_parciales * 0.55 + examen * 0.30 + trabajo * 0.15
print("Nota final:", nota_final)

