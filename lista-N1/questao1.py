# minha resolução
with open('cedulas.txt','r') as f:
  dinheiro = [] # lista vazia
  for l in f: # eu itero sobre cada item no arquivo
    n = int(l.strip()) # Descarta o '\n' e faz que somente o número seja convertido para inteiro
    dinheiro.append(n) # adiciono os números em uma lista
  f.close()

with open('cedulasSaida.txt','w') as f:
  cedulas = [100,50,20,10,5,2,1] # cedulas
  for i in dinheiro: # percorro sobre cada valor na lista dinheiro
    if i == -1: # se o valor for igual a -1 eu quebro a execução
      break
    else:
      f.write('{}'.format(f'\n{i}\n')) # caso contrário eu escrevo o valor
    for j in cedulas: # percorro cada valor na lista cedula
        qtd = i//j 
        i%=j
        f.write('{}'.format(f'{qtd} nota(s) de R$ {j},00\n'))
  f.close()