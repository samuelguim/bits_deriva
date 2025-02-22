# 1362 - Minha Camiseta Me Serve

from collections import deque
import sys


def edmonds_karp(capacity, source, sink):
    flow = 0
    n = len(capacity)
    while True:
        parent = [-1] * n
        parent[source] = source
        queue = deque([source])
        while queue and parent[sink] == -1:
            current = queue.popleft()
            for nxt in range(n):
                if capacity[current][nxt] > 0 and parent[nxt] == -1:
                    parent[nxt] = current
                    queue.append(nxt)
        if parent[sink] == -1:
            break
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u
        flow += path_flow
    return flow


def main():
    
    t = int(sys.stdin.readline())
    resultados = []
    tamanhos = ["XXL", "XL", "L", "M", "S", "XS"]
    for _ in range(t):
        qtd_camisas, qtd_voluntarios = map(int, sys.stdin.readline().split())
        
        por_tamanho = qtd_camisas // 6
        
        tamanho_index = {size: i for i, size in enumerate(tamanhos)}
        
        voluntarios = []
        for _ in range(qtd_voluntarios):
            t1, t2 = sys.stdin.readline().split()
            voluntarios.append((t1, t2))
        
    
        total_nodes = qtd_voluntarios + 8
        source = 0
        sink = total_nodes - 1
        
        capacity = [[0] * total_nodes for _ in range(total_nodes)]
        
        for i in range(qtd_voluntarios):
            capacity[source][i+1] = 1
        
        for i, (t1, t2) in enumerate(voluntarios):
            v_node = i+1
            capacity[v_node][qtd_voluntarios + 1 + tamanho_index[t1]] = 1
            if t2 != t1:
                capacity[v_node][qtd_voluntarios + 1 + tamanho_index[t2]] = 1
        
        for i in range(6):
            capacity[qtd_voluntarios + 1 + i][sink] = por_tamanho
        
        max_flow = edmonds_karp(capacity, source, sink)
        if max_flow == qtd_voluntarios:
            resultados.append("YES")
        else:
            resultados.append("NO")
    
    print("\n".join(resultados))

if __name__ == '__main__':
    main()