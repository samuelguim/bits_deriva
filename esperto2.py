# 1584 Espertofone
# bits à deriva
# Samuel Guimarães Silva
# João Guilherme Alves
# Caio Vinicius da Cruz Coelho

def contar_padroes(n, k):
    MOD = 10**9 + 7
    
    if k == 0:
        return (n*n) % MOD
    
    matriz_adj = [[0 for _ in range(n*n)] for _ in range(n*n)]
    
    for r1 in range(n):
        for c1 in range(n):
            btn1 = r1 * n + c1
            for r2 in range(n):
                for c2 in range(n):
                    btn2 = r2 * n + c2
                    
                    if r1 == r2 and c1 == c2:
                        continue
                    
                    bloqueado = False
                    
                    if r1 == r2 or c1 == c2 or abs(r1-r2) == abs(c1-c2):
                        dr = 0 if r1 == r2 else (1 if r2 > r1 else -1)
                        dc = 0 if c1 == c2 else (1 if c2 > c1 else -1)
                        
                        r, c = r1 + dr, c1 + dc
                        while r != r2 or c != c2:
                            if 0 <= r < n and 0 <= c < n:
                                meio_btn = r * n + c
                                if meio_btn != btn1 and meio_btn != btn2:
                                    bloqueado = True
                                    break
                            r += dr
                            c += dc
                    
                    if not bloqueado:
                        matriz_adj[btn1][btn2] = 1
    
    if k == 1:
        resultado = 0
        for i in range(n*n):
            for j in range(n*n):
                resultado = (resultado + matriz_adj[i][j]) % MOD
        return resultado
    
    matriz_potencia = elevar_matriz(matriz_adj, k, MOD)
    
    resultado = 0
    for i in range(n*n):
        for j in range(n*n):
            resultado = (resultado + matriz_potencia[i][j]) % MOD
    
    return resultado

def multiplicar_matriz(A, B, mod):
    n = len(A)
    resultado = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] = (resultado[i][j] + A[i][k] * B[k][j]) % mod
    
    return resultado

def elevar_matriz(matriz, potencia, mod):
    n = len(matriz)
    
    if potencia == 0:
        identidade = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            identidade[i][i] = 1
        return identidade
    
    if potencia % 2 == 0:
        meia_potencia = elevar_matriz(matriz, potencia // 2, mod)
        return multiplicar_matriz(meia_potencia, meia_potencia, mod)
    else:
        return multiplicar_matriz(matriz, elevar_matriz(matriz, potencia - 1, mod), mod)

def main():
    entradas = []
    
    while True:
        try:
            n, k = map(int, input().split())
            entradas.append((n, k))
        except EOFError:
            break
    
    for n, k in entradas:
        resultado = contar_padroes(n, k)
        print(resultado)

if __name__ == "__main__":
    main()