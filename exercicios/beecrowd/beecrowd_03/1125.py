while True:
    l1 = input().split()
    G = int(l1[0])
    P = int(l1[1])
    
    if G == 0:
        break
    
    tabela = []
    for i in range(G):
        corrida = []
        l2 = input().split()
        for j in range(P):
            corrida.append(int(l2[j]))
        tabela.append(corrida)
        
    S = int(input())
    for i in range(S):
        l3 = input().split()
        pos = int(l3[0])
        pontos = []
        for j in range(pos):
            pontos.append(int(l3[j+1]))
        pontospilostos = [0]*P
        for c in tabela:
            for j in range(P):
                if c[j] <= pos:
                    pontospilostos[j] += pontos[c[j]-1]
        maxp = max(pontospilostos)
        flag = False
        for j in range(P):
            if pontospilostos[j] == maxp:
                if flag:
                    print('',end='')
                print(j+1)
                flag = True
        print('')