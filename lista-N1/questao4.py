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
print(sequencia)

# soma da diagonal
diagonal = 0
for i in range(len(sequencia)):
    for j in range(len(sequencia)):
        if i == j:
            diagonal += sequencia[i][j]
print('\n')
print(diagonal)

#adicionando os multiplos de 5
mult = []
for i in range(len(sequencia)):
    for j in range(len(sequencia)):
        if sequencia[i][j] % 5 == 0:
            mult.append(sequencia[i][j])
print('\n')
print(mult)

# primeira linha transposta
fibonacci_transposta = sequencia.T
linha_transposta = []
for i in range(len(fibonacci_transposta)):
    for j in range(len(fibonacci_transposta)):
        if i == 0:
            linha_transposta.append(fibonacci_transposta[i][j])
print("\n")
print(linha_transposta)

# A linha com maior múltiplo de 3
cont = 0
for i in range(len(sequencia)):
    for j in range(len(sequencia)):
        if sequencia[i][j] % 3 == 0:
            cont += 1
            
# NÃO ESQUECER DE FAZER A SAIDA.TXT