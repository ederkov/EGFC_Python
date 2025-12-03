dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
n = int(input("Número (1-7): "))
if 1 <= n <= 7:
    print("Día:", dias[n-1])
else:
    print("Error")

