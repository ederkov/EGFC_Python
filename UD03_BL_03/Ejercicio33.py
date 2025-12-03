dado = int(input("Número del dado (1-6): "))
opuestos = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
nombres = {1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis"}
if 1 <= dado <= 6:
    print("Cara opuesta:", nombres[opuestos[dado]])
else:
    print("ERROR: número incorrecto.")
