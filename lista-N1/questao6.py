with open('led.txt','r') as f:
    led = []
    n = int(f.readline())
    for i in range(n):
        linha = f.readline().strip()
        led.append(linha)
    f.close()

with open('saidaLed.txt','w') as f:
    dicionario = {
        '1':2, '2':5, '3':5,
        '4':4, '5':5, '6':6,
        '7':3, '8':7, '9':6, '0':6 
    }

    for i in led:
        somatorio = 0
        for n in i:
            somatorio += dicionario[n]
        f.write('{} leds\n'.format(somatorio))
    f.close()