class FenwickTree:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tree = [0] * (tamanho + 1)
    
    def atualizar(self, indice, valor):
        while indice <= self.tamanho:
            self.tree[indice] += valor
            indice += indice & -indice
    
    def consultar(self, indice):
        soma = 0
        while indice > 0:
            soma += self.tree[indice]
            indice -= indice & -indice
        return soma

def contar_mega_inversoes(arr):
    n = len(arr)
    max_val = max(arr)
    
    BIT1 = FenwickTree(max_val)  # Guarda quantos valores menores já apareceram
    BIT2 = FenwickTree(max_val)  # Guarda quantos pares válidos já foram formados
    
    inversoes = 0
    
    for j in range(n - 1, -1, -1):
        aj = arr[j]
        inversoes += BIT2.consultar(aj - 1)  # Conta quantas triplas já foram formadas
        qtd_menores = BIT1.consultar(aj - 1)  # Conta quantos elementos menores que aj já apareceram
        BIT2.atualizar(aj, qtd_menores)  # Atualiza a árvore de pares válidos
        BIT1.atualizar(aj, 1)  # Marca que aj apareceu
    
    return inversoes

# Entrada de dados
n = int(input())
arr = list(map(int, input().split()))
print(contar_mega_inversoes(arr))