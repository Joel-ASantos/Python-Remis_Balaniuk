n_listas = int(input())
listas = []

for i in range(n_listas):
    listas.append(list(map(int,input().split())))
    
if n_listas <= 1:
    resultado = []
else:
    primeira_lista = set(listas[0])
    outros_elementos = set()
    
    for lista in listas[1:]:
        outros_elementos.update(lista)
    
    elementos_excluidos = sorted(primeira_lista.difference(outros_elementos))
    resultado = elementos_excluidos
print(resultado)