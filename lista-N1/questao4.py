import numpy as np

#Expressão de Fibonacci: Fn = fn-1 + fn-2

# função que gera a sequência de fibonacci
def fibonacci(y):
    fibonacci = [1,1]
    for i in range((n**2)-2):
        a = fibonacci[i+1]
        p = fibonacci[i]
        fibonacci.append(a + p)
    
    arr = np.array(fibonacci).reshape((n,-1))
    return arr

n = int(input('digite o n da fibonacci: '))
sequencia = fibonacci(n)

# soma da diagonal
diagonal = 0
for i in range(len(sequencia)):
    for j in range(len(sequencia)):
        if i == j:
            diagonal += sequencia[i][j]

#adicionando os multiplos de 5
mult = []
for i in range(len(sequencia)):
    for j in range(len(sequencia)):
        if sequencia[i][j] % 5 == 0:
            mult.append(sequencia[i][j])

# primeira linha transposta
fibonacci_transposta = sequencia.T
linha_transposta = []
for i in range(len(fibonacci_transposta)):
    for j in range(len(fibonacci_transposta)):
        if i == 0:
            linha_transposta.append(fibonacci_transposta[i][j])


# A linha com maior múltiplo de 3
filtro = sequencia % 3 == 0
mult3 = np.sum(filtro,axis=1)
big_mult3 = np.argmax(mult3)

with open('fiboSaida.txt','w') as f:
    f.write('Soma da diagonal: {}\n'.format(diagonal))
    f.write('A matriz que contem 5 multiplos de 5: {}\n'.format(mult))
    f.write('A primeira linha da sua transposta e: {}\n'.format(linha_transposta))
    f.write('A linha com maior múltiplo de 3 e {}, a soma e {}'.format(big_mult3,mult3))
    f.close()