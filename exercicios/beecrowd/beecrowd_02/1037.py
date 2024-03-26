var = float(input())

if  0 <= var <= 25:
    print("Intervalo (0,25]")
elif 25 <= var <= 50:
    print("Intervalo (25,50]")
elif 50 <= var <= 75:
    print("Intervalo (50,70]")
elif 75 <= var <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de Intervalo")