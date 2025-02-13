from collections import defaultdict
from heapq import nlargest


def prender(grafo, n):
    folhas = pegar_folhas(grafo)
    visitados = [0] * (len(grafo) + 1)
    maiores_alturas = maior_altura(1, gerar_grafo_invertido(grafo))
    alturas = [pegar_altura(a,grafo,visitados) for a in maiores_alturas if a in folhas]
    return sum(nlargest(n,alturas))


def pegar_altura(no, grafo, visitados):
    c = 0
    while no != 1:
        if visitados[no] == 0:
            c += 1
            visitados[no] = 1
        no = grafo[no]
        if no == 1 and visitados[1] == 0:
            c += 1
            visitados[1] = 1
    return c


def gerar_grafo_invertido(grafo):
    grafo_invertido = defaultdict(list)

    for no, superior in grafo.items():
        if superior != 0:
            grafo_invertido[superior].append(no)
    return grafo_invertido


def maior_altura(no, grafo):
    pilha = [(no,1)]
    visitados = set()
    alturas = {}

    while pilha:

        no, altura = pilha.pop()
        if no not in visitados:
            visitados.add(no)
            alturas[no] = altura
            for vizinho in grafo[no]:
                if vizinho not in visitados:
                    pilha.append((vizinho, altura+1))
    return dict(sorted(alturas.items(), key=lambda x: x[1], reverse=True))



def pegar_folhas(grafo):
    filhos = set(grafo.values())
    folhas = [k for k in grafo if k not in filhos]
    return folhas


def main():
    qtd_membros, previsoes = map(int, input().split())
    superiores = input().split()
    grafo = {1: 1}
    for i, superior in enumerate(superiores, start=2):
        grafo[i] = int(superior)
    print(prender(grafo, previsoes))


if __name__ == '__main__':
    main()
