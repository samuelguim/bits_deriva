import heapq

def main():
    dados_entrada = []
    while True:
        linha = input().strip()
        if not linha:
            continue
        dados_entrada.extend(linha.split())
        if len(dados_entrada) >= 2 and dados_entrada[-2] == '0' and dados_entrada[-1] == '0':
            break

    ponteiro = 0
    while True:
        num_cidades, num_rotas = map(int, dados_entrada[ponteiro:ponteiro+2])
        ponteiro += 2
        
        if num_cidades == 0 and num_rotas == 0:
            break
            
        origem, destino = map(int, dados_entrada[ponteiro:ponteiro+2])
        ponteiro += 2
        
        grafo = [[] for _ in range(num_cidades)]
        grafo_reverso = [[] for _ in range(num_cidades)]
        lista_arestas = []
        
        for _ in range(num_rotas):
            cidade_a, cidade_b, peso = map(int, dados_entrada[ponteiro:ponteiro+3])
            ponteiro += 3
            grafo[cidade_a].append((cidade_b, peso))
            grafo_reverso[cidade_b].append((cidade_a, peso))
            lista_arestas.append((cidade_a, cidade_b, peso))
        
        dist_origem = [float('inf')] * num_cidades
        dist_origem[origem] = 0
        heap = [(0, origem)]
        
        while heap:
            dist_atual, cidade_atual = heapq.heappop(heap)
            if dist_atual > dist_origem[cidade_atual]:
                continue
            for vizinho, peso in grafo[cidade_atual]:
                if dist_origem[vizinho] > dist_origem[cidade_atual] + peso:
                    dist_origem[vizinho] = dist_origem[cidade_atual] + peso
                    heapq.heappush(heap, (dist_origem[vizinho], vizinho))
        
        dist_destino = [float('inf')] * num_cidades
        dist_destino[destino] = 0
        heap = [(0, destino)]
        
        while heap:
            dist_atual, cidade_atual = heapq.heappop(heap)
            if dist_atual > dist_destino[cidade_atual]:
                continue
            for vizinho, peso in grafo_reverso[cidade_atual]:
                if dist_destino[vizinho] > dist_destino[cidade_atual] + peso:
                    dist_destino[vizinho] = dist_destino[cidade_atual] + peso
                    heapq.heappush(heap, (dist_destino[vizinho], vizinho))
        
        novo_grafo = [[] for _ in range(num_cidades)]
        for cidade_a, cidade_b, peso in lista_arestas:
            if dist_origem[cidade_a] + peso + dist_destino[cidade_b] != dist_origem[destino]:
                novo_grafo[cidade_a].append((cidade_b, peso))
        
        dist_final = [float('inf')] * num_cidades
        dist_final[origem] = 0
        heap = [(0, origem)]
        encontrou = False
        resultado = -1
        
        while heap:
            dist_atual, cidade_atual = heapq.heappop(heap)
            if cidade_atual == destino:
                encontrou = True
                resultado = dist_atual
                break
            if dist_atual > dist_final[cidade_atual]:
                continue
            for vizinho, peso in novo_grafo[cidade_atual]:
                if dist_final[vizinho] > dist_final[cidade_atual] + peso:
                    dist_final[vizinho] = dist_final[cidade_atual] + peso
                    heapq.heappush(heap, (dist_final[vizinho], vizinho))
        
        print(resultado)

if __name__ == '__main__':
    main()