from dataclasses import dataclass
from typing import List

def confereTipico(i, porcoes, porcoes_tipicas, ingredientes_tipicos): 
    for j in range(len(porcoes[i].ingredientes_porcao)):
        for l in range(len(porcoes)):
            if (porcoes[i].ingredientes_porcao[j] == porcoes[l].nome and porcoes[i].nome != porcoes[l].nome):
                confereTipico(l, porcoes, porcoes_tipicas, ingredientes_tipicos)
            if (porcoes[i].ingredientes_porcao[j] == porcoes[l].nome and porcoes[l].tipico == True):
                porcoes[i].contador = porcoes[i].contador + 1
        for k in range(len(ingredientes_tipicos)):
            if (porcoes[i].ingredientes_porcao[j] == ingredientes_tipicos[k]):
                porcoes[i].contador = porcoes[i].contador + 1
    
    if (porcoes[i].contador/len(porcoes[i].ingredientes_porcao)>0.5):
        porcoes[i].tipico = True
        porcoes_tipicas.append(porcoes[i])
    

@dataclass
class Porcao:
    tipico: bool
    nome: str
    ingredientes_porcao: list[str]
    contador: int

numero_ingredientes_tipicos = int(input()) 
ingredientes_tipicos = input ('').split()

numero_porcoes = int(input()) 
porcoes = []
porcoes_tipicas = []
for i in range(numero_porcoes):
    input_porcao = input('').split()
    ingredientes_porcao = input('').split()
    porcoes.append(Porcao(False, input_porcao[0], ingredientes_porcao, 0))

for f in range (numero_porcoes):
    confereTipico(f, porcoes, porcoes_tipicas, ingredientes_tipicos)

for p in range(numero_porcoes):
    if (porcoes[p].tipico == True):
        print ('porcao tipica')
    else:
        print ('porcao comum')