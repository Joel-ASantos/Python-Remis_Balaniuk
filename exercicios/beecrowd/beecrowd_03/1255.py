#Neste problema estamos interessados na frequência das letras em uma dada linha de texto.

#Especificamente, deseja-se saber qual(is) a(s) letra(s) de maior frequência do texto, ignorando o “case sensitive”, 
# ou seja maiúsculas ou minúsculas (sendo mais claro, “letras” referem-se precisamente às 26 letras do alfabeto).

#Entrada
#A entrada contém vários casos de teste. A primeira linha contém um inteiro N que indica a quantidade de casos de teste. 
# Cada caso de teste consiste de uma única linha de texto. A linha pode conter caracteres “não letras”, 
# mas é garantido que tenha ao menos uma letra e que tenha no máximo 200 caracteres no total.

#Saída
#Para cada caso de teste, imprima uma linha contendo a(s) letra(s) que mais ocorreu(ocorreram) no texto em minúsculas
# (se houver empate, imprima as letras em ordem alfabética).

def letras_freq(texto):
    freq = {}
    for char in texto:
        if char in freq:
            if char.isalpha():
                freq[char] += 1
        else:
            freq[char] = 1
    maxOcorr = max(freq.values())
    letras_maxOcorr = [letra for letra, freq in freq.items() if freq == maxOcorr]
    letras_maxOcorr.sort()
    return letras_maxOcorr
            
teste = int(input())
for i in range(teste):
    texto = input().lower()
    resul=letras_freq(texto)
    print(''.join(resul))