def calcular_pontuacao(pontuacao_sistema, ordem_chegada):
    pontuacao_total = [0] * len(ordem_chegada)
    for i, posicao in enumerate(ordem_chegada):
        if posicao <= len(pontuacao_sistema):  
            pontuacao_total[i] = pontuacao_sistema[posicao - 1]
        else:
            pontuacao_total[i] = 0  
    return pontuacao_total

def encontrar_campeao(pontuacoes_totais):
    max_pontuacao = max(pontuacoes_totais)
    campeoes = [i + 1 for i, pontuacao in enumerate(pontuacoes_totais) if pontuacao == max_pontuacao]
    return campeoes

while True:
    G, P = map(int, input().split())
    if G == 0 and P == 0:
        break

    resultados = []
    for _ in range(G):
        resultados.append(list(map(int, input().split())))

    S = int(input())
    for _ in range(S):
        K, *pontos = map(int, input().split())
        pontuacao_sistema = pontos[:K]
        pontuacoes_totais = [0] * P

        for corrida in resultados:
            pontuacoes_corrida = calcular_pontuacao(pontuacao_sistema, corrida)
            pontuacoes_totais = [pontuacoes_totais[i] + pontuacoes_corrida[i] for i in range(P)]

        campeoes = encontrar_campeao(pontuacoes_totais)
        print(*campeoes)
