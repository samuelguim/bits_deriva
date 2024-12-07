# 2806 - Ingredientes Típicos

nomes = []
ingredientes = {}
n = int(input())
tipicos = input().split()
porcoes = int(input())
for i in range(porcoes):
    nome, componentes = input().split()
    nomes.append(nome)
    prato = input().split()
    ingredientes[nome] = prato 



def encontra_tipicos(dicionario, lista):
    continua = True
    while continua:
        continua = False
        for k, v in list(dicionario.items()):
            contador = 0
            for v in dicionario[k]:
                if v in lista:
                    contador += 1
            if contador > len(dicionario[k]) // 2:
                lista.append(k)
                del dicionario[k]
                continua = True
    return lista
                
    
novos_tipicos = encontra_tipicos(ingredientes, tipicos)

for item in nomes:
    if item in novos_tipicos:
        print('porcao tipica')
    else:
        print('porcao comum')