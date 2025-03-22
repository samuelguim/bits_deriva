# 2683 - Espaço de Projeto

import sys


def main():
    entradas = int(sys.stdin.readline())
    arestas = []
    for _ in range(entradas):
        u, v, w = map(int, sys.stdin.readline().split())
        arestas.append((u,v,w))
    
    menor_custo = kruskal(entradas, arestas)
    maior_custo = kruskal(entradas, arestas, reverse=True)
    print(maior_custo)
    print(menor_custo)

def find(parent, value):
    if parent[value] != value:
        parent[value] = find(parent, parent[value])
    return parent[value]


def union(parent,rank,v1,v2):
    s1 = find(parent,v1)
    s2 = find(parent,v2)

    if s1 != s2:
        if rank[s1] > rank[s2]:
            parent[s2] = s1
        elif rank[s1] < rank[s2]:
            parent[s1] = s2
        else:
            parent[s2] = s1
            rank[s1] += 1
        return True
    return False


def kruskal(n, arestas, reverse=False):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    arestas.sort(key=lambda x: x[2], reverse=reverse)  
    mst_custo = 0
    mst_arestas = 0

    for u, v, w in arestas:
        if union(parent, rank, u, v):
            mst_custo += w
            mst_arestas += 1
            if mst_arestas == n - 1:
                break

    return mst_custo




if __name__ == '__main__':
    main()