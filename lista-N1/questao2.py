with open('listas.txt','r') as f:
    lista = []
    n = int(f.readline())
    for i in range(n):
        linha = f.readline().strip().split()
        lista.append(linha)
    
dicionario_lista = {
    'casa':0, 'pão':0, 'fogão':0,
    'açucar':0, 'bife':0, 'farinha':0, 'comida':0,
    'carne':0, 'panela':0, 'manteiga':0, 'arroz':0,
    'leite':0, 'ovo':0
}

for index in lista:
    for objeto in index:
        if objeto in dicionario_lista:
            dicionario_lista[objeto] += 1

conjuntos = set()
for nova_lista in lista:
    conjuntos.update(nova_lista)

cont = 0
for i in conjuntos:
    cont+=1

for i in range(len(lista)):
    set(lista[i])

t = set(lista[0])
for i in range(len(lista)):
    t = t.intersection(set(lista[i]))

with open('listasSaida.txt','w') as f:
    f.write('Quantidade de elementos distintos: {}'.format(cont))
    f.write('repetções: {}'.format(dicionario_lista))
    f.write('Elemento presente em todas as listas: {}'.format(t))
    f.close