# 1584 Espertofone
# bits à deriva
# Samuel Guimarães Silva
# João Guilherme Alves
# Caio Vinicius da Cruz Coelho

def exponenciacao(base, expoente):
    auxiliar = base
    for i in range(expoente-1):
        base = base * auxiliar
    return base;

def main():
    respostas = []
    while True:
        try:
            N, K = map(int, input().split())
            combinacoes = N*N

            canto = 4
            borda = (N*4)-8
            centro = (N*N)-canto-borda

            possibilidades_canto = canto*((N*N)-(N+N-3))
            possibilidades_borda = borda*((N*N)-(N+N-4))
            possibilidades_centro = centro*((N*N)-(N+N-5))

            posicoes_possiveis = (N*N)-(N+N-3)
            if (K > 0):
                combinacoes = (possibilidades_canto + possibilidades_borda + possibilidades_centro)*K
                combinacoes = combinacoes % 1000000007
            respostas.append(combinacoes)
        
        except EOFError:
            break
    
    for resposta in respostas:
        print(resposta)

if __name__ == "__main__":
    main()