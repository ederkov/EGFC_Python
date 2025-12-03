pos1 = 70
pos2 = 150
vel = float(input("Velocidad de ambos coches (km/h): "))


tiempo = (pos2 - pos1) / (2 * vel)
encuentro = pos1 + vel * tiempo
print("Se encontrarán en el km:", encuentro)
