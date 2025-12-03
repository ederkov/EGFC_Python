nota = float(input("Nota: "))
edad = int(input("Edad: "))
sexo = input("Sexo (M/F): ").upper()
if nota >= 5 and edad >= 18:
    if sexo == "F":
        print("ACEPTADA")
    elif sexo == "M":
        print("POSIBLE")
else:
    print("NO ACEPTADA")
