while True:
    print("Menú:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Salir")
    opcion = input("Elige opción: ")
    if opcion == "4":
        print("Saliendo...")
        break
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    if opcion == "1":
        print("Resultado:", a+b)
    elif opcion == "2":
        print("Resultado:", a-b)
    elif opcion == "3":
        print("Resultado:", a*b)
    else:
        print("Opción inválida")
 