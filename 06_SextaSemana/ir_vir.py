import sys
from collections import deque

def bfs(inicio, lista_adj, total_nos):
    visitado = [False] * (total_nos + 1)
    fila = deque([inicio])
    visitado[inicio] = True
    contador = 1

    while fila:
        no_atual = fila.popleft()
        for vizinho in lista_adj[no_atual]:
            if not visitado[vizinho]:
                visitado[vizinho] = True
                contador += 1
                fila.append(vizinho)
    
    return contador == total_nos

def main():
    while True:
        linha = sys.stdin.readline().strip()
        if not linha:
            continue
        N, M = map(int, linha.split())
        if N == 0 and M == 0:
            break

        grafo = [[] for j in range(N + 1)]
        for i in range(M):
            V, W, P = map(int, sys.stdin.readline().split())
            grafo[V].append(W)
            if P == 2:
                grafo[W].append(V)

        grafo_reverso = [[] for j in range(N + 1)]
        for no in range(1, N + 1):
            for vizinho in grafo[no]:
                grafo_reverso[vizinho].append(no)

        conectado_original = bfs(1, grafo, N)
        conectado_reverso = bfs(1, grafo_reverso, N)

        print(1 if conectado_original and conectado_reverso else 0)

if __name__ == "__main__":
    main()