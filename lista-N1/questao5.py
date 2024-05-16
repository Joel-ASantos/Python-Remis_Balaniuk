with open('cartas.txt','r') as f:
    baralho = []
    for l in f:
        n = int(l.strip())
        baralho.append(n)
    f.close()
                
with open('cartasSaida.txt','w') as f:
    for i in baralho: # processando os valores
        if i == 0:
            break
        else:
            m = []
            for x in range(1,i + 1):
                m.append(x)
            l = []
            while len(m) > 1:
                m.append(m.pop(1)) # vai pra base
                l.append(m.pop(0)) # é descartada
            f.write('{}\n'.format(f'Cartas descartadas: {l}'))
            f.write('{}\n'.format(f'Carta remanecente: {m[0]}'))
    f.close()

#m = m.pop(m[0]) <-VERSÃO ANTERIOR