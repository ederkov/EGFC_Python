HH = int(input("Hora salida: "))
MM = int(input("Minutos salida: "))
SS = int(input("Segundos salida: "))
T = int(input("Tiempo de viaje en segundos: "))
segundos_totales = HH*3600 + MM*60 + SS + T
HH_llegada = (segundos_totales // 3600) % 24
MM_llegada = (segundos_totales % 3600) // 60
SS_llegada = segundos_totales % 60
print("Hora de llegada:", HH_llegada, ":", MM_llegada, ":", SS_llegada)
