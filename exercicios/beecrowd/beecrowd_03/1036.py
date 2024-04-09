import math

a,b,c = map(float, input().split())
delt = (b**2) - 4 * a * c

if a == 0:
    print("Impossivel calcular")
elif delt < 0:
    print("Impossivel calcular")
else:
    r1 = (-b + math.sqrt(delt))/(2 * a)
    r2 = (-b - math.sqrt(delt))/(2 * a)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))