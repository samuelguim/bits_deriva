# 4230 Anagramas
# bits à deriva
# Samuel Guimarães Silva
# João Guilherme Alves
# Caio Vinicius da Cruz Coelho

import copy

NP = int(input(''))

palavras = []

linha_anagramas = []
anagramas = []

for i in range(NP):
    palavra_original = input('')
    palavra_ordenada = sorted(palavra_original)
    palavras.append((palavra_original, palavra_ordenada))

ana = sorted(palavras, key=lambda x: x[1])
ana.append((' ', ' '))

j = 0
while (j <= NP):
    linha_anagramas.clear()
    if (j+1 < len(ana)):
        while (ana[j][1] == ana[j+1][1]):
            linha_anagramas.append(ana[j])
            j+=1
    linha_anagramas.append(ana[j])
    anagramas.append(copy.deepcopy((linha_anagramas)))
    j+=1

for i in range(len(anagramas)):
    anagramas[i].sort()

anagramas.sort()

for i in range(1, len(anagramas)):
    for j in range(len(anagramas[i])):
        print(anagramas[i][j][0], end=" ")
    print ('')