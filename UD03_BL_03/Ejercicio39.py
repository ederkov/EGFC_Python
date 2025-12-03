import random
num = random.randint(1,100)
intentos = 10
while intentos > 0:
    guess = int(input("Adivina el número: "))
    if guess == num:
        print("¡Correcto! Intentos usados:", 10-intentos+1)
        break
    elif guess < num:
        print("El número es mayor")
    else:
        print("El número es menor")
    intentos -= 1
if intentos == 0:
    print("Se acabaron los intentos. El número era:", num)
