# 1706 - Pontes Mágicas


from collections import deque
import sys


def bfs_teste(grafo, no_inicial, sons, visitados):
    contador = 0

    q = deque([no_inicial])
    while q:
        no = q.popleft()
        if visitados[no-1] == 0:
            visitados[no-1] = 1
            if sons[no-1] == 'B':
                contador += 1
            for vizinho in grafo[no]:
                if visitados[vizinho-1] == 0:
                    q.append(vizinho) 
                    
    #print(f'ligacoes: {qtd_ligacoes_BB//2}')
    return contador

sys.stdin = open('teste.txt', 'r')

def main():
    resultados = []
    while True:
        try:
            qtd_torres, m = map(int, input().split())
            sons_iniciais = input().split()
            conexoes = {}
            for _ in range(m):
                a, b = map(int, input().split())
                conexoes.setdefault(a, []).append(b)
                conexoes.setdefault(b, []).append(a)

            lista_visitados = [0] * qtd_torres
            #print(f'VISITADOS: {lista_visitados}')
            possivel = True

            #print(f'Grafo: {conexoes}')
            #print(f'Sons: {sons_iniciais}')
            for i in range(qtd_torres):
                if lista_visitados[i] == 0:
                    contador = bfs_teste(conexoes,i+1,sons_iniciais,lista_visitados)
                    #print(f'CONTADOR: {contador}')
                    if contador % 2 != 0:
                        possivel = False
                        break    
            if possivel:
                resultados.append('Y')
            else:
                resultados.append('N')

        except EOFError:
            break
    print('\n'.join(resultados))



if __name__ == '__main__':
    main()              
                    

g = {
    1: [2],
    2: [1],
}



# print(dfs(g,1,['A', 'B']))

def dfs(grafo, no_inicial, sons):
    visitados = []
    qtd_ligacoes_BB = 0 

    pilha = [no_inicial]
    while pilha:
        no = pilha.pop()
        if no not in visitados:
            visitados.append(no)
            pilha.extend(reversed(grafo[no]))
            for v in grafo[no]:
                if sons[no-1] == 'B' and sons[v-1] == 'B':
                    #print('achei a aresta B-B')
                    qtd_ligacoes_BB += 1
                    
    #print(f'ligacoes: {qtd_ligacoes_BB//2}')
    return (qtd_ligacoes_BB//2) % 2 == 0