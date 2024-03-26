posicao = 0
maior_valor = -1

for i in range(1,101):
    var = int(input())
    
    if maior_valor < var:
        maior_valor = var 
        posicao = i
        
print(maior_valor)
print(posicao)