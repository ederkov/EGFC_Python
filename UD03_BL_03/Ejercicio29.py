import math
A = float(input("Lado A: "))
B = float(input("Lado B: "))
C = float(input("Lado C: "))
if A == B == C:
    print("Equilátero")
elif A == B or B == C or A == C:
    print("Isósceles")
elif math.isclose(A**2 + B**2, C**2) or math.isclose(A**2 + C**2, B**2) or math.isclose(B**2 + C**2, A**2):
    print("Rectángulo")
else:
    print("Escaleno")