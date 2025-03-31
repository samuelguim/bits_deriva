# 1539 - Empresa de Telecom

from collections import defaultdict
import heapq
import math
import sys


def main():
    resultados = []
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        antenas = []
        for _ in range(n):
            x, y, r = map(int, (sys.stdin.readline().split()))
            antenas.append((x,y,r))

        grafo = defaultdict(list)

        for i in range(n):
            x1, y1, r1 = antenas[i]
            for j in range(n):
                if i != j:
                    x2, y2, r2 = antenas[j]
                    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                    if distancia <= r1:
                        grafo[i+1].append((j+1, distancia))
        
        c = int(sys.stdin.readline())
        for _ in range(c):
            a1, a2 = map(int, (sys.stdin.readline().split()))
            result = dijkstra(grafo, a1, a2, n)
            resultados.append(result)
    print('\n'.join(map(str, resultados)))



def dijkstra(graph, start, end, n):
    INF = math.inf
    dist = {i: INF for i in range(1, n + 1)}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]: 
            continue
        
        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    return math.floor(dist[end]) if dist[end] != INF else -1

if __name__ == '__main__':
    main()