with open('texto.txt','r') as f:
    lista = []
    lista.append(f.readline())
    f.close()
    
dict_consoantes = {
    'b':0, 'c':0, 'ç':0, 'd':0, 'f':0,
    'g':0, 'h':0, 'j':0, 'k':0, 'l':0,
    'm':0, 'n':0, 'p':0, 'q':0, 'r':0,
    's':0, 't':0, 'v':0, 'w':0, 'x':0,
    'y':0, 'z':0
}
for index in lista:
    for char in index:
        if char.isupper():
            char = char.lower()
            if char in dict_consoantes:
                dict_consoantes[char] += 1

with open('textoSaida.txt','w') as f:
    f.write('{}'.format(dict_consoantes))
    f.close