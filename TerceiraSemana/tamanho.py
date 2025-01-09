quantidade = int(input())

for i in range(quantidade):
    texto = input()
    lista_palavras = texto.split()
    lista_ordenada = sorted(lista_palavras, key=len, reverse= True)
    print(' '.join(lista_ordenada))  