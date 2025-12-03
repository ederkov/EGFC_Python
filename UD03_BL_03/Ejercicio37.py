peso = float(input("Peso del paquete (kg): "))
zona = input("Zona (NA, CA, SA, EU, AS): ").upper()
tarifas = {"NA":24,"CA":20,"SA":21,"EU":10,"AS":18}
if zona in tarifas:
    print("Costo:", peso * tarifas[zona])
else:
    print("Zona no disponible")
