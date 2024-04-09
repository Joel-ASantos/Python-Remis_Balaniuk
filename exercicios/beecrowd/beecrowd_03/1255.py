def letras_freq(texto):
    freq = {}
    for char in texto:
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
                
    max_ocorr = max(freq.values())
    letras_max_ocorr = [letra for letra, freq in freq.items() if freq == max_ocorr]
    letras_max_ocorr.sort()
    return letras_max_ocorr

teste = int(input())
for i in range(teste):
    texto = input().lower()
    resul = letras_freq(texto)
    print(''.join(resul))